users_number = int(input("Введите положительное целое число больше 1 : ")) # Пользователь задаёт число N, которое будет последним в ряду для анализа
if users_number >= 2: 
   prime_numbers = [True] * (users_number + 1) # Создаем список истинности для всех чисел от 2 до n  
   p = 2 #Наш помошник для удаления ненужных нам чисел
   while p*p <= users_number:
     if prime_numbers[p]: #усли число простое, а мы начнём с 2, которое является простым в любом случае
       for i in range(p*p, users_number+1, p): #Помечаем все кратные ему числа как False, т.е. неподходящие нам
         prime_numbers[i] = False
   p += 1 #счётчик идёт дальше
   print(f"Простые числа до {users_number} :")
   for n in range(2, users_number+1): #цикл, чтобы каждое число было с новой строчки
     if prime_numbers[n]:
      print(n)
else: 
  print("Ошибка! Число должно быть не меньше 2")
