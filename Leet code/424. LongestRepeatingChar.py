""" 424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
"""
        
class Solution(object):
    def characterReplacement(self, s, k):
        dict = {}
        i,j = 0, 0
        while (j<len(s)):
            if s[j] in dict:
                dict[s[j]] +=1
            else:
                dict[s[j]] = 1
            max_freq = max(dict.values())
            if (j - i + 1 - max_freq) > k:
                dict[s[i]] -= 1
                if dict[s[i]] == 0:
                    del dict[s[i]]
                i += 1
            max_len = max(len(dict), j - i + 1)
            j+=1
        return max_len
            
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("AABABBA", 1))
    