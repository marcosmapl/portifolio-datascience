import locale
import pandas as pd
import streamlit as st

from datetime import datetime


df = pd.read_csv("data/imigrantes_canada.csv")
st.dataframe(df)

# with st.sidebar:
#     st.selectbox(
#         "Ano",
#         tuple(range(1980, 2014)),
#         index=0,
#         key='year'
#     )

#     st.selectbox(
#         "Mês da Análise",
#         ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"),
#         index=datetime.now().month - 1,
#         key='month'
#     )
#     st.session_state['month_number'] = constants.month_to_number(st.session_state.month)


# tab_emp_liquidacao, tab_emp_pagamento, tab_emp_liquidado = st.tabs(["Liquidação x Anulação Liq. (AGG)", "Pagamento x Anulação Pag. (AGG)", "Liquidação Liq. x Pagamento Liq. (AGG)"])
# with tab_emp_liquidacao:
#     df_emp_liq = pd.DataFrame(
#         database.fetchall_liquidacao_anulacao(st.session_state.year, st.session_state.month_number, database.TipoAnalise.AGG), 
#         columns=[
#             'Ano',
#             'Cód. Unidade Orçamentária',
#             'Nº Empenho',
#             'Nº Nota Liquidação',
#             'Soma Liquidação',
#             'Soma Anulação Liq.',
#             'Diferença'
#     ])
#     with st.expander('Filtrar Colunas', icon=":material/tune:"):
#         filter_cols_emp_liq = st.multiselect('Selecione as colunas', list(df_emp_liq.columns), list(df_emp_liq.columns), key='df_emp_liq.columns')
#     st.dataframe(df_emp_liq[filter_cols_emp_liq], hide_index=True)
#     st.divider()
#     tab_emp_liq_col1, tab_emp_liq_col2, tab_emp_liq_col3 = st.columns(3)
#     tab_emp_liq_col1.metric(
#         "Total Liquidação", 
#         locale.currency(df_emp_liq['Soma Liquidação'].sum(), grouping=True)
#     )
#     tab_emp_liq_col2.metric(
#         "Total Anulação Liq.", 
#         locale.currency(df_emp_liq['Soma Anulação Liq.'].sum(), grouping=True)
#     )
#     valor = df_emp_liq['Diferença'].sum()
#     cor = 'green' if valor >= 0 else 'red'
#     tab_emp_liq_col3.metric(f":{cor}[Total Liq. Líquida]", locale.currency(valor, grouping=True))

# with tab_emp_pagamento:
#     df_emp_pag = pd.DataFrame(
#         database.fetchall_pagamento_anulacao(st.session_state.year, st.session_state.month_number, database.TipoAnalise.AGG), 
#         columns=[
#             'Ano',
#             'Cód. Unidade Orçamentária',
#             'Nº Empenho',
#             'Nº Nota Liquidação',
#             'Nº Ordem Bancária',
#             'Cód. Evento',
#             'Soma Pagamento',
#             'Soma Anulação Pag.',
#             'Diferença'
#     ])
#     with st.expander('Filtrar Colunas', icon=":material/tune:"):
#         filter_cols_emp_pag = st.multiselect('Selecione as colunas', list(df_emp_pag.columns), list(df_emp_pag.columns), key='df_emp_pag.columns')
#     st.dataframe(df_emp_pag[filter_cols_emp_pag], hide_index=True)
#     st.divider()
#     tab_emp_pag_col1, tab_emp_pag_col2, tab_emp_pag_col3 = st.columns(3)
#     tab_emp_pag_col1.metric("Total Pagamento", locale.currency(df_emp_pag['Soma Pagamento'].sum(), grouping=True))
#     tab_emp_pag_col2.metric("Total Anulação Pag.", locale.currency(df_emp_pag['Soma Anulação Pag.'].sum(), grouping=True))
#     valor = df_emp_pag['Diferença'].sum()
#     cor = 'green' if valor >= 0 else 'red'
#     tab_emp_pag_col3.metric(f":{cor}[Total Pagamento Líquido]", locale.currency(valor, grouping=True))

