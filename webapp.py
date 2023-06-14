from tkinter.tix import COLUMN
import streamlit as st
import pandas as pd
import numpy as np
import os


st.title('Corridas de Uber em Nova Yorque')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://github.com/streamlit/demo-uber-nyc-pickups/raw/main/uber-raw-data-sep14.csv.gz')

@st.cache_resource
def load_data():
    path = "uber-raw-data-sep14.csv.gz"
    if not os.path.isfile(path):
        path = f"https://github.com/streamlit/demo-uber-nyc-pickups/raw/main/{path}"

    data = pd.read_csv(
        path,
        nrows=100000,  # approx. 10% of data
        names=[
            "date/time",
            "lat",
            "lon",
        ],  # specify names directly since they don't change
        skiprows=1,  # don't read header since names specified directly
        usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
        parse_dates=[
            "date/time"
        ],  # set as datetime instead of converting after the fact
    )

    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data()
df=data
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache)")


st.subheader('Dados brutos')
st.write(data)



st.subheader('Número de corridas por hora')

hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]

st.bar_chart(hist_values)



st.subheader('Mapa das corridas.')
st.map(data)

st.write("Esta é a nossa primeira tentativa de usar dados para criar uma tabela:")
st.write(pd.DataFrame({
    'primeira coluna': [1, 2, 3, 4],
    'segunda coluna': [10, 20, 30, 40]
}))

# Parte 3

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

# Parte 4

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns = (f'col{i}' for i in range(20))
)
st.dataframe(dataframe.style.highlight_max(axis=0))

# Parte 5

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns = (f'col{i}' for i in range(20))
)
st.table(dataframe)

# Parte 6

st.subheader('st.line_chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c']
)
st.area_chart(chart_data)
st.line_chart(chart_data)



# Parte 8

x = st.slider('x')
st.write(x, 'ao quadrado é', x * x)

# Parte 9

st.text_input("Seu nome", key='nome')
st.session_state.nome

# Parte 10

if st.checkbox('Mostrar dataframe'):
    chart_data = df
    
    chart_data

# Parte 11

df = pd.DataFrame({
    'primeira coluna': [1, 2, 3, 4],
    'segunda coluna': [10, 20, 30, 40]
})
option = st.selectbox(
    'Qual dos números você gosta mais?',
    df['primeira coluna']
)
f'Você selecionou: {option}'

# Parte 12

sidebar_selectbox = st.sidebar.selectbox(
    'Como você gostaria de ser contactado?',
    ('Email', 'Telefone fixo', 'Celular')
)
sidebar_slider = st.sidebar.slider(
    'Selecione um intervalo de valores:',
    0.0, 100.0, (25.0, 75.0)
)
st.sidebar.write(sidebar_slider)

# Parte 13

left_column, right_column = st.columns(2)
left_column.button('Pressione-me!')

with right_column:
    chosen = st.radio(
        'Chapéu seletor',
        ('Grifinória', 'Corvinal', 'Lufa-lufa', 'Sonserina')
    )
    st.write(f'Você está na casa {chosen}')

# Parte 14

import time

'Iniciando uma longa computação...'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteração {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'...e agora, terminamos!'

# Parte 15

st.markdown("# Página principal 🎈")
st.sidebar.markdown("# Página principal 🎈")
