temp_str = input("Введите температуру (например, 25C или 77F): ")
temperature = float(temp_str[:-1])  # Извлекаем числовое значение
scale = temp_str[-1]  # Извлекаем символ шкалы (C или F)
if scale != 'C' or scale != 'F':
  print("Ошибка: Некорректная шкала. Используйте C для Цельсия или F для Фаренгейта.")
# Конвертируем из Цельсия в Фаренгейта
if scale == 'C':
  fahrenheit = (temperature * 9/5) + 32
  print(f"{temperature:.1f}C = {fahrenheit:.1f}F")
if scale == 'F': 
  celsius = (temperature - 32) * 5/9 
  print(f"{temperature:.1f}F = {celsius:.1f}C")