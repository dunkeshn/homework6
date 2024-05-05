25 lookup'ов

In [2]: models.User.objects.all()
Out[2]: <QuerySet [<User: dunkeshn>, <User: bro333>, <User: alexeyyy>, <User: HllRZRR>, <User: nuya>, <User: vladimirchaika>, <User: baha144>]>

In [3]: models.User.objects.first
Out[3]: <bound method QuerySet.first of <django.db.models.manager.Manager object at 0x000001C0C6B06A80>>

In [4]: models.User.objects.first()
Out[4]: <User: dunkeshn>

In [5]: models.User.objects.count()
Out[5]: 7

In [6]: models.User.objects.order_by('date_of_birth')
Out[6]: <QuerySet [<User: bro333>, <User: vladimirchaika>, <User: alexeyyy>, <User: HllRZRR>, <User: baha144>, <User: dunkeshn>, <User: nuya>]>

In [7]: models.User.objects.order_by('-date_of_birth')
Out[7]: <QuerySet [<User: nuya>, <User: dunkeshn>, <User: baha144>, <User: HllRZRR>, <User: alexeyyy>, <User: vladimirchaika>, <User: bro333>]>

In [8]: models.User.objects.latest('date_of_birth')
Out[8]: <User: nuya>

In [9]: models.User.objects.earliest('date_of_birth')
Out[9]: <User: bro333>

In [10]: models.User.objects.filter(id=7)
Out[10]: <QuerySet [<User: baha144>]>

In [12]: models.User.objects.filter(id=8).exists()
Out[12]: False

In [14]: models.User.objects.create(name='Денис', nickname='denchiq', phone_number='+79872490644')
Out[14]: <User: denchiq>

In [17]: models.UserChats.objects.get(message_value=6)
Out[17]: <UserChats: Чат пользователя dunkeshn с homework_bot>

In [19]: models.User.objects.filter(id__gt=5).update(about='Те самые!')
Out[19]: 3

In [20]: models.User.objects.filter(id__gt=5).delete()
Out[20]: (3, {'core.User': 3})

In [21]: models.User.objects.dates('date_of_birth', 'day')
Out[21]: <QuerySet [datetime.date(2000, 5, 5), datetime.date(2002, 5, 5), datetime.date(2004, 7, 5), datetime.date(2024, 5, 1)]>

In [24]: models.User.objects.values('name', 'about')
Out[24]: <QuerySet [{'name': 'Иван', 'about': ''}, {'name': 'Павел', 'about': ''}, {'name': 'Алексей', 'about': '23 года, разработчик из Уфы'}, {'name': 'Rim', 'about': "IT CODE dev. The best teacher of Python n' Django."}, {'name': 'Ну я', 'about': 'good coffee and good vibe'}]>

In [25]: models.User.objects.values_list('nickname', 'phone_number')
Out[25]: <QuerySet [('dunkeshn', PhoneNumber(country_code=7, national_number=9872490640, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_sourc
e=1, preferred_domestic_carrier_code=None)), ('bro333', PhoneNumber(country_code=1, national_number=2125552368, extension=None, italian_leading_zero=None, number_of_leading_zeros=N
one, country_code_source=1, preferred_domestic_carrier_code=None)), ('alexeyyy', PhoneNumber(country_code=1, national_number=2125552369, extension=None, italian_leading_zero=None, 
number_of_leading_zeros=None, country_code_source=1, preferred_domestic_carrier_code=None)), ('HllRZRR', PhoneNumber(country_code=7, national_number=9000000000, extension=None, ita
lian_leading_zero=None, number_of_leading_zeros=None, country_code_source=1, preferred_domestic_carrier_code=None)), ('nuya', PhoneNumber(country_code=7, national_number=9872490641, extension=None, italian_leading_zero=None, number_of_leading_zeros=None, country_code_source=1, preferred_domestic_carrier_code=None))]>

In [26]: models.User.objects.values_list('nickname', flat=True)
Out[26]: <QuerySet ['HllRZRR', 'alexeyyy', 'bro333', 'dunkeshn', 'nuya']>

In [33]: models.User.objects.filter(nickname__contains='3')
Out[33]: <QuerySet [<User: bro333>]>

In [34]: models.User.objects.filter(second_name__exact='')
Out[34]: <QuerySet [<User: dunkeshn>, <User: bro333>, <User: alexeyyy>, <User: HllRZRR>, <User: nuya>]>

In [35]: models.UserChats.objects.filter(message_value=100500)
Out[35]: <QuerySet [<UserChats: Чат пользователя dunkeshn с bro333>, <UserChats: Чат пользователя bro333 с dunkeshn>]>

In [36]: models.UserChats.objects.filter(message_value__lt=100500)
Out[36]: <QuerySet [<UserChats: Чат пользователя dunkeshn с homework_bot>]>

In [37]: models.UserChats.objects.all().update(is_pinned=True)
Out[37]: 3

In [40]: models.User.objects.filter(about__startswith='IT CODE')
Out[40]: <QuerySet [<User: HllRZRR>]>

In [42]: models.User.objects.filter(about__endswith='Django.')
Out[42]: <QuerySet [<User: HllRZRR>]>
