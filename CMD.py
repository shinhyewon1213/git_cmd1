str1=input()
chk=[]
sum=[]
res=[]
cnt=0
for i in range(0,100):
    chk.append(0)
    sum.append(0)
    res.append(0)

def getord(s):
    n=ord(s)
    if s <= "Z" and s >= "A":
        i = n-65
        return i
    else:
        i = n-97+26
        return i

def checkstr(s):
    global cnt
    i = getord(s)
    if chk[i]==1:
        sum[i]+=1
        return 1
    else:
        chk[i]=1
        sum[i]+=1
        res[cnt]=s
        cnt+=1
        return 0
    return -1


for i in str1:
    checkstr(i)

for i in range(cnt):
    print("%s%d"%(res[i], sum[getord(res[i])]), end="")
