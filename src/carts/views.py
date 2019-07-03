from django.shortcuts import render


def cart_home(request):
    cart_id = request.session.get('cart_id', None)
    if cart_id is None:
        print('create new cart')
        request.session['cart_id'] = 1
    else:
        print('cart id exists')
    return render(request, 'carts/home.html', {})
