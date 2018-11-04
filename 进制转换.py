'''二进制转十进制
def TwotoTen (num):
    str1 = num.split('.')
    if(len(str1) == 2):
        list1 = list(str1[0])
        list2 = list(str1[1])
        
        sum0 , a = 0 , 0
        for i in list1:
            p = int(i)
            sum0 += p * 2**((len(list1)-1) - a)
            a += 1
    
        b = 1
    
        for j in list2:
            q = int(j)
            sum0 += q * 2**(-b)
            b += 1
    
    else:
        list1 = list(str1[0])
   
        sum0 , a = 0 , 0
        for i in list1:
            p = int(i)
            sum0 += p * 2**((len(list1)-1) - a)
            a += 1
    
    
    return sum0
'''




'''十进制转二进制。。。。。。。
def TenToTwoX (x):
    str1 = x.split('.')
    if(len(str1) == 2):
        b = '0.'
        while(x > 0 and len(b) < 102):带小数的转换
            b += str(int(x * 2))
            x = x * 2 - int(x * 2)
    else:
        Bin = []
        while(x > 1):
            Bin.append(x % 2)
            x = x // 2
        
        Bin.append(x)
        Bin.reverse()
    
        sum1 = 0
        a = 0
    
        for i in Bin:
            sum1 += i * 10 ** (len(Bin) - 1 - a)
            a += 1
    
    return b
'''



'''八进制转二进制
def TenToTwo(x):
    Bin = []
    while(x > 1):
        Bin.append(x % 2)
        x = x // 2
    Bin.append(x)
    Bin.reverse()
    
    sum1 = 0
    a = 0
    
    for i in Bin:
        sum1 += i * 10 ** (len(Bin) - 1 - a)
        a += 1
    return sum1
    
    
def EightToTen (num):
    list1 = str(num)
    sum0 , a = 0 , 0
    for i in list1:
        p = int(i)
        sum0 += p * 8**((len(list1)-1) - a)
        a += 1
    return sum0


def EightToBin (x):
    return TenToTwo(EightToTen(x))
'''        


'''二进制转八进制
def BinToEight(x):
    list1 = list(str(x))
    sum0 , a = 0 , 1 
    for i in list1:
       p = int(i)
       sum0 += p * 2**(len(list1) - 1)
       a += 1
     
    Bin = []
    while(x > 7):
        Bin.append(x % 8)
        x = x // 8
        
    Bin.append(x)
    Bin.reverse()
    
    sum1 = 0
    a = 0
    
    for i in Bin:
        sum1 += i * 10 ** (len(Bin) - 1 - a)
        a += 1
        
    return sum1
'''



'''十六进制转换成二进制
def HexToBin(x):
    list1 = list(str(x))
    a = 0
    b = len(list1)
    
    while(a<b):
        if(list1[a] == 'A' or list1[a] == 'a'):
            list1[a] = '10'
        if(list1[a] == 'B' or list1[a] == 'b'):
            list1[a] = '11'
        if(list1[a] == 'C' or list1[a] == 'c'):
            list1[a] = '12'
        if(list1[a] == 'D' or list1[a] == 'd'):
            list1[a] = '13'
        if(list1[a] == 'E' or list1[a] == 'e'):
            list1[a] = '14'
        if(list1[a] == 'F' or list1[a] == 'f'):
            list1[a] = '15'
        a += 1
        
    sum0 , d = 0 , 0
    for i in list1:
        p = int(i)
        sum0 += p * 16**(b - 1 - d)
        d += 1
    
    x = sum0
    Bin = []
    while(x > 1):
        Bin.append(x % 2)
        x = x // 2
        
    Bin.append(x)
    Bin.reverse()
    
    sum1 = 0
    a = 0
    
    for i in Bin:
        sum1 += i * 10 ** (len(Bin) - 1 - a)
        a += 1
    
    return sum1

print(HexToBin('1AF'))
'''

'''二进制转十六进制
def BintoHex(x):
    sum0 , a = 0 , 0
    listnum = list(str(x))
    
    for i in listnum:
        p = int(i)
        sum0 += p * 2**(len(listnum) - 1 - a)
        a += 1
    
    Bin = []
    while(sum0 > 15):
        Bin.append(sum0 % 16)
        sum0 = sum0 // 16
    Bin.append(sum0)
    Bin.reverse()
    
    sum1 , t = 0 , 1
    for i in Bin:
        sum1 += int(i) * 10 ** (len(Bin) - t)
        t += 1
        
    return sum1
'''          







