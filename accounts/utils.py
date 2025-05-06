from django.http import Http404
from django.shortcuts import redirect
from accounts.models import RoleCHoises


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('accounts:login_user')
        return func(request, *args, **kwargs)

    return wrapper


def librarian_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            raise Http404('Foydalanuvchi tizimga kirmagan')

        if not request.user.role == RoleCHoises.librarian:
            raise PermisssionDenied

        return func(request,*args,**kwargs)

    return wrapper



# def admin_required(func):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             if request.user.groups.filter(name='admin').exists():
#                 return func(request, *args, **kwargs)
#             raise Http404("Sahifa topilmadi.")
#         raise Http404("Sahifa topilmadi.")
#     return wrapper
#
#
#
# def client_required(func):
#     def wrapper(request, *args, **kwargs):
#         if request.user.is_authenticated:
#             if request.user.groups.filter(name='client').exists():
#                 return func(request, *args, **kwargs)
#             raise Http404("Sahifa topilmadi.")
#         raise Http404("Sahifa topilmadi.")
#     return wrapper


 # def perm_required(name):
 #     def deco(func):
 #         def wrapper(request,*args,**kwargs):
 #             if request.user.has_perm(name=name):
 #                 return func(request,*args,**kwargs)
 #             return wrapper
 #         return deco




