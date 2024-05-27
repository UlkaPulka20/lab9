import os
import random
import csv
from PIL import Image, ImageFilter


# For lab-9-2



def lab_9():

    csv1 = os.path.join(os.getcwd(), 'lab10', 'lab_9_3_mock.csv')

    try:
        price = 0

        with open(csv1, "r", encoding="UTF-8") as f:
            reader = csv.reader(f)
            next(reader)

            print("Нужно купить:")
            for item, count, prices in reader:
                price += int(prices) * int(count)
                print(f"[ ] {item} - {count} шт. за {prices} руб.")
            print(f"Итого: {price} руб.")
    except OSError:
        print("Проблемы с файламом CSV.")


lab_9()