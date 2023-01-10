# Exercicio 01
print('Hello world')

# Exercicio 02
message = 'Hello World'
print(message)

# Exercicio 03
message = 'Bobby\'s World'
print(message)

# Exercicio 04
message = "Bobby's World"
print(message)

# Exercicio 05
message = """Bobby's World was a good cartoon in the 1990s"""
print(message)

# Exercicio 06
message = 'Hello World'
print(len(message))

# Exercicio 07
message = 'Hello World'
print(message[10])

# Exercicio 08
message = 'Hello World'
print(message[0:5])

message = 'Hello World'
print(message[:5])

# Exercicio 09
message = 'Hello World'
print(message.lower())

# Exercicio 10
message = 'Hello World'
print(message.upper())

# Exercicio 11
message = 'Hello World'
print(message.count('Hello'))
print(message.count('l'))

# Exercicio 12
message = 'Hello World'
print(message.find('Hello'))
print(message.find('World'))

# Exercicio 13
message = 'Hello World'
new_message = message.replace('World','Universe')
print(new_message)

# Exercicio 14
greeting = 'Hello'
name = 'Michael'
message = greeting + ', ' + name + '. Welcome!'
print(message)

# Exercicio 15
greeting = 'Hello'
name = 'Michael'
message = '{}, {}. Welcome!'.format(greeting,name)
print(message)

# Exercicio 16
greeting = 'Hello'
name = 'Michael'
message = f'{greeting}, {name.upper()}. Welcome!' #fstrings
print(message)

# Exercicio 17
greeting = 'Hello'
name = 'Michael'
print(dir(name))

# Exercicio 18
greeting = 'Hello'
name = 'Michael'
print(help(str.lower))