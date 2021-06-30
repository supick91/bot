import datetime
from binance.client import Client
from binance.websockets import BinanceSocketManager
from decimal import Decimal, ROUND_HALF_UP, ROUND_FLOOR
from bot.models import BotProfit



def RunBot(first_asset, second_asset, third_asset, api, secret, ros, trade_balance):

    if 0.01 < ros < 0.1:

        r_o_s = 1 + ros / 10


    else:

        r_o_s = 1 + ros / 100


    client = Client(api_key=api, api_secret=secret)
    bm = BinanceSocketManager(client)

    [first_order_ask, first_order_vol, second_order_bid, second_order_vol, third_order_bid,
     third_order_vol, quantity_1, quantity_2, quantity_3] = [], [], [], [], [], [], [], [], []


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

    def first_coin_amount(trade_amount, ask, minQty2, balance):
        global first_coin_netto, first_coin_brutto
        if Decimal(trade_amount) <= Decimal(balance):
            first_coin_netto = (Decimal(trade_amount) / Decimal(ask)).quantize(Decimal(f'{minQty2}'),
                                                                               ROUND_FLOOR)
            # first_coin_brutto = (first_coin_netto * Decimal(1.001)).quantize(Decimal(f'{minQty1}'),
            #                                                                  ROUND_FLOOR)
            return first_coin_netto

        else:
            first_coin_netto = (Decimal(balance) / Decimal(ask)).quantize(Decimal(f'{minQty2}'),
                                                                          ROUND_FLOOR)
            # first_coin_brutto = (first_coin_netto * Decimal(1.001)).quantize(Decimal(f'{minQty1}'),
            #                                                                  ROUND_FLOOR)
            return first_coin_netto


    def second_coin_amount(first_coin, bid, minQty):
        global second_coin_brutto
        second_coin_no_round = first_coin * Decimal(bid)
        second_coin_brutto = Decimal(second_coin_no_round).quantize(Decimal(minQty), ROUND_FLOOR)
        second_coin_netto = (second_coin_brutto * Decimal(0.999)).quantize(Decimal(minQty), ROUND_FLOOR)
        return second_coin_netto


    def third_coin_amount(second_coin, bid, minQty):
        second_coin_no_round = second_coin * Decimal(bid)
        third_coin_brutto = Decimal(second_coin_no_round).quantize(Decimal(f'{minQty}'), ROUND_FLOOR)
        third_coin_netto = (third_coin_brutto * Decimal(0.999))
        return third_coin_netto


    def min_qty(list):
        minimum = max(list)
        return minimum


    def process_m_message(msg):

            data = msg['data']
            symbol = data.get('s')

            if 'q' in data:

                if symbol == f'{second_asset}{first_asset}':
                    quantity_1.append(data.get('q'))
                elif symbol == f'{second_asset}{third_asset}':
                    quantity_2.append(data.get('q'))
                elif symbol == f'{third_asset}{first_asset}':
                    quantity_3.append(data.get('q'))

            elif 'u' in data:

                if symbol == f'{second_asset}{first_asset}':
                    first_order_ask.append(data.get('a'))
                    first_order_vol.append(data.get('A'))


                elif symbol == f'{second_asset}{third_asset}':
                    second_order_bid.append(data.get('b'))
                    second_order_vol.append(data.get('B'))


                elif symbol == f'{third_asset}{first_asset}':
                    third_order_bid.append(data.get('b'))
                    third_order_vol.append(data.get('B'))

                    if len(first_order_ask) < 25 and len(second_order_bid) < 25 and len(third_order_bid) < 25:
                        print('Loading data...')
                    else:

                        try:
                            first_minQty = min_qty(quantity_1[:20])
                            first_minQty = first_minQty.rstrip('0').split('.')
                            if len(first_minQty[1]) == 0:
                                first_minQty = '1.'
                            else:
                                first_minQty = len(first_minQty[1])
                                first_minQty = '1.' + first_minQty * '0'


                            second_minQty = min_qty(quantity_2[:20])
                            second_minQty = second_minQty.rstrip('0').split('.')
                            if len(second_minQty[1]) == 0:
                                second_minQty = '1.'
                            else:
                                second_minQty = len(second_minQty[1])
                                second_minQty = '1.' + second_minQty * '0'


                            third_minQty = min_qty(quantity_3[:20])
                            third_minQty = third_minQty.rstrip('0').split('.')
                            if len(third_minQty[1]) == 0:
                                third_minQty = ''
                            else:
                                third_minQty = len(third_minQty[1])
                                third_minQty = '1.' + third_minQty * '0'

                                if len(first_order_ask) < 0 and len(second_order_bid) < 0 and len(third_order_bid) < 0:
                                    print('Please wait...bot load')

                                else:
                                    max_trade_amount = max_amount(first_order_vol[-1], first_order_ask[-1],
                                                                  second_order_vol[-1],
                                                                  third_order_vol[-1], third_order_bid[-1])

                                    first_coin = (first_coin_amount(max_trade_amount, first_order_ask[-1], second_minQty,
                                                                    balance=trade_balance) * Decimal(1.001)).quantize(Decimal(f'{second_minQty}0'))

                                    second_coin = second_coin_amount(first_coin_netto, second_order_bid[-1],
                                                                     third_minQty)

                                    third_coin = third_coin_amount(second_coin, third_order_bid[-1],
                                                                   third_minQty).quantize(Decimal(f'{third_minQty}'),
                                                                                          ROUND_FLOOR)

                                    start_trade_amount = (first_coin * Decimal(first_order_ask[-1]) * r_o_s).quantize(
                                        Decimal(f'{third_minQty}'), ROUND_FLOOR)

                                    if third_coin > start_trade_amount > Decimal(12) < trade_balance and max_trade_amount > Decimal(
                                            12):
                                        # start_asset = client.get_asset_balance(f'{first_asset}')
                                        # client.order_market_buy(
                                        #     symbol=f'{second_asset}{first_asset}',
                                        #     quantity=first_coin)
                                        # s = client.get_asset_balance(f'{second_asset}')
                                        # s = Decimal(s.get('free')).quantize(Decimal(f'{first_minQty}'), ROUND_FLOOR)
                                        # client.order_market_sell(
                                        #     symbol=f'{second_asset}{third_asset}',
                                        #     quantity=s)
                                        # th = client.get_asset_balance(f'{third_asset}')
                                        # th = Decimal(th.get('free')).quantize(Decimal(f'{third_minQty}'), ROUND_FLOOR)
                                        # client.order_market_sell(
                                        #     symbol=f'{third_asset}{first_asset}',
                                        #     quantity=th)
                                        # finish_asset = client.get_asset_balance(f'{first_asset}')

                                        text = 'Время: {}. Успешная сделка! Стартовый баланс = {}, окончательный баланс = {}, {}>{}>{}, первая валюта neto {}, первая валюта brutto {}, вторая валюта {} first ask {}, second {}, third bid {}, secon qty {}, first qty {}'.format(datetime.datetime.now(), start_trade_amount, third_coin, first_asset, second_asset, third_asset, first_coin_netto, first_coin, second_coin, first_order_ask[-1], second_order_bid[-1], third_order_bid[-1], second_minQty, first_minQty)
                                        bot_data = BotProfit(logs_deal=text)
                                        bot_data.save()
                                        # print(f'first_coin_brutto {first_coin_brutto}')
                                        # print(f'first_coin {first_coin}')
                                        # print(f'second_coin {second_coin}')
                                    # else:
                                    #     print(first_coin, first_coin_netto)
                                    #     print(
                                    #         f'Bot looking for profit tickers! Start amount = {start_trade_amount}, finish amount = {third_coin}, {first_asset}>{second_asset}>{third_asset}')

                        except ValueError:
                            pass

    conn_key = bm.start_multiplex_socket([f'{second_asset.lower()}{first_asset.lower()}@bookTicker',
                                          f'{second_asset.lower()}{third_asset.lower()}@bookTicker',
                                          f'{third_asset.lower()}{first_asset.lower()}@bookTicker',
                                          f'{second_asset.lower()}{first_asset.lower()}@trade',
                                          f'{second_asset.lower()}{third_asset.lower()}@trade',
                                          f'{third_asset.lower()}{first_asset.lower()}@trade'
                                          ],
                                         process_m_message)

    bm.start()