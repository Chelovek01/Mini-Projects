import random

number = random.randint(0, 100)
print('Добро пожаловать в числовую угадайку :)')

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 100:
            return True
        else:
            return False
    else:
        return False

while True:
    user_num = input('Введите целое число от 1 до 100:')
    if not is_valid(user_num):
        print('Не пытайтесь меня обмануть, введите число от 1 до 100 :)')
        continue
    user_num = int(user_num)

    if user_num < number:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif user_num > number:
        print('Ваше число больше загаданного, попробуйте еще разок')
    else:
        print('Вы угадали, поздравляем!')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')