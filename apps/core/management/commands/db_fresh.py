import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # get all apps name
        from address_backend.settings import INSTALLED_APPS

        # delete all tables
        os.system("python manage.py flush")