# with tab_emp_liquidado:
#     df_emp_lid = pd.DataFrame(
#         database.fetchall_liquidacao_pagamento(st.session_state.year, st.session_state.month_number, database.TipoAnalise.AGG), 
#         columns=[
#             'Ano',
#             'Cód. Unidade Orçamentária',
#             'Nº Empenho',
#             'Nº Nota Liquidação',
#             'Soma Liquidação',
#             'Soma Anulação Liq.',
#             'Soma Pagamento',
#             'Soma Anulação Pag.',
#             'Diferença'
#     ])
#     with st.expander('Filtrar Colunas', icon=":material/tune:"):
#         filter_cols_emp_lid = st.multiselect('Selecione as colunas', list(df_emp_lid.columns), list(df_emp_lid.columns), key='df_emp_lid.columns')
#     st.dataframe(df_emp_lid[filter_cols_emp_lid], hide_index=True)
#     st.divider()
#     tab_emp_lid_col1, tab_emp_lid_col2, tab_emp_lid_col3 = st.columns(3)          
#     tab_emp_lid_col1.metric("Total Liquidação", locale.currency(df_emp_lid['Soma Liquidação'].sum(), grouping=True))
#     tab_emp_lid_col2.metric("Total Anulação Liq.", locale.currency(df_emp_lid['Soma Anulação Liq.'].sum(), grouping=True))
#     tab_emp_lid_col3.metric("Total Liq. Líquida", locale.currency(df_emp_lid['Soma Liquidação'].sum() - df_emp_lid['Soma Anulação Liq.'].sum(), grouping=True))
#     tab_emp_lid_col4, tab_emp_lid_col5, tab_emp_lid_col6 = st.columns(3)     
#     tab_emp_lid_col4.metric("Total Pagamento", locale.currency(df_emp_lid['Soma Pagamento'].sum(), grouping=True))
#     tab_emp_lid_col5.metric("Total Anulação Pag.", locale.currency(df_emp_lid['Soma Anulação Pag.'].sum(), grouping=True))
#     tab_emp_lid_col6.metric("Total Pag. Líquido", locale.currency(df_emp_lid['Soma Pagamento'].sum() - df_emp_lid['Soma Anulação Pag.'].sum(), grouping=True))
#     valor = df_emp_lid['Diferença'].sum()
#     cor = 'green' if valor >= 0 else 'red'
#     st.metric(f":{cor}[Total Diferença Líquida]", locale.currency(valor, grouping=True))

# st.divider()

# st.header('Análise de Restos a Pagar')

# tab_rap_liquidacao, tab_rap_pagamento, tab_rap_liquidado = st.tabs(["Liquidação x Anulação Liq. (RAP)", "Pagamento x Anulação Pag. (RAP)", "Liquidação Liq. x Pagamento Liq. (RAP)"])
# with tab_rap_liquidacao:
#     df_rap_liq = pd.DataFrame(
#         database.fetchall_liquidacao_anulacao(st.session_state.year, tipo_analise=database.TipoAnalise.RAP), 
#         columns=[
#             'Ano',
#             'Cód. Unidade Orçamentária',
#             'Nº Empenho',
#             'Nº Nota Liquidação',
#             'Soma Liquidação',
#             'Soma Anulação Liq.',
#             'Diferença'
#     ])
#     with st.expander('Filtrar Colunas', icon=":material/tune:"):
#         filter_cols_rap_liq = st.multiselect('Selecione as colunas', list(df_rap_liq.columns), list(df_rap_liq.columns), key='df_rap_liq.columns')
#     st.dataframe(df_rap_liq[filter_cols_rap_liq], hide_index=True)
#     st.divider()
#     tab_rap_liq_col1, tab_rap_liq_col2, tab_rap_liq_col3 = st.columns(3)
#     tab_rap_liq_col1.metric(
#         "Total Liquidação", 
#         locale.currency(df_rap_liq['Soma Liquidação'].sum(), grouping=True)
#     )
#     tab_rap_liq_col2.metric(
#         "Total Anulação Liq.", 
#         locale.currency(df_rap_liq['Soma Anulação Liq.'].sum(), grouping=True)
#     )
#     valor = df_rap_liq['Diferença'].sum()
#     cor = 'green' if valor >= 0 else 'red'
#     tab_rap_liq_col3.metric(f":{cor}[Total Liq. Líquida]", locale.currency(valor, grouping=True))

