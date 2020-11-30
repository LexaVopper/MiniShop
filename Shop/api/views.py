from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from cart.models import *
from .serializers import *


@api_view(['POST'])
@csrf_exempt
def add_product(request):
    """  Response element to js script +  """

    if request.method == 'POST':
        body = request.data
        product = Product.objects.get(pk=body['id'])
        serializer = ProductSerializer(product)

        request.session['cart'][body['id']] = serializer.data
        request.session.save()
        print(request.session['cart'])
        return Response(serializer.data)


@api_view(['POST'])
@csrf_exempt
def delete_product(request):
    """  Response element to js script for deleting  """

    if request.method == 'POST':

        body = request.data
        del request.session['cart'][body['id']]
        request.session.save()

        return Response()


@api_view(['POST'])
@csrf_exempt
def clear_cart(request):
    """  Response element to js script for deleting + """

    if request.method == 'POST':
        request.session['cart'] = {}

        return Response()


@api_view(['GET'])
def update_session(request):
    """    Update cart.  + """
    if request.method == 'GET':

        session_key = request.session.session_key
        if 'cart' not in request.session:
            request.session['cart'] = {}
        if not session_key:
            request.session.cycle_key()


        else:

            active_goods = []
            for Value in request.session['cart']:
                active_goods.append(request.session['cart'][Value])

            return Response(active_goods)


@api_view(['POST'])
def complete_cart(request):
    """    add cart.  + """
    if request.method == 'POST':

        new_order = Order.objects.create(customer_name='Alex', is_active=True, stage=StageGeneration.base)
        for value in request.session['cart']:
            ProductInOrder.objects.create(order=new_order, product=Product.objects.get(id=value))
        request.session['cart'] = {}
        return Response()
