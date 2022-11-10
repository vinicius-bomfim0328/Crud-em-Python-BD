from configparser import Interpolation
import streamlit as st
import controllers.gastoController as GastoController
import models.gasto as Gasto
import Pages.Gastos.incluir as IncluirGastos
import Pages.Gastos.consultar as ConsultarGastos



st.sidebar.title("Menu")
Page_Gastos = st.sidebar.selectbox('Gestão de Patrimônio', ['Incluir', 'Consultar'])

if Page_Gastos == 'Incluir':
    st.experimental_set_query_params()
    IncluirGastos.Incluir()

if Page_Gastos == 'Consultar':
    ConsultarGastos.Consultar()
