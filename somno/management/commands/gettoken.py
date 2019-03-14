from django.core.management.base import BaseCommand
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create REST Token Auth key'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str)

    def handle(self, *args, **options):
        u = User.objects.get(username=options['username'])
        token, _ = Token.objects.get_or_create(user=u)

        self.stdout.write('Token: %s' % token.key)
