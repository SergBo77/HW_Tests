class Stack:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def push(self, item):
       self.items.append(item)

   def pop(self):
       return self.items.pop()

   def peek(self):
       return self.items[-1]


stack = Stack()

if stack.is_empty():  # Исправлено: добавлен экземпляр класса
    print("Словарь пуст.")
else:
    print(f'В словаре : {len(stack.items)} ')  # Длина словаря

while True:
    word = input("Введите слово в словарь или 'нет' для завершения работы): ")
    if word.lower() == 'нет':  # Проверка на "нет", регистронезависимо
        break
    stack.push(word)

print(f'Теперь в словаре {len(stack.items)} слов(a).')
print(f'Последнее записанное слово {stack.peek()}')

if input("Хотите его удалить (y/n)?:): ") == 'y':
    stack.pop()
    print(f'Удалено последнее слово: {stack.peek()}')

# Вывод всех слов, которые были добавлены в стек
print("Содержимое словаря:")
for item in reversed(stack.items):  # Используем reversed, чтобы напечатать в порядке добавления
    print(item)
