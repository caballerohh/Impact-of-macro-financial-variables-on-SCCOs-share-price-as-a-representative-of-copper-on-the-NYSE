# Impact-of-macro-financial-variables-on-SCCOs-share-price-as-a-representative-of-copper-on-the-NYSE
This code is supplementary material for a research project, which describes how macro-financial variables impact the price of $SCCO as a proxy for copper. Modify parameters to adapt to a specific stock.

This repository features a Python-based analytical engine designed to merge macroeconomic indicators with financial market data. The project quantifies the relationship between "Real Economy" variables—such as inflation and interest rates—and the performance of equities and commodities, providing a holistic view of market drivers.
Objective: To automate the extraction of multi-source financial data and apply advanced statistical techniques (Rolling Correlations and Annualized Volatility) to identify macroeconomic regimes.
Extended Version

The system integrates high-frequency market data from Yahoo Finance with low-frequency macroeconomic series from the Federal Reserve Economic Data (FRED). By synchronizing these datasets into a unified "Master Table," the project enables the study of cross-asset dynamics, such as the effectiveness of Gold as an inflation hedge and the impact of Fed interest rate cycles on equity market risk.

Key Objectives of the Analysis
•	Macro-Market Synchronization: Automated data pipeline that aligns disparate frequencies (daily market prices vs. monthly macro data) using resampling and time-offset techniques.
•	Rolling Correlation Dynamics: Implementation of 24-month rolling windows to track the evolution of historical hedges (e.g., Inflation vs. Gold) and sensitivity to capital costs (Fed Funds Rate vs. SPY).
•	Multi-Asset Risk Assessment: Calculation of 63-day (quarterly) rolling annualized volatility to compare systematic market risk against idiosyncratic commodity risk (Copper/SCCO).
•	Statistical Visualization: Generation of comprehensive heatmaps and multi-subplot time series to isolate trends in unemployment, CPI, and interest rates.

Assets & Indicators Analyzed
•	Macro Indicators (FRED): Consumer Price Index (CPIAUCSL), Unemployment Rate (UNRATE), and Effective Federal Funds Rate (FEDFUNDS).
•	Financial Assets (Yahoo Finance):
o	Equities: SPY (S&P 500) and SCCO (Southern Copper Corp) for industrial exposure.
o	Commodities: GLD (Gold) as a defensive/inflation-linked asset.

Key Portfolio & Macro Results
•	Risk Regimes: The engine identified a significant volatility gap, with SCCO (38.49%) exhibiting more than triple the annualized risk of the SPY benchmark (11.47%) by early 2026.
•	Macro Correlations:
o	Inflation vs. Interest Rates: A strong positive correlation (0.88) between CPI and the Fed Funds Rate, reflecting active monetary policy response.
o	Monetary Policy Impact: An inverse relationship (-0.63) between Unemployment and the Fed Funds Rate, validating the Phillips Curve dynamics within the analyzed period.
•	Market Efficiency: Gold (GLD) demonstrated a moderate positive correlation (0.21) with Inflation, acting as a partial hedge during the 2020-2025 cycle.

Code Structure & Pipeline
•	Data Extraction: Utilizes pandas_datareader for FRED API and yfinance for equity markets.
•	Feature Engineering: Implementation of monthly percentage changes and data cleaning through dropna() and resample() to maintain statistical integrity.
•	Statistical Core: * rolling().corr(): Computes dynamic relationships over a 24-month window.rolling().std() * np.sqrt(252): Standardizes daily returns into annualized risk metrics.
•	Visualization Stack: Uses Seaborn for correlation heatmaps and Matplotlib for synchronized macro trend plotting.

Technologies/Concepts Used
•	Macroeconometrics: Monetary Policy Analysis, Inflation Hedging, and Business Cycle tracking.
•	Quantitative Finance: Rolling Volatility, Cross-Asset Correlation, and Returns Analysis.
•	Python Stack: Pandas (Advanced Resampling), NumPy (Mathematical Vectorization), Seaborn (Statistical Viz), Matplotlib.
•	Data Engineering: API Integration (FRED & Yahoo Finance), Time-Series Synchronization.
