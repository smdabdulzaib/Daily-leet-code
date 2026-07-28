class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count=Counter(s)
        left=[]
        mid=""

        for ch in "abcdefghijklmnopqrstuvwxyz":
            left.append(ch*(count[ch]//2))
            if count[ch]%2==1:
                mid=ch
        left="".join(left)
        right=left[::-1]
        return left+mid+right