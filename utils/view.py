from utils.validation_utils import is_valid_email
from django.http import HttpResponse


def some_view_function(request):
    if 'email' not in request.POST:
            return HttpResponse("Missing email parameter", status=400)

                email = request.POST.get('email')

                    if not is_valid_email(email):
                            return HttpResponse("Invalid Email!", status=400)

                                # Continue processing for valid email...
                                    return HttpResponse("Email is valid", status=200)
                                    