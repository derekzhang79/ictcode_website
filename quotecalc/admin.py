from models import Category, SubCategory, Task, Quote
from django.contrib import admin


class TaskAdmin(admin.ModelAdmin):

    list_display = ('name', 'category', 'hours')
    list_filter = ('category',)
    search_fields = ('name',)


class QuoteAdmin(admin.ModelAdmin):

    date_hierarchy = 'creation_date'
    list_display = ('creation_date',)
    filter_horizontal = ('tasks',)


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Task, TaskAdmin)
admin.site.register(Quote, QuoteAdmin)
