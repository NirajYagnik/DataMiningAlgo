"""
Aprior Implemenation
Input Type: List of lists, where each list item indicates a transaction
Functions implemented:
loadDataset
C1 generation
Frequent Itemset generation
Candidate Generation
powerset(all poss subset of transactions)
prune
aprior integrator

"""
def loadDataSet():
	x = [[1,2,3], [2,3,4],[4,5,6], [7,8,9], [10, 11, 12]] #INPUT Database
	return x

def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
    return C1


def L_gen(C,min_supp):
    L_count={}
    for i in C:
        count = 0 
        for j in x:
            if all(ele_check in j for ele_check in i):
                count= count + 1 
                L_count[tuple(i)] = count
            else:
            	L_count[tuple(i)] = count
    L_count = { k : v for k,v in L_count.items() if v>=min_supp}
    return L_count


def can_gen(L,k):
    C_new = []
    L_old = [list(ele) for ele in L.keys()]
    for i in range(len(L_old)):
        for j in range(i+1, len(L_old)): 
            L1 = list(L_old[i])[:k]
            L2 = list(L_old[j])[:k]
            L1.sort()
            L2.sort()
            if L1==L2:
                a = list(set((L_old[i] + L_old[j])))
                C_new.append(sorted(a)) 
    return C_new

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 0:
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def prune(L,C):
    L = [list(ele) for ele in L.keys()]
    for r in C:
        r_set = [x for x in powerset(r)]
        r_set.remove(r)
        r_set.remove([])
        #print(r_set)
        count = 0
        for i in r_set:
            #print("Checking ",i)
            for j in L:
                if all(ele_check in j for ele_check in i):
                    count = count + 1
                    break
        if(count != len(r_set)):
            C.remove(r)
            #print("This",r)
    return C


def apriori(support):
    frequent = []
    global x 
    x = loadDataSet()
    print("Dataset Loaded")
    c1 = createC1(x)
    print("C1 Created")
    #print(c1)
    Lk= L_gen(c1,support)
    print("L1 Created")
    L = [list(ele) for ele in Lk.keys()]
    print("L for iteration ",L)
    #print(L)
    for i in L:
        frequent.append(i)
    #print("frequent",frequent)
    k = 0
    print("Until Lk is null")
    while L !=[]:
        Ck = can_gen(Lk,k)
        #print(Ck)
        k = k+1
        Ck = prune(Lk,Ck)
        #print(Ck)
        Lk = L_gen(Ck,support)
        L = [list(ele) for ele in Lk.keys()]
        print("L for iteration ",L)
        for i in L:
            frequent.append(i)
        #frequent.append(L)
    return frequent
support = int(input('Enter the support '))

frequent  = apriori(support)
print("---"*50)
print("---"*50)
print("Frequent Itemsets are:")
print(frequent)
