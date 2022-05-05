def docID(p):
    return p[0]

def positions(p):
    return p[1]
    
def positional_intersect(p1,p2,k):
    answer=[]
    i=j=0
    while i!=len(p1) and j!=len(p2) : 
        if docID(p1[i]) ==docID(p2[j]):
            l=[]
            pp1=positions(p1[i])
            pp2=positions(p2[j])
            ii=jj=0
            while ii!=len(pp1):
                while jj!=len(pp2):
                    if abs(pp1[ii]-pp2[jj])<=k : 
                        l.append(pp2[jj]) 
                    elif pp2[jj]>pp1[ii]:
                        break
                    jj+=1
                while l and abs(l[0]-pp1[ii])>k:
                    l.remove(l[0])
                for ps in l:
                    answer.append([docID(p1[i]),pp1[ii],ps])
                ii+=1
            i+=1
            j+=1
        elif docID(p1[i])<docID(p2[j]):
            i+=1
        else : 
            j+=1
    return answer
    
            
    
if __name__ == "__main__":
    posting_lists={
        "to": [
            [1,[7,18,33,72,86,231]],
            [2,[1,17,74,222,255]],
            [4,[8,16,190,429,433]],
            [5,[363,367]],
            [7,[13,23,191]]
            ],
        "be": [
            [1,[17,25]],
            [4,[17,191,291,430,434]],
            [5,[14,19,101]]
        ]
    }
    
    
    # to be or not to be 
    
    # we look for places in the lists where there is an occurrence of be with a token index one higher than a position of to :
    print(positional_intersect(posting_lists['to'],posting_lists['be'],1),'\n')
    # we look for another occurrence of each word with token index 4 higher than the first occurrence : 
    print(positional_intersect(posting_lists['to'],posting_lists['to'],4),'\n')
    print(positional_intersect(posting_lists['be'],posting_lists['be'],4),'\n')
    