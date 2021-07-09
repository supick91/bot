
from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.utils.input_checker import format_date


# ACCESS_KEY = 'f5b12b8e-60f1b783-1hrfj6yhgg-a1a64'
# SECRET_KEY = 'ddb2a042-aa4ede09-2ee1b5aa-57382'

# last_ask_price, last_bid_price_ada_eth, last_bid_price_eth_usdt = [], [], []


from huobi.web_socket import subscribe
from functools import partial
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR
import asyncio
import json
import gzip




def RunBot(first_asset, second_asset, third_asset, ros, balance, first_qty, second_qty, third_qty):

    if 0.01 < ros < 0.1:

        r_o_s = 1 + ros / 10


    else:

        r_o_s = 1 + ros / 100

    ACCESS_KEY = 'f5b12b8e-60f1b783-1hrfj6yhgg-a1a64'
    SECRET_KEY = 'ddb2a042-aa4ede09-2ee1b5aa-57382'


    [first_order_ask, first_order_vol, second_order_bid, second_order_vol, third_order_bid,
     third_order_vol] = [], [], [], [], [], []


    def max_amount(first_vol, first_ask, second_vol, third_vol, third_bid):
        if Decimal(first_vol) * Decimal(first_ask) >= Decimal(second_vol) * Decimal(first_ask) >= Decimal(
                third_bid) * Decimal(third_vol):
            return Decimal(third_vol) * Decimal(third_bid)
        elif Decimal(first_vol) * Decimal(first_ask) <= Decimal(second_vol) * Decimal(first_ask) <= Decimal(
                third_bid) * Decimal(third_vol):
            return Decimal(first_vol) * Decimal(first_ask)
        elif Decimal(third_vol) * Decimal(third_bid) >= Decimal(second_vol) * Decimal(first_ask) and Decimal(
                second_vol) * Decimal(first_ask) <= Decimal(third_bid) * Decimal(third_vol):
            return Decimal(second_vol) * Decimal(first_ask)
        elif Decimal(first_vol) * Decimal(first_ask) <= Decimal(second_vol) * Decimal(first_ask) >= Decimal(
                third_bid) * Decimal(third_vol):
            if Decimal(first_vol) * Decimal(first_ask) >= Decimal(third_bid) * Decimal(third_vol):
                return Decimal(third_bid) * Decimal(third_vol)
            else:
                return Decimal(first_vol) * Decimal(first_ask)
    

    def first_coin_amount(trade_amount, ask, balance):
        global first_coin_brutto
        if Decimal(trade_amount) <= Decimal(balance):
            first_coin_netto = ((Decimal(trade_amount) / Decimal(ask)) * Decimal(0.998)).quantize(Decimal(f'{second_qty}'),
                                                                               ROUND_FLOOR)
            first_coin_brutto = (first_coin_netto * Decimal(1.002)).quantize(Decimal(f'{first_qty}'),
                                                                             ROUND_HALF_UP)
            return first_coin_netto

        else:
            first_coin_netto = ((Decimal(balance) / Decimal(ask)) * Decimal(0.998)).quantize(Decimal(f'{second_qty}'),
                                                                          ROUND_FLOOR)
            first_coin_brutto = (first_coin_netto * Decimal(1.002)).quantize(Decimal(f'{first_qty}'),
                                                                             ROUND_HALF_UP)
            return first_coin_netto


    def second_coin_amount(first_coin_neto, bid):
        second_coin_no_round = first_coin_neto * Decimal(bid)
        second_coin_brutto = Decimal(second_coin_no_round).quantize(Decimal(third_qty), ROUND_FLOOR)
        second_coin_netto = (second_coin_brutto * Decimal(0.998)).quantize(Decimal(third_qty), ROUND_FLOOR)
        return second_coin_netto


    def third_coin_amount(second_coin, bid):
        second_coin_no_round = second_coin * Decimal(bid)
        third_coin_brutto = Decimal(second_coin_no_round).quantize(Decimal(f'{third_qty}'), ROUND_FLOOR)
        third_coin_netto = (third_coin_brutto * Decimal(0.998)).quantize(Decimal(f'{third_qty}'), ROUND_FLOOR)
        return third_coin_netto


    async def callback(callback_data):


        if callback_data['ch'] == ('market.{}{}.mbp.refresh.10'.format(second_asset, first_asset)).lower():
            tick_1 = callback_data['tick']
            tick_ask_list = tick_1['asks']
            tick_ask = tick_ask_list[0]
            best_ask_price = tick_ask[0]
            vol_best_ask_price = tick_ask[1]
            first_order_ask.append(best_ask_price)
            first_order_vol.append(vol_best_ask_price)

        elif callback_data['ch'] == ('market.{}{}.mbp.refresh.10'.format(second_asset, third_asset)).lower():
            tick_2 = callback_data['tick']
            tick_bid_list = tick_2['bids']
            tick_bid = tick_bid_list[0]
            best_first_bid_price = tick_bid[0]
            vol_best_first_bid_price = tick_bid[1]
            second_order_bid.append(best_first_bid_price)
            second_order_vol.append(vol_best_first_bid_price)

        elif callback_data['ch'] == ('market.{}{}.mbp.refresh.10'.format(third_asset, first_asset)).lower():
            tick_3 = callback_data['tick']
            tick_bid_list = tick_3['bids']
            tick_bid = tick_bid_list[0]
            best_second_bid_price = tick_bid[0]
            vol_best_second_bid_price = tick_bid[1]
            third_order_bid.append(best_second_bid_price)
            third_order_vol.append(vol_best_second_bid_price)


            if len(first_order_ask) < 1 and len(second_order_bid) < 1 and len(third_order_bid) < 1:
                print('Please wait...bot load')
            else:
                try:  
                    max_trade_amount = max_amount(first_order_vol[-1], first_order_ask[-1],
                                                          second_order_vol[-1],
                                                          third_order_vol[-1], third_order_bid[-1])

                    first_coin = first_coin_amount(max_trade_amount, first_order_ask[-1],
                                                    balance)

                    second_coin = second_coin_amount(first_coin, second_order_bid[-1])

                    third_coin = third_coin_amount(second_coin, third_order_bid[-1])

                    start_trade_amount = ((first_coin_brutto * Decimal(first_order_ask[-1])) * r_o_s).quantize(
                        Decimal(f'{third_qty}'), ROUND_FLOOR)


                    if third_coin > start_trade_amount > Decimal(12) < balance and max_trade_amount > Decimal(12):
                        print(f'Deal done! Soon you will be reach. START BALANCE = {start_trade_amount} FINAL BALANCE = {third_coin}')
                    else:
                        print(f'DEAL NOT PROFIT. START BALANCE = {start_trade_amount} FINAL BALANCE = {third_coin}')
                except Exception as e:
                    print(e)



    task = subscribe({
                ('market.{}{}.mbp.refresh.10'.format(second_asset, first_asset)).lower(): {
                    'callback': callback
                },
                ('market.{}{}.mbp.refresh.10'.format(second_asset, third_asset)).lower(): {
                    'callback': callback
                },
                ('market.{}{}.mbp.refresh.10'.format(third_asset, first_asset)).lower(): {
                    'callback': callback
                }
            })

            
    asyncio.get_event_loop().run_until_complete(task)
