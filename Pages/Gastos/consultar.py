import streamlit as st
import controllers.gastoController as GastoController
import models.gasto as Gasto
import pandas as pd


def Consultar():
    st.title("Consultar Gasto")
    costumerList = []
    for lista in GastoController.consultar():
        costumerList.append([lista.mes, lista.renda, lista.lazer, lista.alimentacao, lista.casa, lista.saude, lista.transporte])
    df = pd.DataFrame(
        costumerList,
        columns=['Mes', 'Renda', 'Lazer', 'Alimentação', 'Casa', 'Saúde', 'Transporte']
    )
    st.table(df)