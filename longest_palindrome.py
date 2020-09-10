    def isPalindrome(self, s:str) -> bool:
        return s == "".join(list(reversed(s)))
    
    def longestPalindrome_naive(self, s: str) -> str:
        if len(s) == 0:
            return ""
        elif len(s) == 1:
            return s
        
        for offset in range(len(s), 0, -1):
            for i in range(len(s)-offset+1):
              
                if self.isPalindrome(s[i:offset+i]):
                    return s[i:offset+i]
                
    def longestPalindrome(self, s: str) -> str:
        P = {}
        ans = ""
        max_len = 0
        if len(s) == 1:
            ans = s
        for i in range(len(s)):
            P[(i,i)] = True
        for i in range(len(s)-1):   
            P[(i,i+1)] = s[i] == s[i+1]
        for j in range(0, len(s)):
            for i in range(0, j-1):
                P[(i, j)] = P[(i+1, j-1)] and s[i] == s[j]
                

        for j in range(0, len(s)):
            for i in range(0, j+1): 
                if P[(i, j)] == True and max_len < j-i+1:
                    ans = s[i:j+1]
                    max_len = j - i + 1
            
        return ans


# Dymamic programming
 def longestPalindrome(self, s: str) -> str:
        """
        for each char, look left and right.
        if palindrome, continue.
        """
        if not s:
            return ""

        ispalindrome = lambda x: x == x[::-1]
        max_len = 0
        mem = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = None
        # letters are palindromes of themselves
        for i in range(len(s)):
            mem[i][i] = True
            max_len = 1
            res =  s[i:i+1]

        # two identical letters form trivial palindromes
        for i in range(len(s)-1):
            mem[i+1][i] = s[i] == s[i+1]
            if mem[i+1][i]:
                res = s[i:i+2]
                max_len = 2

        for x in range(2,len(s)):
            for y in range(x):
                mem[y][x] = mem[y+1][x-1] and s[y] == s[x]
                if mem[y][x] and abs(x-y)+1 > max_len:
                    max_len = abs(x-y)+1
                    res = s[y:x+1]

        return res
