import datetime
import asyncio
from binance.client import Client
from binance.websockets import BinanceSocketManager
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR
from bot.models import BotProfit



def RunBot(first_asset, second_asset, third_asset, api, secret, ros, trade_balance, first_qty, second_qty, third_qty):

    if 0.01 < ros < 0.1:

        r_o_s = 1 + ros / 10


    else:

        r_o_s = 1 + ros / 100


    client = Client(api_key=api, api_secret=secret)
    bm = BinanceSocketManager(client)

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
            first_coin_brutto = (first_coin_netto * Decimal(1.001)).quantize(Decimal(f'{first_qty}'),
                                                                             ROUND_HALF_UP)
            return first_coin_netto

        else:
            first_coin_netto = ((Decimal(balance) / Decimal(ask)) * Decimal(0.998)).quantize(Decimal(f'{second_qty}'),
                                                                          ROUND_FLOOR)
            first_coin_brutto = (first_coin_netto * Decimal(1.001)).quantize(Decimal(f'{first_qty}'),
                                                                             ROUND_HALF_UP)
            return first_coin_netto


    def second_coin_amount(first_coin_neto, bid):
        global second_coin_brutto
        second_coin_no_round = first_coin_neto * Decimal(bid)
        second_coin_brutto = Decimal(second_coin_no_round).quantize(Decimal(third_qty), ROUND_FLOOR)
        second_coin_netto = (second_coin_brutto * Decimal(0.993)).quantize(Decimal(third_qty), ROUND_FLOOR)
        return second_coin_netto


    def third_coin_amount(second_coin, bid):
        second_coin_no_round = second_coin * Decimal(bid)
        third_coin_brutto = Decimal(second_coin_no_round).quantize(Decimal(f'{third_qty}'), ROUND_FLOOR)
        third_coin_netto = (third_coin_brutto * Decimal(0.999)).quantize(Decimal(f'{third_qty}'), ROUND_FLOOR)
        return third_coin_netto


    def process_m_message(msg):

            data = msg['data']
            symbol = data.get('s')

            if 'u' in data:

                if symbol == f'{second_asset}{first_asset}':
                    first_order_ask.append(data.get('a'))
                    first_order_vol.append(data.get('A'))


                elif symbol == f'{second_asset}{third_asset}':
                    second_order_bid.append(data.get('b'))
                    second_order_vol.append(data.get('B'))


                elif symbol == f'{third_asset}{first_asset}':
                    third_order_bid.append(data.get('b'))
                    third_order_vol.append(data.get('B'))

                    if len(first_order_ask) < 5 and len(second_order_bid) < 5 and len(third_order_bid) < 5:
                        pass
                    else:
                        try:
                            max_trade_amount = max_amount(first_order_vol[-1], first_order_ask[-1],
                                                          second_order_vol[-1],
                                                          third_order_vol[-1], third_order_bid[-1])

                            first_coin = first_coin_amount(max_trade_amount, first_order_ask[-1],
                                                            balance=trade_balance)

                            second_coin = second_coin_amount(first_coin, second_order_bid[-1])

                            third_coin = third_coin_amount(second_coin, third_order_bid[-1])

                            start_trade_amount = ((first_coin_brutto * Decimal(first_order_ask[-1])) * r_o_s).quantize(
                                Decimal(f'{third_qty}'), ROUND_FLOOR)


                            if third_coin > start_trade_amount > Decimal(12) < trade_balance and max_trade_amount > Decimal(12):

                                start_asset = client.get_asset_balance(f'{first_asset}')

                                client.order_market_buy(
                                    symbol=f'{second_asset}{first_asset}',
                                    quantity=first_coin_brutto)


                                s = client.get_asset_balance(f'{second_asset}')
                                s = Decimal(s.get('free')).quantize(Decimal(f'{second_qty}'), ROUND_FLOOR)
                                client.order_market_sell(
                                    symbol=f'{second_asset}{third_asset}',
                                    quantity=s)


                                th = client.get_asset_balance(f'{third_asset}')
                                th = Decimal(th.get('free')).quantize(Decimal(f'{third_qty}'), ROUND_FLOOR)
                                client.order_market_sell(
                                    symbol=f'{third_asset}{first_asset}',
                                    quantity=th)

                                finish_asset = client.get_asset_balance(f'{first_asset}')
                                #
                                text = 'Время: {}. Успешная сделка! Стартовый баланс = {}, окончательный баланс = {}, {}>{}>{} || первая валюта брутто {} первая валюта нетто {} вторая валюта {} третья валюта {}, ПЕРВЫЙ АСК {} ПЕРВЫЙ БИД {} ВТОРОЙ БИД{}'.format(datetime.datetime.now(), start_asset, finish_asset, first_asset, second_asset, third_asset, first_coin_brutto, first_coin, second_coin, third_coin, first_order_ask[-1], second_order_bid[-1], third_order_bid[-1])
                                bot_data = BotProfit(logs_deal=text)
                                bot_data.save()
                                    # # print(f'first_coin_netto {first_coin_netto}')
                                    # # print(f'first_coin_brutto {first_coin}')
                                    # # print(f'second_coin {second_coin}')
                            # else:
                            #     print(f'Бот ищет профитную сделку направления {first_asset} > {second_asset} > {third_asset}. Стартовый баланс: {start_trade_amount}, финальный: {third_coin}')
                        except Exception:
                            pass




    conn_key = bm.start_multiplex_socket([f'{second_asset.lower()}{first_asset.lower()}@bookTicker',
                                          f'{second_asset.lower()}{third_asset.lower()}@bookTicker',
                                          f'{third_asset.lower()}{first_asset.lower()}@bookTicker',
                                          ],
                                         process_m_message)

    bm.start()
