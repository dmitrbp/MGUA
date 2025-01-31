import hashlib

print(hashlib.sha256(b'Password').hexdigest())
print(hashlib.sha256(b'1234').hexdigest())
counter = 0
h_password_ethalon = 'e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a'

while True:
    password = input('Введите пароль:')
    h_password = hashlib.sha256(password.encode()).hexdigest()
    if h_password == h_password_ethalon:
        print('Успешно')
        break
    else:
        print('Неверный пароль')
    counter += 1
    if counter > 2:
        print('Количество попыток истекло')
        break
    else:
        print('Попробуйте еще раз')

