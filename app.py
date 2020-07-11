#Import required libraries

import streamlit as st
import plotly.express as px
import pandas as pd
import statsmodels.api as sm
import plotly.graph_objects as go
from statsmodels.formula.api import ols

from PIL import Image
pd.options.plotting.backend = "plotly"

#Sidebar


# Application title
st.title("Omnivida case - Group 89")

#Sidebar
st.sidebar.header("Omnivida")
st.sidebar.subheader("Non adherence Predictor - Asthma")


#Import data
df = pd.read_csv("LoadDatastudio.csv")

#Menu options
opciones_analisis = ['Dashboard', 'Analysis by patient', 'Predictive Model','Predict my adherence'] 
opciones_edad = ['<4','5-18','19-44','45-60','>60']
opciones_gender = ['F','M']

analisis_seleccionado = st.sidebar.selectbox('Select Analysis.', opciones_analisis)


#Sidebar code

if analisis_seleccionado == 'Dashboard':
    st.sidebar.markdown("Filters")
    age_selection = st.sidebar.multiselect('Age group:',opciones_edad)
     #st.write('You selected:', options)
    
    analisis_seleccionado3 = st.sidebar.selectbox('Gender:', opciones_gender)    
    
    st.header("Dashboard")
    #st.subheader("Dashboard description")
        
    data = pd.read_csv("Total.csv")
    
    st.subheader("Graphics")    
    data2=df[['Id','year','ex_ad']].groupby('year').sum()
    data2.reset_index(inplace=True)
    fig = px.line(data2, x="year", y="ex_ad", title='Non Adherence over time')
    st.plotly_chart(fig)
    
        # Podemos visualizar nuestro DataFrame usando
   

    # Y ahora, un mapa de Dash y Mapbox
    test = px.histogram(data, x="gender", y="Age")
    st.plotly_chart(test)
    
    test1 = px.pie(data, values="gender")
    st.plotly_chart(test1)

    showdf = st.checkbox('Show dataframe')
    if showdf:
        st.markdown("Let's see the dataframe")
        st.dataframe(df)
        
    showdatades = st.checkbox('Show data description')
    if showdatades:
        st.markdown("Let's see data description.")
        st.dataframe(data)
    
    
    
#Analysis by patient

elif analisis_seleccionado == 'Analysis by patient': 
    st.header("Analysis by patient")
    
    
    text2 = """
    ¡Welcome to the patient analysis section. select a **patient** and check graphics.
    
    Try: 512938, 502989.
    """
    st.markdown(text2)
    
    
    
    number = st.number_input('Type ID')

    
    #Adherence over time
    
  
    
    df_asr = df[df['Id']==number]
    fig = px.line(df_asr, x="year", y="Non_adherence", title='Adherence over time')
    st.plotly_chart(fig)

    #BMI over time
    
    
    df_asr = df[df['Id']==number]
    fig = px.line(df_asr, x="year", y="NM_IMC", title='BMI over time')
    st.plotly_chart(fig)
  
    
    #Demographic data
    
    
    
    #Hospitalizations
    
    
    df_asr = df[df['Id']==number]
    fig = px.line(df_asr, x="year", y="count_incosistence", title='Inconsistencies')
    st.plotly_chart(fig)
    
    
    df_asr = df[df['Id']==number]
    fig = px.line(df_asr, x="year", y="ERcount", title='ER Count')
    st.plotly_chart(fig)
  


    df_asr = df[df['Id']==number]
    fig = px.line(df_asr, x="year", y="NoProgCount", title='No prog count')
    st.plotly_chart(fig)
  

    
    
    #Habits
    

elif analisis_seleccionado == 'Predictive Model': # Un mapa en Dash    
    
    spector_data = sm.datasets.spector.load_pandas()
    spector_data.exog = sm.add_constant(spector_data.exog)

    # Logit Model
    logit_mod = sm.Logit(spector_data.endog, spector_data.exog)

    logit_res = logit_mod.fit()
    
    end = logit_res.summary()
    st.markdown(end.as_html(), unsafe_allow_html=True)
    
    
    
elif analisis_seleccionado == 'Predict my adherence': # Un mapa en Dash
    st.header("Predict my adherence")
    st.markdown("Miremos el DataFrame. Podemos hacer clic en los nombres de las columnas para ordenar la tabla.")
    df = px.data.tips()
    fig = px.box(df, x="time", y="total_bill", points="all")
    st.plotly_chart(fig)
    
    options = st.multiselect(
     'Select your habits',
     ['Drink', 'Smoke', 'Gambling'])
    #st.write('You selected:', options)
   
    number = st.number_input('Hospitalizations')
    #st.write('The current number is ', number)
    
    my_placeholder = st.empty()
    my_placeholder.text("Hello world!")
    
    bmi = number / 2
    
    occupation = st.radio(
     "Select your occupation:",
     ('Employed', 'Unemployed', 'Documentary'))

    if occupation == 'Comedy':
        st.write('You selected comedy.')
    
    
    agree = st.checkbox('I agree to predict my adherence')
    if agree:
        if st.button('Predict'):
            st.title('You could be Non adherent.')
            st.write('BMI: '+ str(bmi) + ' - Obese I')
        else:
            st.write('Click on predict button....')  
    
    


    