import trading_auth as ta

api = ta.api

class Orders:

    def buy(stock):

        api.submit_order(
            symbol=stock,
            qty=1,
            side='buy',
            type='market',
            time_in_force='gtc'
        )

    def limited_buy(stock, limit):

        api.submit_order(
            symbol=stock,
            qty=1,
            side='sell',
            type='limit',
            time_in_force='opg',
            limit_price=limit
        )
        
Orders.order("GOOG")