class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check length
        if len(s) != len(t):
            return False
        
        # Step 2: Create frequency array
        count = [0] * 26
        
        # Step 3: Update counts
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # Step 4: Check all values are zero
        for c in count:
            if c != 0:
                return False
        
        # Step 5: Return result
        return True