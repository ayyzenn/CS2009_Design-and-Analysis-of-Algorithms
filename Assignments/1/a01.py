def ftn(x , y):
    
    x = str(x)
    y = str(y)
    
    if len(x) == len(y):
        list1 = []
        list2 = []
        list3 = []
            
        test = []
            
        x = int(x)
        y = int(y)
            
        answer1 = divmod(x, 100)
        for i in answer1:
            list1.append(i)
        
        answer2 = divmod(y, 100)
        for j in answer2:
            list2.append(j)
            
        for i in list1:
            for j in list2:
                num = i
                sum1 = 0
                if list1.index(i) == list2.index(j):                
                    while num != 0:
                        sum1 += j
                        num -=1
                    sum1 *= 10000 
                    test.append(sum1)
                else:
                    while num != 0:
                        sum1 += j
                        num -=1
                    sum1 *= 100
                    test.append(sum1)
        test[-1] //= 10000
        all_sum = 0
        for i in test:
            all_sum += i
        print("Result is:",all_sum)
    
    elif len(x) < len(y):
        list1 = []
        list2 = []
        list3 = []
            
        test = []
            
        x = int(x)
        y = int(y)
            
        answer1 = divmod(x, 100)
        for i in answer1:
            list1.append(i)
        
        answer2 = divmod(y, 100)
        for j in answer2:
            list2.append(j)
            
        for i in list1:
            for j in list2:
                num = i
                sum1 = 0
                if list1.index(i) == list2.index(j):                
                    while num != 0:
                        sum1 += j
                        num -=1
                    sum1 *= 10000 
                    test.append(sum1)
                else:
                    while num != 0:
                        sum1 += j
                        num -=1
                    sum1 *= 100
                    test.append(sum1)
        test[-1] //= 10000
        all_sum = 0
        for i in test:
            all_sum += i
        print("Result is:",all_sum)
        
    elif len(x) > len(y):
        list1 = []
        list2 = []
        list3 = []
            
        test = []
            
        x = int(x)
        y = int(y)
            
        answer1 = divmod(x, 100)
        for i in answer1:
            list1.append(i)
        
        answer2 = divmod(y, 100)
        for j in answer2:
            list2.append(j)
            
        for i in list1:
            for j in list2:
                num = i
                sum1 = 0
                if list1.index(i) == list2.index(j):                
                    while num != 0:
                        sum1 += j
                        num -=1
                    sum1 *= 10000 
                    test.append(sum1)
                else:
                    while num != 0:
                        sum1 += j
                        num -=1
                    sum1 *= 100
                    test.append(sum1)
        test[-1] //= 10000
        all_sum = 0
        for i in test:
            all_sum += i
        print("Result is:",all_sum)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
ftn(x , y)