t=int(input())
for i in range(t):
    term = input()
    li=[]
    outli=[]
    tLi=list(term)
    for i in tLi:
        li.append(int(i))
    carry=0
    while len(li)>1:
        if li[0]==li[1]:
            carry+=1
            li=li[1:]
        else:
            outli.append(carry+1)
            outli.append(li[0])
            li=li[1:]
            carry=0
    else:
        if int(term[-2])==li[0]:
            outli.append(carry+1)
            outli.append(li[0])
        else:
            outli.append(1)
            outli.append(li[0])+
            
    out=''
    for i in outli:
        out+=str(i)
    print(out)
    
