class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
       return self.items.pop()

   def size(self):
       return len(self.items)

queue = Queue()

if queue.is_empty():  # Исправлено: добавлен экземпляр класса
    print("Список дел пуст.")
else:
    print(f'В списке накопилось дел : {len(queue.items)} ')

while True:
    print("\nМеню:")
    print("1. Добавить задачу")
    print("2. Выполнить первую адачу в списке")
    print("3. Показать список дел")
    print("4. Выход")

    choice = input("Выберите действие (1-4): ")

    if choice == '1':
        task = input("Введите задачу: ")
        queue.enqueue(task)
        print(f"Задача '{task}' добавлена в список дел.")

    elif choice == '2':
        if not queue.is_empty():
            completed_task = queue.dequeue()
            print(f"Задача '{completed_task}' выполнена.")
        else:
            print("Список дел пуст.")

    elif choice == '3':
        if queue.is_empty():
            print("Список дел пуст.")
        else:
            print(f'В списке накопилось дел : {len(queue.items)}')
            print("Список дел:")
            for task in reversed(queue.items):  # Печатаем в порядке добавления
                print(task)

    elif choice == '4':
        print("Выход из программы.")
        break

    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")