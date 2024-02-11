depends = []
disk = []
graf=[[]for i in range(len(depends))]
    prev=[len(depends[i])for i in range(len(depends))]
    stosA = []
    stosB= []
    for i in range(len(depends)):
        for j in depends[i]:
            graf[j].append(i)
        if len(depends[i])==0 and disk[i]=="A":
            stosA.append(i)
    u="A"
    print(graf)
    counter=0
    while len(stosA)!=0 or len(stosB)!=0:
        while len(stosA)!=0:
            x=stosA.pop()
            #print(x,'A')
            for i in graf[x]:
                prev[i]-=1
                #print(prev[i])
                if prev[i]==0:
                    #print(i,disk[i])
                    if disk[i]=='A':
                        stosA.append(i)
                    else:
                        stosB.append(i)
        counter += 1
        if len(stosB)==0:
            break
        while len(stosB)!=0:
            x = stosB.pop()
            #print(x,'B')
            for i in graf[x]:
                prev[i] -= 1
                if prev[i] == 0:
                    if disk[i] == 'A':
                        stosA.append(i)
                    else:
                        stosB.append(i)
        counter += 1
