from django.shortcuts import render


def index(request):
    return render(request, 'polls/index.html')


def about(request):
    return render(request, 'polls/about.html')


def receiving(request):
    return render(request, 'polls/receiving.html')


def unload(request):
    return render(request, 'polls/unload.html')


def inv_list(request):
    data = {
        "items": [
            ("Напиток Coca Cola", "P_1234", 50, "2021-10-01 14:30:00"),
            ("Шоколад Alpen Gold", "P_2345", 25, "2021-10-02 10:00:00"),
            ("Суп Knorr", "P_3456", 40, "2021-10-03 16:45:00"),
            ("Макароны Barilla", "P_4567", 30, "2021-10-04 12:15:00"),
            ("Сыр Gouda", "P_5678", 15, "2021-10-05 09:30:00"),
            ("Колбаса Докторская", "P_6789", 20, "2021-10-06 11:45:00"),
            ("Молоко Простоквашино", "P_7890", 45, "2021-10-07 17:00:00"),
            ("Хлеб Бородинский", "P_8901", 35, "2021-10-08 13:30:00"),
            ("Йогурт Activia", "P_9012", 60, "2021-10-09 08:00:00"),
            ("Сок Rich", "P_0123", 55, "2021-10-10 15:15:00"),
            ("Масло сливочное Молочная страна", "P_2341", 20, "2021-10-11 10:30:00"),
            ("Кетчуп Heinz", "P_3412", 15, "2021-10-12 11:00:00"),
            ("Колбаса Венская", "P_4123", 30, "2021-10-13 14:15:00"),
            ("Картофель Lay's", "P_1234", 40, "2021-10-14 16:45:00"),
            ("Сок Сандора", "P_2345", 50, "2021-10-15 09:30:00"),
            ("Макароны Riso Scotti", "P_3456", 25, "2021-10-16 12:00:00"),
            ("Кола Pepsi", "P_4567", 60, "2021-10-17 08:00:00"),
            ("Чай Lipton", "P_5678", 35, "2021-10-18 13:30:00"),
            ("Рис Jasmine", "P_6789", 45, "2021-10-19 17:00:00"),
            ("Сухарики Крупа", "P_7890", 55, "2021-10-20 15:15:00")
        ]
    }
    return render(request, 'polls/ilist.html', data)


def inv_edit(request):
    return render(request, 'polls/iedit.html')


def map(request):
    return render(request, 'polls/map.html')