# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 10:53:28 2020
Dijkstra Algorithm to find the shortes way between vertexes in a graph.

The function Dejkstra(numvertpath,graph,startend) takes 
three argumens: numvertpath = [A, B], where A is the number of vertexes 
in the graph and B is number of edges; 
graph is a list of vertexes merged by an edge  and weights each of 
the edge (e.g. [[1,2,3],[3,4,5]])
startend = [start,end] is the number of initial and ending vertexes to find the
shortest path between them.


The function returns the length of the shortest way between the start and end 
vertexes or -1 if the way does not exist.  

@author: Vitalii
"""

#Алгоритм Дейкстры


def Dejkstra(numvertpath,graph,startend):
#проверяю есть ли начальная и конечная точка в списках (можно ли пройти вообще)
    [numvert, path] = numvertpath
    [start, end] = startend
    mark1 = False
    mark2 = False
    for i in graph:
        if  i[1] == end:
            mark1 = True
            break
    
    
    for i in graph:
        if  i[0] == start:
            mark2 = True
            break
    
    #если путь потенциально сужествует то        
    if mark1 and mark2 and path > 0 and (numvert > 1):
        #заполняю массив бесконечными весовами, 
        #индекс массива это точка в которую можно пройти из старта
    
        weight = [[False,float('Inf')] for i in range(numvert)]
        weight[start-1] = [True,0]
        for i in graph:
            if i[1] == start: #удаляю из начального графа пути с концом в старте               
                graph.remove(i)
    
        #всем точкам в которые можно пройти из старта даю веса
        for i in range(len(graph)):
            if graph[i][0] == start:
                weight[graph[i][1]-1][1] = graph[i][2]
    
        for i in graph[::-1]:
            if i[1] == start or i[0] == start:
                graph.remove(i)
    
        iter = 0
        flag = True
        #ищу доступную непосещенную вершину с мин весом и обхожу 
        #все что с ней связано, после обхода вершина удаляется из графа
        while graph:    
            #print(graph)
            iter += 1
            minW = float('Inf')
            j = start - 1
            for i in range(len(weight)):
                if (not weight[i][0]) and minW > weight[i][1]:
                    minW = weight[i][1]
                    j = i
    
            # если новый суммарный путь короче чем исходный, то заменить исходный им
            for ln in graph:
                if ln[0] == j + 1:
                    if weight[j][1] + ln[2] < weight[ln[1] - 1][1]:
                        weight[ln[1] - 1][1] = weight[j][1] + ln[2]
            weight[j][0]= True
    
            for i in graph[::-1]:
                if i[0] == j + 1:
                    graph.remove(i)
            # если число итераций большое, то значит алгоритм не может больше найти путей и нужно заканчивать
            if iter > 500:
                flag = False
                break
    
       
        if flag:
            return weight[end-1][1]
        else:
            return -1
    
    
    else:
        return -1
    
if __name__ == '__main__':
    graph = [[1, 2, 6], [1, 3, 2], [1, 4, 10], [2, 4, 4], [3, 1, 5], [3, 2, 3], [3, 4, 8], [4, 2, 1]] 
    Dejkstra([4,8],graph,[4,3])    
    