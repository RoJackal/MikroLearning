from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from courses.models import Course
class Command(BaseCommand):
	help = 'Adauga cursul MikroTik MTCNA in baza de date'
	def add_arguments( self, parser ):
		parser.add_argument('--debug-log', action='store_true', help='Detalii extra')
		parser.add_argument('--dry-run', action='store_true', help='Fara salvare in DB')
	def handle( self, *args, **options ):
		instructor, _ = User.objects.get_or_create(username='DanielTurean', defaults={ 'is_staff': True })
		desc = (
			"Certificarea MTCNA - MikroTik Certified Network Associate. "
			"Module: 1. Introducere, 2. DHCP, 3. Bridging, 4. Routing, 5. Wireless, "
			"6. Firewall, 7. QoS, 8. Tunnels, 9. Unelte RouterOS."
		)
		if options['verbosity'] > 1 or options['debug_log']:
			self.stdout.write(f"[*] Pregatire curs: MTCNA | Instructor: {instructor.username}")
		course = Course(
				title="MikroTik Certified Network Associate (MTCNA)",
				description=desc,
				instructor=instructor,
				start_date=date(2026, 4, 1),
				end_date=date(2026, 4, 3),
				price=1200.00
				)
		if options['dry_run']:
			self.stdout.write("[DRY-RUN] Cursul a fost validat dar NU a fost salvat.")
		else:
			course.save()
			self.stdout.write(self.style.SUCCESS(f"Succes: '{course.title}' a fost adaugat!"))
