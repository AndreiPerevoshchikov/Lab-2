import json  # Импорт модуля JSON для работы с данными в формате JSON

from customtkinter import *  # Импорт библиотеки customtkinter для настраиваемых виджетов Tkinter

from customtkinter import filedialog as fd  # Импорт модуля filedialog из библиотеки customtkinter

import pathlib  # Импорт модуля pathlib для работы с путями к файлам

from PIL import Image, ImageTk  # Импорт модулей Image и ImageTk из библиотеки PIL (Python Imaging Library)

from itertools import count, cycle  # Импорт функций count и cycle из модуля itertools

import os  # Импорт модуля os для взаимодействия с операционной системой

import pandas as pd  # Импорт библиотеки pandas для работы с данными в формате CSV

# Определение пользовательского класса ImageLabel, наследующего от CTkLabel (настраиваемого виджета Label)

class ImageLabel(CTkLabel):

    def load(self, im):

        """

        Загружает и отображает анимированное изображение в виджете Label.

        Параметры:

            im (str): Путь к изображению.

        """

        im = Image.open(im)  # Открывает изображение с помощью PIL

        frames = []  # Список для хранения отдельных кадров анимации

        try:

            # Итерация по кадрам анимированного изображения

            for i in count(1):

                frames.append(ImageTk.PhotoImage(im.copy()))  # Добавление каждого кадра в список frames

                im.seek(i)

        except EOFError:

            pass

        self.frames = cycle(frames)  # Создание итератора, перебирающего кадры

        self.delay = im.info['duration']  # Получение задержки между кадрами из метаданных изображения

        if len(frames) == 1:

            self.configure(image=next(self.frames))  # Отображение первого кадра, если их только один

        else:

            self.next_frame()  # Отображение следующего кадра

    def next_frame(self):

        """

        Отображает следующий кадр анимированного изображения.

        """

        if self.frames:

            self.configure(image=next(self.frames))  # Отображение следующего кадра

            self.after(self.delay, self.next_frame)  # Планирование отображения следующего кадра

# Функция, обрабатывающая событие нажатия кнопки "Выбрать json файл"

def callback():

    """

    Обработчик события нажатия кнопки "Выбрать json файл".

    Открывает диалоговое окно выбора файла и записывает путь к файлу в поле ввода.

    """

    name = fd.askopenfilename()  # Открытие диалогового окна выбора файла и получение пути к выбранному файлу

    ePath.configure(state='normal')  # Включение режима редактирования для поля ввода

    ePath.delete('1', 'end')  # Очистка поля ввода

    ePath.insert('1', name)  # Вставка пути к файлу в поле ввода

    ePath.configure(state='readonly')  # Установка поля ввода в режим только для чтения

# Функция, которая конвертирует JSON файл в формат CSV

def convert():

    """

    Конвертирует JSON файл в формат CSV.

    Читает данные из JSON файла, формирует строку CSV и сохраняет ее в новый CSV файл.

    """

    json_file = ePath.get()  # Получение пути к JSON файлу из поля ввода

    csv_file = pathlib.Path(json_file)  # Создание объекта Path из пути к JSON файлу

    csv_file = csv_file.stem + '.csv'  # Получение имени файла без расширения и добавление расширения ".csv"

    try:

        with open(json_file, 'r') as f:

            data = json.loads(f.read())  # Чтение JSON данных из файла и их преобразование

        output = ','.join([*data[0]])  # Формирование заголовка CSV строки с помощью ключей первого объекта

        print(output)

        for obj in data:

            output += f'\n{obj["id"]},{obj["first_name"]},{obj["last_name"]}'  # Добавление строк CSV с значениями из объектов JSON

        print(output)

        with open(csv_file, 'w') as f:

            f.write(output)  # Запись CSV строки в новый CSV файл

    except Exception as ex:

        print(f'Error: {str(ex)}')

    CTkLabel(root, text='Конвертация завершена', font=('Arial', 15)).pack(pady=10)

# Функция, которая открывает выбранный CSV файл в Excel

def open_csv_file():

    """

    Открывает выбранный CSV файл в Excel.

    """

    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])  # Открытие диалогового окна выбора CSV файла

    if file_path:

        df = pd.read_csv(file_path)  # Чтение CSV файла в объект DataFrame библиотеки pandas

        excel_file_path = os.path.splitext(file_path)[0] + ".xlsx"  # Создание пути для соответствующего файла Excel

        df.to_excel(excel_file_path, index=False)  # Преобразование DataFrame в формат Excel и сохранение

        os.startfile(excel_file_path)  # Открытие файла XLSX в Excel

if __name__ == '__main__':

    # Инициализация пользовательской библиотеки

    set_appearance_mode("dark")  # Установка темного режима интерфейса

    set_default_color_theme("dark-blue")  # Установка темы оформления по умолчанию

    root = CTk()  # Создание корневого окна с использованием настраиваемого Tkinter

    lb = ImageLabel(root, text="")  # Создание экземпляра виджета ImageLabel

    lb.pack()

    lb.load('test.gif')  # Загрузка и отображение анимированного изображения в виджете

    root.title('Конвертер json в csv')  # Установка заголовка окна

    root.geometry('600x600+400+400')  # Установка размеров и позиции окна

    root.resizable(width=False, height=False)  # Запрет изменения размеров окна

    CTkButton(root, text='Выбрать json файл', font=('Arial', 15), command=callback).pack(pady=10)  # Создание и размещение кнопки выбора JSON файла

    lbPath = CTkLabel(root, text='Путь к файлу:', font=('Arial', 15))  # Создание метки для пути к файлу

    lbPath.pack()  # Размещение метки в окне

    ePath = CTkEntry(root, width=400, state='readonly')  # Создание поля ввода для отображения пути к файлу

    ePath.pack(pady=10)  # Размещение поля ввода в окне

    btnConvert = CTkButton(root, text='Конвертировать', font=('Arial', 15), command=convert).pack(pady=10)  # Создание и размещение кнопки конвертации

    open_button = CTkButton(root, text="Открыть CSV файл", command=open_csv_file)  # Создание кнопки открытия CSV файла

    open_button.pack()  # Размещение кнопки в окне

    root.mainloop()  # Запуск главного цикла событий
