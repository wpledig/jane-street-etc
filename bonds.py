import random

short = 1

def trade_bonds(exchange, log, buy, sell, add):
    if(len(buy) > 0 and buy[0][0] < 1000):
        buy_best = buy[0]
        price = buy_best[0]
        size = min(buy_best[1], log.max_buy("BOND"))
        return_val = add(exchange, random.randint(0, 2**32), "BOND", "BUY", price, size)

    if(len(sell) > 0 and sell[0][0] > 1000):
        sell_best = sell[0]
        price = sell_best[0]
        size = min(sell_best[1] if short else min(0, sell_best[0][1]), log.max_sell("BOND"))
        return_val = add(exchange, random.randint(0, 2**32), "BOND", "SELL", price, size)

def trade_bonds2(exchange, log, buy, sell, add):
    for order in buy:
        if(order[0] < 1000):
            size = min(order[1], log.max_buy("BOND"))
            return_val = add(exchange, random.randint(0, 2**32), "BOND", "BUY", order[0], size)

    for order in sell:
        if(order[0] > 1000):
            size = min(order[1], log.max_sell("BOND"))
            return_val = add(exchange, random.randint(0, 2**32), "BOND", "SELL", order[0], size)