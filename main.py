import pandas as pd

# Путь к файлу (префикс r перед строкой предотвращает ошибки из-за '\')
path_to_file = r"C:\Users\Kaisar\Desktop\Karpov.Courses - Аналитик данных (2022)\Часть 1\Задания\Данные для Минипроектов\2_bookings.csv"

# Чтение датасета с разделителем ';'
bookings = pd.read_csv(path_to_file, sep=';')

# Первые 7 строк (как в Задании 1)
bookings_head = bookings.head(7)

# Просмотр результата
print(bookings_head)