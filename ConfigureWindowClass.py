import tkinter as tk
import MenuWindowClass as mw # Импортируем модуль для работы с Меню

class ConfigureWindow():
    #Метод для отчистки окно от виджетов
    def clear_window_widgets(window):
        # Удаляем все виджеты из окна
        for widget in window.winfo_children():
            widget.destroy()

    #  Метод для настройки окна с заданными параметрами.
    def configure_window(window, title, width, height, bg_color = None, text_font = None):
        window.title(title)  # Установка заголовка окна
        window.configure(bg=bg_color)  # Установка цвета фона окна
        window.minsize(width, height)  # Установка минимальных размеров окна
        window.maxsize(width, height)  # Установка максимальных размеров окна
        window.font = text_font # Установка шрифта и его размера

    # Метод для создания кнопки и упаковки ее в окне.
    def create_button_pack(window, text, font, fg , command, side = None, padx = None, pady = None):
        button = tk.Button(window, text=text, font=font, fg=fg,  command=command)
        button.pack(side=side, padx=padx, pady=pady)
    
    #  Метод для создания кнопки и размещения ее в сетке окна.
    def create_button_grid(window, text, font, fg, row, col, command, colSpan = None, sticky = None):
        button = tk.Button(window, text=text, font=font, fg=fg,  command=command)
        button.grid(row=row, column=col, columnspan=colSpan, sticky=sticky)

    def create_bg_image(window, filename, x, y, relwidth, relheight):
        # Загружаем изображение из файла и присваиваем его переменной background_image окна
        window.background_image = tk.PhotoImage(file=filename)
        # Создаем метку для отображения фонового изображения и привязываем к окну
        window.background_label = tk.Label(window, image=window.background_image)
        # Размещаем метку с фоновым изображением в окне с указанными параметрами
        window.background_label.place(x=x, y=y, relwidth=relwidth, relheight=relheight)

    # Метод для создания метки и упаковки ее в окне.
    def create_label_pack(window, text, font, fg, bg = None, side = None, padx = None, pady = None ):
        label = tk.Label(window, text=text, font=font, fg=fg, bg=bg)
        label.pack(side = side, padx=padx, pady=pady)

    #  Метод для возвращения пользователя в главное меню.
    def return_to_menu(window):
        window.destroy()
        mw.MenuWindow()

    
    

        

    
    

