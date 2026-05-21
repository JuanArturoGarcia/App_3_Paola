import sys
print(sys.executable)

import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



st.title("📊 Simulador de Inversión")

ticker = st.text_input("Ingresa el ticker (ej. AAPL, MSFT, TSLA):", "AAPL")
monto_inicial = st.number_input("Monto inicial ($):", min_value=100.0, value=1000.0)
años = st.slider("Horizonte de inversión (años):", 1, 10, 5)
data = yf.download(ticker, period="5y")




if not data.empty:
    precios = data["Close"]

rendimientos = precios.pct_change().dropna()
media = rendimientos.mean()
volatilidad = rendimientos.std()

num_simulaciones = 100
dias = 252 * años

resultados = []
for i in range(num_simulaciones):
        precios_sim = [monto_inicial]
        
        
for j in range(dias):

    retorno = np.random.normal(media, volatilidad)
    precios_sim.append(precios_sim[-1] * (1 + retorno))

resultados.append(precios_sim)
df_sim = pd.DataFrame(resultados).T

st.subheader("📈 Simulador")
fig, ax = plt.subplots()
ax.plot(df_sim, alpha=0.5)
ax.set_title("Simulación de Inversión")
ax.set_xlabel("Días")
ax.set_ylabel("Valor del portafolio ($)")


st.pyplot(fig)
valores_finales = df_sim.iloc[-1]
promedio = valores_finales.mean()
st.write(f"💰 Valor promedio final: ${promedio:,.2f}")# -*- coding: utf-8 -*-
"""
Created on Wed May 20 20:53:31 2026

@author: 0245739
"""

