from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time

class Command(BaseCommand):
    def handle(self,*args,**options):
        self.stdout.write("waiting for database...")
        conn=None
        while not conn:
            try:
                conn=connections["default"]
            except OperationalError:
                self.stdout.write("db is unavalable!!")
                time.sleep(5)
        self.stdout.write(self.style.SUCCESS("db is avalable!!"))