#Check if a Number is Even or Odd
n = int(input("Enter a number: "))

if n % 2 == 0:
    print(f"{n} is an even number.")
else:
    print(f"{n} is an odd number.")

#Sum of Integers from 1 to 50 Using a Loop
i = 1
sum = 0
while i <= 50:
    sum += i
    i += 1
print(f"The sum of integers from 1 to 50 is: {sum}")