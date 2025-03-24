import string

def delete_punctuation_marks(input_text): # Метод, що видалає всі розділові знаки
    return input_text.translate(str.maketrans('', '', string.punctuation)).split()


def number_of_vowels_in_words(edit_text): # Метод, який вираховує кількість голосних в кожному слові і заносить це в словник
    for i in set(edit_text):
        words_with_vowels[i] = 0
        for j in VOWELS:
            if j in i:
                words_with_vowels[i] += i.count(j)


VOWELS = "аеєиіїоуюя"
text = input('Введіть речення: ').lower()

words_with_vowels = {} # Словник, який міститиме слова і їхню кількість голосних
text_without_punctuation = delete_punctuation_marks(text) # Змінна, що містить готовий текст

number_of_vowels_in_words(text_without_punctuation) # Виклик методу, що підраховує кількість голосних в словах, з передаванням змінної, яка містить готовий текст

edited_dictionary = sorted(words_with_vowels.items()) # Посортований словник від слова з найбільшою кількістю голосних, до слова з найменшою

print(f'{str(list(edited_dictionary)[0][0]).title()}: {list(edited_dictionary)[0][1]} голосних')