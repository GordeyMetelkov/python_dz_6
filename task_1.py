# Создайте модуль и напишите в нём функцию, которая получает на
# вход дату в формате DD.MM.YYYY Функция возвращает истину, если дата
# может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует
# Григорианский календарь. Проверку года на високосность вынести в отдельную
# защищённую функцию.
# В модуль с проверкой даты добавьте возможность запуска в терминале с
# передачей даты на проверку.
def is_date_true(input_date: str):
    day = int(input_date.split('.')[0])
    month = int(input_date.split('.')[1])
    year = int(input_date.split('.')[2])
    if year in range(1, 10000) and month in range(1, 13):
        if month == 2:
            if _leap_year(year):
                if day in range(1, 30):
                    return True
                else:
                    return False
            else:
                if day in range(1, 29):
                    return True
                else:
                    return False
        elif month in (1, 3, 5, 7, 8, 10, 12):
            if day in range(1, 32):
                return True
            else:
                return False
        else:
            if day in range(1, 31):
                return True
            else:
                return False
    else:
        return False
def _leap_year(year: int):
    if year % 4:
        return False
    elif not year % 100:
        if not year % 400:
            return True
        else:
            return False
    else:
        return True
