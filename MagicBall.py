import random
answers =  ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом",
            "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да",
            "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
            "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет",
            "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]



print("Привет мой друг, я знаю ответ на любой твой вопрос.")

name = input("Скажи, как тебя зовут?: ")
print("Привет,", name,"!")

again = "да"

while again.lower() == "да":
    question = input("Задавай свой вопрос: ")
    print(random.choice(answers))
    again = input("Хочешь задать еще одни вопрос? (введи 'да' или 'нет'): ")
    if not again.lower() == 'да':
        print("Если понадоблюсь, я всегда рядом...")

