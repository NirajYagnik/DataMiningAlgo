"""
Pincer Search Algo, Pythonic implementation
Input Type: List of lists, where each list item indicates a transaction
"""

def loadDataSet():
    x = [[1,2,3], [2,4],[2,3], [1,2,4],[1,3],[2,3],[1,3],[1,2,3,5],[1,2,5]] #INPUT Database
    return x
def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
                
    C1.sort()
    return C1

def generateMFCS1(dataSet):
    C1 = []
    C2 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.extend([item])
                
    C1.sort()
    return list(set(C1))

def L_gen(C,min_supp,MFCS):
    L_count={}
    MFS = {}
    S = []
    for i in C:
        count = 0 
        for j in x:
            if all(ele_check in j for ele_check in i):
                count= count + 1 
                L_count[tuple(i)] = count
            else:
                L_count[tuple(i)] = count
    #print("L is",L_count)
    S = [list(k) for k,v in L_count.items() if v<min_supp]
    L_count = { k : v for k,v in L_count.items() if v>=min_supp}
    for i in MFCS:
        #print(i)
        count = 0 
        for j in x:
            if all(ele_check in j for ele_check in i):
                count= count + 1 
                MFS[tuple(i)] = count
                #print(MFS)
            else:
                MFS[tuple(i)] = 0
    
    MFCS = [list(k) for k,v in MFS.items() if v<min_supp]
    MFS = [list(k) for k,v in MFS.items() if v>=min_supp]
    
   
    return L_count,S,MFS,MFCS


def mgcs_gen(S,mfcs):
    for i in S:
        #print("S element",i)
        for j in mfcs:
            if all(ele_check in j for ele_check in i):
                mfcs.remove(j)
                #print("After check ", mfcs)
                for k in i:
                    #print("e is ",k)
                    j1 = j.copy()
                    j1.remove(k)
                    #print(j1)
                    flag = 0
                    for l in mfcs:
                        if all(ele_check in l for ele_check in j1):
                            flag = 1
                            break
                    if(flag == 0):
                        mfcs.append(j1)
    return mfcs
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
def mfcs_prune(C,mfcs):
    C_new = []
    for c in C:
        for l in mfcs:
            flag = 0
            if all(ele_check in l for ele_check in c):
                flag = 1
                C_new.append(c)
                break
        #if(flag == 0):
            #C.remove(c)
    return C_new
support = int(input('Enter the support '))
L = []
frequent= []
k = 0
x = loadDataSet()
Ck = createC1(x)
MFCS = []
MFS = []
MFCS.append(generateMFCS1(x))
while Ck!=[]:
    print("Iteration ", k+1)
    print("Ck is ",Ck)
    L,S,MFS_iter,MFCS = L_gen(Ck,support,MFCS)
    print("L is ",L)
    print("S is ",S)
    Lk = [list(ele) for ele in L.keys()]
    for i in Lk:
        frequent.append(i)
    
    MFS.append(MFS_iter)
    if [] in MFS:
        MFS.remove([])
    print("MFS IS",MFS)
    print("MFCS IS",MFCS)
    if S != []:
        MFSC = mgcs_gen(S,MFCS)
        print("New MFCS ", MFCS)
        for m in MFCS:
            if m in Lk:
                MFCS.remove(m)
                print("New MFCS",MFCS)
                MFS.append(m)
                print("New MFS",MFS)
    Ck = can_gen(L,k)
    print("Ck is ",Ck)
    k = k+1
    Ck = mfcs_prune(Ck,MFCS)
    print("New Ck is ", Ck)
for i in MFS:
    if i not in frequent:
        frequent.append(i)


print("------"*40)
print("\n")
print("------"*40)
print("Frequent is ",frequent)