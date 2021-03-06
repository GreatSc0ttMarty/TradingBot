import trading_auth as ta


api = ta.api

class Orders:

    def buy(stock):
        try:
            api.submit_order(
                symbol=stock,
                qty=1,
                side='buy',
                type='market',
                time_in_force='gtc'
            )
            print(f"Your order for {stock} has been executed.")
        except:
            print(f"Unable to place order for {stock} at this time!")


    def sell(stock):
        try:
            api.submit_order(
                symbol=stock,
                qty=1,
                side='sell',
                type='market',
                time_in_force='opg',
            )
        except:
            print(f"Unable to sell {stock} at this time!")
        

    def limite_sell(stock, limit):

        api.submit_order(
            symbol=stock,
            qty=1,
            side='sell',
            type='limit',
            time_in_force='opg',
            limit_price=limit
        )

    def view_current_orders(position, limit=500):
        api.list_orders(
            status=position,
            limit=limit,
            nested=True

        )

    def list_positions():
        return api.list_positions()

    def list_orders():
        return api.list_orders()
