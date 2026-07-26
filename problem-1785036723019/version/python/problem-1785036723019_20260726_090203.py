# Last updated: 26/07/2026, 09:02:03
1class Solution:
2    def countValidSequences(self, n: int, k: int) -> int:
3        MOD=10**9+7
4        def comb(N,R):
5            if R<0 or R>N:
6                return 0
7            R= min(R, N -R)
8            num = den =1
9            for i in range(R):
10                num=num*(N-i)%MOD
11                den=den*(i+1)%MOD
12            return num*pow(den,MOD-2,MOD)%MOD
13        total=comb(n-1,k-1)
14        odd=0
15        if n>=k and (n-k)%2==0:
16            odd =comb((n+k-2)//2,k-1)
17        return(total-odd)%MOD
18                