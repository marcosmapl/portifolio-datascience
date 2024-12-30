import json
import locale
import os
import streamlit as st

# Configurações de localidade para formatação de números e datas
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

# Configuração inicial da página do Streamlit
st.set_page_config(
    page_title="Portifólio - DataScience", # Título da aba do navegador
    page_icon="💻", # Ícone da página
    layout='wide' # Layout em largura total
)

# Dicionário de páginas de navegação com caminhos e ícones
paginas = {
    'Data Analysis': [
        st.Page(os.path.join("pages", "immigration_canada.py"), title="Immigration to Canada", icon="🧳")
    ],
    "Machine Learning": [
        st.Page(os.path.join("pages","titanic_prediction.py"), title="Titanic Suvivor Prediction", icon="📑")
    ]
}

# Adiciona a navegação lateral e executa a página selecionada
pg = st.navigation(paginas, position='sidebar')
pg.run()
