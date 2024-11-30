#     "Задача "Банковские операции"

import threading
import time
from random import randint
# Cоздать класс Bank со следующими свойствами:
# Атрибуты объекта:
# balance - баланс банка (int)
# lock - объект класса Lock для блокировки потоков.
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    # Метод deposit:
    # Будет совершать 100 транзакций пополнения средств.
    def deposit(self):
        for i in range(100):
            replenishment_balance = randint(50, 500) # Пополнение баланса

            with self.lock: # Если баланс больше или равен 500 и замок lock
                               # заблокирован - lock.locked(), то разблокировать его.
                if self.balance < 500 and self.lock.locked():
                    self.balance += replenishment_balance

                    # "Пополнение: <случайное число>. Баланс: <текущий баланс>".
                    print(f'Пополнение: {replenishment_balance}. Баланс: {self.balance}')
            # После всех операций поставьте ожидание в 0.001 секунды,
            # тем самым имитируя скорость выполнения пополнения.
            time.sleep(0.001)

    # Метод take:
    # Будет совершать 100 транзакций снятия.
    def take(self):
        for i in range(100):
            # Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
            reducing_balance = randint(50, 500)
            print(f'Запрос на {reducing_balance}')
            # Далее производится проверка:если случайное число меньше или равно текущему балансу,
            # то произвести снятие, уменьшив balance на соответствующее число и вывести на экран
            # "Снятие: <случайное число>. Баланс: <текущий баланс>".
            with self.lock:
                if reducing_balance <= self.balance:
                    self.balance -= reducing_balance
                    print(f'Снятие: {reducing_balance}. Баланс: {self.balance}')
                # Если случайное число оказалось больше баланса, то вывести строку
                #"Запрос отклонён, недостаточно средств" и заблокировать поток.
                else:
                    print(f'Запрос отклонен, недостаточно средств')
            time.sleep(0.001)

# Далее создайте объект класса Bank
bk = Bank()
#Создайте 2 потока для его методов deposit и take.
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
#  Запустите эти потоки.
th1.start()
th2.start()
th1.join()
th2.join()
# #После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".
print(f'Итоговый баланс: {bk.balance}')