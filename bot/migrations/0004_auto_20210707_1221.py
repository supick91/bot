# Generated by Django 3.2.3 on 2021-07-07 09:21

import bot.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_auto_20210706_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBotBNB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_asset', models.CharField(default='USDT', max_length=5, verbose_name='Первая криптовалюта')),
                ('second_asset', models.CharField(choices=[], max_length=5, verbose_name='Вторая криптовалюта')),
                ('third_asset', models.CharField(default='ETH', max_length=5, verbose_name='Третья криптовалюта')),
                ('api_key', models.CharField(default='hgdMrqTZgqqhmhIlQ2jv1ZDfAe2gPxqurscpL62JLnXSUlk9lxI8vGwBKoI4PMIm', max_length=256, verbose_name='API ключ')),
                ('secret_key', models.CharField(default='EOrL81ooW1l6WmsGb3ZrqFeOJWgLQYU3qAU2juttRtfXQZz5s6pOE7QBwN9JQgPf', max_length=256, verbose_name='Секретный ключ')),
                ('return_on_sales', models.DecimalField(decimal_places=2, default=0.02, max_digits=5, validators=[bot.models.validate_percent], verbose_name='Процент прибыли, %')),
                ('trade_balance', models.DecimalField(decimal_places=2, default=20, max_digits=7, validators=[bot.models.validate_trade_balance], verbose_name='Торговый баланс')),
                ('bot_name', models.CharField(default=25397, max_length=100, verbose_name='Имя бота')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания бота')),
                ('activity', models.BooleanField(default=True, verbose_name='Вкл./Выкл. бота')),
                ('qty_1', models.CharField(max_length=8, verbose_name='minQty первой пары')),
                ('qty_2', models.CharField(max_length=8, verbose_name='minQty второй пары')),
                ('qty_3', models.CharField(default='1.00000', max_length=8, verbose_name='minQty третей пары')),
            ],
            options={
                'verbose_name': 'Бот ETH',
                'verbose_name_plural': 'Боты ETH',
                'ordering': ['-create_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='addbotbtc',
            options={'ordering': ['-create_at'], 'verbose_name': 'Бот BTC', 'verbose_name_plural': 'Боты BTC'},
        ),
        migrations.AlterModelOptions(
            name='addboteth',
            options={'ordering': ['-create_at'], 'verbose_name': 'Бот ETH', 'verbose_name_plural': 'Боты ETH'},
        ),
        migrations.AlterField(
            model_name='addbotbtc',
            name='bot_name',
            field=models.CharField(default=2058, max_length=100, verbose_name='Имя бота'),
        ),
        migrations.AlterField(
            model_name='addbotbtc',
            name='first_asset',
            field=models.CharField(default='USDT', max_length=5, verbose_name='Первая криптовалюта'),
        ),
        migrations.AlterField(
            model_name='addbotbtc',
            name='second_asset',
            field=models.CharField(choices=[('PERP', 'PERP'), ('FTM', 'FTM'), ('NANO', 'NANO'), ('ONT', 'ONT'), ('ENJ', 'ENJ'), ('WAVES', 'WAVES'), ('CTSI', 'CTSI'), ('ICX', 'ICX'), ('ALGO', 'ALGO'), ('SNX', 'SNX'), ('LRC', 'LRC'), ('GRT', 'GRT'), ('HIVE', 'HIVE'), ('XTZ', 'XTZ'), ('HBAR', 'HBAR'), ('BZRX', 'BZRX'), ('IOTA', 'IOTA'), ('PAXG', 'PAXG'), ('OGN', 'OGN'), ('CRV', 'CRV'), ('KMD', 'KMD'), ('ONE', 'ONE'), ('CELR', 'CELR'), ('GTC', 'GTC'), ('SKL', 'SKL'), ('BAT', 'BAT'), ('XEM', 'XEM'), ('MDX', 'MDX'), ('ZRX', 'ZRX'), ('QTUM', 'QTUM'), ('FORTH', 'FORTH'), ('LTO', 'LTO'), ('AVAX', 'AVAX'), ('MTL', 'MTL'), ('STPT', 'STPT'), ('COTI', 'COTI'), ('STORJ', 'STORJ'), ('TLM', 'TLM'), ('MKR', 'MKR'), ('BAL', 'BAL'), ('RLC', 'RLC'), ('STX', 'STX'), ('ZEN', 'ZEN'), ('BAKE', 'BAKE'), ('KAVA', 'KAVA'), ('TOMO', 'TOMO'), ('PERL', 'PERL'), ('MANA', 'MANA'), ('BAND', 'BAND'), ('DCR', 'DCR'), ('SRM', 'SRM'), ('AXS', 'AXS'), ('UMA', 'UMA'), ('DGB', 'DGB'), ('FTT', 'FTT'), ('ANT', 'ANT'), ('RSR', 'RSR'), ('FIO', 'FIO'), ('SRM', 'SRM'), ('NEAR', 'NEAR'), ('BLZ', 'BLZ'), ('TWT', 'TWT'), ('RVN', 'RVN'), ('CVC', 'CVC'), ('WRX', 'WRX'), ('XVS', 'XVS'), ('REN', 'REN'), ('ONG', 'ONG'), ('NMR', 'NMR'), ('SAND', 'SAND'), ('ARDR', 'ARDR'), ('KNC', 'KNC'), ('ONG', 'ONG'), ('STRAX', 'STRAX'), ('DATA', 'DATA'), ('ALICE', 'ALICE'), ('TRU', 'TRU'), ('INJ', 'INJ'), ('BEL', 'BEL'), ('CTK', 'CTK'), ('BTG', 'BTG'), ('CHR', 'CHR'), ('CTXC', 'CTXC'), ('ANKR', 'ANKR'), ('POLS', 'POLS'), ('TRB', 'TRB'), ('PSG', 'PSG'), ('LINA', 'LINA'), ('OXT', 'OXT'), ('UTK', 'UTK'), ('HNT', 'HNT'), ('JUV', 'JUV'), ('AR', 'AR'), ('COS', 'COS'), ('YFII', 'YFII'), ('AVA', 'AVA'), ('FIRO', 'FIRO'), ('DEGO', 'DEGO'), ('FIS', 'FIS'), ('DNT', 'DNT'), ('AUTO', 'AUTO'), ('FLM', 'FLM'), ('IRIS', 'IRIS'), ('ATM', 'ATM'), ('BAR', 'BAR'), ('NBS', 'NBS'), ('COS', 'COS'), ('HARD', 'HARD'), ('PNT', 'PNT'), ('MIR', 'MIR'), ('UNFI', 'UNFI'), ('LPT', 'LPT'), ('OG', 'OG'), ('ETH', 'ETH'), ('BNB', 'BNB'), ('ADA', 'ADA'), ('XRP', 'XRP'), ('DOGE', 'DOGE'), ('DOT', 'DOT'), ('SOL', 'SOL'), ('LTC', 'LTC'), ('LINK', 'LINK'), ('ETC', 'ETC'), ('KSM', 'KSM'), ('VET', 'VET'), ('AAVE', 'AAVE'), ('TFUEL', 'TFUEL'), ('COMP', 'COMP'), ('FET', 'FET'), ('BCH', 'BCH'), ('RUNE', 'RUNE'), ('EOS', 'EOS'), ('ARPA', 'ARPA'), ('NULS', 'NULS'), ('TKO', 'TKO'), ('OM', 'OM'), ('AION', 'AION'), ('GXS', 'GXS'), ('WING', 'WING'), ('REP', 'REP'), ('SFP', 'SFP'), ('GTO', 'GTO'), ('ORN', 'ORN'), ('CFX', 'CFX'), ('ROSE', 'ROSE'), ('WAN', 'WAN'), ('BOND', 'BOND'), ('POND', 'POND'), ('BTS', 'BTS'), ('WTC', 'WTC'), ('XMR', 'XMR'), ('UNI', 'UNI'), ('THETA', 'THETA'), ('SUSHI', 'SUSHI'), ('FIL', 'FIL'), ('NEO', 'NEO'), ('CHZ', 'CHZ'), ('TRX', 'TRX'), ('ZIL', 'ZIL'), ('ATOM', 'ATOM'), ('XLM', 'XLM'), ('CELO', 'CELO'), ('SXP', 'SXP'), ('LUNA', 'LUNA'), ('1INCH', '1INCH'), ('YFI', 'YFI'), ('OMG', 'OMG'), ('BNT', 'BNT'), ('CAKE', 'CAKE')], max_length=5, verbose_name='Вторая криптовалюта'),
        ),
        migrations.AlterField(
            model_name='addbotbtc',
            name='third_asset',
            field=models.CharField(default='BTC', max_length=5, verbose_name='Третья криптовалюта'),
        ),
        migrations.AlterField(
            model_name='addboteth',
            name='bot_name',
            field=models.CharField(default=14621, max_length=100, verbose_name='Имя бота'),
        ),
        migrations.AlterField(
            model_name='addboteth',
            name='first_asset',
            field=models.CharField(default='USDT', max_length=5, verbose_name='Первая криптовалюта'),
        ),
        migrations.AlterField(
            model_name='addboteth',
            name='second_asset',
            field=models.CharField(choices=[('LRC', 'LRC'), ('ZEN', 'ZEN'), ('FIRO', 'FIRO'), ('GXS', 'GXS'), ('STRAX', 'STRAX'), ('BNB', 'BNB'), ('AAVE', 'AAVE'), ('TRX', 'TRX'), ('ADA', 'ADA'), ('XRP', 'XRP'), ('LTC', 'LTC'), ('LINK', 'LINK'), ('VET', 'VET'), ('ENJ', 'ENJ'), ('ETC', 'ETC'), ('NEO', 'NEO'), ('EOS', 'EOS'), ('THETA', 'THETA'), ('XLM', 'XLM'), ('GRT', 'GRT'), ('CVC', 'CVC'), ('ZIL', 'ZIL'), ('DASH', 'DASH'), ('RLC', 'RLC'), ('OMG', 'OMG'), ('QTUM', 'QTUM'), ('ZRX', 'ZRX'), ('WAVES', 'WAVES'), ('MANA', 'MANA'), ('ICX', 'ICX'), ('KMD', 'KMD'), ('IOTA', 'IOTA'), ('DATA', 'DATA'), ('ZEC', 'ZEC'), ('ONT', 'ONT'), ('LSK', 'LSK'), ('MTL', 'MTL'), ('XEM', 'XEM'), ('KNC', 'KNC'), ('BLZ', 'BLZ'), ('BNT', 'BNT'), ('BAT', 'BAT'), ('WAN', 'WAN')], max_length=5, verbose_name='Вторая криптовалюта'),
        ),
        migrations.AlterField(
            model_name='addboteth',
            name='third_asset',
            field=models.CharField(default='ETH', max_length=5, verbose_name='Третья криптовалюта'),
        ),
    ]
