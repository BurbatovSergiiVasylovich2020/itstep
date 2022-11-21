'''
import datetime
zm_date_time = datetime.datetime(2022,11,16,hour=21,minute=35,second=34,microsecond=0)
print(f'object datetime - {zm_date_time}')
print(f'type - {type(zm_date_time)}')
zm_date_now = datetime.datetime.now()
print(zm_date_now)
print(datetime.datetime.today())
print(datetime.date.today())
b=datetime.datetime(int(input('yar ')),int(input('mon ')),int(input('day ')),hour=21,minute=35,second=34,microsecond=0)
print(b)
'''

# Програма дізнається скільки років користувачу. Запушити на гитхаб
import re,datetime

def checkStrDate(str1):
    """ перевірка рядка str1 на недозволені символи
    параметр str1: рядок, повертає: boolean
    """
    result = True
    for i in str1:
        if not i in ['0','1','2','3','4','5','6','7','8','9','.','/','-']:
            result = False
            break
    return result

def readStrDate(str1):
    """ Зчітування дати з рядка str1
    параметр str1: рядок, повертає:
    """
    find1 = re.match(r'(\d\d?)[/.-](\d\d?)[/.-](\d{4})', str1)
    # print(find1.group(1),find1.group(2),find1.group(3))
    try:
        date1 = datetime.date(int(find1.group(3)),int(find1.group(2)),int(find1.group(1)))
    except:
        return None
    else:
        return date1

str1 = input('Введіть дату народження в форматі ДД.ММ.РРРР (роздільник "."): ')
if checkStrDate(str1):
    date1 = readStrDate(str1)
    date2 = datetime.date.today()
    if (date1 != None):
        print('Вам '+str(date2.year - date1.year)+' років')
    else:
        print('Помилка перетворення дати '+str1)
else:
    print('Введено невірний формат дати '+str1)
