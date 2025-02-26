name_1 = str(input("Введите своё имя : "))
myname = "Марина"
if name_1 == myname :
  print("Привет! О, это я!")
else :
  print("Привет, незнакомец!")

#игра человек вводит число 0-99, система гененрирует число, и отвечает угадал или нет
import random
user = int(input("Попробуйте отгадать число! Введите число от 0 до 99 : "))
generated = random.randint(0,99)
if user == generated : print(f"Ура, ты угадал! {number_generated}")
else :
    if user > generated : print("Нет, загаданное число меньше!")
    else: print("Нет, загаданное число больше!")