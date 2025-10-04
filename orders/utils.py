from datetime import date
from django.db.models import Sum
from .models import Order

def get_daily_sales_total(date: date):
    orders = Order.objects.filter(created_at__date=date)
        total_sum = orders.aggregate(total_sum=Sum('total_price'))['total_sum']
            return total_sum or 0