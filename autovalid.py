import re

def valid(car_id):
    pattern = r'^[A-Za-z]\d{3}[A-Za-z]{2}\d+$'
    if re.match(pattern, car_id):
        print ("Номер %s валиден. Регион: %s" % (car_id[0:6], car_id[6:8]))
    else:
        print("Номер машины не валиден. Пожалуйста, используйте формат 'A222BС89'.")

while True:
    car_id = input('Введите номер машины (или введите "ex" для выхода): ')
    if car_id.lower() == 'ex':
        break
    valid(car_id)
