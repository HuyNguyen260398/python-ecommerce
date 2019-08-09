from django.shortcuts import render

import stripe


stripe.api_key = "sk_test_L2UkxaY9kJLqL3veVS0fCuLv00uVo6w8I4"
STRIPE_PUB_KEY = "pk_test_8hljcboVHoSIRIswWFCEwlIY00Xdsw19Ue"


def payment_method_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'billing/payment-method.html', {'publish_key': STRIPE_PUB_KEY})
