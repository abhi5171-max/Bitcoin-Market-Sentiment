# Bitcoin Market Sentiment & Trader Behavior Analysis

## Dataset Note

The original `historical_data.csv` file is not included in this repository because it exceeds GitHub’s file size limit. The analysis code and methodology remain fully reproducible using the provided scripts and dataset structure.


## Project Overview

This project analyzes the relationship between cryptocurrency market sentiment and trader performance using:

* Bitcoin Fear & Greed Index Dataset
* Historical Hyperliquid Trader Dataset

The objective is to understand how market emotions influence:

* Trading activity
* Profitability
* Win rate
* Risk exposure
* Trader behavior
* Asset-level performance

Using Python-based data analytics and visualization techniques, the project uncovers behavioral-finance insights and proposes actionable trading strategies.

---

# Dataset Information

## 1. Bitcoin Fear & Greed Dataset

### Features

* Timestamp
* Fear & Greed Value
* Sentiment Classification
* Date

### Sentiment Categories

* Extreme Fear
* Fear
* Neutral
* Greed
* Extreme Greed

---

## 2. Historical Trader Dataset

### Features

* Account
* Coin
* Execution Price
* Size Tokens
* Size USD
* Side
* Direction
* Closed PnL
* Fee
* Timestamp

The dataset contains over 200,000 cryptocurrency trades.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

# Methodology

## 1. Data Cleaning

* Converted timestamps into datetime format
* Standardized date columns
* Removed inconsistencies

## 2. Dataset Merging

Merged trader data with Fear & Greed sentiment data using daily timestamps.

## 3. Exploratory Data Analysis

Performed:

* profitability analysis
* volatility analysis
* win-rate analysis
* directional trading analysis
* trader segmentation
* correlation analysis

## 4. Visualization

Created multiple visualizations including:

* bar charts
* boxplots
* heatmaps
* profitability graphs
* trader ranking charts

---

# Key Findings

## Fear Markets

* Highest trading activity
* Highest total profitability
* Highest volatility
* Largest profit and loss outliers

## Greed Markets

* Highest average profit per trade
* More efficient trading conditions
* Strong profitability consistency

## Extreme Greed Markets

* Highest win rate
* Lower overall profitability
* Possible overconfidence and trend exhaustion

## Trader Behavior

* Profitability concentrated among elite traders
* Volatile markets amplify performance differences
* Strategic execution matters more than trade size alone

## Asset Performance

* Several altcoins outperformed Bitcoin in trader profitability
* High-volatility assets generated stronger opportunities

---

# Actionable Strategy Recommendations

## Strategy 1 — Fear Market Volatility Strategy

### Rule of Thumb

During Fear market conditions, traders should reduce leverage and focus on high-probability setups because Fear markets generate the highest volatility and largest loss outliers.

### Recommended Actions

* Reduce leverage exposure
* Use tighter stop-loss mechanisms
* Trade selectively during volatile periods
* Focus on experienced trader segments

---

## Strategy 2 — Greed Market Efficiency Strategy

### Rule of Thumb

During Greed market conditions, traders should moderately increase trade participation and prioritize trend-following strategies because Greed periods produced the highest average profit per trade.

### Recommended Actions

* Use momentum/trend-following strategies
* Increase participation in trending markets
* Maintain moderate leverage
* Avoid excessive exposure during Extreme Greed

---

# Charts Included

* Trade Count by Market Sentiment
* Average Closed PnL by Sentiment
* Total Closed PnL by Sentiment
* PnL Distribution Boxplot
* Win Rate by Sentiment
* Long vs Short Position Heatmap
* Top Traders by Profitability
* Top Coins by Profitability
* Correlation Heatmap

---

# Project Structure

```text
bitcoin-sentiment-analysis/
│
├── datapor.py
├── fear_greed_index.csv
├── historical_data.csv
├── merged_analysis.csv
├── README.md
├── report.pdf
├── charts/
│   ├── trade_count_sentiment.png
│   ├── average_pnl_sentiment.png
│   ├── total_pnl_sentiment.png
│   ├── pnl_distribution_boxplot.png
│   ├── win_rate_sentiment.png
│   ├── long_short_heatmap.png
│   ├── top_traders_pnl.png
│   ├── top_coins_profitability.png
│   └── correlation_heatmap.png
```

---

# How to Run

## Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn
```

## Run the Project

```bash
python datapor.py
```

---

# Sample Insights

* Fear markets created the highest cumulative profits due to increased participation.
* Greed markets produced the highest average profitability per trade.
* Extreme Greed generated higher win rates but lower profitability.
* Trader profitability was heavily concentrated among a small group of participants.
* Alternative cryptocurrencies outperformed Bitcoin in trader profitability.

---

# Future Improvements

Potential future enhancements include:

* Machine learning prediction models
* Trader clustering using K-Means
* Real-time sentiment integration
* Interactive Streamlit dashboard
* Risk-adjusted return analysis

---

# Conclusion

This project demonstrates that market sentiment significantly influences cryptocurrency trader behavior and profitability. Fear markets generated the highest activity and volatility, while Greed markets produced more efficient trading conditions.

The analysis also revealed that successful trading performance depends heavily on strategic execution, behavioral adaptation, and risk management rather than trade size alone.

Overall, the project highlights the importance of behavioral finance in cryptocurrency trading and demonstrates how sentiment analysis can provide valuable insights for understanding market dynamics.

---
