# Створено змінну filename для імені файлу, у якому будемо робити пошук і заміну
filename = input("Введіть ім'я файлу для пошуку і заміни: ")

# Створено змінні word_to_find і word_to_replace для слова/фрази, яку шукаємо та на що замінюємо
word_to_find = input("Введіть слово або фразу для пошуку: ")
word_to_replace = input("Введіть слово або фразу для заміни: ")

# Створено змінну new_filename для імені нового файлу, у який запишемо змінений текст
new_filename = "updated_" + filename

# Відкриваємо оригінальний файл для читання
with open(filename, 'r', encoding='utf-8') as file:
    # Зчитуємо весь текст файлу у змінну content
    content = file.read()

# Замінюємо усі входження word_to_find на word_to_replace у змінній content
new_content = content.replace(word_to_find, word_to_replace)

# Записуємо змінений текст у новий файл
with open(new_filename, 'w', encoding='utf-8') as file:
    file.write(new_content)

# Повідомляємо користувача про завершення операції та ім'я нового файлу
print(f"Заміна завершена. Збережено у файл '{new_filename}'.")
