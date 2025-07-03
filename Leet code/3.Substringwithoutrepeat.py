""" 3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters."""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        set = []
        max_len = 0
        n=0
        for j in range(len(s)):
            if s[j] in set:
                while s[j] in set:
                    set.pop(0)
            set.append(s[j])
            max_len = max(max_len, len(set))
        return(max_len)  
    


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("aab"))
            