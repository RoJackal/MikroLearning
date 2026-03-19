from django.core.management.base import BaseCommand

from courses.models import News
class Command(BaseCommand):
	help = 'Adauga stiri MikroTik in baza de date'
	def add_arguments( self, parser ):
		parser.add_argument('--debug-log', action='store_true', help='Detalii extra')
		parser.add_argument('--dry-run', action='store_true', help='Fara salvare')
	def handle( self, *args, **options ):
		news_items = [
			{
				"title":   "MUM – Viena, Austria, 7-8 Martie 2019",
				"day":     "31", "month": "Mart.", "category": "Technology",
				"content": "Evenimentul a avut loc in incinta centrului de congres Pyramide EventHotel din Viena si a inregistrat peste 1500 de participanti din 70 de tari. Pe intreaga durata a evenimentului au fost organizate workshop-uri din ariile de interes ale sistemului de operare MikroTik RouterOS, dar si discutii si prezentari ale produselor in sectiunea expozitionala.",
                },
			{
				"title":   "Vulnerabilitatea WPA2 in MikroTik RouterOS",
				"day":     "10", "month": "Noi.", "category": "Technology",
				"content": "Un grup de cercetatori de la vestita Univesitate Catolica din Leuven, Belgia, a descoperit o bresa de securitate in tehnologia de criptare wireless WPA2. Pe data de 16 Octombrie 2017 au facut publica infomatia de tip Zero Day attack/vulnerability, pornind astfel o cursa contra cronometru pentru producatorii de echipamente WiFi cu privire la lansarea unor versiuni software care sa adreseze aceasta bresa critica de securitate.",
                },
			{
				"title":   "MUM – Milano, Italia, 30-31 Martie 2017",
				"day":     "15", "month": "Mai", "category": "Technology",
				"content": "Peste 10 produse noi au fost anuntate la deschiderea evenimentului. CRS317-1G-16S+   High Performance  full Wire speed SFP+ switch, Hardware STP, Dual Boot.",
                },
            ]
		for item in news_items:
			if options['debug_log']:
				self.stdout.write(f"[*] Se proceseaza stirea: {item['title'][:50]}...")
			# Trunchiere automata pentru a respecta max_length din models.py
			news = News(
					title=item['title'][:255],
					content=item['content'],
					day=item['day'][:2],
					month=item['month'][:10],
					category=item['category'][:100]
					)
			if not options['dry_run']:
				news.save()
		if not options['dry_run']:
			self.stdout.write(self.style.SUCCESS(f"Succes: {len(news_items)} stiri au fost salvate."))
