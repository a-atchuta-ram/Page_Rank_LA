from bs4 import BeautifulSoup
from numpy import linalg as LA

import numpy as np
 ## Give a list of all HTML files , list of strings
def trans_mat(l):
    s1=set(l)
    mat_a=[]
    for i in l:
        HTMLFile = open(i, "r")
        index = HTMLFile.read()

        soup = BeautifulSoup(index,'lxml')
        d={}
        s=set()
        for a in soup.find_all('a', href=True):
            s.add(a['href'])
        ##print("Found the URL:", a['href'])
            if(a['href'] not in d):
                d[a['href']]=0
            d[a['href']]+=1
        # print(s)
        # print(s1)
        s3=(s1.difference(s))
        for l in s3:
            d[l]=0
        n=sorted(d)
        ans=[]
        for index in n:
            ans.append(d[index])
       
        #ans=[round(i/sum(ans),2) for i in ans]
        ans=[i/sum(ans) for i in ans]
        mat_a.append(ans)
        #print(mat_a)
    
    n=np.array(mat_a)
    k=np.transpose(n)
    ##print(k)
    b=k.tolist()
    return b
        
            

        

l=["page1.html","page2.html","page3.html","page4.html"]

p=trans_mat(l)
print(p)
