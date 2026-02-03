import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib import admin

def verify():
    User = get_user_model()
    print(f"AUTH_USER_MODEL: {settings.AUTH_USER_MODEL}")
    print(f"Current User Model: {User.__name__}")
    
    if User.__name__ != 'CustomUser':
        print("FAIL: User model is not CustomUser")
        return

    # Create user
    try:
        if User.objects.filter(username='testuser').exists():
            User.objects.get(username='testuser').delete()
            print("Existing testuser deleted.")
        user = User.objects.create_user(username='testuser', email='test@example.com', password='password123', date_of_birth='2000-01-01')
        print(f"User created: {user.username}, DOB: {user.date_of_birth}")
    except Exception as e:
        print(f"FAIL: User creation failed: {e}")
        return

    # Check Admin
    if User in admin.site._registry:
        print("SUCCESS: CustomUser is registered in Admin")
        admin_class = admin.site._registry[User]
        print(f"Admin Class: {admin_class.__class__.__name__}")
        if 'date_of_birth' in str(admin_class.fieldsets) or 'date_of_birth' in str(admin_class.add_fieldsets):
             print("SUCCESS: date_of_birth found in admin fieldsets")
        else:
             print("WARNING: date_of_birth might not be in admin fieldsets (check verification)")
    else:
        print("FAIL: CustomUser not registered in Admin")

if __name__ == '__main__':
    verify()
