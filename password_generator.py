import random

digits =  '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

count_pass = int(input('Укажите количество паролей для генерации:'))
len_pass = int(input('Укажите длину одного пароля:'))
digit_in_pass = input('Включать ли цифры 0123456789? (y/n) ').strip()
ABC_in_pass = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n) ').strip()
abc_in_pass = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n) ').strip()
ch_in_pass = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ').strip()
exceptions_in_pass = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ').strip()

if digit_in_pass.lower() == 'y':
    chars += digits
if ABC_in_pass.lower() == 'y':
    chars += uppercase_letters
if abc_in_pass.lower() == 'y':
    chars += lowercase_letters
if ch_in_pass.lower() == 'y':
    chars += punctuation
if exceptions_in_pass.lower() == 'y':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')


def generate_password(len_pass, chars):
    password = ''
    for j in range(len_pass):
        password += random.choice(chars)
    return password


for _ in range(count_pass):
    print(generate_password(len_pass, chars))