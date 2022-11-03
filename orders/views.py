from django.core import serializers
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.shortcuts import HttpResponse
from orders.models import Orders_model, Orders_Diamond_Model
from cart.models import CartModal
from filter.models import Diamond_Model
from users.models import CustomUsers, CompanyDetails
import json


from django.utils import timezone
from tools.inspector import inspect_level, inspect_type



# * Get orders page
def get_orders(request):
    
    if not inspect_type(request, 1):
        return redirect(reverse_lazy('signin'))

    if not inspect_level(request, 2):
        return redirect(reverse_lazy('signin'))

    orders_model = Orders_model.objects.filter(user_id = request.user.id)

    try:
        cart = len(json.loads(CartModal.objects.get(user = request.user.pk).user_cart))
    except:
        cart = 0

    context = {
        'orders': orders_model,
        'title': 'Orders',
        'cart_len': cart,

    }

    return render(request, 'orders.html', context)

# * Get order details page
def get_order_details(request):

    # * request data
    requestData = json.loads(request.body)

    # * order items
    order = Orders_model.objects.filter(user_id = request.user.id).get(order_number = requestData['number'])

    # * diamonds list
    diamonds = Orders_Diamond_Model.objects.filter(key__in = json.loads(order.diamonds_list))

    # * user info
    user = CustomUsers.objects.get(pk=request.user.pk)
    
    # * create responce object
    responce = {
        'diamonds': serializers.serialize('json', diamonds),
        'carat': round(order.total_carat, 2),
        'len': order.total_diamonds,
        'price': order.total_price,
        'status': order.order_status,
        'type': order.order_type,
        'number': order.order_number,
        'placed': order.created_at.strftime('%b-%d-%m-%Y'),

        'name': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'tel': user.tel,
        
    }
    try:
        company = CompanyDetails.objects.get(user_id = request.user.id)
        responce['address'] = company.company_address,
    except:
        responce['address'] = '--'
    return HttpResponse (json.dumps(responce), content_type="application/json")

# * create new order
def create_order(request):

    # <-- get request data
    requestData = json.loads(request.body)
    
    # * create empty data list
    order_data = {
        'user_id': request.user.pk,
        'total_carat': 0,
        'total_price': 0,
        'pay_within': 0,
        'p_ct_offer': 0,
        'total_price_offer': 0,
        'hold_hours': 0,
        'diamonds_list': json.dumps([])
    }

    try:

        # * get cart items
        cart = CartModal.objects.get(user_id=request.user.id)
        user_cart = json.loads(cart.user_cart)
        cart_diamonds = Diamond_Model.objects.filter(pk__in=user_cart)
        cart.delete()

        # * order price , carat, len
        order_data['total_diamonds'] = len(cart_diamonds)
        for diamond in cart_diamonds:
            order_data['total_carat'] += diamond.weight
            order_data['total_price'] += diamond.sale_price
        order_data['total_carat'] = round(order_data['total_carat'], 2)

        # * create order number
        try:
            order_last = Orders_model.objects.all().order_by('-id')[0].id + 1
        except Exception as ex:
            order_last = 0

        order_data['order_number'] = f'{order_data["user_id"]}{order_data["total_diamonds"]}{order_last}'
        nulls = 10 - len(order_data['order_number'])
        while nulls:
            order_data['order_number'] = f'{order_data["order_number"]}0'
            nulls -= 1

        for key in requestData:
            if key != 'comment':
                order_data[key] = int(requestData[key])
            else:
                order_data[key] = requestData[key]

        # * create order and get order id

        order = Orders_model.objects.create(**order_data)
        order_item = Orders_model.objects.get(order_number=order_data['order_number'])

        # * create order diamonds list
        
        order_keys = []
        for diamond in cart_diamonds:
            filter_diamonds_values = {
                'cert_number': diamond.cert_number,
                'shape': diamond.shape,
                'clarity': diamond.clarity,
                'color': diamond.color,
                'rap_1ct': diamond.rap_1ct,
                'rap_price': diamond.rap_price,
                'sale_price': diamond.sale_price,
                'disc': diamond.disc,
                'girdle': diamond.girdle,
                'culet': diamond.culet,
                'weight': diamond.weight,
                'cut': diamond.cut,
                'polish': diamond.polish,
                'symmetry': diamond.symmetry,
                'culet': diamond.culet,
                'fluor': diamond.fluor,
                'length': diamond.length,
                'width': diamond.width,
                'depth': diamond.depth,
                'lw': diamond.lw,
                'measurements': diamond.measurements,
                'lab': diamond.lab,
                'depth_procent': diamond.depth_procent,
                'table_procent': diamond.table_procent,
                'photo': diamond.photo,
                'video': diamond.video,

                'key': diamond.key,

                'buyer': request.user,
                'order_id': order_item.id,
                'order_number': order_data['order_number']
            }
            Orders_Diamond_Model.objects.create(**filter_diamonds_values)
            order_keys.append(diamond.key)
       
        # * update order diamonds list 
        order.diamonds_list = json.dumps(order_keys)
        order.save()

        responce = {
            'alert': 'success'
        }

    except Exception as ex:
        print(ex)
        responce = {
            'alert': 'error',
        }
        

    return HttpResponse (json.dumps(responce), content_type="application/json")

# * order search form
def order_search(request):

    # <-- get values from request
    requestData = json.loads(request.body)
    search = requestData['search']
    date_from = requestData['date_from']
    date_to = requestData['date_to']

    # <-- get orders model
    orders_model = Orders_model.objects.filter(user_id=request.user.id)
    date = []
    time_zone = str(timezone.now())
    time_zone = time_zone[20:len(time_zone)]

    for item in orders_model:
        dateItem = item.created_at.strftime('%b-%d-%m-%Y')
        date.append(dateItem)
    
    # order number search
    if search != '0000000000':
        orders_model = orders_model.filter(order_number=search)

    # date search
    if date_from != '' and date_to != '':
        orders_model = orders_model.filter(created_at__range=[f'{date_from} 00:00:00.{time_zone}', f'{date_to} 23:59:59.{time_zone}'])
    elif date_from != '':
        orders_model = orders_model.filter(created_at__range=[f'{date_from} 00:00:00.{time_zone}', timezone.now()])
    elif date_to != '':
        orders_model = orders_model.filter(created_at__range=[f'2000-01-01 00:00:00.{time_zone}', f'{date_to} 23:59:59.{time_zone}'])

    # * create responce
    responce = {
        'orders': serializers.serialize('json', orders_model),
        'date': date
    }

    return HttpResponse (json.dumps(responce), content_type="application/json")
