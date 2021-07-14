# Generated by Django 3.2.4 on 2021-07-09 12:13

import bot_huobi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HuobiBotBTC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_asset', models.CharField(default='USDT', max_length=5, verbose_name='Первая криптовалюта')),
                ('second_asset', models.CharField(choices=[('XEM', 'XEM'), ('HNT', 'HNT'), ('CHZ', 'CHZ'), ('MANA', 'MANA'), ('ONE', 'ONE'), ('MATIC', 'MATIC'), ('ZEN', 'ZEN'), ('FTM', 'FTM'), ('CELO', 'CELO'), ('STX', 'STX'), ('RUNE', 'RUNE'), ('PERP', 'PERP'), ('FTM', 'FTM'), ('NANO', 'NANO'), ('ONT', 'ONT'), ('ENJ', 'ENJ'), ('WAVES', 'WAVES'), ('CTSI', 'CTSI'), ('ICX', 'ICX'), ('ALGO', 'ALGO'), ('SNX', 'SNX'), ('LRC', 'LRC'), ('GRT', 'GRT'), ('HIVE', 'HIVE'), ('XTZ', 'XTZ'), ('HBAR', 'HBAR'), ('BZRX', 'BZRX'), ('IOTA', 'IOTA'), ('PAXG', 'PAXG'), ('OGN', 'OGN'), ('CRV', 'CRV'), ('KMD', 'KMD'), ('ONE', 'ONE'), ('CELR', 'CELR'), ('GTC', 'GTC'), ('SKL', 'SKL'), ('BAT', 'BAT'), ('XEM', 'XEM'), ('MDX', 'MDX'), ('ZRX', 'ZRX'), ('QTUM', 'QTUM'), ('FORTH', 'FORTH'), ('LTO', 'LTO'), ('AVAX', 'AVAX'), ('MTL', 'MTL'), ('STPT', 'STPT'), ('COTI', 'COTI'), ('STORJ', 'STORJ'), ('TLM', 'TLM'), ('MKR', 'MKR'), ('BAL', 'BAL'), ('RLC', 'RLC'), ('STX', 'STX'), ('ZEN', 'ZEN'), ('BAKE', 'BAKE'), ('KAVA', 'KAVA'), ('TOMO', 'TOMO'), ('PERL', 'PERL'), ('MANA', 'MANA'), ('BAND', 'BAND'), ('DCR', 'DCR'), ('SRM', 'SRM'), ('AXS', 'AXS'), ('UMA', 'UMA'), ('DGB', 'DGB'), ('FTT', 'FTT'), ('ANT', 'ANT'), ('RSR', 'RSR'), ('FIO', 'FIO'), ('SRM', 'SRM'), ('NEAR', 'NEAR'), ('BLZ', 'BLZ'), ('TWT', 'TWT'), ('RVN', 'RVN'), ('CVC', 'CVC'), ('WRX', 'WRX'), ('XVS', 'XVS'), ('REN', 'REN'), ('ONG', 'ONG'), ('NMR', 'NMR'), ('SAND', 'SAND'), ('ARDR', 'ARDR'), ('KNC', 'KNC'), ('ONG', 'ONG'), ('STRAX', 'STRAX'), ('DATA', 'DATA'), ('ALICE', 'ALICE'), ('TRU', 'TRU'), ('INJ', 'INJ'), ('BEL', 'BEL'), ('CTK', 'CTK'), ('BTG', 'BTG'), ('CHR', 'CHR'), ('CTXC', 'CTXC'), ('ANKR', 'ANKR'), ('POLS', 'POLS'), ('TRB', 'TRB'), ('PSG', 'PSG'), ('LINA', 'LINA'), ('OXT', 'OXT'), ('UTK', 'UTK'), ('HNT', 'HNT'), ('JUV', 'JUV'), ('AR', 'AR'), ('COS', 'COS'), ('YFII', 'YFII'), ('AVA', 'AVA'), ('FIRO', 'FIRO'), ('DEGO', 'DEGO'), ('FIS', 'FIS'), ('DNT', 'DNT'), ('AUTO', 'AUTO'), ('FLM', 'FLM'), ('IRIS', 'IRIS'), ('ATM', 'ATM'), ('BAR', 'BAR'), ('NBS', 'NBS'), ('COS', 'COS'), ('HARD', 'HARD'), ('PNT', 'PNT'), ('MIR', 'MIR'), ('UNFI', 'UNFI'), ('LPT', 'LPT'), ('OG', 'OG'), ('ETH', 'ETH'), ('BNB', 'BNB'), ('ADA', 'ADA'), ('XRP', 'XRP'), ('DOGE', 'DOGE'), ('DOT', 'DOT'), ('SOL', 'SOL'), ('LTC', 'LTC'), ('LINK', 'LINK'), ('ETC', 'ETC'), ('KSM', 'KSM'), ('VET', 'VET'), ('AAVE', 'AAVE'), ('TFUEL', 'TFUEL'), ('COMP', 'COMP'), ('FET', 'FET'), ('BCH', 'BCH'), ('RUNE', 'RUNE'), ('EOS', 'EOS'), ('ARPA', 'ARPA'), ('NULS', 'NULS'), ('TKO', 'TKO'), ('OM', 'OM'), ('AION', 'AION'), ('GXS', 'GXS'), ('WING', 'WING'), ('REP', 'REP'), ('SFP', 'SFP'), ('GTO', 'GTO'), ('ORN', 'ORN'), ('CFX', 'CFX'), ('ROSE', 'ROSE'), ('WAN', 'WAN'), ('BOND', 'BOND'), ('POND', 'POND'), ('BTS', 'BTS'), ('WTC', 'WTC'), ('XMR', 'XMR'), ('UNI', 'UNI'), ('THETA', 'THETA'), ('SUSHI', 'SUSHI'), ('FIL', 'FIL'), ('NEO', 'NEO'), ('CHZ', 'CHZ'), ('TRX', 'TRX'), ('ZIL', 'ZIL'), ('ATOM', 'ATOM'), ('XLM', 'XLM'), ('CELO', 'CELO'), ('SXP', 'SXP'), ('LUNA', 'LUNA'), ('1INCH', '1INCH'), ('YFI', 'YFI'), ('OMG', 'OMG'), ('BNT', 'BNT'), ('CAKE', 'CAKE')], max_length=5, verbose_name='Вторая криптовалюта')),
                ('third_asset', models.CharField(default='BTC', max_length=5, verbose_name='Третья криптовалюта')),
                ('api_key', models.CharField(default='hgdMrqTZgqqhmhIlQ2jv1ZDfAe2gPxqurscpL62JLnXSUlk9lxI8vGwBKoI4PMIm', max_length=256, verbose_name='API ключ')),
                ('secret_key', models.CharField(default='EOrL81ooW1l6WmsGb3ZrqFeOJWgLQYU3qAU2juttRtfXQZz5s6pOE7QBwN9JQgPf', max_length=256, verbose_name='Секретный ключ')),
                ('return_on_sales', models.DecimalField(decimal_places=2, default=0.01, max_digits=5, validators=[bot_huobi.models.validate_percent], verbose_name='Процент прибыли, %')),
                ('trade_balance', models.DecimalField(decimal_places=2, default=19, max_digits=7, validators=[bot_huobi.models.validate_trade_balance], verbose_name='Торговый баланс')),
                ('bot_name', models.CharField(default=[bot_huobi.models.bot_name], max_length=100, unique=True, verbose_name='Имя бота')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бота')),
                ('activity', models.BooleanField(default=True, verbose_name='Вкл./Выкл. бота')),
                ('qty_1', models.CharField(max_length=8, verbose_name='minQty первой пары')),
                ('qty_2', models.CharField(max_length=8, verbose_name='minQty второй пары')),
                ('qty_3', models.CharField(default='1.000000', max_length=8, verbose_name='minQty третей пары')),
            ],
            options={
                'verbose_name': 'Бот BTC',
                'verbose_name_plural': 'Боты BTC',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='HuobiBotProfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logs_deal', models.TextField(verbose_name='Текст отчёта')),
                ('deal_time', models.DateTimeField(auto_now=True, verbose_name='Время сделки')),
            ],
            options={
                'verbose_name': 'Логи работы бота Huobi',
                'verbose_name_plural': 'Логи работы бота Huobi',
                'ordering': ['-deal_time'],
            },
        ),
    ]