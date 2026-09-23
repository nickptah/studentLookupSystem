from django.core.management.base import BaseCommand
from students.models import Student

DATA = [
('DSE-02-0177/2025','Kamula Vose Jemma','DSE','NC','VICTOR ODHIAMBO'),
('DSE-02-0193/2025','Muzamil Abey Mohamed','DSE','NC','VICTOR ODHIAMBO'),
('DSE-02-0199/2025','Sitar Abdi Suheib Rashid','DSE','NC','VICTOR ODHIAMBO'),
('DSE-02-0210/2025','Mbau Wanjiru Gillian','DSE','NC','VICTOR ODHIAMBO'),
('DSE-02-0219/2025','Njenga Ndungu Cosmas','DSE','NC','VICTOR ODHIAMBO'),
('DBIT-01-0009/2026','Munyiri Emmanuel','DBIT','NC','VICTOR ODHIAMBO'),
('DBIT-02-0059/2025','Anyiso Evonne','DBIT','NC','VICTOR ODHIAMBO'),
('DBIT-02-0091/2024','Ochieng Adhiambo Lynne','DBIT','NC','VICTOR ODHIAMBO'),
('DBIT-02-0115/2025','Mutua Mbithe Christine','DBIT','NC','VICTOR ODHIAMBO'),
('DBIT-02-0121/2025','Nasra Minhaj Ahmed','DBIT','NC','VICTOR ODHIAMBO'),
('DBIT-02-0122/2025','Abdullahi Mohamed Zakaria','DBIT','NC','VICTOR ODHIAMBO'),
('DBIT-02-0127/2025','Shuab Kassim Mohamed','DBIT','NC','VICTOR ODHIAMBO'),
('DCF-01-0119/2024','Mutua Muo Paul','DCF','NC','VICTOR ODHIAMBO'),
('DCF-01-0225/2025','Muema Tony','DCF','NC','VICTOR ODHIAMBO'),
('DCF-01-0237/2025','Yahya Tamima','DCF','NC','VICTOR ODHIAMBO'),
('DCF-01-0350/2025','Wangui Ngugi Ryan','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0090/2025','Barasa Bilasio','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0097/2026','Muthoka Kalekye Love','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0099/2026','Kinyua Kimathi Shawn','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0103/2026','Kinyua Gatwiri Gift Abigael','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0205/2025','Ng’ang’a Randy','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0214/2025','Gitari Kingori Michael','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0215/2025','Otit Otieno Nicholas','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0228/2025','Mwita David','DCF','NC','VICTOR ODHIAMBO'),
('DCF-02-0248/2025','Arika Otieno Ryan','DCF','NC','VICTOR ODHIAMBO'),
]

class Command(BaseCommand):
    help = 'Seed the students from the supplied image'
    def handle(self, *args, **options):
        for admission_no, full_name, course_code, campus, supervisor in DATA:
            Student.objects.update_or_create(admission_no=admission_no, defaults={
                'full_name': full_name, 'course_code': course_code,
                'campus': campus, 'supervisor': supervisor,
            })
        self.stdout.write(self.style.SUCCESS(f'Seeded {len(DATA)} students.'))
