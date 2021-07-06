from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext
from .models import AddBot, BotProfit



# Register your models here.


class BotAdmin(admin.ModelAdmin):

    @admin.action(description='Отключить ботов')
    def off_bot(self, request, queryset):
        updated = queryset.update(activity=False)
        self.message_user(request, ngettext(
            '%d направление было остановлено.',
            '%d направления были остановлены.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Включить ботов')
    def on_bot(self, request, queryset):
        updated = queryset.update(activity=True)
        self.message_user(request, ngettext(
            '%d направление было успешно запущен.',
            '%d направления были успешно запущены.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Изменить процент прибыли')
    def change_ros(self, request, queryset):
        updated = queryset.update(return_on_sales=0.05, trade_balance=108)
        self.message_user(request, ngettext(
            '%d процент успешно изменен.',
            '%d проценты успешно изменены',
            updated,
        ) % updated, messages.SUCCESS)

    list_display = ('id', 'bot_name', 'create_at', 'return_on_sales', 'first_asset', 'second_asset', 'third_asset', 'activity')
    search_fields = ['id', 'bot_name']
    list_filter = ['create_at', 'bot_name']
    list_display_links = ['id', 'bot_name']
    list_editable = ['activity', 'return_on_sales']
    actions = [off_bot, on_bot, change_ros]


class LogsAdmin(admin.ModelAdmin):
    list_display = ('deal_time', 'logs_deal')
    readonly_fields = ('logs_deal', )
    search_fields = ['deal_time', 'logs_deal']
    list_filter = ['deal_time']

    def has_add_permission(self, request):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False





admin.site.register(AddBot, BotAdmin)
admin.site.register(BotProfit, LogsAdmin)

