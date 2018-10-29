print ("Weird Numbers")
num = int(input("Enter your number: "))

def odd_num(num):
    if (num%2 !=0 and num<=100) or (6<=num<=20 and num<=100):
            answer='Weirdo'
    elif (num%2==0 and 2<=num<=5 and num<=100) or (num>20 and num<=100):
            answer='Not Weird'
    else:
        answer="¡Number out of Range!"
    return answer

print(odd_num(int(num)))
