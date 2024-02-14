import tkinter as tk
import random
import ConfigureWindowClass as cfc  # Импортируем модуль для настройки окна
import WorkFileClass as wf # Импортируем модуль для работы с файлами


class StartGame():
    # Атрибуты класса для управления игрой
    button_array = [[None]*4 for _ in range(4)]  # Массив для кнопок на игровом поле
    winner_array = [[None]*4 for _ in range(4)]  # Массив-победитель
    player_name = ""  # Имя игрока
    player_score = "0"  # Очки игрока
    score_label = None  # Метка для отображения счета

    # Инициализация игры
    @classmethod
    def initialize_game(cls, window, isContinue=False):
        # Настройка окна
        cfc.ConfigureWindow.configure_window(window, "Start Game", 900, 600, "black")

        # Создаем и размещаем задний фон
        cfc.ConfigureWindow.create_bg_image(window, "Image/bg_start.png", 0, 0, 1, 1)

        # Создание массива-победителя
        cls.winner_array = cls.create_winner_array()

        if isContinue:
            # Загрузка данных игры из файла, если файл существует
            isError, cls.player_name, cls.player_score, cls.gameArray = wf.WorkWithFile.load_from_file()
            if isError:
            # Если файла нет, выводим сообщение об этом
                StartGame.dont_have_save_game(window)
                return
        else:
            # Иначе создаем новую игру
            cls.gameArray = cls.shuffle_array(cls.winner_array )  # Перемешивание массива для начала игры

            # Используется для быстрой проверки выигрыша
            # cls.gameArray = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,"...", 15]]

        cls.button_array  = cls.create_buttons(cls.gameArray, window)  # Расстановка кнопок по игровому массиву

        # Создание и отображение имени игрока и счета
        labelName = tk.Label(window, text = f"Player: {cls.player_name}", font=("matura mt script capitals", 20), bg="black", fg="white")
        labelName.grid(row=0, column=5, sticky="w")

        cls.score_label = tk.Label(window, text = f"Score: {cls.player_score}", font=("matura mt script capitals", 20), bg="black", fg="white")
        cls.score_label.grid(row=1, column=5, sticky="nw")

        # Создание кнопки для возврата в меню, предварительно сохранив текущее состояние игры
        cfc.ConfigureWindow.create_button_grid(window, "Return in Menu", ("Algerian", 20), "black",2, 5, 
                                                lambda: StartGame.save_game(window, cls.player_name, cls.player_score, cls.gameArray), 2, "nw")
        
    @classmethod
    def clear_attribute_data(cls):
        # Очистка данных игры
        cls.button_array  = [[None]*4 for _ in range(4)]  
        cls.winner_array  = [[None]*4 for _ in range(4)]
        cls.player_name = ""
        cls.player_score = "0"
        cls.score_label = None

    @staticmethod
    def create_winner_array():
        # Создание массива-победителя
        numbers = list(range(1, 16))  
        numbers.append("...")  
        winNumberArray4x4 = [numbers[i:i+4] for i in range(0, len(numbers), 4)]  
        return winNumberArray4x4

    def shuffle_array(array):
        # Перемешивание массива
        random.shuffle(array)  
        return array

    @classmethod
    def create_buttons(cls, array, window):
        # Создание кнопок для игрового поля
        btnArray = [[None]*4 for _ in range(4)]
        for row_index, row in enumerate(array):
            for col_index, value in enumerate(row):
                btn = tk.Button(window, text=str(value), font=("mv boli", 10), width=11, height=5, bg="#6fa8dc",
                                command=lambda r=row_index, c=col_index, win = window: cls.button_click_handler(r, c, win))
                if btn["text"] == "...":
                    btn.configure(bg="#e06666")  
                btnArray[row_index][col_index] = btn  
                btn.grid(row=row_index, column=col_index, padx=5, pady=5)  
        return btnArray

    @classmethod
    # Обработчик нажатия кнопки
    def button_click_handler(cls, row, col, win):
        
        if cls.can_move_button(row, col): # Проверка, можно ли сдвинуть кнопку
            cls.swap_buttons_positions(row, col) # Двигаем кнопку
            cls.counting_moves() # Подсчёт очков
            if cls.is_player_win(cls.winner_array ): # Проверка на выигрыш 
                cfc.ConfigureWindow.clear_window_widgets(win) # Отчистка экрана от виджетов
                cls.create_label_win(win) # Вывод информации о выигрыше
            
    @classmethod
    def is_player_win(cls, winArray):
        # Проверка, является ли текущее состояние поля выигрышным
        for row in range(4):
            for col in range(4):
                if winArray[row][col] == "...":
                    continue
                if cls.button_array [row][col]["text"] != str(winArray[row][col]):
                    return False
        return True

    @classmethod
    # Настройка окна для отображения сообщения о победе игрока
    def create_label_win(cls, window):

        # Настройка окна с указанием размеров и цвета фона
        cfc.ConfigureWindow.configure_window(window, "Start Game", 736, 460, "black") 
        
        # Создаем и размещаем задний фон для окна победы
        cfc.ConfigureWindow.create_bg_image(window,"Image/bg_win.png", 0, 0, 1, 1)  

        # Создание метки "You Win!!!" и размещение на окне
        label_you_win = tk.Label(window, text="You Win!!!", font=("matura mt script capitals", 45), bg="black", fg="#c27ba0")
        label_you_win.place(x=180, y=130)

        # Создание метки с статистикой игры (имя игрока и количество ходов)
        label_statistics_text = f"Player {cls.player_name} completed the game in {cls.player_score} moves (^_^)"
        label_statistics = tk.Label(window, text=label_statistics_text, font=("matura mt script capitals", 20), bg="black", fg="white")
        label_statistics.place(x=115, y=250)

        # Создание кнопки "Return in Menu" для возврата в главное меню и ее размещение
        cfc.ConfigureWindow.create_button_pack(window, "Return in Menu", ("Algerian", 20), "black", 
                                               lambda: StartGame.return_to_menu_for_game(window), tk.BOTTOM, 0, 80)

        
    @classmethod
    def counting_moves(cls):
        # Подсчет количества ходов и обновление метки счета
        cls.player_score = str(eval(f"{cls.player_score} + 1"))
        cls.score_label["text"] = "Score: " + str(eval(f"{cls.player_score}")) 

    @classmethod
    def can_move_button(cls, row, col):
        # Проверка, можно ли сдвинуть кнопку на пустое место
        return (row > 0 and cls.button_array [row - 1][col]["text"] == "...") or \
            (row < 3 and cls.button_array [row + 1][col]["text"] == "...") or \
            (col > 0 and cls.button_array [row][col - 1]["text"] == "...") or \
            (col < 3 and cls.button_array [row][col + 1]["text"] == "...")
    
    @classmethod
    def swap_buttons_positions(cls, row, col):
        # Находим пустую ячейку (пустую кнопку) и меняем ее местами с текущей кнопкой
        empty_row, empty_col = cls.find_empty_button_position()

        # Меняем местами элементы в массиве игрового поля
        cls.gameArray[row][col], cls.gameArray[empty_row][empty_col] = cls.gameArray[empty_row][empty_col], cls.gameArray[row][col]

        # Меняем текст и цвет кнопок на игровом поле в соответствии с перемещением
        cls.button_array[row][col]["text"], cls.button_array[empty_row][empty_col]["text"] = cls.button_array[empty_row][empty_col]["text"], cls.button_array[row][col]["text"]
        cls.button_array[row][col]["bg"], cls.button_array[empty_row][empty_col]["bg"] = cls.button_array[empty_row][empty_col]["bg"], cls.button_array[row][col]["bg"]


    @classmethod
    # Поиск пустой ячейки на игровом поле
    def find_empty_button_position(cls):
        for row in range(4):
            for col in range(4):
                if cls.button_array[row][col] and cls.button_array[row][col]["text"] == "...":
                    return row, col
                
    @staticmethod
    def enter_player_name(window):
        # Создаем и размещаем задний фон
        cfc.ConfigureWindow.create_bg_image(window, "Image/bg_menu.png", 0, 0, 1, 1)

        # Создаем метку с текстом "Enter your name:"
        label_name = tk.Label(window, text="Enter your name:", font=("matura mt script capitals", 18), bg="black", fg="white")
        label_name.pack(side=tk.TOP, pady=30)  # Размещаем метку в верхней части окна с отступом

        # Создаем поле для ввода имени игрока
        entry = tk.Entry(window, font=("matura mt script capitals", 18), fg="black")
        entry.pack()  # Размещаем поле ввода имени

        def startCommand():
            # Функция, вызываемая при нажатии кнопки "Start"
            name = entry.get()  # Получаем введенное имя из поля ввода
            if not name.strip():  # Проверяем, что имя не пустое
                label_name.config(text="Please enter your name!!!", fg="red")  # Устанавливаем предупреждающий текст метки
            else:
                StartGame.player_name += name  # Добавляем имя игрока к атрибуту класса
                cfc.ConfigureWindow.clear_window_widgets(window)  # Очищаем окно от элементов
                StartGame.initialize_game(window)  # Инициализируем игру

        # Размещаем кнопку "Start" в верхней части окна с отступом
        cfc.ConfigureWindow.create_button_pack(window, "Start", ("Algerian", 20), "black", startCommand, tk.TOP, 0, 30)
        # Создаём кнопку "Return in Menu" и размещаем ее
        cfc.ConfigureWindow.create_button_pack(window, "Return in Menu", ("Algerian", 20), "black", lambda: StartGame.return_to_menu_for_game(window))


    def return_to_menu_for_game(window):
        # Возвращаемся в главное меню и очищаем данные игры
        StartGame.clear_attribute_data()  # Очищаем атрибуты класса игры
        cfc.ConfigureWindow.return_to_menu(window)  # Возвращаемся в главное меню с помощью метода из класса окна


    def save_game(window, playerName, playerScore, gameArr):
        # Сохраняем текущее состояние игры в файл
        wf.WorkWithFile.save_in_file(playerName, playerScore, gameArr)
        # Возвращаемся в главное меню после сохранения игры
        StartGame.return_to_menu_for_game(window)


    def dont_have_save_game(window):
        # Создаем и размещаем задний фон
        cfc.ConfigureWindow.create_bg_image(window,"Image/bg_menu.png", 0, 0, 1, 1)

        # Создаем метку с сообщением о том, что игра не была сохранена
        cfc.ConfigureWindow.create_label_pack(window, "You haven't saved the game yet!!!", ("matura mt script capitals", 35), "red", "black", tk.TOP, 0, 150)

        # Создаем кнопку "Return in Menu" для возвращения в главное меню и размещаем ее
        cfc.ConfigureWindow.create_button_pack(window, "Return in Menu", ("Algerian", 20), "black", lambda: StartGame.return_to_menu_for_game(window))


        

