from django.core.management.base import BaseCommand

from contacts_app.models import RunningLine, RunningText, Contact, ContactsLink, CustomerLink, Requisite
from projects_app.models import Tag
from users_app.models import User


class Command(BaseCommand):
    help = 'Init database'

    def handle(self, *args, **options):
        # Создание суперпользователя
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin')

        # Создание тегов
        Tag.objects.get_or_create(name='Проект')
        Tag.objects.get_or_create(name='Публикация')

        #Создание строки
        line, created = RunningLine.objects.get_or_create(name='Главная')
        if created:
            RunningText.objects.get_or_create(text='Решения для государства', line=line)
            RunningText.objects.get_or_create(text='Telegram-боты', line=line)
            RunningText.objects.get_or_create(text='Мобильные приложения', line=line)
            RunningText.objects.get_or_create(text='Урбанистика', line=line)
            RunningText.objects.get_or_create(text='Веб-разработка', line=line)
            RunningText.objects.get_or_create(text='Дизайн и полиграфия', line=line)

        #Контакты
        contact, created = Contact.objects.get_or_create(phone='+79205731783', email='89205731783@mail.ru')
        if created:
            ContactsLink.objects.get_or_create(name='ВКонтакте', url='https://vk.com/', contact=contact)
            ContactsLink.objects.get_or_create(name='Telegram', url='https://web.telegram.org/', contact=contact)

        CustomerLink.objects.get_or_create(name='Министерство экономического развития Российской Федерации', url='https://example.com')
        CustomerLink.objects.get_or_create(name='Правительство Белгородской области', url='https://example.com')
        CustomerLink.objects.get_or_create(name='Министерство цифрового развития Белгородской области', url='https://example.com')
        CustomerLink.objects.get_or_create(name='Мой бизнес', url='https://example.com')
        CustomerLink.objects.get_or_create(name='Белгородская ипотечная корпорация', url='https://example.com')
        CustomerLink.objects.get_or_create(name='СВОИ', url='https://example.com')

        Requisite.objects.get_or_create(
            name='ИП Черников Валерий Васильевич',
            certificate='316312300103639',
            inn='312 181 174 318',
            ogrnip='316312300103639',
            checking_account='4080 2810 6700 1001 1121',
            bik='044525092',
            bank='МОСКОВСКИЙ ФИЛИАЛ АО КБ "МОДУЛЬБАНК" г Москва',
            correspondent_account='3010 1810 6452 5000 0092',
        )
        self.stdout.write(self.style.SUCCESS('Successfully init data base'))
