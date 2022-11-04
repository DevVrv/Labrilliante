from re import T
from django.db import models
from users.models import CustomUsers

# * Create your models here.
class Orders_model(models.Model):

    # * choice lists
    order_status_list = (
        ('0', 'Rejected'),
        ('1', 'On verification'),
        ('2', 'Order accepted'),
        ('3', 'Delivery is in progress'),
        ('4', 'Delivered'),
        ('5', 'Completed'), 
    )
    
    order_type_list = (
        ('0', 'COD'),
        ('1', 'Invocie'),
        ('2', 'Cash Memo'),
        ('3', 'Memo'),
        ('4', 'Hold'),
    )
    
    # * order info
    user = models.ForeignKey(CustomUsers, verbose_name="user", on_delete=models.CASCADE, db_index=True)
    order_type = models.CharField(max_length=1, verbose_name="Order Type", choices=order_type_list, db_index=True, default='1')
    order_status = models.CharField(max_length=1, verbose_name="Order Status", choices=order_status_list, default='1', db_index=True)
    order_number = models.CharField(max_length=255, verbose_name="Order Number", db_index=True, unique=True)
    
    # * request info
    comment = models.CharField(max_length=255, verbose_name="Comment", blank=True)
    pay_within = models.IntegerField(verbose_name="Pay Within", blank=True)
    p_ct_offer = models.FloatField(verbose_name="P/ct Offer", blank=True)
    total_price_offer = models.FloatField(verbose_name="Total Price Offer", blank=True)
    hold_hours = models.IntegerField(verbose_name='hold_hours', blank=True)

    # * order diamonds info
    diamonds_list = models.JSONField(verbose_name="Diamonds List")
    total_diamonds = models.IntegerField(verbose_name="Total Diamonds")
    total_carat = models.FloatField(verbose_name="Total Carat")
    total_price = models.IntegerField(verbose_name="Total Price")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated Date")
    
    def __str__(self):
        return f''

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ['user']

# * filter diamond model
class Orders_Diamond_Model(models.Model):

    ref = models.CharField(max_length=255, verbose_name="Ref")

    cert_number = models.CharField(max_length=255, verbose_name="Cert Number")
    shape = models.CharField(max_length=255, verbose_name="Shape")
    clarity = models.CharField(max_length=255, verbose_name="Clarity")
    color = models.CharField(max_length=255, verbose_name="Color")
    
    rap_1ct = models.IntegerField(verbose_name="Rap_1ct", blank=True)
    sale_price = models.IntegerField(verbose_name="Sale Price", blank=True)
    disc = models.FloatField(verbose_name="Discount", blank=True)
    girdle = models.CharField(max_length=255, verbose_name="Gridle", blank=True)
    culet = models.CharField(max_length=255, verbose_name="Culet", blank=True)
    weight = models.FloatField(max_length=255, verbose_name="Weight", blank=True)
    cut = models.CharField(max_length=255, verbose_name="Cut", blank=True)
    polish = models.CharField(max_length=255, verbose_name="Polish", blank=True)
    symmetry = models.CharField(max_length=255, verbose_name="Symmetry", blank=True)
    culet = models.CharField(max_length=255, verbose_name="Culet", blank=True)
    fluor = models.CharField(max_length=255, verbose_name="Fluour", blank=True)
    length = models.FloatField(verbose_name="Length", blank=True)
    width = models.FloatField(verbose_name="Width", blank=True)
    depth = models.FloatField(verbose_name="Depth", blank=True)
    lw = models.FloatField(verbose_name="L/W")
    measurements = models.CharField(max_length=255, verbose_name="Measurements", blank=True)
    lab = models.CharField(max_length=255, verbose_name="Lab", blank=True)
    depth_procent = models.FloatField(verbose_name="Depth %", blank=True)
    table_procent = models.FloatField(verbose_name="Table %", blank=True)

    rap_price = models.IntegerField(verbose_name='Rap Price', blank=True, null=True)

    photo = models.URLField(verbose_name="Image URL", blank=True)
    video = models.URLField(verbose_name="Video URL", blank=True)

    # dates
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated date")

    # key
    key = models.CharField(max_length=255, verbose_name="Key", db_index=True)

    buyer = models.ForeignKey(CustomUsers, verbose_name="Buyer", on_delete=models.CASCADE, db_index=True)
    order = models.ForeignKey(Orders_model, verbose_name="Order ID", on_delete=models.CASCADE, db_index=True)
    order_number = models.CharField(max_length=255, verbose_name="Order Number", db_index=True)

    def __str__(self):
        return f'Clarity: {self.clarity}, Color: {self.color}, Weight: {self.weight}'

    class Meta:
        verbose_name = 'Orders Diamond'
        verbose_name_plural = 'Orders Diamonds'
        ordering = ['sale_price']
