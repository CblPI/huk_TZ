from django.contrib import admin

from .models import Round, FortuneUser, RouletteLog


# Register your models here.

@admin.register(Round)
class RoundAdmin(admin.ModelAdmin):
    filter_horizontal = ['cells']
    fields = ['cells', 'jackpot_cell', 'is_active', 'user_cnt']
    readonly_fields = ['user_cnt']

    def user_cnt(self, obj):
        return obj.users_in_round()

    user_cnt.short_description = 'Коль-во пользователей учавствующих в раунде'


@admin.register(FortuneUser)
class RoundUser(admin.ModelAdmin):
    pass
