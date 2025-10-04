from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Coupon

class CouponValidationView(APIView):
    def post(self, request, *args, **kwargs):
            code = request.data.get('code')
                    if not code:
                                return Response({'error': 'Coupon code required'}, status=status.HTTP_400_BAD_REQUEST)
                                        today = timezone.now().date()
                                                try:
                                                            coupon = Coupon.objects.get(
                                                                            code=code,
                                                                                            is_active=True,
                                                                                                            valid_from__lte=today,
                                                                                                                            valid_until__gte=today
                                                                                                                                        )
                                                                                                                                                    return Response({'success': True, 'discount_percentage': coupon.discount_percentage}, status=status.HTTP_200_OK)
                                                                                                                                                            except Coupon.DoesNotExist:
                                                                                                                                                                        return Response({'success': False, 'error': 'Invalid or expired coupon'}, status=status.HTTP_400_BAD_REQUEST)