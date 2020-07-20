from trading_clock import Time_Date as td
from trading_orders import Orders as o
import trading_auth

# TEST AREA
print(f"\nThe market is open:{td.is_open()}")
print(f"The market will open next on{td.next_open()}")
print(f"The market will close next on{td.next_close()}")
print(f"The current time and date is:{td.timestamp()}\n")

#o.buy("RUN")
#o.sell("GOOG")
#current_orders = o.view_current_orders("open")
#print(current_orders)
#print(o.list_positions())
print(o.list_orders())