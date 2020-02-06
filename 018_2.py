#编写一个函数Findstr(),该函数统计一个长度为2的字字符串在另一个字符串中出现的次数





def findstr(motherstr,sonstr):
    mostr = list(motherstr)
    sostr = list(sonstr)
    times = 0
    long = len(mostr)
    i = 0
    while i < (long-1):
        if sostr[0] == mostr[i]:
            if sostr[1] == mostr[i + 1]:
                times += 1
        i += 1
    return times
            
    
motherstr = input("请输入一个字符串：")
sonstr = input("请输入一个长度为2的子字符串：")
result = findstr(motherstr,sonstr)
print(result)

'''
#virsion 2.0
def findstr(motherstr,sonstr):
    #mostr = list(motherstr)
    #sostr = list(sonstr)
    times = 0
    long = len(motherstr)
    #i = 0
    for each in range(long-1):
    #while i < (long-1):
        if sonstr[0] == motherstr[each]:
            if sonstr[1] == motherstr[each + 1]:
                times += 1
        #i += 1
    #return times
    print('字符串在目标字符串中出现的次数为 %d 次'% times)       
    
motherstr = input("请输入一个字符串：")
sonstr = input("请输入一个长度为2的子字符串：")
result = findstr(motherstr,sonstr)
#print(result)    
'''
