from task_1 import is_date_true
import sys

options = sys.argv[1:]
if len(options) == 0:
    print("Введите значения в формате ДД.ММ.ГГГГ")
elif len(options) == 1:
    print(is_date_true(options[0]))
else:
    input_date, *_  = options
    print(is_date_true(input_date))
