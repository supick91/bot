from django.contrib import admin
from .models import AddBot, BotProfit


# Register your models here.


class BotAdmin(admin.ModelAdmin):
    list_display = ('id', 'bot_name', 'create_at', 'return_on_sales', 'first_asset', 'second_asset', 'third_asset', 'activity')
    search_fields = ['id', 'bot_name']
    list_filter = ['create_at', 'bot_name']
    list_display_links = ['id', 'bot_name']
    list_editable = ['activity', 'return_on_sales']


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

