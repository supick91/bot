
from bot_huobi.models import HuobiBotProfit
# from huobi.client.market import MarketClient
from huobi.client.market import MarketClient
from huobi.utils import *
from huobi.constant import *
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR
import asyncio





def RunBot(first_asset, second_asset, third_asset, access_key, secret_key, ros, balance, first_qty, second_qty, third_qty):

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


    def callback(mbp_event: 'MbpFullEvent'):


        if mbp_event[1] == ('market.{}{}.mbp.refresh.5'.format(second_asset, first_asset)).lower():
            tick_1 = mbp_event[0]
            tick_ask_list = tick_1.get('asks')
            tick_ask = tick_ask_list[0]
            best_ask_price = tick_ask[0]
            vol_best_ask_price = tick_ask[1]
            first_order_ask.append(best_ask_price)
            first_order_vol.append(vol_best_ask_price)

        elif mbp_event[1] == ('market.{}{}.mbp.refresh.5'.format(second_asset, third_asset)).lower():
            tick_2 = mbp_event[0]
            tick_bid_list = tick_2.get('bids')
            tick_bid = tick_bid_list[0]
            best_first_bid_price = tick_bid[0]
            vol_best_first_bid_price = tick_bid[1]
            second_order_bid.append(best_first_bid_price)
            second_order_vol.append(vol_best_first_bid_price)

        elif mbp_event[1] == ('market.{}{}.mbp.refresh.5'.format(third_asset, first_asset)).lower():
            tick_3 = mbp_event[0]
            tick_bid_list = tick_3.get('bids')
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
                        print(f'Успешная сделка. Стартовый торговый баланс = {start_trade_amount} Финальный баланс = {third_coin}. {first_asset}>{second_asset}>{third_asset}')
                        text = f'Успешная сделка. Стартовый торговый баланс = {start_trade_amount} Финальный баланс = {third_coin}. {first_asset}>{second_asset}>{third_asset}'
                        bot_data = HuobiBotProfit(logs_deal=text)
                        bot_data.save()
                    # else:
                    #     print(f'Бот ищет профитные сделки. Стартовый торговый баланс = {start_trade_amount} Финальный баланс = {third_coin}. {first_asset}>{second_asset}>{third_asset}')
                except Exception as e:
                    print(e)

    
    def error(e: 'HuobiApiException'):
        print(e.error_code + e.error_message)

            
    market_client = MarketClient(init_log=False)
    market_client.sub_mbp_full(f"{second_asset.lower()}{first_asset.lower()},{second_asset.lower()}{third_asset.lower()},{third_asset.lower()}{first_asset.lower()}", MbpLevel.MBP5, callback, error)
