def isPrime(number):
    prime = True
    for i in range (2,int(number**0.5)+1):
        if(number%i == 0):
            prime = False
    return prime


enterNumber= int(input('Enter the number whose largest prime factor you want to know : '))

largestPF=1

for i  in range (2, int(enterNumber**0.5)+1):
    if (enterNumber % i == 0):
        if (isPrime(i)):
            print (i ,"was a prime factor ")
            if (i>largestPF):
                largestPF = i

print ("The Largest Prime Factor of the number ",enterNumber , "is ", largestPF)
            
