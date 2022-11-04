import streamlit as st
import controllers.gastoController as GastoController
import models.gasto as Gasto


def Incluir():
    st.title("Incluir Gasto")
    with st.form(key="Include_Gasto"):
        input_mes = st.selectbox(
        'Qual mês você deseja gerir seu patrimônio?',
        ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'))
        input_renda = st.number_input(label="Qual foi sua renda deste mês?")
        input_lazer = st.number_input(label="Quanto você gastou com lazer este mês?")
        input_alimentacao = st.number_input(label="Quanto você gastou com alimentação este mês?")
        input_casa = st.number_input(label="Quanto você gastou com sua casa este mês (ex: aluguel, internet, luz e telefone)?")
        input_saude = st.number_input(label="Quanto você gastou com saúde este mês (ex: dentista, médico, plano de saúde)?")
        input_transporte = st.number_input(label="Quanto você gastou com transporte este mês (ex: combustível, metrô/ônibus)?")
        new_var = st.form_submit_button("Salvar")
        input_button_submit = new_var

    if input_button_submit:
        Gasto.mes = input_mes
        Gasto.renda = input_renda
        Gasto.lazer = input_lazer
        Gasto.alimentacao = input_alimentacao
        Gasto.casa = input_casa
        Gasto.saude = input_saude
        Gasto.transporte = input_transporte
        GastoController.incluir(Gasto)
        st.success("Gasto incluido com sucesso")
