import tkinter as tk
import ConfigureWindowClass as cfc # Импортируем модуль для настройки окна
import StartGameClass as sg # Импортируем модуль для начала игры
import InfoWebScraperClass as Info # Импортируем модуль для правил игры

class MenuWindow(tk.Tk):
    # Список надписей для кнопок
    fields = ("Start Game", "Continue", "Info", "Exit")

    def __init__(self, master=None):
        super().__init__(master)

        # Создаем и размещаем задний фон
        cfc.ConfigureWindow.create_bg_image(self,"Image/bg_menu.png", 0, 0, 1, 1)

        # Создаем и размещаем название игры
        self.label_title = tk.Label(self, text="The 15 Puzzle", font=("Algerian",45), bg="black", fg="white")
        self.label_title.grid(row=0, column=0)

        # Передаём данные для настройки окна
        cfc.ConfigureWindow.configure_window(self, "Menu", 700, 500, "black", ("Algerian", 20))

        self.buttons = []  # Инициализируем список кнопок
        self.place_buttons()  # Размещаем кнопки на окне

    # Метод для размещения кнопок
    def place_buttons(self):
        # Создаем список команд для каждой кнопки
        commands = [self.start_command, self.continue_command, self.info_command, self.exit_command]
        # Итерируем по списку надписей и команд
        for index, (field, command) in enumerate(zip(self.fields, commands)):
            # Создаем кнопку с указанной надписью, шрифтом и командой
            button = tk.Button(self, text=field, font=self.font, fg="black",  command=command)
            # Размещаем кнопку на сетке в указанных строке и столбце с отступами и выравниванием
            button.grid(row=index+1, column=0, padx=250, pady=10, sticky="nsew")

    # Метод для обработки нажатия на кнопку "Start"
    def start_command(self):
        # Очищаем окно от элементов
        cfc.ConfigureWindow.clear_window_widgets(self)
        # Вызываем метод для ввода имени игрока из класса StartGame
        sg.StartGame.enter_player_name(self)

    # Метод для обработки нажатия на кнопку "Continue"
    def continue_command(self):
        # Очищаем окно от элементов
        cfc.ConfigureWindow.clear_window_widgets(self)
        # Инициализируем игру с параметром isContinue=True для продолжения игры
        sg.StartGame.initialize_game(self, True)

    # Метод для обработки нажатия на кнопку "Info"
    def info_command(self):
        # Очищаем окно от элементов
        cfc.ConfigureWindow.clear_window_widgets(self)
        # Получаем информацию с веб-сайта
        text_contents = Info.InfoWebScraper.fetch_website_info()
        # Отображаем информацию на экране
        self.display_info(text_contents)

    # Метод для отображения информации на экране
    def display_info(self, text_contents):
        # Создаем холст и прокрутку для отображения текста
        canvas = Info.InfoWebScraper.create_canvas(self, text_contents)
        # Создаем полосу прокрутки
        Info.InfoWebScraper.create_scrollbar(self, canvas)
        # Создаем кнопку "Назад в меню" и размещаем её
        cfc.ConfigureWindow.create_button_pack(self, "Return in Menu", ("Algerian", 15), "black", lambda: cfc.ConfigureWindow.return_to_menu(self))


    # Метод для обработки нажатия на кнопку "Exit"
    def exit_command(self):
        # Закрываем окно приложения
        self.destroy()
