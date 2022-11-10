import streamlit as st
import controllers.gastoController as GastoController
import models.gasto as Gasto


def Incluir():
    idAlteracao = st.experimental_get_query_params()
    st.experimental_set_query_params()
    gastoRecuperado = None
    if idAlteracao.get("id") != None:
        idAlteracao = idAlteracao.get("id")[0]
        gastoRecuperado = GastoController.selecionargasto(idAlteracao)
        st.experimental_set_query_params(
            id=[gastoRecuperado.ID]
        )
        st.title("Alterar Gasto")

    else:
        st.title("Incluir Gasto")

    with st.form(key="Include_Gasto"):
        listademeses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        if gastoRecuperado == None:
            input_mes = st.selectbox(
                label='Qual mês você deseja gerir seu patrimônio?', options=listademeses)
            input_renda = st.number_input(
                label="Qual foi sua renda deste mês?")
            input_lazer = st.number_input(
                label="Quanto você gastou com lazer este mês?")
            input_alimentacao = st.number_input(
                label="Quanto você gastou com alimentação este mês?")
            input_casa = st.number_input(
                label="Quanto você gastou com sua casa este mês (ex: aluguel, internet, luz e telefone)?")
            input_saude = st.number_input(
                label="Quanto você gastou com saúde este mês (ex: dentista, médico, plano de saúde)?")
            input_transporte = st.number_input(
                label="Quanto você gastou com transporte este mês (ex: combustível, metrô/ônibus)?")
        else:
            input_mes = st.selectbox(
                label='Qual mês você deseja gerir seu patrimônio?', options=listademeses)
            input_renda = st.text_input(
                label="Qual foi sua renda deste mês?", value=gastoRecuperado.renda)
            input_lazer = st.text_input(
                label="Quanto você gastou com lazer este mês?", value=gastoRecuperado.lazer)
            input_alimentacao = st.text_input(
                label="Quanto você gastou com alimentação este mês?", value=gastoRecuperado.alimentacao)
            input_casa = st.text_input(
                label="Quanto você gastou com sua casa este mês (ex: aluguel, internet, luz e telefone)?", value=gastoRecuperado.casa)
            input_saude = st.text_input(
                label="Quanto você gastou com saúde este mês (ex: dentista, médico, plano de saúde)?", value=gastoRecuperado.saude)
            input_transporte = st.text_input(
                label="Quanto você gastou com transporte este mês (ex: combustível, metrô/ônibus)?", value=gastoRecuperado.transporte)
        input_button_submit = st.form_submit_button("Salvar")

    if input_button_submit:
        if gastoRecuperado == None:
            GastoController.incluir(Gasto.Gasto(0, input_mes, input_renda, input_lazer, input_alimentacao, input_casa, input_saude, input_transporte))
            st.success("Gasto incluido com sucesso")

        else:
            st.experimental_set_query_params()
            GastoController.alterar(Gasto.Gasto(gastoRecuperado.ID, input_mes, input_renda, input_lazer, input_alimentacao, input_casa, input_saude, input_transporte))
            st.success("Gasto alterado com sucesso")
