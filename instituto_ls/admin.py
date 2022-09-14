from django.contrib import admin
from instituto_ls.models import Feedback, Hero, Product

admin.site.register(Hero)
admin.site.register(Feedback)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'index',)
    list_editable = ('index',)
