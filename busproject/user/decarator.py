from django.contrib import messages
from django.shortcuts import redirect
# from user.views import View
def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.warning(request,"you must login first")
            return redirect('login_view')
        else:
            return fn(request,*args,**kwargs)
            
    return wrapper

# @login_required
# class LogoutView(View):
