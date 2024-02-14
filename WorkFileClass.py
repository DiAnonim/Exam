class WorkWithFile:
    @staticmethod
    def save_in_file(playerName, playerScore, arrayGameBtn):
        # Определяем имя файла для сохранения данных
        fileName = "Continue_Game.txt"
        # Открываем файл для записи
        with open(fileName, "w") as file:
            # Записываем имя игрока и его счет в файл
            file.write(f"{playerName}\n")
            file.write(f"{playerScore}\n")
            # Записываем состояние игрового поля
            for row in arrayGameBtn:
                file.write(' '.join(map(str, row)) + '\n')


    @staticmethod
    def load_from_file():
        # Определяем имя файла для загрузки данных
        fileName = "Continue_Game.txt"
        playerName = ""
        playerScore = ""
        arrayGameBtn = []
        isError = False

        try:
            # Пытаемся открыть файл для чтения
            with open(fileName, "r") as file:
                # Считываем имя игрока и его счет из файла
                playerName = file.readline().strip()
                playerScore = file.readline().strip()
                # Считываем состояние игрового поля
                for line in file:
                    row = line.strip().split()
                    arrayGameBtn.append([cell for cell in row])

            return isError, playerName, playerScore, arrayGameBtn
        except FileNotFoundError:
            # Если файл не найден, устанавливаем флаг ошибки и возвращаем пустые данные
            isError = True
            return isError, playerName, playerScore, arrayGameBtn
                