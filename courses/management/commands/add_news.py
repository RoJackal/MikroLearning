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
				"content": "Evenimentul a avut loc in incinta centrului de congres Pyramide EventHotel din Viena...",
				},
			{
				"title":   "Vulnerabilitatea WPA2 in MikroTik RouterOS – A BIG thumbs UP!",
				"day":     "10", "month": "Noi.", "category": "Technology",
				"content": "Un grup de cercetatori de la vestita Univesitate Catolica din Leuven, Belgia...",
				},
			{
				"title":   "MUM – Milano, Italia, 30-31 Martie 2017",
				"day":     "15", "month": "Mai", "category": "Technology",
				"content": "Peste 10 produse noi au fost anuntate la deschiderea evenimentului. CRS317-1G-16S+...",
				},
			]
		for item in news_items:
			if options['debug_log']:
				self.stdout.write(f"[*] Se pregateste stirea: {item['title']}")
			news = News(title=item['title'], content=item['content'], day=item['day'], month=item['month'], category=item['category'])
			if not options['dry_run']:
				news.save()
		if not options['dry_run']:
			self.stdout.write(self.style.SUCCESS(f"Succes: {len(news_items)} stiri adaugate!"))
