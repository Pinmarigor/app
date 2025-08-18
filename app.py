import streamlit as st
from functions.plot_ts import plot

st.title('Histórico de cotações')

st.write('Veja o histórico das cotações')

ticker =  st.sidebar.text_input('Escolha o ticket: ', value = 'AAPL')

fig = plot(ticker)
st.plotly_chart(fig)