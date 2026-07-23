# Last updated: 23/07/2026, 10:59:06
class Solution:
    def concatHex36(self, n: int) -> str:
        def convert(num, base):
            chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            if num == 0:
                return "0"

            res = []
            while num > 0:
                res.append(chars[num % base])
                num //= base

            return "".join(reversed(res))

        return convert(n * n, 16) + convert(n * n * n, 36)