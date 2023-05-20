from ast import main
import math
import os

#რიცხვის ფაქტორიალის პოვნა
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#უმცირესის პოვნა სამ რიცხვს შორის
def find_smallest(num1, num2, num3):
    smallest = min(num1, num2, num3)
    return smallest

#ტემპერატურა ფარენგეიტიდან ცელსიუსში
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

#ტემპერატურა ცელსიუსიდან ფარენგეიტში
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#მოცემულ დიაპაზონში მარტივი რიცხვების პოვნა
def find_prime_numbers(n):
  primes = []
  for num in range(2, n+1):
    if num > 1:
      for i in range(2, num):
        if (num % i) == 0:
          break
      else:
        primes.append(num)

#1-დან n-ამდე ყველა რიცხვის ჯამი
def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

# 1-დან n-მდე ყველა რიცხვის საშუალო არითმეტიკული
def arithmetic_mean(n):
    sum = arithmetic_mean(n)
    Arithmetic = sum / n
    return Arithmetic

# 1-დან n-მდე ყველა რიცივის კვადრატების ჯამი
def sum_of_squares(n):
    sum_squares = (n * (n + 1) * (2 * n + 1)) // 6
    return sum_squares

# 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი
def sum_of_even_numbers(n):
     sum_even = 0
     for i in range(2, n+1, 2):
        sum_even += i
     return sum_even


# ორი რიცხვის უმცირესი საერთო ჯერადი
def smallest_common_multiple(a, b):
    max_num = max(a, b)

    lcm = max_num
    while True:
        if lcm % a == 0 and lcm % b == 0:
            break
        lcm += max_num

    return lcm


#მოცემული რიცხვის ყველა გამყოფის პოვნა
def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

while True:
    os.system("cls" if os.name == "nt" else "clear")


# მენიუ
print("მენიუ:")
print("1. ფაქტორიალის გამოთვლა")
print("2. სამი რიცხვიდან უმცირესის პოვნა")
print("3. ტემპერატურს შკალის კონვერტორი ცელსიუსიდან ფარენგეიტში და პირიქით")
print("4. მოცემულ დიაპაზონში (1..n) ყველა მარტივი რიცხვის პოვნა")
print("5. 1-დან n-მდე ყველა რიცხვის ჯამი")
print("6. 1-დან n-მდე ყველა რიცხვის საშუალო არითმეტიკული")
print("7. 1-დან n-მდე ყველა რიცივის კვადრატების ჯამი")
print("8. 1-დან n-მდე ყველა ლუწი რიცხვის ჯამი")
print("9. ორი რიცხვის უმცირესი საერთო ჯერადი")
print("10. მოცემული რიცხვის ყველა გამყოფის პოვნა")
print("11. გამოსვლა")


# ლექსიკონი
menu_items = {
    '1': factorial,
    '2': find_smallest,
    '3': celsius_to_fahrenheit,
    '4': fahrenheit_to_celsius,
    '5': find_prime_numbers,
    '6': sum_of_numbers,
    '7': arithmetic_mean,
    '8': sum_of_squares,
    '9': sum_of_even_numbers,
    '10': smallest_common_multiple,
    '11': find_divisors
}



while True:
    choice = input("აირჩიეთ თქვენთვის სასურველი ფუნქცია (1-11): ")

    if choice == '11':
        print("პროგრამიდან გასვლა...")
        break

    if choice in menu_items:
        function = menu_items[choice]
        function_input = input("შეიყვანეთ შესაბამისი input თქვენი ფუნქციისთის: ")
        result = function(function_input)
        print("შედეგი:", result)
    else:
        print("არასწორი არჩევანი. სცადეთ ხელახლა.")

if __name__ == "__main__":
  main()