import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Simulador de Inversión")

# Inputs
ticker = st.text_input(
    "Ingresa el ticker (ej. AAPL, MSFT, TSLA):",
    "AAPL"
)

monto_inicial = st.number_input(
    "Monto inicial ($):",
    min_value=100.0,
    value=1000.0
)

anios = st.slider(
    "Horizonte de inversión (años):",
    1,
    10,
    5
)

# Descargar datos
data = yf.download(ticker, period="5y")

if not data.empty:

    precios = data["Close"]

    # Rendimientos históricos
    rendimientos = precios.pct_change().dropna()

    # Convertir a float para evitar errores
    media = float(rendimientos.mean())
    volatilidad = float(rendimientos.std())

    num_simulaciones = 100
    dias = 252 * anios

    resultados = []

    # Simulación Monte Carlo
    for i in range(num_simulaciones):

        precios_sim = [float(monto_inicial)]

        for j in range(dias):

            retorno = np.random.normal(media, volatilidad)

            nuevo_precio = precios_sim[-1] * (1 + retorno)

            precios_sim.append(float(nuevo_precio))

        resultados.append(precios_sim)

    # DataFrame limpio
    df_sim = pd.DataFrame(resultados).T.astype(float)

    # Gráfico
    st.subheader("📈 Simulador")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(df_sim.values, alpha=0.5)

    ax.set_title("Simulación de Inversión")
    ax.set_xlabel("Días")
    ax.set_ylabel("Valor del portafolio ($)")

    st.pyplot(fig)

    # Resultado final
    valores_finales = df_sim.iloc[-1]
    promedio = valores_finales.mean()

    st.write(f"💰 Valor promedio final: ${promedio:,.2f}")

else:
    st.error("No se pudo descargar información del ticker.")