quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()  # Разбиваем фразу на список слов
    if len(word_list) >= 3:  # Проверяем, достаточно ли слов в фразе
        return word_list[-3]  # Возвращаем третье слово с конца
    else:
        return 'Фраза содержит менее трех слов'

# Вызовы функции готовы к работе, не изменяйте их!

# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))
