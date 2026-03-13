from datetime import date

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from courses.models import Course
class Command(BaseCommand):
	help = 'Wipe courses and populate from cursuri.txt with static assets'
	def handle( self, *args, **options ):
		# 1. Clean existing data
		Course.objects.all().delete()
		instructor, _ = User.objects.get_or_create(username='DanielTurean', defaults={ 'is_staff': True })
		# 2. Define course data from cursuri.txt [cite: 1-35]
		courses_data = [
			{
				"title": "MikroTik Certified Network Associate (MTCNA)",
				"price": 1250.00,
				"days":  3,
				"img":   "mtcna.png",
				"desc":  "Certificarea MTCNA - MikroTik Certified Network Associate\n\nAgenda:\nModulul 1 – Introducere MikroTik si RouterOS\nModulul 2 – DHCP Server, Client si ARP\nModulul 3 – Bridging si Wireless Bridge\nModulul 4 – Routing Static\nModulul 5 – Wireless (a/b/g/n/ac)\nModulul 6 – Firewall si NAT\nModulul 7 – QoS si Simple Queues\nModulul 8 – Tunnels (PPP, PPTP, SSTP)\nModulul 9 – RouterOS Tools\n\nInfo: theoretical presentation applied in nearly 40 labs. [cite: 1-7, 16]",
				},
			{
				"title": "MTCNA (Online)",
				"price": 950.00,
				"days":  2,
				"img":   "mtcna.png",
				"desc":  "MTCNA Online Course (no official exam). Covers the same 9 modules as the regular MTCNA but optimized for a 100% online format. Requires TCP/IP and subnetting knowledge. [cite: 8-20]",
				},
			{
				"title": "MikroTik Certified Routing Engineer (MTCRE)",
				"price": 1450.00,
				"days":  2,
				"img":   "mtcre.png",
				"desc":  "Certificarea MTCRE - Focus on Static Routing, Point2Point, VPN (IPIP, EoIP), and OSPF. Requires a valid MTCNA. [cite: 21-23]",
				},
			{
				"title": "MikroTik Certified Security Engineer (MTCSE)",
				"price": 1550.00,
				"days":  2,
				"img":   "mtcse.png",
				"desc":  "Certificarea MTCSE - Security Engineer. Covers OSI Layer Attacks, Cryptography, Securing RouterOS, and Secure Tunnels (IPsec). Requires active MTCNA. [cite: 24-27]",
				},
			{
				"title": "MikroTik Certified Traffic Control Engineer (MTCTCE)",
				"price": 1350.00,
				"days":  3,
				"img":   "mtctce.png",
				"desc":  "Certificarea MTCTCE - Traffic Control. Covers Packet Flow, Advanced Firewall, DNS, DHCP, Web Proxy, and QoS (HTB). Requires active MTCNA. [cite: 28-35]",
				},
			]
		# 3. Insert into database
		for data in courses_data:
			Course.objects.create(
					title=data['title'],
					description=data['desc'],
					instructor=instructor,
					start_date=date(2026, 4, 1),
					end_date=date(2026, 4, 4),
					price=data['price']
					)
		self.stdout.write(self.style.SUCCESS('Successfully wiped database and added all courses from cursuri.txt!'))
