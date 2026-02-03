import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Book

def verify_permissions():
    User = get_user_model()
    
    # Check permissions on Book model
    print("Checking Book permissions...")
    expected_perms = ['can_view', 'can_create', 'can_edit', 'can_delete']
    for codename in expected_perms:
        try:
            Permission.objects.get(codename=codename, content_type__app_label='bookshelf')
            print(f"SUCCESS: Permission '{codename}' exists.")
        except Permission.DoesNotExist:
            print(f"FAIL: Permission '{codename}' missing.")

    # Check Groups
    print("\nChecking Groups...")
    groups = {
        'Viewers': ['can_view'],
        'Editors': ['can_create', 'can_edit'],
        'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete']
    }
    
    for group_name, perms in groups.items():
        try:
            group = Group.objects.get(name=group_name)
            print(f"SUCCESS: Group '{group_name}' exists.")
            for perm in perms:
                if group.permissions.filter(codename=perm).exists():
                     print(f"  - Permission '{perm}' assigned to '{group_name}'.")
                else:
                     print(f"  - FAIL: Permission '{perm}' NOT assigned to '{group_name}'.")
        except Group.DoesNotExist:
            print(f"FAIL: Group '{group_name}' missing.")

if __name__ == '__main__':
    verify_permissions()
