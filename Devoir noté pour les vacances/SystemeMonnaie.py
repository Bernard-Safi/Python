#question:1 la structure optimal est en utilisant les tuples

#question 2.1
def rendreMonnaieRecursive(billet,type,count1=0,count2=0):
    print(count1,count2)
    if(billet-type[0]>=0):
        return rendreMonnaieRecursive(billet-type[0],type,count1+1,count2)
    else:
       if(billet-type[1]>=0):
        return rendreMonnaieRecursive(billet-type[1],type,count1,count2+1)
#question 2.3 imperative
def rendreMonnaie(billet,*type):
    typesort=sorted(type,reverse=True)
    returned=[0]*len(type)
    for i in typesort: 
        count=0
        while billet>=i:
            billet-=i
            count=count+1
        returned[type.index(i)]=count
    return returned

def rendreMonnaieComprehension(billet,*type):
    typesort=sorted(type,reverse=True)
    z=0
    number_list = [ billet-x for x in typesort if billet>=x]
    print(number_list)


#rendreMonnaieComprehension(250000,50000,100000,5000)
print(rendreMonnaie(525000,100000,5000,20000,50000,10000))
#rendreMonnaieRecursive(7000,(5000,1000))
