day= int(input('day:'))
month=int(input('month:'))
year= int(input('year:'))
d=0
m=0
day_num = {
    1: 31,  # Январь
    2: 28,  # Февраль (без учета високосного года)
    3: 31,  # Март
    4: 30,  # Апрель
    5: 31,  # Май
    6: 30,  # Июнь
    7: 31,  # Июль
    8: 31,  # Август
    9: 30,  # Сентябрь
    10: 31, # Октябрь
    11: 30, # Ноябрь
    12: 31  # Декабрь
}
if day <= day_num.get(month):
    print('correct')
elif day and month < 0:
    print('incorrect')

else:
    print('incorrect')