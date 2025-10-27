# home/tests.py

from rest_framework.test import APITestCase
from rest_framework import status
from home.models import Restaurant

class RestaurantInfoAPITest(APITestCase):
    def test_get_restaurant_info(self):
            # Create a sample restaurant
                    sample_restaurant = Restaurant.objects.create(
                                name='Test Restaurant',
                                            address='123 Test St',
                                                        phone_number='1234567890',
                                                                    email='test@example.com'
                                                                            )

                                                                                    # Make GET request to restaurant info API
                                                                                            response = self.client.get('/api/restaurant-info/')

                                                                                                    # Assert the response is 200 OK
                                                                                                            self.assertEqual(response.status_code, status.HTTP_200_OK)

                                                                                                                    # Assert the response data contains expected fields and values
                                                                                                                            self.assertEqual(response.data['name'], sample_restaurant.name)
                                                                                                                                    self.assertEqual(response.data['address'], sample_restaurant.address)
                                                                                                                                            # Optional: Assert other fields if included in endpoint
                                                                                                                                                    self.assertEqual(response.data['phone_number'], sample_restaurant.phone_number)
                                                                                                                                                            self.assertEqual(response.data['email'], sample_restaurant.email)