# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 15:23:53 2020

The Rabin-Karp algorithm for searching substring in a string

Returns the indexes of appearing substring in a string.

Call RabinKarp(substring,string)

@author: Vitalii
"""

#Алгоритм Рабина-Карпа для поиска подстроки в тексте!!!!!
def RabinKarp(X,Y):    
    x = 1
    p = 10009
    #функция хеширования
    def hash(S):
        s = 0
        L = len(S)
        for c in range(L):
            s = (s + ((ord(S[c]) * x**c) ))%p
        return s
    coin = []

    L1 = len(X)
    L2 = len(Y)
    h1 = hash(X)
    h2 = hash(Y[L2-L1:L2])
    if h1 == h2 and X == Y[L2-L1:L2]:
        coin.append(L2-L1)
    for j in range(L2-L1-1,-1,-1):
        h2 = ((h2 - ord(Y[j+L1])*x**(L1-1))*x % p+ord(Y[j])) 
        if h2 == h1 and X == Y[j:j+L1]:
            coin.append(j)
    coin.reverse()
    print(" ".join(map(str, coin)))
    return coin


if __name__ == '__main__':
   RabinKarp('aba', 'abacabacabacaba')   