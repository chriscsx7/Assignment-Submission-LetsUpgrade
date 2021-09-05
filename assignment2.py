# Write a program to find the prime number
# Enter a number to program and get the output "Prime" or "Not Prime"
num = int(input("Enter the number: "))
prime = True;

for i in range(2, num):
    if num % i == 0: prime = False

if prime: print("Prime")
else: print("Not Prime")
