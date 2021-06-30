import multiprocessing
import signal, os
import sys

import psutil
from django.core.management.base import BaseCommand, CommandError
from bot.models import AddBot
from multiprocessing import Process
from bot.multi import RunBot
import time
from bot.models import BotProfit
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):

        proc = []
        while True:
            try:
                for _ in AddBot.objects.get_queryset():
                        first_asset = _.first_asset
                        second_asset = _.second_asset
                        third_asset = _.third_asset
                        api = _.api_key
                        secret = _.secret_key
                        ros = _.return_on_sales
                        trade_balance = _.trade_balance
                        active = _.activity
                        if active:
                            p = Process(target=RunBot, kwargs={'first_asset': first_asset, 'second_asset': second_asset,
                                                       'third_asset': third_asset, 'api': api, 'secret': secret, 'ros': ros, 'trade_balance': trade_balance})

                            p.start()
                            proc.append(p)
                time.sleep(600)
                text = 'Бот ищет профитные сделки, ожидайте...'
                bot_data = BotProfit(logs_deal=text)
                bot_data.save()
                for p in proc:
                    p.terminate()
                    p.join()

            except Exception as e:
                text2 = 'Возникла ошибка при работе бота, причина: {}'.format({e})
                bot_data = BotProfit(logs_deal=text2)
                bot_data.save()





























        # while True:
        #     assets = AddBot.objects.all()
        #     for i in assets:
        #         # firs_asset = i.first_asset
        #         # second_asset = i.second_asset
        #         # third_asset = i.third_asset
        #         # activity = i.activity
        #         # trade_balance = i.trade_balance
        #         # api = i.api_key
        #         # secret = i.secret_key
        #         # ros = i.return_on_sales
        #         id = i.pk
        #         try:
        #             kwargs = {
        #                 'bot_id': id
        #                     }
        #             print(f"BEGIN BOT {id}")
        #             p = Process(target=RunBot, kwargs=kwargs)
        #             # p = multiprocessing.Process(target=RunBot(bot_id=id, first_asset=first_asset, second_asset=second_asset, third_asset=third_asset, api=api, secret=secret, ros=ros, trade_balance=trade_balance))
        #             p.start()
        #             p.join()

        #             # self.proc.append(p)
        #             # for p in self.proc:
        #             #     p.join()
        #         except Exception as e:
        #             self.stdout.write(e)

                # for x in self.proc:
                #     x.terminate()



#




