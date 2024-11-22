from dictionaries import words_easy, words_medium, words_hard, levels

level_input = input("Выберите уровень сложности (легкий, средний, тяжелый): ").strip().lower()

if level_input == "легкий":
    words = words_easy
elif level_input == "средний":
    words = words_medium
elif level_input == "тяжелый":
    words = words_hard
else:
    words = words_easy

answers = {}
for word, translation in words.items():
    print(f"Слово: {word}, {len(translation)} букв, начинается на {translation[0]}.")

    user_answer = input("Ваш ответ: ").strip().lower()

    if user_answer == translation:
        print(f"Верно! {word.capitalize()} - это {translation}.")
        answers[word] = True
    else:
        print(f"Неверно. {word.capitalize()} - это {translation}.")
        answers[word] = False

correct_words = [word for word, correct in answers.items() if correct]
incorrect_words = [word for word, correct in answers.items() if not correct]

print("\nПравильно отвеченные слова:")
print("\n".join(correct_words) if incorrect_words else "Нет правильных ответов.")

print("\nНеправильно отвеченные слова:")
print("\n".join(incorrect_words) if incorrect_words else "Нет неправильных ответов.")

correct_count = sum(1 for correct in answers.values() if correct)
user_rank = levels[min(correct_count, len(levels) - 1)]

print(f"\nВаш ранг: {user_rank}")