


# ============================================
# BITCOIN MARKET SENTIMENT VS TRADER ANALYSIS
# ============================================

# ---------- IMPORT LIBRARIES ----------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------- LOAD DATASETS ----------
fear_greed = pd.read_csv(r"C:\Users\AbhinavShivang\OneDrive\Desktop\pythonfile\dataprocessassignment\fear_greed_index.csv")
trades = pd.read_csv(r"C:\Users\AbhinavShivang\OneDrive\Desktop\pythonfile\dataprocessassignment\historical_data.csv")

# ---------- DISPLAY BASIC INFO ----------
print("\n========== FEAR & GREED DATA ==========\n")
print(fear_greed.head())
print(fear_greed.info())

print("\n========== TRADER DATA ==========\n")
print(trades.head())
print(trades.info())

# ============================================
# DATA CLEANING
# ============================================

# ---------- CONVERT DATES ----------
fear_greed['date'] = pd.to_datetime(
    fear_greed['date']
).dt.date

# Convert Unix timestamp (milliseconds) to datetime
trades['Timestamp'] = pd.to_datetime(
    trades['Timestamp'],
    unit='ms'
)

trades['date'] = trades['Timestamp'].dt.date

# ---------- CHECK MISSING VALUES ----------
print("\n========== MISSING VALUES ==========\n")
print(fear_greed.isnull().sum())
print(trades.isnull().sum())

# ============================================
# MERGE DATASETS
# ============================================

merged = trades.merge(
    fear_greed[['date', 'classification', 'value']],
    on='date',
    how='left'
)

print("\n========== MERGED DATA ==========\n")
print(merged.head())

# ---------- CHECK MERGE SUCCESS ----------
missing_sentiment = merged['classification'].isnull().sum()

print("\nMissing Sentiment Rows:", missing_sentiment)

# ============================================
# BASIC ANALYSIS
# ============================================

# ---------- AVERAGE PNL BY SENTIMENT ----------
print("\n========== AVERAGE PNL BY SENTIMENT ==========\n")

avg_pnl = (
    merged.groupby('classification')['Closed PnL']
    .mean()
    .sort_values(ascending=False)
)

print(avg_pnl)

# ---------- TOTAL PNL BY SENTIMENT ----------
print("\n========== TOTAL PNL BY SENTIMENT ==========\n")

total_pnl = (
    merged.groupby('classification')['Closed PnL']
    .sum()
    .sort_values(ascending=False)
)

print(total_pnl)

# ---------- NUMBER OF TRADES ----------
print("\n========== NUMBER OF TRADES ==========\n")

trade_count = merged['classification'].value_counts()

print(trade_count)

# ---------- WIN RATE ----------
merged['Win'] = merged['Closed PnL'] > 0

win_rate = (
    merged.groupby('classification')['Win']
    .mean() * 100
)

print("\n========== WIN RATE (%) ==========\n")
print(win_rate)

# ---------- AVERAGE TRADE SIZE ----------
avg_trade_size = (
    merged.groupby('classification')['Size USD']
    .mean()
)

print("\n========== AVERAGE TRADE SIZE ==========\n")
print(avg_trade_size)

# ============================================
# LONG VS SHORT ANALYSIS
# ============================================

print("\n========== LONG VS SHORT ==========\n")

long_short = pd.crosstab(
    merged['classification'],
    merged['Direction']
)

print(long_short)

# ============================================
# VISUALIZATIONS
# ============================================

sns.set_style("darkgrid")

# ---------- 1. SENTIMENT DISTRIBUTION ----------
plt.figure(figsize=(10, 6))

sns.countplot(
    x='classification',
    data=merged,
    order=merged['classification'].value_counts().index
)

plt.title("Trade Count by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Number of Trades")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ---------- 2. AVERAGE PNL ----------
plt.figure(figsize=(10, 6))

avg_pnl.plot(kind='bar')

plt.title("Average Closed PnL by Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Average Closed PnL")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ---------- 3. TOTAL PNL ----------
plt.figure(figsize=(10, 6))

total_pnl.plot(kind='bar')

plt.title("Total Closed PnL by Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Total Closed PnL")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ---------- 4. BOXPLOT ----------
plt.figure(figsize=(12, 6))

sns.boxplot(
    x='classification',
    y='Closed PnL',
    data=merged
)

plt.title("Closed PnL Distribution by Market Sentiment")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ---------- 5. WIN RATE ----------
plt.figure(figsize=(10, 6))

win_rate.plot(kind='bar')

plt.title("Win Rate by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Win Rate (%)")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ---------- 6. LONG VS SHORT HEATMAP ----------
plt.figure(figsize=(10, 6))

sns.heatmap(
    long_short,
    annot=True,
    fmt='d',
    cmap='Blues'
)

plt.title("Long vs Short Positions by Sentiment")

plt.tight_layout()
plt.show()

# ============================================
# TOP TRADERS ANALYSIS
# ============================================

top_traders = (
    merged.groupby('Account')['Closed PnL']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 TRADERS ==========\n")
print(top_traders)

# ---------- TOP TRADERS VISUALIZATION ----------
plt.figure(figsize=(12, 6))

top_traders.plot(kind='bar')

plt.title("Top 10 Traders by Total Closed PnL")
plt.xlabel("Trader Account")
plt.ylabel("Total Closed PnL")

plt.xticks(rotation=75)

plt.tight_layout()
plt.show()

# ============================================
# COIN ANALYSIS
# ============================================

coin_pnl = (
    merged.groupby('Coin')['Closed PnL']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP COINS BY PNL ==========\n")
print(coin_pnl)

# ---------- COIN VISUALIZATION ----------
plt.figure(figsize=(12, 6))

coin_pnl.plot(kind='bar')

plt.title("Top Coins by Total Closed PnL")
plt.xlabel("Coin")
plt.ylabel("Total Closed PnL")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# ============================================
# CORRELATION ANALYSIS
# ============================================

numeric_cols = [
    'Execution Price',
    'Size Tokens',
    'Size USD',
    'Closed PnL',
    'Fee',
    'value'
]

correlation = merged[numeric_cols].corr()

print("\n========== CORRELATION MATRIX ==========\n")
print(correlation)

# ---------- CORRELATION HEATMAP ----------
plt.figure(figsize=(10, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

# ============================================
# FINAL INSIGHTS
# ============================================

print("\n========== FINAL INSIGHTS ==========\n")

best_sentiment = avg_pnl.idxmax()
worst_sentiment = avg_pnl.idxmin()

print(f"Best average trader profitability occurred during: {best_sentiment}")

print(f"Worst average trader profitability occurred during: {worst_sentiment}")

highest_volume = trade_count.idxmax()

print(f"Most trading activity occurred during: {highest_volume}")

best_win_rate = win_rate.idxmax()

print(f"Highest trader win rate occurred during: {best_win_rate}")

print("\nAnalysis Completed Successfully!")