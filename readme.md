# Crypto Trading bot for Top Losing or Gaining Coins

This is a Python-based cryptocurrency trading bot designed to automate trading for highly volatile crypto assets. Whether you focus on **top gainers** or **top losers**, this bot uses CoinGecko's API to identify the top gaining and top losing coins by price change and trade the most volatile ones, in each direction you choose. It comes with a basic Stop Loss and Take Profit and it works with the Binance API. 

---

## Features

- **Dynamic Trading Strategies**: Switch between trading top gaining or losing assets.
- **Customisable Settings**: Configure stop-loss, take-profit, trade amounts, bot frequency.

---

## Limitations
Currently, the take profit and stop loss checks are performed once per bot cycle, which could lead to delays in responding to market changes. To improve this, a separate thread could be introduced for monitoring these conditions independently of the buy logic, allowing faster reactions in volatile markets. Additionally, the bot currently lacks a test mode, but this could be considered for future updates. Always ensure your config.json aligns with your strategy and risk tolerance, and trade responsibly.