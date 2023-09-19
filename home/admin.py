from django.contrib import admin
from .models import Day, TelegamAdmin, Token, Video, DayStatistics

# Register your models here.

class DayStatisticsAdmin(admin.ModelAdmin):
    list_display = ('video', 'day', 'play_count', 'digg_count', 'collect_count', 'share_count', 'comment_count', 'created_at', 'updated_at')
    list_filter = ('video', 'day', 'created_at', 'updated_at')
    search_fields = ('video', 'day', 'created_at', 'updated_at')
    ordering = ('video', 'day', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
admin.site.register(TelegamAdmin)
admin.site.register(Video)
admin.site.register(Day)
admin.site.register(DayStatistics, DayStatisticsAdmin)
admin.site.register(Token)