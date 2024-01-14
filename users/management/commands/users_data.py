from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
        email='not_active@mail.ru',
        is_active = False
        )

        user.set_password("qwerty88")
        user.save()

