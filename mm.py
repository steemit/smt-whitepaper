#!/usr/bin/env python3

# (c) 2017 Steemit, Inc.  All rights reserved
# CONFIDENTIAL - STEEMIT INTERNAL USE ONLY

import decimal

class Order(object):
    def __init__(self, price=1, q_token=1, is_sell=False, tchar=" "):
        self.price = decimal.Decimal(price)
        self.q_token = decimal.Decimal(q_token)
        self.q_steem = self.price * self.q_token
        self.is_sell = is_sell
        self.tchar = tchar
        return

class Book(object):
    def __init__(self):
        self.bids = []
        self.asks = []
        return

    def sort_bids(self):
        self.bids.sort(key=lambda bid : -bid.price)

    def sort_asks(self):
        self.asks.sort(key=lambda ask : ask.price)

    def buy(self, price=1, qty=1):
        self.bids.append( Order(price=price, q_token=qty, is_sell=False) )
        self.sort_bids()
        return

    def sell(self, price=1, qty=1):
        self.asks.append( Order(price=price, q_token=qty, is_sell=True) )
        self.sort_asks()
        return

    def to_string(self):
        def get_max_length(f):
            return max(len("{:.6f}".format(f(order))) for order in self.bids+self.asks)
        price_max = get_max_length(lambda order : order.price)
        q_token_max = get_max_length(lambda order : order.q_token)
        q_steem_max = get_max_length(lambda order : order.q_steem)

        total_length = price_max + q_token_max + q_steem_max + 7

        title_fstr = "| {{:{total_length}}} |".format(**locals())
        heading_fstr = "| {{:{price_max}}}  | {{:{q_token_max}}} | {{:{q_steem_max}}} |".format(**locals())
        fstr = "| {{}}{{:{price_max}.6f}} | {{:{q_token_max}.6f}} | {{:{q_steem_max}.6f}} |".format(**locals())

        asks_book = []
        asks_book.append(title_fstr.format("ASKS"))
        asks_book.append(heading_fstr.format("p", "q_token", "q_steem"))
        for a in self.asks:
            asks_book.append(fstr.format(a.tchar, a.price, a.q_token, a.q_steem))

        bids_book = []
        bids_book.append(title_fstr.format("BIDS"))
        bids_book.append(heading_fstr.format("p", "q_token", "q_steem"))
        for b in self.bids:
            bids_book.append(fstr.format(b.tchar, b.price, b.q_token, b.q_steem))
        result = ""
        for i in range(max(len(asks_book), len(bids_book))):
            if i >= len(asks_book):
                a = " " * len(asks_book[-1])
            else:
                a = asks_book[i]
            if i >= len(bids_book):
                b = " " * len(bids_book[-1])
            else:
                b = bids_book[i]

            result += a+"      "+b+"\n"


        return result

book = Book()
book.buy("0.1", 1000)
book.buy("0.09", 2000)
book.buy("0.08", 750)
book.sell("0.11", 500)
book.sell("0.115", 750)
print(book.to_string())
