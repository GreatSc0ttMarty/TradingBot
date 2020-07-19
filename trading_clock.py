import alpaca_trade_api as tradeapi
import trading_auth as ta



# tdocd: the api returns the object Clock() wrapping the is_open, 
# next_close, next_open, timestamp. str(clock)[7:-2].split(',') takes that, converts 
# it into a string and removes the Clock({}). split breaks the string data into seperate 
# parts. clo.lstrip().split(':', 1) cleans up the string before it's put into the dict.

clock = ta.api.get_clock()
tdocd = dict([clo.lstrip().split(':', 1) for clo in str(clock)[7:-2].split(',')])

class Time_Date:

    def is_open():
        # returns boolian response indicating if the market is currently open
        return tdocd["'is_open'"]


    def next_close():
        # returns time for next close
        return tdocd["'next_close'"]


    def next_open():
        # returns time for next_open
        return tdocd["'next_open'"]


    def timestamp():
        # returns current timestamp
        return tdocd["'timestamp'"]