# with tab_rap_pagamento:
#     df_rap_pag = pd.DataFrame(
#         database.fetchall_pagamento_anulacao(st.session_state.year, tipo_analise=database.TipoAnalise.RAP), 
#         columns=[
#             'Ano',
#             'Cód. Unidade Orçamentária',
#             'Nº Empenho',
#             'Nº Nota Liquidação',
#             'Nº Ordem Bancária',
#             'Cód. Evento',
#             'Soma Pagamento',
#             'Soma Anulação Pag.',
#             'Diferença'
#     ])
#     with st.expander('Filtrar Colunas', icon=":material/tune:"):
#         filter_cols_rap_pag = st.multiselect('Selecione as colunas', list(df_rap_pag.columns), list(df_rap_pag.columns), key='df_rap_pag.columns')
#     st.dataframe(df_rap_pag[filter_cols_rap_pag], hide_index=True)
#     st.divider()
#     tab_rap_pag_col1, tab_rap_pag_col2, tab_rap_pag_col3 = st.columns(3)
#     tab_rap_pag_col1.metric("Total Pagamento", locale.currency(df_rap_pag['Soma Pagamento'].sum(), grouping=True))
#     tab_rap_pag_col2.metric("Total Anulação Pag.", locale.currency(df_rap_pag['Soma Anulação Pag.'].sum(), grouping=True))
#     valor = df_rap_pag['Diferença'].sum()
#     cor = 'green' if valor >= 0 else 'red'
#     tab_rap_pag_col3.metric(f":{cor}[Total Pagamento Líquido]", locale.currency(valor, grouping=True))

# with tab_rap_liquidado:
#     df_rap_lid = pd.DataFrame(
#         database.fetchall_liquidacao_pagamento(st.session_state.year, tipo_analise=database.TipoAnalise.RAP), 
#         columns=[
#             'Ano',
#             'Cód. Unidade Orçamentária',
#             'Nº Empenho',
#             'Nº Nota Liquidação',
#             'Soma Liquidação',
#             'Soma Anulação Liq.',
#             'Soma Pagamento',
#             'Soma Anulação Pag.',
#             'Diferença'
#     ])
#     with st.expander('Filtrar Colunas', icon=":material/tune:"):
#         filter_cols_rap_lid = st.multiselect('Selecione as colunas', list(df_rap_lid.columns), list(df_rap_lid.columns), key='df_rap_lid.columns')
#     st.dataframe(df_rap_lid[filter_cols_rap_lid], hide_index=True)
#     st.divider()
#     tab_rap_lid_col1, tab_rap_lid_col2, tab_rap_lid_col3 = st.columns(3)          
#     tab_rap_lid_col1.metric("Total Liquidação", locale.currency(df_rap_lid['Soma Liquidação'].sum(), grouping=True))
#     tab_rap_lid_col2.metric("Total Anulação Liq.", locale.currency(df_rap_lid['Soma Anulação Liq.'].sum(), grouping=True))
#     tab_rap_lid_col3.metric("Total Liq. Líquida", locale.currency(df_rap_lid['Soma Liquidação'].sum() - df_rap_lid['Soma Anulação Liq.'].sum(), grouping=True))
#     tab_rap_lid_col4, tab_rap_lid_col5, tab_rap_lid_col6 = st.columns(3)     
#     tab_rap_lid_col4.metric("Total Pagamento", locale.currency(df_rap_lid['Soma Pagamento'].sum(), grouping=True))
#     tab_rap_lid_col5.metric("Total Anulação Pag.", locale.currency(df_rap_lid['Soma Anulação Pag.'].sum(), grouping=True))
#     tab_rap_lid_col6.metric("Total Pag. Líquido", locale.currency(df_rap_lid['Soma Pagamento'].sum() - df_rap_lid['Soma Anulação Pag.'].sum(), grouping=True))
#     valor = df_rap_lid['Diferença'].sum()
#     cor = 'green' if valor >= 0 else 'red'
#     st.metric(f":{cor}[Total Diferença Líquida]", locale.currency(valor, grouping=True))
