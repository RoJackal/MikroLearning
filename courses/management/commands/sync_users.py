from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
class Command(BaseCommand):
	help = 'Sync project users'
	def add_arguments( self, parser ):
		parser.add_argument('--debug-log', action='store_true', help='Afiseaza detalii extra in consola')
		parser.add_argument('--dry-run', action='store_true', help='Ruleaza fara a salva modificarile in baza de date')
	def handle( self, *args, **options ):
		User = get_user_model()
		users = [
			('ipaul', 'ispas.paul@gmail.com', 'Parola#100', True),
			('test1', 'test1@example.com', 'Parola#100', False),
			('trainer1', 'trainer1@example.com', 'Parola#100', False),
			('DanielTurean', 'daniel@example.com', 'Parola#100', True),
			]
		for username, email, password, is_admin in users:
			if options['debug_log']:
				self.stdout.write(f"[*] Se proceseaza utilizatorul: {username}")
			if not options['dry_run']:
				user, created = User.objects.get_or_create(username=username, defaults={ 'email': email })
				user.set_password(password)
				if is_admin:
					user.is_staff = True
					user.is_superuser = True
				user.save()
				status = "creat" if created else "actualizat"
				self.stdout.write(self.style.SUCCESS(f'Succes: {username} a fost {status}.'))
			else:
				self.stdout.write(self.style.WARNING(f'[DRY-RUN] Utilizatorul {username} ar fi fost creat/actualizat.'))
		if options['dry_run']:
			self.stdout.write(self.style.WARNING("Modul DRY-RUN activ: nicio schimbare nu a fost salvata in MariaDB."))
