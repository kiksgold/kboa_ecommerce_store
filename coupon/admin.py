from django.contrib import admin
from .models import Coupon


class CouponAdmin(admin.ModelAdmin):
    list_dispaly = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']


admin.site.register(Coupon, CouponAdmin)
