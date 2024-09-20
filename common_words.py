# 3. Парсинг

import re

def get_most_common_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Удаляем HTML теги
        text = re.sub(r'<[^>]+>', ' ', html_content)

        # Находим все слова длиной не менее 3 символов
        words = re.findall(r'\b\w{3,}\b', text.lower())

        # Подсчитываем частоту слов
        word_count = {}
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        
        # Сортируем слова по убыванию частоты и выбираем топ-10
        common_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:10]
        
        for word, count in common_words:
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь и имя файла.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    path = input("Введите путь к HTML файлу: ")
    get_most_common_words(path)
