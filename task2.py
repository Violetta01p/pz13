# Створено змінну filename для імені файлу, який буде аналізуватися
filename = input("Введіть ім'я файлу для аналізу: ")

# Відкриваємо файл у режимі читання ('r')
with open(filename, 'r', encoding='utf-8') as file:
    # Створено змінну lines, яка містить список рядків файлу
    lines = file.readlines()

# Обчислюємо кількість рядків
num_lines = len(lines)

# Обчислюємо кількість слів у файлі (складаємо кількість слів у кожному рядку)
num_words = sum(len(line.split()) for line in lines)

# Обчислюємо кількість символів (включно з пробілами та переходами рядків)
num_chars = sum(len(line) for line in lines)

# Виводимо результати аналізу
print(f"\nАналіз файлу '{filename}':")
print(f"Кількість рядків: {num_lines}")
print(f"Кількість слів: {num_words}")
print(f"Кількість символів (включно з пробілами та переходами рядків): {num_chars}")
