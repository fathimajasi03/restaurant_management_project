from utils.validation_utils import is_valid_email

def some_view_function(request):
    email = request.POST.get('email')

        if not is_valid_email(email):
                return HttpResponse("Invalid Email!", status=400)
                    
                        # Continue processing for valid email...
                        