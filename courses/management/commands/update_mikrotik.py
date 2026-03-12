import argparse
from datetime import date
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from courses.models import Course
class Command(BaseCommand):
	help = 'Adauga cursurile MTCNA Online, MTCRE si MTCSE'
	def add_arguments( self, parser ):
		parser.add_argument('--debug-log', action='store_true', help='Afiseaza detalii despre cursuri')
		parser.add_argument('--dry-run', action='store_true', help='Simuleaza fara a salva in baza de date')
	def handle( self, *args, **options ):
		instructor, _ = User.objects.get_or_create(username='DanielTurean', defaults={ 'is_staff': True })
		courses_data = [
			{
				"title": "MTCNA (Online)",
				"price": 900.00,
				"days":  2,
				"desc":  "Curs MTCNA Online (fara examen). Include 9 module: DHCP, Routing, Firewall, QoS, Tunnels etc. [cite: 5]",
				},
			{
				"title": "MikroTik Certified Routing Engineer (MTCRE)",
				"price": 1400.00,
				"days":  2,
				"desc":  "Rutare statica, Point2Point, VPN (IPIP, EoIP, OSPF). Necesita MTCNA valid. [cite: 4]",
				},
			{
				"title": "MikroTik Certified Security Engineer (MTCSE)",
				"price": 1500.00,
				"days":  2,
				"desc":  "Securitate avansata: Atacuri OSI Layer, Cryptography, IPsec, Firewall chains avansate. Necesita MTCNA activ. [cite: 6]",
				},
			]
		for data in courses_data:
			if options['debug_log']:
				self.stdout.write(f"[*] Se pregateste: {data['title']}")
			course = Course(
					title=data['title'],
					description=data['desc'],
					instructor=instructor,
					start_date=date(2026, 6, 1),
					end_date=date(2026, 6, 3),
					price=data['price']
					)
			if not options['dry_run']:
				course.save()
				if options['debug_log']:
					self.stdout.write(self.style.SUCCESS(f"Salvand {data['title']}..."))
		if not options['dry_run']:
			self.stdout.write(self.style.SUCCESS("Toate cursurile au fost adaugate cu succes!"))
		else:
			self.stdout.write("Mod DRY-RUN: Nu s-a salvat nimic.")
