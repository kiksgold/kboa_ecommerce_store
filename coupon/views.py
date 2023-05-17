from django.shortcuts import render, redirect, reverse
from django.utils import timezone

# Create your views here.
from .models import Coupon
from .forms import CouponApplyForm


def coupon_apply(request):
    now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                    valid_from__lte=now,
                                    valid_to__gte=now,
                                    active=True)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect(reverse('view_cart'))