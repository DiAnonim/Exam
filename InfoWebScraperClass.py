import tkinter as tk
import requests
from bs4 import BeautifulSoup



class InfoWebScraper:
    @staticmethod
    def fetch_website_info():
        try:
            # URL веб-страницы для извлечения информации
            url = "https://razvivashka.site/igra-pyatnashki/"
            response = requests.get(url)
            response.raise_for_status()  # Проверяем наличие ошибок при запросе

            # Получаем HTML-контент страницы
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Извлекаем заголовки и описание страницы
            title = soup.findAll("h2")
            description = soup.find_all("p")

            # Формируем текстовое содержимое для отображения
            text_contents = f"\n{title[0].text}\n\n{description[0].text}\n{description[1].text}\n{description[7].text}\n\n{title[1].text}\n\n{description[8].text}\n{description[9].text}\n\n"

            return text_contents

        except requests.exceptions.RequestException as e:
            # Обработка ошибок при запросе к веб-странице
            errorText = f"Ошибка при запросе к веб-странице: {e}"
            return errorText

        except Exception as e:
            # Обработка остальных исключений
            errorTextAll = f"Ошибка: {e}"
            return errorTextAll

    def create_canvas(window, text_to_display):
        # Создание холста для отображения текста
        canvas = tk.Canvas(window, width=400, height=300, bg="black")
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Привязка события прокрутки колеса мыши к холсту
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))

        # Создание текста на холсте
        canvas.create_text(10, 10, anchor="n", text=text_to_display, font=("mv boli", 14), fill="white", width=380)
        
        # Конфигурация области прокрутки для холста
        canvas.config(scrollregion=canvas.bbox("all"))

        return canvas


    def create_scrollbar(window, canvas):
        # Создание вертикальной полосы прокрутки для холста
        scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
