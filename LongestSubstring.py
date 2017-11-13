"""
Given a string, find the length of the longest substring without repeating
characters.
(给定一个字符串，求最大子串长度，子串不含重复字符)
"""
def lengthOfLongestSubstring(self,s):
    start = maxlength = 0
    usedchar = {} #用字典记录出现过的字符，和其位置
    for i in range(len(s)):
        if s[i] in usedchar and start <= usedchar[s[i]]: 
            start = usedchar[s[i]]+1
        else:
            maxlength = max(maxlength, i-start+1)

        usedchar[s[i]] = i #每循环一次记录出现的字符，如果出现过更新位置

    return maxlength

