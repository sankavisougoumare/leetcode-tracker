# Last updated: 23/07/2026, 10:59:08
from collections import defaultdict
class Solution:
    def shortestPath(self,n:int,edges:list[list[int]],labels:str,k:int)->int:
        graph=defaultdict(list)
        for u,v,w in edges:
            graph[u].append((v,w))
        pq=[(0,0,labels[0],1)]
        visited=set()
        while pq:
            cost,node,last_char,count=heapq.heappop(pq)
            if node==n-1:
                return cost
            if(node,last_char,count)in visited:
               continue
            visited.add((node,last_char,count))
            for nei,w in graph[node]:
                char=labels[nei]
                if char==last_char:
                    if count +1 >k:
                        continue
                    new_count=count +1
                else:
                    new_count=1
                heapq.heappush(pq,(cost + w,nei,char,new_count))
        return -1                