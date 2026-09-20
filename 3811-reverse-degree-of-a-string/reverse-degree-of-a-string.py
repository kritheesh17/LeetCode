class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0

        for i, c in enumerate(s):
            value = ord('z') - ord(c) + 1
            ans += (i + 1) * value

        return ans