#7.4 Problem 4: Basic statistics of three integers

try: 
        n1 = int (input("Type a number: "))
        n2 = int (input("Type a number: "))
        n3 = int (input ("Type a number: "))
        sum= n1+n2+n3
        average= (n1+n2+n3)/3
        max_number = max(n1,n2,n3)
        min_number = min (n1,n2,n3)
        all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0) #this is like what we see in class-print (2>0) #Outpot- True
        print (f"Sum: {sum}")
        print (f"Average: {average: .2f}")
        print (f"Max: {max_number}")
        print (f"Min: {min_number}")
        print (f"All even: {all_even}")
except ValueError:
        print ("Error: invalid input")
    


