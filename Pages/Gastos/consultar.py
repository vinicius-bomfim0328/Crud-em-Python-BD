import streamlit as st
import controllers.gastoController as GastoController
import models.gasto as Gasto
import Pages.Gastos.incluir as IncluirGastos


def Consultar():
    paramID = st.experimental_get_query_params()
    if paramID.get("id") == None:
        st.title("Consultar Gasto")
        colms = st.columns((2, 2, 2, 2, 2, 2, 2, 2, 3, 2))
        campos = ['Nº', 'Mês', 'Renda', 'Lazer', 'Aliment',
                  'Casa', 'Saude', 'Transp', 'Excluir', 'Alterar']
        for col, campos_nome in zip(colms, campos):
            col.write(campos_nome)

        for item in GastoController.consultar():
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col10 = st.columns(
                (2, 2, 2, 2, 2, 2, 2, 2, 3, 2))
            col1.write(item.ID)
            col2.write(item.mes)
            col3.write(item.renda)
            col4.write(item.lazer)
            col5.write(item.alimentacao)
            col6.write(item.casa)
            col7.write(item.saude)
            col8.write(item.transporte)
            button_space_excluir = col9.empty()
            on_click_excluir = button_space_excluir.button(
                'Excluir', 'btnExcluir' + str(item.ID))
            button_space_alterar = col10.empty()
            on_click_alterar = button_space_alterar.button(
                'Alterar', 'btnAlterar' + str(item.ID))

            if on_click_excluir:
                GastoController.excluir(item.ID)

            if on_click_alterar:
                st.experimental_set_query_params(
                    id=[item.ID]
                )
                st.experimental_rerun()

    else:
        on_click_voltar = st.button("voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        IncluirGastos.Incluir()
