# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:02:14 2020

The function realises the Hoffan code for an arbitrary string


@author: Vitalii
"""


def Hoffman(string):
# functon for sorting
    def sor(args):
        return args.sort(key = lambda x: x[1])
    s = string
    #Replace blank to # for more convenient
    s = s.replace(' ','#')
    string=s
    X=[]
    
    #I count the frequency of each element
    while len(s)>0:
        X.append([s[0],s.count(s[0])])
        s=s.replace(s[0],'')   
    X.sort(key = lambda x: x[1])
    Z=X.copy()
    
    #nested list (like binary tree)
    while len(Z)>2:
        Z[1]=[[Z[0][0],(Z[1][0])],Z[0][1]+Z[1][1]]
        del Z[0]
        sor(Z)
    if len(Z)<2:
        Z=X[0]
    else:
        Z[0]=Z[0][0]
        Z[1]=Z[1][0]
    
    #function correspondece between element and its code
    def numb(Z, s):
        inn=''
        for kk in str(Z):
            if kk=='[' or kk =="]" or kk==',':
                inn=inn+kk
            inn=inn.replace('[,]','')
            if kk==s: break
        inn=inn.replace('[,','1')
        inn=inn.replace('[','0')
        return [s, inn]
    
    #codes of each element in the string
    CD=[]
    for code in range(len(X)):
        CD.append(numb(Z,X[code][0]))
    
    #replacing each element in the initial string by its code
    for j in CD:
        string=string.replace(j[0],j[1])
    
    print(" ".join(list(map(str, [len(X),len(string)]))))
    for k in CD:
        print(": ".join(list(map(str, k))))
    print(string)


if __name__ == '__main__':
   Hoffman('Мама мыла раму')    