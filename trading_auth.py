import alpaca_trade_api as tradeapi
import trading_config as tc


api = tradeapi.REST(
    tc.authentication["APCA-API-SECRET-ID"],
    tc.authentication["APCA-API-SECRET-KEY"],
    tc.authentication["API-URL"]
)
