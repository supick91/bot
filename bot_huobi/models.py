from django.db import models
from bot_huobi.huobi_btc_choises import SECOND_CHOISE_BTC
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import random



def validate_percent(value):
    if value > 100:
        raise ValidationError(
            _('Вы указали %(value)s, процент прибыли может быть от 0.01 до 100'),
            params={'value': value},
        )
    if value < 0:
        raise ValidationError(
            _('Вы указали %(value)s, процент прибыли может быть от 0.01 до 100'),
            params={'value': value},
        )


def validate_trade_balance(value):
    if value < 12:
        raise ValidationError(
            _('Торговый баланс не может быть быть меньше 12 $'),
            params={'value': value},
        )

def validate_qty(value):
    if value < 0:
        raise ValidationError(
            _('Минимальное кол-во не может быть меньше 0'),
            params={'value': value},
        )


def bot_name():
    while True:
        count = random.randrange(1, 10000, 1)
        return count



# Create your models here.


class HuobiBotBTC(models.Model):
    

    first_asset = models.CharField(max_length=5, default='USDT', verbose_name='Первая криптовалюта')
    second_asset = models.CharField(max_length=5, choices=SECOND_CHOISE_BTC, verbose_name="Вторая криптовалюта")
    third_asset = models.CharField(max_length=5, default='BTC', verbose_name="Третья криптовалюта")
    api_key = models.CharField(max_length=256, default='f5b12b8e-60f1b783-1hrfj6yhgg-a1a64', verbose_name="ACCESS ключ")
    secret_key = models.CharField(max_length=256, default='ddb2a042-aa4ede09-2ee1b5aa-57382', verbose_name="SECRET ключ")
    return_on_sales = models.DecimalField(max_digits=5, decimal_places=2, default=0.01, validators=[validate_percent], verbose_name="Процент прибыли, %")
    trade_balance = models.DecimalField(max_digits=7, decimal_places=2, default=19, validators=[validate_trade_balance], verbose_name="Торговый баланс")
    bot_name = models.CharField(max_length=100, verbose_name='Имя бота', default=bot_name, unique=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бота')
    activity = models.BooleanField(default=True, verbose_name='Вкл./Выкл. бота')
    qty_1 = models.CharField(max_length=8, verbose_name="minQty первой пары",)
    qty_2 = models.CharField(max_length=8, verbose_name="minQty второй пары",)
    qty_3 = models.CharField(max_length=8,  verbose_name="minQty третей пары", default='1.000000')


    def __str__(self):
        return self.bot_name


    class Meta:
        verbose_name = 'Бот BTC'
        verbose_name_plural = 'Боты BTC'
        ordering = ['-create_at']


# class AddBotETH(models.Model):
#     count = random.randrange(10001, 20000, 1)


#     first_asset = models.CharField(max_length=5, default='USDT', verbose_name='Первая криптовалюта')
#     second_asset = models.CharField(max_length=5, choices=SECOND_CHOISE_ETH, verbose_name="Вторая криптовалюта")
#     third_asset = models.CharField(max_length=5, default='ETH', verbose_name="Третья криптовалюта")
#     api_key = models.CharField(max_length=256, default='hgdMrqTZgqqhmhIlQ2jv1ZDfAe2gPxqurscpL62JLnXSUlk9lxI8vGwBKoI4PMIm', verbose_name="API ключ")
#     secret_key = models.CharField(max_length=256, default='EOrL81ooW1l6WmsGb3ZrqFeOJWgLQYU3qAU2juttRtfXQZz5s6pOE7QBwN9JQgPf', verbose_name="Секретный ключ")
#     return_on_sales = models.DecimalField(max_digits=5, decimal_places=2, default=0.01, validators=[validate_percent], verbose_name="Процент прибыли, %")
#     trade_balance = models.DecimalField(max_digits=7, decimal_places=2, default=19, validators=[validate_trade_balance], verbose_name="Торговый баланс")
#     bot_name = models.CharField(max_length=100, verbose_name='Имя бота', default=count)
#     create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бота')
#     activity = models.BooleanField(default=True, verbose_name='Вкл./Выкл. бота')
#     qty_1 = models.CharField(max_length=8, verbose_name="minQty первой пары",)
#     qty_2 = models.CharField(max_length=8, verbose_name="minQty второй пары",)
#     qty_3 = models.CharField(max_length=8,  verbose_name="minQty третей пары", default='1.00000')


#     def __str__(self):
#         return self.bot_name


#     class Meta:
#         verbose_name = 'Бот ETH'
#         verbose_name_plural = 'Боты ETH'
#         ordering = ['-create_at']


# class AddBotBNB(models.Model):
#     count = random.randrange(20001, 30000, 1)


#     first_asset = models.CharField(max_length=5, default='USDT', verbose_name='Первая криптовалюта')
#     second_asset = models.CharField(max_length=5, choices=SECOND_CHOISE_BNB, verbose_name="Вторая криптовалюта")
#     third_asset = models.CharField(max_length=5, default='BNB', verbose_name="Третья криптовалюта")
#     api_key = models.CharField(max_length=256, default='hgdMrqTZgqqhmhIlQ2jv1ZDfAe2gPxqurscpL62JLnXSUlk9lxI8vGwBKoI4PMIm', verbose_name="API ключ")
#     secret_key = models.CharField(max_length=256, default='EOrL81ooW1l6WmsGb3ZrqFeOJWgLQYU3qAU2juttRtfXQZz5s6pOE7QBwN9JQgPf', verbose_name="Секретный ключ")
#     return_on_sales = models.DecimalField(max_digits=5, decimal_places=2, default=0.01, validators=[validate_percent], verbose_name="Процент прибыли, %")
#     trade_balance = models.DecimalField(max_digits=7, decimal_places=2, default=19, validators=[validate_trade_balance], verbose_name="Торговый баланс")
#     bot_name = models.CharField(max_length=100, verbose_name='Имя бота', default=count)
#     create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бота')
#     activity = models.BooleanField(default=True, verbose_name='Вкл./Выкл. бота')
#     qty_1 = models.CharField(max_length=8, verbose_name="minQty первой пары",)
#     qty_2 = models.CharField(max_length=8, verbose_name="minQty второй пары",)
#     qty_3 = models.CharField(max_length=8,  verbose_name="minQty третей пары", default='1.0000')


#     def __str__(self):
#         return self.bot_name


#     class Meta:
#         verbose_name = 'Бот BNB'
#         verbose_name_plural = 'Боты BNB'
#         ordering = ['-create_at']



class HuobiBotProfit(models.Model):
    # bot = models.ForeignKey(AddBot, on_delete=models.CASCADE)
    logs_deal = models.TextField(verbose_name='Текст отчёта')
    # stock_balance_start = models.CharField(max_length=30, verbose_name='Стартовый баланс')
    # stock_balance_end = models.CharField(max_length=30, verbose_name='Баланс после сделки')
    deal_time = models.DateTimeField(auto_now=True, verbose_name='Время сделки')

    class Meta:
        ordering = ['-deal_time']
        verbose_name = 'Логи работы бота Huobi'
        verbose_name_plural = 'Логи работы бота Huobi'