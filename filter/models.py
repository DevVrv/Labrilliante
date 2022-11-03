
from email.policy import default
from django.db import models
from users.models import CustomUsers

# * filter diamond model
class Diamond_Model(models.Model):

    ref = models.CharField(max_length=255, verbose_name="Ref")
    vendor = models.ForeignKey(CustomUsers, on_delete=models.PROTECT, verbose_name="vendor_id")
    best_selling = models.BooleanField(verbose_name="Best Selling", default=0)

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
    key = models.CharField(max_length=255, verbose_name="Key", db_index=True, unique=True)
    is_published = models.BooleanField(default=False, verbose_name="Is Published")

    def __str__(self):
        return f'Clarity: {self.clarity}, Color: {self.color}, Weight: {self.weight}'

    class Meta:
        verbose_name = 'Diamond'
        verbose_name_plural = 'Diamonds'
        ordering = ['sale_price']

# * fitler max min values
class MaxMin(models.Model):

    name = models.CharField(max_length=255, verbose_name="Filter Name", db_index=True, unique=True)
    
    min = models.FloatField(max_length=255, verbose_name="Min Value")
    max = models.FloatField(max_length=255, verbose_name="Max Value")


    def __str__(self):
        return f'{self.name}'.upper()

    class Meta:
        verbose_name = 'Max / Min Range Values'
        verbose_name_plural = 'Max / Min Range Values'
        ordering = ['name']  