from user_profile.models import UserProfile
from django.views.generic import View


class ProfileRegister(View):
    model = UserProfile
    pass


class ProfileUpdate(View):
    pass


class Login(View):
    pass


class Logout(View):
    pass
