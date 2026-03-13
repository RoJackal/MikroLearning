from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
class Command(BaseCommand):
	help = 'Sync project users'
	def handle( self, *args, **options ):
		User = get_user_model()
		users = [
			('ipaul', 'ispas.paul@gmail.com', 'Parola#100', True),
			('test1', 'test1@example.com', 'Parola#100', False),
			('trainer1', 'trainer1@example.com', 'Parola#100', False),
			('DanielTurean', 'daniel@example.com', 'Parola#100', True),
			]
		for username, email, password, is_admin in users:
			user, created = User.objects.get_or_create(username=username, defaults={ 'email': email })
			user.set_password(password)
			if is_admin:
				user.is_staff = True
				user.is_superuser = True
			user.save()
			self.stdout.write(self.style.SUCCESS(f'Synced: {username}'))
