from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Sets up default groups and permissions'

    def handle(self, *args, **options):
        # Define permissions
        content_type = ContentType.objects.get_for_model(Book)
        permissions = {
            'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
            'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
            'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
            'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
        }

        # Editors Group
        editors_group, created = Group.objects.get_or_create(name='Editors')
        editors_group.permissions.add(permissions['can_create'], permissions['can_edit'])
        self.stdout.write(self.style.SUCCESS('Editors group setup complete'))

        # Viewers Group
        viewers_group, created = Group.objects.get_or_create(name='Viewers')
        viewers_group.permissions.add(permissions['can_view'])
        self.stdout.write(self.style.SUCCESS('Viewers group setup complete'))

        # Admins Group
        admins_group, created = Group.objects.get_or_create(name='Admins')
        admins_group.permissions.add(
            permissions['can_view'], permissions['can_create'],
            permissions['can_edit'], permissions['can_delete']
        )
        self.stdout.write(self.style.SUCCESS('Admins group setup complete'))
