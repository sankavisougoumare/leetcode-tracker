# Last updated: 23/07/2026, 10:59:04
class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals,freeStart,freeEnd):
        occupiedIntervals.sort()
        merged=[]
        for s,e in occupiedIntervals:
            if not merged or s >merged[-1][1]+1:
               merged.append([s,e])
            else:
                merged[-1][1]=max(merged[-1][1],e)
        result=[]
        for s,e in merged:
            if e<freeStart or s>freeEnd:
               result.append([s,e])
            else:
                if s<freeStart:
                    result.append([s,freeStart-1])
                if e>freeEnd:
                    result.append([freeEnd+1,e])
        return result