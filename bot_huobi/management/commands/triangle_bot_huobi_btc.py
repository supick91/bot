
from django.core.management.base import BaseCommand
from bot_huobi.models import HuobiBotBTC, HuobiBotProfit
from multiprocessing import Process
from bot_huobi.daemon import RunBot
import time




class Command(BaseCommand):



    def handle(self, *args, **options):

        proc = []

        while True:
            try:
                for _ in HuobiBotBTC.objects.get_queryset():
                        first_asset = _.first_asset
                        second_asset = _.second_asset
                        third_asset = _.third_asset
                        api = _.api_key
                        secret = _.secret_key
                        ros = _.return_on_sales
                        trade_balance = _.trade_balance
                        active = _.activity
                        firs_qty = _.qty_1
                        second_qty = _.qty_2
                        third_qty = _.qty_3
                        if active:
                            p = Process(target=RunBot, kwargs={'first_asset': first_asset, 'second_asset': second_asset,
                                                       'third_asset': third_asset, 'api': api, 'secret': secret, 'ros': ros, 'trade_balance': trade_balance, 'first_qty': firs_qty, 'second_qty': second_qty, 'third_qty': third_qty})

                            p.start()
                            proc.append(p)
                time.sleep(60*30)
                text = 'Бот BTC ищет профитные сделки, ожидайте...'
                bot_data = HuobiBotProfit(logs_deal=text)
                bot_data.save()
                for p in proc:
                    p.terminate()
                    p.join()

            except Exception as e:
