import pandas_datareader.data as web
import datetime
import pandas as pd
import yfinance as yf

## PARTE 1:
1) Descargar la data, ordenar y modificar para elaborar análisis.
# Definir fechas
start = datetime.datetime(2020, 1, 1)
end = datetime.datetime.today()
print("Descargando datos macroeconómicos de FRED")

# Códigos de Series en FRED (Son universales):
# 'CPIAUCSL': Consumer Price Index (Inflación EE.UU.)
# 'UNRATE': Unemployment Rate (Tasa de Desempleo)
# 'FEDFUNDS': Effective Federal Funds Rate (Tasa de interés Fed)
# 'GDP': Gross Domestic Product

series_codes = ['CPIAUCSL', 'UNRATE', 'FEDFUNDS']

try:
    macro_data = web.DataReader(series_codes, 'fred', start, end)
    macro_data.columns = ['Inflación (CPI)', 'Desempleo (%)', 'Tasa Fed (%)']
    print(macro_data.tail())

    import matplotlib.pyplot as plt
    macro_data.plot(subplots=True, figsize=(8, 8), title="Datos Macro de FRED")
    plt.show()

except Exception as e:
    print(f"Error al conectar con FRED: {e}")

#Tickets for download
tickers = ['SPY', 'SCCO', 'GLD']
market_data = yf.download(tickers, start='2020-01-01', end=None)['Close']
print(market_data.tail())

monthly_returns = market_data.resample('M').last().pct_change() * 100
print(monthly_returns.tail())

# Limpieza rápida
macro_data.index = macro_data.index + pd.offsets.MonthEnd(0)
monthly_returns.index = monthly_returns.index + pd.offsets.MonthEnd(0)

# Unir las tablas (concat)
master_df = pd.concat([monthly_returns, macro_data], axis=1).dropna()

print("TABLA MAESTRA (Macro + Mercado):")
print(master_df.tail())

import seaborn as sns
import matplotlib.pyplot as plt

# Crear mapa de calor
plt.figure(figsize=(10, 8))
sns.heatmap(master_df.corr(), annot=True, cmap='vlag', fmt=".2f")
plt.title("Matriz de Correlación: Macroeconomía vs Activos")
plt.show()

import matplotlib.pyplot as plt
# Usaremos 24 meses (2 años) para capturar tendencias de mediano plazo
window_size = 24

# 2. Calcular las Correlaciones Móviles

# A) Tasa Fed vs SPY (Costo del dinero vs Acciones)
roll_fed_spy = master_df['Tasa Fed (%)'].rolling(window_size).corr(master_df['SPY'])

# B) Inflación vs Oro (Cobertura histórica)
roll_cpi_gld = master_df['Inflación (CPI)'].rolling(window_size).corr(master_df['GLD'])

# C) Desempleo vs Cobre (Economía Real vs Materias Primas)
roll_unemp_scco = master_df['Desempleo (%)'].rolling(window_size).corr(master_df['SCCO'])

# 3. Graficar
plt.figure(figsize=(12, 6))

# Trazar las líneas
plt.plot(roll_fed_spy, label='Tasa Fed vs SPY', linewidth=2, color='red')
plt.plot(roll_cpi_gld, label='Inflación vs Oro (GLD)', linewidth=2, color='gold')
plt.plot(roll_unemp_scco, label='Desempleo vs Cobre (SCCO)', linewidth=2, color='green')

# Estética
plt.axhline(0, color='black', linestyle='--', alpha=0.5) # Línea cero de referencia
plt.title(f'Evolución de Correlaciones (Ventana Móvil {window_size} meses)', fontsize=14)
plt.ylabel('Coeficiente de Correlación (-1 a 1)')
plt.legend(loc='lower left')
plt.grid(True, alpha=0.3)

# Ajustar límites para ver bien el detalle
plt.ylim(-1.1, 1.1)

plt.show()



### PARTE 2: Convalidar/confirmar hipótesis con data

import numpy as np
import matplotlib.pyplot as plt

# 1. Calcular Retornos Diarios (Usamos los datos diarios originales de Yahoo)
daily_returns = market_data.pct_change().dropna()

# 2. Definir ventana de volatilidad (63 días = 1 Trimestre fiscal aprox)
vol_window = 63

# 3. Calcular Desviación Estándar Móvil y Anualizar
rolling_vol = daily_returns.rolling(window=vol_window).std() * np.sqrt(252)

# 4. Graficar Comparativa de Riesgo
plt.figure(figsize=(12, 6))

# Graficamos SPY (Mercado) vs SCCO (Minera)
plt.plot(rolling_vol['SPY'], label='Volatilidad SPY (Mercado)', color='black', alpha=0.6, linewidth=1.5)
plt.plot(rolling_vol['SCCO'], label='Volatilidad SCCO (Cobre)', color='darkorange', linewidth=2)

# Estética
plt.title(f'Riesgo: Volatilidad Anualizada Móvil ({vol_window} días)', fontsize=14)
plt.ylabel('Volatilidad Anualizada (Desv. Std)')
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)

# Formato de porcentaje en eje Y
vals = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0%}'.format(x) for x in vals])

plt.show()

# 5. Imprimir Volatilidad Actual
print("Volatilidad Actual (Anualizada)")
print(rolling_vol.iloc[-1].round(4) * 100)



