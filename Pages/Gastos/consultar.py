import streamlit as st
import controllers.gastoController as GastoController
import models.gasto as Gasto


def Consultar():
    st.title("Consultar Gasto")
    colms = st.columns((2, 2, 2, 2, 2, 2, 2))
    campos = ['mes', 'renda', 'lazer', 'alimentacao', 'casa', 'saude', 'transporte', 'Excluir', 'Alterar']
    for col, campos_nome in zip(colms, campos):
        col.write(campos_nome)

    for item in GastoController.consultar():
        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns((2, 2, 2, 2, 2, 2, 2, 1, 1))
        col1.write(item.mes)
        col2.write(item.renda)
        col3.write(item.lazer)
        col4.write(item.alimentacao)
        col5.write(item.casa)
        col6.write(item.saude)
        col7.write(item.transporte)
        button_space_excluir = col8.empty()
        on_click_excluir = button_space_excluir('Excluir', 'btnExcluir' + str(item.mes))
        button_space_alterar = col9.empty()
        on_click_alterar = button_space_alterar('Alterar', 'btnAlterar' + str(item.mes))