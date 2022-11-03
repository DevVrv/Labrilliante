from django.contrib import admin
from .models import Vedor_Diamond_Model
from filter.models import Diamond_Model, MaxMin
# Register your models here.


# @ update maxmin values
def max_min():
    diamonds = Diamond_Model.objects.all()
    max_min = {
        'price': {
            'min': diamonds.order_by('sale_price')[0].sale_price,
            'max': diamonds.order_by('-sale_price')[0].sale_price
        },
        'carat': {
            'min': diamonds.order_by('weight')[0].weight,
            'max': diamonds.order_by('-weight')[0].weight
        },
        'length': {
            'min': diamonds.order_by('length')[0].length,
            'max': diamonds.order_by('-length')[0].length
        },
        'width': {
            'min': diamonds.order_by('width')[0].width,
            'max': diamonds.order_by('-width')[0].width
        },
        'depth': {
            'min': diamonds.order_by('depth')[0].depth,
            'max': diamonds.order_by('-depth')[0].depth
        },
        'depth_procent': {
            'min': diamonds.order_by('depth_procent')[0].depth_procent,
            'max': diamonds.order_by('-depth_procent')[0].depth_procent
        },
        'table': {
            'min': diamonds.order_by('table_procent')[0].table_procent,
            'max': diamonds.order_by('-table_procent')[0].table_procent
        },
        'lw': {
            'min': diamonds.order_by('lw')[0].lw,
            'max': diamonds.order_by('-lw')[0].lw
        },
    }

    for key in max_min:
        try:
            value = MaxMin.objects.get(name=key)
            value.min = max_min[key]['min']
            value.max = max_min[key]['max']
            value.save()
        except:
            value = MaxMin.objects.create(**{
                'name': key,
                'min': max_min[key]['min'],
                'max': max_min[key]['max'],
            })
            
# * accept white functions
@admin.action(description='Approve stones')
def accept(modeladmin, request, queryset):
    for item in queryset:
        diamond = {
                'ref': item.ref,
                'vendor': item.vendor,
                'best_selling': 0,
                'cert_number': item.cert_number,
                'shape': item.shape,
                'clarity': item.clarity,
                'color': item.color,
                'rap_1ct': item.rap_1ct,
                'sale_price': item.sale_price,
                'disc': item.disc,
                'girdle': item.girdle,
                'culet': item.culet,
                'weight': item.weight,
                'cut': item.cut,
                'polish': item.polish,
                'symmetry': item.symmetry,
                'culet': item.culet,
                'fluor': item.fluor,
                'length': item.length,
                'width': item.width,
                'depth': item.depth,
                'lw': item.lw,
                'measurements': item.measurements,
                'lab': item.lab,
                'depth_procent': item.depth_procent,
                'table_procent': item.table_procent,
                'photo': item.photo,
                'video': item.video,
                'is_published': 0,
                'key': item.key,
                'rap_price': item.rap_price
        }
        
        vendor_diamond = Vedor_Diamond_Model.objects.get(key=item.key)
        vendor_diamond.delete()

        Diamond_Model.objects.update_or_create(**diamond)
    max_min()

@admin.action(description='Approve stones and set published')
def accept_published(modeladmin, request, queryset):
    for item in queryset:
        diamond = {
            'ref': item.ref,
            'vendor': item.vendor,
            'best_selling': 0,
            'cert_number': item.cert_number,
            'shape': item.shape,
            'clarity': item.clarity,
            'color': item.color,
            'rap_1ct': item.rap_1ct,
            'sale_price': item.sale_price,
            'disc': item.disc,
            'girdle': item.girdle,
            'culet': item.culet,
            'weight': item.weight,
            'cut': item.cut,
            'polish': item.polish,
            'symmetry': item.symmetry,
            'culet': item.culet,
            'fluor': item.fluor,
            'length': item.length,
            'width': item.width,
            'depth': item.depth,
            'lw': item.lw,
            'measurements': item.measurements,
            'lab': item.lab,
            'depth_procent': item.depth_procent,
            'table_procent': item.table_procent,
            'photo': item.photo,
            'video': item.video,
            'is_published': 1,
            'key': item.key,
            'rap_price': item.rap_price
        }
        
        vendor_diamond = Vedor_Diamond_Model.objects.get(key=item.key)
        vendor_diamond.delete()

        Diamond_Model.objects.update_or_create(**diamond)
    max_min()

@admin.action(description='Approve stones, set best and published')
def accept_best_published(modeladmin, request, queryset):
    for item in queryset:
        diamond = {
            'ref': item.ref,
            'vendor': item.vendor,
            'best_selling': 1,
            'cert_number': item.cert_number,
            'shape': item.shape,
            'clarity': item.clarity,
            'color': item.color,
            'rap_1ct': item.rap_1ct,
            'sale_price': item.sale_price,
            'disc': item.disc,
            'girdle': item.girdle,
            'culet': item.culet,
            'weight': item.weight,
            'cut': item.cut,
            'polish': item.polish,
            'symmetry': item.symmetry,
            'culet': item.culet,
            'fluor': item.fluor,
            'length': item.length,
            'width': item.width,
            'depth': item.depth,
            'lw': item.lw,
            'measurements': item.measurements,
            'lab': item.lab,
            'depth_procent': item.depth_procent,
            'table_procent': item.table_procent,
            'photo': item.photo,
            'video': item.video,
            'is_published': 1,
            'key': item.key,
            'rap_price': item.rap_price
        }
        
        vendor_diamond = Vedor_Diamond_Model.objects.get(key=item.key)
        vendor_diamond.delete()

        Diamond_Model.objects.update_or_create(**diamond)
    max_min()

# * User details
@admin.register(Vedor_Diamond_Model)
class VendorDiamondsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'vendor',
        'shape',
        'cert_number', 
        'weight', 
        'color', 
        'clarity', 
        'rap_1ct', 
        'sale_price', 
        'created_at', 
        'updated_at',
    )
    list_display_links = ('id', 'shape')
    list_filter = ['shape', 'color', 'clarity', 'is_published']
    search_fields = ('vendor__id',)
    save_on_top = True
    actions = [accept, accept_published, accept_best_published]
    readonly_fields = ('key', 'vendor')