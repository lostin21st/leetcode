"""Given a string s, find the longest palindromic substring in s. You may
assume that the maximum length of s is 1000.
(寻找最大长度的回文子串)
exp:
    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
"""
def longestPalindrome(self,s):
    """
    当新增一个字符最大回文子串长只可能增加1或者2.而且最大回文子串办函这个新字符。
    """
    maxlength = 1
    start = 0

    for i in range(len(s)):
        if i-maxlength >= 1 and s[i-maxlength-1:i+1] ==
        s[i-maxlength-1:i+1][::-1]:
            start = i-maxlength-1
            maxlength += 2
            continue
        if i-maxlength >= 0 and s[i-maxlength:i+1] == s[i-maxlength:i+1][::-1]:
            start = i-maxlength
            maxlength += 1
    return s[start:start+maxlength]
