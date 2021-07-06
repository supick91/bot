from django.db import models
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





# Create your models here.
FIRST_CHOISE = [
    ('USDT', 'USDT'),
]

SECOND_CHOISE = [
    ('ARPA', 'ARPA'),
    ('NULS', 'NULS'),
    ('TKO', 'TKO'),
    ('OM', 'OM'),
    ('AION', 'AION'),
    ('GXS', 'GXS'),
    ('WING', 'WING'),
    ('REP', 'REP'),
    ('SFP', 'SFP'),
    ('GTO', 'GTO'),
    ('ORN', 'ORN'),
    ('CFX', 'CFX'),
    ('ROSE', 'ROSE'),
    ('WAN', 'WAN'),
    ('BOND', 'BOND'),
    ('POND', 'POND'),
    ('BTS', 'BTS'),
    ('WTC', 'WTC'),
    ('ETH', 'ETH'),
    ('BNB', 'BNB'),
    ('ADA', 'ADA'),
    ('XRP', 'XRP'),
    ('DOGE', 'DOGE'),
    ('DOT', 'DOT'),
    ('SOL', 'SOL'),
    ('LTC', 'LTC'),
    ('LINK', 'LINK'),
    ('ETC', 'ETC'),
    ('KSM', 'KSM'),
    ('VET', 'VET'),
    ('AAVE', 'AAVE'),
    ('TFUEL', 'TFUEL'),
    ('COMP', 'COMP'),
    ('FET', 'FET'),
    ('BCH', 'BCH'),
    ('RUNE', 'RUNE'),
    ('EOS', 'EOS'),
    ('XMR', 'XMR'),
    ('UNI', 'UNI'),
    ('THETA', 'THETA'),
    ('SUSHI', 'SUSHI'),
    ('FIL', 'FIL'),
    ('NEO', 'NEO'),
    ('CHZ', 'CHZ'),
    ('TRX', 'TRX'),
    ('ZIL', 'ZIL'),
    ('ATOM', 'ATOM'),
    ('XLM', 'XLM'),
    ('CELO', 'CELO'),
    ('SXP', 'SXP'),
    ('LUNA', 'LUNA'),
    ('1INCH', '1INCH'),
    ('YFI', 'YFI'),
    ('OMG', 'OMG'),
    ('BNT', 'BNT'),
    ('CAKE', 'CAKE'),
    ('PERP', 'PERP'),
    ('FTM', 'FTM'),
    ('NANO', 'NANO'),
    ('ONT', 'ONT'),
    ('ENJ', 'ENJ'),
    ('WAVES', 'WAVES'),
    ('CTSI', 'CTSI'),
    ('ICX', 'ICX'),
    ('ALGO', 'ALGO'),
    ('SNX', 'SNX'),
    ('LRC', 'LRC'),
    ('GRT', 'GRT'),
    ('HIVE', 'HIVE'),
    ('XTZ', 'XTZ'),
    ('HBAR', 'HBAR'),
    ('BZRX', 'BZRX'),
    ('IOTA', 'IOTA'),
    ('PAXG', 'PAXG'),
    ('OGN', 'OGN'),
    ('CRV', 'CRV'),
    ('KMD', 'KMD'),
    ('ONE', 'ONE'),
    ('CELR', 'CELR'),
    ('GTC', 'GTC'),
    ('SKL', 'SKL'),
    ('BAT', 'BAT'),
    ('XEM', 'XEM'),
    ('MDX', 'MDX'),
    ('ZRX', 'ZRX'),
    ('QTUM', 'QTUM'),
    ('FORTH', 'FORTH'),
    ('LTO', 'LTO'),
    ('AVAX', 'AVAX'),
    ('MTL', 'MTL'),
    ('STPT', 'STPT'),
    ('COTI', 'COTI'),
    ('STORJ', 'STORJ'),
    ('TLM', 'TLM'),
    ('MKR', 'MKR'),
    ('BAL', 'BAL'),
    ('RLC', 'RLC'),
    ('STX', 'STX'),
    ('ZEN', 'ZEN'),
    ('BAKE', 'BAKE'),
    ('KAVA', 'KAVA'),
    ('TOMO', 'TOMO'),
    ('PERL', 'PERL'),
    ('MANA', 'MANA'),
    ('BAND', 'BAND'),
    ('DCR', 'DCR'),
    ('SRM', 'SRM'),
    ('AXS', 'AXS'),
    ('UMA', 'UMA'),
    ('DGB', 'DGB'),
    ('FTT', 'FTT'),
    ('ANT', 'ANT'),
    ('RSR', 'RSR'),
    ('FIO', 'FIO'),
    ('SRM', 'SRM'),
    ('NEAR', 'NEAR'),
    ('BLZ', 'BLZ'),
    ('TWT', 'TWT'),
    ('RVN', 'RVN'),
    ('CVC', 'CVC'),
    ('WRX', 'WRX'),
    ('XVS', 'XVS'),
    ('REN', 'REN'),
    ('ONG', 'ONG'),
    ('NMR', 'NMR'),
    ('SAND', 'SAND'),
    ('ARDR', 'ARDR'),
    ('KNC', 'KNC'),
    ('ONG', 'ONG'),
    ('STRAX', 'STRAX'),
    ('DATA', 'DATA'),
    ('ALICE', 'ALICE'),
    ('TRU', 'TRU'),
    ('INJ', 'INJ'),
    ('BEL', 'BEL'),
    ('CTK', 'CTK'),
    ('BTG', 'BTG'),
    ('CHR', 'CHR'),
    ('CTXC', 'CTXC'),
    ('ANKR', 'ANKR'),
    ('POLS', 'POLS'),
    ('TRB', 'TRB'),
    ('PSG', 'PSG'),
    ('LINA', 'LINA'),
    ('OXT', 'OXT'),
    ('UTK', 'UTK'),
    ('HNT', 'HNT'),
    ('JUV', 'JUV'),
    ('AR', 'AR'),
    ('COS', 'COS'),
    ('YFII', 'YFII'),
    ('AVA', 'AVA'),
    ('FIRO', 'FIRO'),
    ('DEGO', 'DEGO'),
    ('FIS', 'FIS'),
    ('DNT', 'DNT'),
    ('AUTO', 'AUTO'),
    ('FLM', 'FLM'),
    ('IRIS', 'IRIS'),
    ('ATM', 'ATM'),
    ('BAR', 'BAR'),
    ('NBS', 'NBS'),
    ('COS', 'COS'),
    ('HARD', 'HARD'),
    ('PNT', 'PNT'),
    ('MIR', 'MIR'),
    ('UNFI', 'UNFI'),
    ('LPT', 'LPT'),
    ('OG', 'OG'),
]


