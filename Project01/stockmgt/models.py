from django.db import models

class ReceiptInfo(models.Model):
    RCTTYPE = (
        ('stockin' , 'received'),
        ('stockout' , 'issued'),
    )
    rctno = models.CharField(max_length=50, blank=True, null=True)
    rcttype = models.CharField(max_length=50, null=True,choices=RCTTYPE)
    
    def __str__(self):
        return str(self.rctno)
    
class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return str(self.name)


# Create your models here.
class Stock(models.Model):
    rctno = models.ForeignKey(ReceiptInfo, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=False, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    #export_to_CSV = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.item_name)
    
    
class StockOut(models.Model):
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=False, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    txn_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return str(self.item_name)
    

class StockIn(models.Model):
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=False, null=True)
    provided_by = models.CharField(max_length=50, blank=True, null=True)
    received_by = models.CharField(max_length=50, blank=True, null=True)
    txn_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return str(self.item_name)

class StockHistory(models.Model):
    rctno = models.ForeignKey(ReceiptInfo, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    uom = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    receive_by = models.CharField(max_length=50, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    issue_by = models.CharField(max_length=50, blank=True, null=True)
    issue_to = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, null=True)
    #export_to_CSV = models.BooleanField(default=False)    
        