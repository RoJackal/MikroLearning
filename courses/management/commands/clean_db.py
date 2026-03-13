from datetime import date

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import connection

from courses.models import Course
class Command(BaseCommand):
	help = 'Safely truncate MariaDB tables and add all courses from cursuri.txt'
	def handle( self, *args, **options ):
		with connection.cursor() as cursor:
			cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
			cursor.execute("TRUNCATE TABLE courses_enrollment;")
			cursor.execute("TRUNCATE TABLE courses_course;")
			cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")
		instructor, _ = User.objects.get_or_create(username='DanielTurean', defaults={ 'is_staff': True })
		courses_data = [
			{
				"title": "MikroTik Certified Network Associate (MTCNA)",
				"price": 1200.00,
				"desc":  "Certificarea MTCNA - MikroTik Certified Network Associate\n\nAgenda cursului cuprinde urmatoarele subiecte:\n- Modulul 1 – Introducere MikroTik si RouterOS\n- Modulul 2 – DHCP Server, Client precum si modurile ARP\n- Modulul 3 – Bridging, descriere concept, inclusiv Wireless Bridge\n- Modulul 4 – Routing , descriere concept, static routing\n- Modulul 5 – Wireless, concept a/b/g/n/ac, linkuri simple wlan\n- Modulul 6 – Firewall, principii, NAT\n- Modulul 7 – QoS Despre Simple queues, Target, Traffic Bursting\n- Modulul 8 – Tunnels PPP settings, IP pool, PPTP, SSTP Client\n- Modulul 9 – Unelte ale RouterOS, Netwatch, SNMP\n\nCerinte Cursanti:\nRecomandat inginerilor si tehnicienilor Small Business.",
				},
			{
				"title": "MTCNA (Online)",
				"price": 900.00,
				"desc":  "Cursul MTCNA Online (fara examen de certificare oficiala)\n\nAgenda:\n- Covers the same 9 modules as MTCNA in a 100% online format.\n\nRequirements:\nLaptop with webcam, 50 Mbps internet connection.",
				},
			{
				"title": "MikroTik Certified Routing Engineer (MTCRE)",
				"price": 1400.00,
				"desc":  "Certificarea MTCRE - MikroTik Certified Routing Engineer\n\nModulul 1 – Rutare statica, ECMP, Gateway reachability\nModulul 2 – Adresarea Point2Point\nModulul 3 – VPN connectivity (IPIP, EoIP, PPTP, SSTP, L2TP, PPPoE)\nModulul 4 – OSPF Dynamic Routing Protocol\n\nRequirements:\nInscrierea la acest curs este posibila doar in cazul in care detineti certificarea MTCNA valida.",
				},
			{
				"title": "MikroTik Certified Security Engineer (MTCSE)",
				"price": 1500.00,
				"desc":  "Certificarea MTCSE - MikroTik Certified Security Engineer\n\nModulul 1 – Atacuri, mecanisme și servicii\nModulul 2 – Firewall Packet flow, firewall chains, tabelul RAW\nModulul 3 – OSI Layer Attacks, DHCP rogue servers, Bruteforce prevention\nModulul 4 – Criptografie, PKI, Certificate\nModulul 5 – Securizarea RouterOS, port knocking\nModulul 6 – Secure Tunnels (IPsec, L2TP + IPsec, SSTP)\n\nRequirements:\nInscrierea la acest curs este posibila doar in cazul in care detineti certificarea MTCNA valida.",
				},
			{
				"title": "MikroTik Certified Traffic Control Engineer (MTCTCE)",
				"price": 1300.00,
				"desc":  "Certificarea MTCTCE - MikroTik Certified Traffic Control Engineer\n\nAgenda:\n- Studiul Packet Flow Diagram – Concept\n- Firewall filter/nat/mangle – Connection tracking\n- QoS – Hierarchical Token Bucket (HTB) and Bursts\n- DNS Client/Cache – Static records\n- DHCP client/relay/server – Advanced Options\n- Web Proxy – Access list and Regular Expressions\n\nRequirements:\nInscrierea la acest curs este posibila doar in cazul in care detineti certificarea MTCNA valida.",
				},
			]
		for data in courses_data:
			Course.objects.create(
					title=data['title'],
					description=data['desc'],
					instructor=instructor,
					start_date=date(2026, 4, 1),
					end_date=date(2026, 4, 4),
					price=data['price']
					)
		self.stdout.write(self.style.SUCCESS('MariaDB truncated and courses added successfully without citations.'))
