import alpaca_trade_api as tradeapi
import trading_config as tc

if __name__ == "__main__":

    api = tradeapi.REST(
        tc.authentication["APCA-API-SECRET-ID"],
        tc.authentication["APCA-API-SECRET-KEY"],
        tc.authentication["API-URL"]
    )

clock = api.get_clock()

def time_date_info(clock):
    '''
    time_date_open_close_data: the api returns the object Clock() wrapping the is_open, 
    next_close, next_open, timestamp. str(clock)[7:-2].split(',') takes that, converts 
    it into a string and removes the Clock({}). split breaks the string data into seperate 
    parts. clo.lstrip().split(':', 1) cleans up the string before it's put into the dict.
    '''
    time_date_open_close_data = dict([clo.lstrip().split(':', 1) for clo in str(clock)[7:-2].split(',')])
    
    is_open = time_date_open_close_data["'is_open'"]
    next_close = time_date_open_close_data["'next_close'"]
    next_open = time_date_open_close_data["'next_open'"]
    timestamp = time_date_open_close_data["'timestamp'"]

    return is_open, next_open, next_close, timestamp


is_open, next_open, next_close, timestamp = time_date_info(clock)

print(is_open, next_open, next_close, timestamp)

#balance_change = float(account.equity) - float(account.last_equity)
#print("Today's balance change:", balance_change)

#print(account)