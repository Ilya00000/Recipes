import json


def read_cook_book(file_path):
    """Читает рецепты из файла и возвращает словарь с рецептами."""
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()  # Читаем название блюда
            if not dish_name:  # Если пустая строка, выходим из цикла
                break

            ingredient_count = int(file.readline().strip())  # Читаем количество ингредиентов
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip()
                ingredient_name, quantity, measure = ingredient_line.split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                })

            cook_book[dish_name] = ingredients  # Добавляем блюдо и его ингредиенты в словарь

    return cook_book


# Пример использования:
if __name__ == "__main__":
    file_path = 'recipes.txt'  # Укажите правильный путь к вашему файлу
    cook_book = read_cook_book(file_path)

    # Используем json.dumps для удобного и красивого вывода
    print(json.dumps(cook_book, ensure_ascii=False, indent=4))