THIRD_CHOISE = [
    ('BTC', 'BTC'),
]


class AddBot(models.Model):
    count = random.randrange(1, 10000, 1)


    first_asset = models.CharField(max_length=5, choices=FIRST_CHOISE, verbose_name='Первая криптовалюта')
    second_asset = models.CharField(max_length=5, choices=SECOND_CHOISE, verbose_name="Вторая криптовалюта")
    third_asset = models.CharField(max_length=5, choices=THIRD_CHOISE, verbose_name="Третья криптовалюта")
    api_key = models.CharField(max_length=256, default='hgdMrqTZgqqhmhIlQ2jv1ZDfAe2gPxqurscpL62JLnXSUlk9lxI8vGwBKoI4PMIm', verbose_name="API ключ")
    secret_key = models.CharField(max_length=256, default='EOrL81ooW1l6WmsGb3ZrqFeOJWgLQYU3qAU2juttRtfXQZz5s6pOE7QBwN9JQgPf', verbose_name="Секретный ключ")
    return_on_sales = models.DecimalField(max_digits=5, decimal_places=2, default=0.05, validators=[validate_percent], verbose_name="Процент прибыли, %")
    trade_balance = models.DecimalField(max_digits=7, decimal_places=2, default=108, validators=[validate_trade_balance], verbose_name="Торговый баланс")
    bot_name = models.CharField(max_length=100, verbose_name='Имя бота', default=count)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бота')
    activity = models.BooleanField(default=True, verbose_name='Вкл./Выкл. бота')
    qty_1 = models.CharField(max_length=8, verbose_name="minQty первой пары",)
    qty_2 = models.CharField(max_length=8, verbose_name="minQty второй пары",)
    qty_3 = models.CharField(max_length=8,  verbose_name="minQty третей пары", default='1.000000')


    def __str__(self):
        return self.bot_name


    class Meta:
        verbose_name = 'Бота'
        verbose_name_plural = 'Боты'
        ordering = ['-create_at']


class BotProfit(models.Model):
    # bot = models.ForeignKey(AddBot, on_delete=models.CASCADE)
    logs_deal = models.TextField(verbose_name='Текст отчёта')
    # stock_balance_start = models.CharField(max_length=30, verbose_name='Стартовый баланс')
    # stock_balance_end = models.CharField(max_length=30, verbose_name='Баланс после сделки')
    deal_time = models.DateTimeField(auto_now=True, verbose_name='Время сделки')

    class Meta:
        ordering = ['-deal_time']
        verbose_name = 'Логи работы бота'
        verbose_name_plural = 'Логи работы бота'











