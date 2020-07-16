import alpaca_trade_api as tradeapi

if __name__ == "__main__":

    api = tradeapi.REST(

    )

#account = api.get_account()

clock = api.get_clock()

print(clock)

#CLOCK_RAW = str(clock)[7:-2].split(',')
'''
CLOCK_RAW: the api returns the object Clock() wrapping the is_open, next_close,
next_open, timestamp
Clock({})
'''

CLOCK_RAW = dict([clo.lstrip().split(':', 1) for clo in str(clock)[7:-2].split(',')])

print(CLOCK_RAW)
#print(CLOCK["is_open"])
#print(CLOCK["'next_close'"])
#print(CLOCK["'next_open'"])
#print(CLOCK["'timestamp'"])
#
#print('The market is {}.'.format('open.' if clock.is_open else 'closed.'))

#balance_change = float(account.equity) - float(account.last_equity)
#print("Today's balance change:", balance_change)

#print(account)