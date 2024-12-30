import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
import seaborn as sns
import streamlit as st

# Cabeçalho principal da aplicação
st.header("Canadian Immigration - Exploratory Data Analysis", divider="gray")
st.subheader(f"Kaggle Dataset: [Link](https://www.kaggle.com/datasets/ammaraahmad/immigration-to-canada)")

# Carregando o dataset
df = pd.read_csv("data/canadian_immegration_data.csv")

anos = [str(ano) for ano in range(1980, 2014)]
# Calculando o total acumulado para cada país, ano a ano
df_cum = df[anos].cumsum(axis=1)

# Adicionando os totais acumulados ao dataframe original
df_cum["Country"] = df["Country"]
df_cum["Continent"] = df["Continent"]
df_cum["Region"] = df["Region"]
# Substituir qualquer valor 0 em 1980 para evitar divisão por zero (se necessário)
df_cum["1980"] = df_cum["1980"].replace(0, np.nan).fillna(0)

# Transformar os dados de anos em formato longo (tidy data)
df_melted = df.melt(
    id_vars=["Country", "Continent", "Region"], 
    value_vars=[str(year) for year in range(1980, 2014)], 
    var_name="Year", 
    value_name="Immigrants"
)

df_melted_cum = df_cum.melt(
    id_vars=["Country", "Continent", "Region"], 
    value_vars=[str(year) for year in range(1980, 2014)], 
    var_name="Year", 
    value_name="Immigrants"
)

# Agrupar por Continente e Ano para obter os totais
df_grouped = df_melted.groupby(["Continent", "Year"])["Immigrants"].sum().reset_index()
df_grouped_cum = df_melted_cum.groupby(["Continent", "Year"])["Immigrants"].sum().reset_index()

## TEMPORAL
temporal_fig = px.line(
    df_grouped,
    x="Year",
    y="Immigrants",
    color="Continent",
    line_dash="Continent",
    title="Temporal Trend of Immigration to Canada by Continent (1980-2013)",
    labels={"Year": "Year", "Immigrants": "Number of Immigrants", "Continent": "Continent"}
)

# Ajustar layout
temporal_fig.update_layout(
    xaxis=dict(title="Year"),
    yaxis=dict(title="Number of Immigrants"),
    legend_title="Continent",
    template="plotly_white"
)

## TEMPORAL CUM
temporal_cum_fig = px.line(
    df_grouped_cum,
    x="Year",
    y="Immigrants",
    color="Continent",
    line_dash="Continent",
    title="Temporal Trend of Cummulative Immigration to Canada by Continent (1980-2013)",
    labels={"Year": "Year", "Immigrants": "Number of Immigrants", "Continent": "Continent"}
)

# Ajustar layout
temporal_cum_fig.update_layout(
    xaxis=dict(title="Year"),
    yaxis=dict(title="Cummulative Number of Immigrants"),
    legend_title="Continent",
    template="plotly_white"
)

cols_line = st.columns(2)

with cols_line[0]:
    st.plotly_chart(temporal_fig, use_container_width=True)

with cols_line[1]:
    st.plotly_chart(temporal_cum_fig, use_container_width=True)

st.write("In 2010, Asia recorded the highest absolute number of immigrants, totaling 163k, while Oceania had the lowest number, with just 878, in 1984.")
st.write("The immigration growth curve for Asia exhibits an exponential pattern, which contrasts sharply with the trends observed in other continents.")

cols_bar = st.columns(2)

with cols_bar[0]:
    ## TOP 10
    # Selecionar os 10 países com maior imigração total
    top_10_cont = df.groupby(by="Region")["Total"].sum().reset_index().nlargest(10, 'Total')

    # Criar o gráfico de barras
    top10_cont_fig = px.bar(
        top_10_cont,
        x="Region",
        y="Total",
        title="Top 10 Regions with the Most Immigration to Canada",
        labels={"Region": "Region", "Total": "Total of Immigrants"},
        text="Total",
        color="Total",
        color_continuous_scale="Blues"
    )

    # Ajustar layout
    top10_cont_fig.update_layout(
        xaxis=dict(title="Region"),
        yaxis=dict(title="Total of Immigrants"),
        template="plotly_white"
    )

    st.plotly_chart(top10_cont_fig, use_container_width=True)
st.write("The Southern Asia region was the only one to record over 1 million immigrants to Canada during the entire analyzed period.")


with cols_bar[1]:
        ## TOP 10
    # Selecionar os 10 países com maior imigração total
    top_10 = df.nlargest(10, 'Total')

    # Criar o gráfico de barras
    top10_fig = px.bar(
        top_10,
        x="Country",
        y="Total",
        title="Top 10 Countries with the Most Immigration to Canada",
        labels={"Country": "Country", "Total": "Total of Immigrants"},
        text="Total",
        color="Total",
        color_continuous_scale="Blues"
    )

    # Ajustar layout
    top10_fig.update_layout(
        xaxis=dict(title="Country"),
        yaxis=dict(title="Total of Immigrants"),
        template="plotly_white"
    )

    st.plotly_chart(top10_fig, use_container_width=True)

st.write("India and China were the countries with the highest number of immigrants during the analyzed period, each exceeding 650,000 immigrants.")


cols_cont = st.columns(2)

# Agrupar os dados por Continente e somar o total de imigrantes
continente_distribution = df.groupby("Continent")["Total"].sum().sort_values().reset_index()

# Criar o gráfico de pizza
continent_fig = px.pie(
    continente_distribution,
    names="Continent",
    values="Total",
    title="Total Distribution of Immigration to Canada by Continent",
    color="Continent",
    color_discrete_sequence=px.colors.sequential.Blues
)

# Ajustar layout
continent_fig.update_traces(
    textinfo="percent+label",
    pull=[0.1 if i == continente_distribution["Total"].idxmax() else 0 for i in range(len(continente_distribution))]
)
continent_fig.update_layout(template="plotly_white")

with cols_cont[0]:
    st.plotly_chart(continent_fig, use_container_width=True)
    st.write("More than half of the immigrants to Canada come from Asia. Europe ranks second, accounting for 22% of the total immigrants.")


plt.figure(figsize=(21, 15))
corr = df.loc[:, '1980':'2013'].corr()
plot = sns.heatmap(corr, annot=True, fmt=".2f", cmap='Blues', vmin=-1.0, vmax=1.0)

with cols_cont[1]:
    st.pyplot(plot.get_figure())
    st.write("The analysis of correlation values near the main diagonal elements reveals a significant expansion in the window (time interval) of very strong correlations (r > ±0.9). In 1980, this window spanned only 3 years, whereas by 2013, it had increased to 15 years. This finding suggests that, over time, the number of immigrants in a given year has become increasingly correlated with the figures from previous years.")

