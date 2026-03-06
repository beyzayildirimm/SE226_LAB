
n=int(input("Enter a number greater than 9: "))
print(n, end="")
steps=0

while n>=10 :
    sum=0
    while n> 0:
        sum +=n%10
        n//=10
    n=sum
    steps+=1
    print(" -> ",n,end="")

print()
print(f"Final Value:{sum}")
print(f"Total Steps: {steps}")


#---------------------------------------------

fizz= 0
buzz = 0
fizzbuzz = 0
while True:
    n = int(input("Please enter a number between 10 and 100: "))
    if 10 <= n <= 100:
        break
    print("Invalid input. Please enter a number between 10 and 100.")

for i in range (1,n+1):
    if i % 7 == 0 :
        continue
        print(f"{i} is skipped")
    elif i%3==0 and i%5==0 :
        print("FizBuzz")
        fizzbuzz +=1
    elif i%3 ==0:
        print("Fizz")
        fizz+=1
    elif i%5 ==0:
        print("Buzz")
        buzz+=1
    else :
        print(i)
print("-----Summary------")
print("Fizz count :", fizz)
print("Buzz count :", buzz)
print("FizzBuzz count :", fizzbuzz)

#-----------------------------------------------------------

n = int(input("Please enter a number between 3 and 9: "))

for i in range(1, 2 * n):
    if i <= n:
        k = i
    else:
        k = 2 * n - i

    for j in range(1, k + 1):
        print(j, end="")
    print()