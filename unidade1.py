import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_database():
    return pd.read_csv('brasil_estados.csv')

st.title('meu primeiro App - GCI')
estados = load_database()
st.dataframe(estados)    


st.title('meu primeiro App - GCI')
estados = load_database()
dados, estatistica = st.tabs (['Dados','Estatistica Descritiva'])

with dados:
    regiao = st.selectbox(
        'selecione a Região',
        estados['regiao_nome'].unique()
    )
    
    st.dataframe(estados[estados['regiao_nome'] == regiao])
with estatistica:
    variavel = st.selecbox(
        'selecione a veriavel',
        ['area','populacao','idh','matricula']
    )
    st.table(estados[variavel].describe())

