#for loop factorial
num =5
factorial =1
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

#recursion

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
    
#ackermann's function

def ack(m, n):
    if m == 0:
        return n+1
    elif n == 0:
        return ack(m-1, 1)
    else:
        return ack(m-1, ack(m, n-1))

print(ack(4,1))


def weather(temperature):
    if temperature > 30:
        return 'Warm'
    else:
        return 'Cold'

#input("Enter the temperature:")
print(weather(int(input("enter a number:"))))

 def red():
                a=1
                def blue():
                                a=2
                                b=2
                                print(a)
                                print(b)
                blue()
                print(a)  
                
lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
#fibinochi recursion
def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
Run Code


#towers of hanoi
def move(f, t):
    print("Move the disk from {} to {}".format(f,t))

def MoveVia(f,v,t):
    mov(f,v)
    mov(v,t)
def hanoi(n,f,h,t):
    if n==0:
        pass
    else:
    hanoi(n-1,f,t,h)
    mov(f,t)
    hanoi(n-1,h,f,t)