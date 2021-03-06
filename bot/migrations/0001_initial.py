# Generated by Django 3.2.3 on 2021-07-01 11:54

import bot.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_asset', models.CharField(choices=[('USDT', 'USDT')], max_length=5, verbose_name='Первая криптовалюта')),
                ('second_asset', models.CharField(choices=[('ETH', 'ETH'), ('BNB', 'BNB'), ('ADA', 'ADA'), ('XRP', 'XRP'), ('DOGE', 'DOGE'), ('DOT', 'DOT'), ('SOL', 'SOL'), ('LTC', 'LTC'), ('LINK', 'LINK'), ('ICP', 'ICP'), ('WBTC', 'WBTC'), ('ETC', 'ETC'), ('KSM', 'KSM'), ('VET', 'VET'), ('AAVE', 'AAVE'), ('TFUEL', 'TFUEL'), ('COMP', 'COMP'), ('FET', 'FET'), ('BCH', 'BCH'), ('RUNE', 'RUNE'), ('EOS', 'EOS'), ('XMR', 'XMR'), ('UNI', 'UNI'), ('PPT', 'PPT'), ('IOTX', 'IOTX'), ('THETA', 'THETA'), ('SUSHI', 'SUSHI'), ('FIL', 'FIL'), ('NEO', 'NEO'), ('CHZ', 'CHZ'), ('TRX', 'TRX'), ('ZIL', 'ZIL'), ('ATOM', 'ATOM'), ('IOST', 'IOST'), ('XLM', 'XLM'), ('CELO', 'CELO'), ('SXP', 'SXP'), ('LUNA', 'LUNA'), ('1INCH', '1INCH'), ('YFI', 'YFI'), ('XVG', 'XVG'), ('OMG', 'OMG'), ('BNT', 'BNT'), ('ZEK', 'ZEK'), ('CAKE', 'CAKE'), ('PERP', 'PERP'), ('SC', 'SC'), ('FTM', 'FTM'), ('BQX', 'BQX'), ('NANO', 'NANO'), ('ONT', 'ONT'), ('ENJ', 'ENJ'), ('WAVES', 'WAVES'), ('CTSI', 'CTSI'), ('ICX', 'ICX'), ('LSX', 'LSX'), ('ALGO', 'ALGO'), ('AUDI', 'AUDI'), ('STMX', 'STMX'), ('SNX', 'SNX'), ('LRC', 'LRC'), ('ADX', 'ADX'), ('GRT', 'GRT'), ('HIVE', 'HIVE'), ('XTZ', 'XTZ'), ('BCD', 'BCD'), ('DIA', 'DIA'), ('HBAR', 'HBAR'), ('BZRX', 'BZRX'), ('IOTA', 'IOTA'), ('ATA', 'ATA'), ('PAXG', 'PAXG'), ('OGN', 'OGN'), ('CRV', 'CRV'), ('KMD', 'KMD'), ('ONE', 'ONE'), ('CELR', 'CELR'), ('GTC', 'GTC'), ('SNT', 'SNT'), ('SKL', 'SKL'), ('BAT', 'BAT'), ('XEM', 'XEM'), ('ARK', 'ARK'), ('MDX', 'MDX'), ('ZRX', 'ZRX'), ('QTUM', 'QTUM'), ('MDA', 'MDA'), ('FORTH', 'FORTH'), ('LTO', 'LTO'), ('AVAX', 'AVAX'), ('LOOM', 'LOOM'), ('MTL', 'MTL'), ('STPT', 'STPT'), ('COTI', 'COTI'), ('STORJ', 'STORJ'), ('TLM', 'TLM'), ('MKR', 'MKR'), ('BAL', 'BAL'), ('GAS', 'GAS'), ('RLC', 'RLC'), ('STX', 'STX'), ('ZEN', 'ZEN'), ('BAKE', 'BAKE'), ('DOCK', 'DOCK'), ('KAVA', 'KAVA'), ('TOMO', 'TOMO'), ('STEEM', 'STEEM'), ('PERL', 'PERL'), ('MANA', 'MANA'), ('POWR', 'POWR'), ('BAND', 'BAND'), ('DCR', 'DCR'), ('SRM', 'SRM'), ('AXS', 'AXS'), ('UMA', 'UMA'), ('DGB', 'DGB'), ('FTT', 'FTT'), ('ANT', 'ANT'), ('RSR', 'RSR'), ('FIO', 'FIO'), ('SRM', 'SRM'), ('NEAR', 'NEAR'), ('BLZ', 'BLZ'), ('TWT', 'TWT'), ('RVN', 'RVN'), ('CVC', 'CVC'), ('WRX', 'WRX'), ('XVS', 'XVS'), ('REN', 'REN'), ('ONG', 'ONG'), ('AERGO', 'AERGO'), ('NMR', 'NMR'), ('ELF', 'ELF'), ('SAND', 'SAND'), ('ARDR', 'ARDR'), ('KNC', 'KNC'), ('GLM', 'GLM'), ('ONG', 'ONG'), ('POLY', 'POLY'), ('STRAX', 'STRAX'), ('DATA', 'DATA'), ('ALICE', 'ALICE'), ('TRU', 'TRU'), ('PHA', 'PHA'), ('OST', 'OST'), ('INJ', 'INJ'), ('BEL', 'BEL'), ('CTK', 'CTK'), ('BTG', 'BTG'), ('CHR', 'CHR'), ('GRS', 'GRS'), ('CTXC', 'CTXC'), ('ANKR', 'ANKR')], max_length=5, verbose_name='Вторая криптовалюта')),
                ('third_asset', models.CharField(choices=[('BTC', 'BTC')], max_length=5, verbose_name='Третья криптовалюта')),
                ('api_key', models.CharField(default='hgdMrqTZgqqhmhIlQ2jv1ZDfAe2gPxqurscpL62JLnXSUlk9lxI8vGwBKoI4PMIm', max_length=256, verbose_name='API ключ')),
                ('secret_key', models.CharField(default='EOrL81ooW1l6WmsGb3ZrqFeOJWgLQYU3qAU2juttRtfXQZz5s6pOE7QBwN9JQgPf', max_length=256, verbose_name='Секретный ключ')),
                ('return_on_sales', models.DecimalField(decimal_places=2, default=0.16, max_digits=5, validators=[bot.models.validate_percent], verbose_name='Процент прибыли, %')),
                ('trade_balance', models.DecimalField(decimal_places=2, default=25, max_digits=7, validators=[bot.models.validate_trade_balance], verbose_name='Торговый баланс')),
                ('bot_name', models.CharField(max_length=100, verbose_name='Имя бота')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бота')),
                ('activity', models.BooleanField(default=True, verbose_name='Вкл./Выкл. бота')),
                ('qty_1', models.CharField(max_length=8, verbose_name='minQty первой пары')),
                ('qty_2', models.CharField(max_length=8, verbose_name='minQty второй пары')),
                ('qty_3', models.CharField(default='000000', max_length=8, verbose_name='minQty третей пары')),
            ],
            options={
                'verbose_name': 'Бота',
                'verbose_name_plural': 'Боты',
                'ordering': ['-create_at'],
            },
        ),
        migrations.CreateModel(
            name='BotProfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logs_deal', models.TextField(verbose_name='Текст отчёта')),
                ('deal_time', models.DateTimeField(auto_now=True, verbose_name='Время сделки')),
            ],
            options={
                'verbose_name': 'Логи работы бота',
                'verbose_name_plural': 'Логи работы бота',
                'ordering': ['-deal_time'],
            },
        ),
    ]
