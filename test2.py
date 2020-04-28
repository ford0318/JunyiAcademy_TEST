def main(num):
    numlist=[]
    remove3=[]
    remove5=[]
    num3_5=[]
    for x in range(1,num+1):
        if x % 3 == 0:
            if not(x % 3 ==0 and x % 5 ==0):
                remove3.append(x)
        elif x % 5 ==0:
            if not(x % 3 ==0 and x % 5 ==0):
                remove5.append(x)
        if not(x % 3 == 0 or x % 5 ==0):
            numlist.append(x)
        if x % 3 ==0 and x % 5 ==0:
            num3_5.append(x)
            numlist.append(x)
    return 'INPUT:'+f'{num}'+'\n'+'所有數字是' + ','.join([str(x) for x in range(1,num+1)])+"\n"+'其中'+ ','.join([str(i) for i in remove3])+'被剃除;'+','.join([str(j) for j in remove5])+'但是'+','.join([str(g) for g in num3_5])+'被保留'+'\n'+'所有剩下來的數字是'+','.join([str(x) for x in numlist])+'\n'+'OUTPUT:'+ str(len(numlist))


if __name__ == "__main__":
    print(main(eval(input('請輸入數字:'))))


