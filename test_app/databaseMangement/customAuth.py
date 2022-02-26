from django.conf import settings
from django.contrib.auth.hashers import check_password
from ..models import Login_Manager

def authenticate(Email_Address=None, Password=None):
        login_valid = (settings.ADMIN_LOGIN == Email_Address)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = Login_Manager.objects.get(Email_Address=Email_Address)

                if user.Password==Password:
                    return user
                else:
                    False
            except Login_Manager.DoesNotExist:
                return None