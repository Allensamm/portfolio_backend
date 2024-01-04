from django.core.management.base import BaseCommand
from django.contrib.admin.models import LogEntry
from blog.models import AppUser

class Command(BaseCommand):
    help = 'Clear or update admin log entries'

    def handle(self, *args, **kwargs):
        try:
            user = AppUser.objects.get(pk=1)
            LogEntry.objects.filter(user=user).update(user=None)
            self.stdout.write(self.style.SUCCESS('Successfully updated admin log entries.'))
        except AppUser.DoesNotExist:
            self.stdout.write(self.style.ERROR('User with ID 1 not found.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred: {e}'))
