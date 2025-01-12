from services.coingecko_service import CoinGecko
from services.exchange_service import Binance
from services.saving_service import SavingService
from utils.load_config import config
from utils.logger import logging
import time


# Initialize Our services
cg = CoinGecko()
exchange = Binance()
trades = SavingService("assets/trades.json")
portfolio = SavingService("assets/portfolio.json")

print(
    "THIS BOT WILL PLACE LIVE ORDERS. Use the Keyboard interrupt (Ctrl + C or Cmd + C) to cancel execution. Waiting 10s before starting execution..."
)
time.sleep(10)


def main():
    # Set the Trading mode
    if config.mode == "GAINING":
        all_assets = cg.get_top_gainers_and_losers().top_gainers
        logging.info(f"Trading the {config.number_of_assets} Top Gaining assets")
    elif config.mode == "LOSING":
        all_assets = cg.get_top_gainers_and_losers().top_losers
        logging.info(f"Trading the {config.number_of_assets} Top Losing assets")
    else:
        logging.error(
            f"Invalid mode, please choose between GAINING and LOSING in config.json "
        )

    # If your number of assets is set to 5, we will trade the 5 most volatilte assets
    top_assets = all_assets[0 : config.number_of_assets]

    # BUY Logic
    for asset in top_assets:
        try:
            res = exchange.buy(asset.symbol.upper(), config.amount, config.vs_currency)
            # Saving the order to Orders and Trades. We log the trade for historical purposes, and we add our order to our portfolio so we know what we hold.
            portfolio.save_order(res)
            trades.save_order(res)
            logging.info(
                f"Bought {res.executedQty} {res.symbol} at ${res.fills[0].price}. "
            )
        except Exception as e:
            logging.error(f"COULD NOT BUY {asset.symbol}: {e} ")

    # Update TP / SL and SELL Logic
    all_portfolio_assets = portfolio.load_orders()
    for order in all_portfolio_assets:
        original_price = float(order.fills[0].price)
        current_price = exchange.get_current_price(order.symbol)
        current_pnl = (current_price - original_price) / original_price * 100

        if current_pnl > config.take_profit or current_pnl < config.stop_loss:
            logging.info(
                f"SELL signal generated for {order.executedQty} {order.symbol} with order Id {order.orderId}"
            )
            # the summed up fees from all fills
            fees = sum([float(item.commission) for item in order.fills])

            try:
                amount_in_vs_currency = round(
                    current_price * (float(order.executedQty) - fees), 4
                )
                res = exchange.sell(order.symbol.upper(), amount_in_vs_currency)

                trades.save_order(res)
                portfolio.delete_order(order.orderId)
                logging.info(
                    f"SOLD {res.executedQty} {res.symbol} at ${res.fills[0].price}. "
                )
            except Exception as e:
                logging.error(
                    f"COULD NOT SELL {order.executedQty} {order.symbol}: {e} "
                )


if __name__ == "__main__":
    while True:
        main()
        logging.info(
            f"Successfully completed bot cycle, waiting {config.bot_frequency_in_seconds} seconds before re-running..."
        )
        time.sleep(config.bot_frequency_in_seconds)
