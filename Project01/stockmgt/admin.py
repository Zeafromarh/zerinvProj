from django.contrib import admin
from .models import Stock,Category,ReceiptInfo
from .forms import StockCreateForm


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['rctno','category', 'item_name', 'quantity']
    form = StockCreateForm
    list_filter = ['category']
    search_fields = ['category', 'item_name']
 
# Register your models here.    
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Category)
admin.site.register(ReceiptInfo)