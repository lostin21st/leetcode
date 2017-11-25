"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
                 better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:
    string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

def convert(s,numRows):
    """
    把原字符串按照zigzag的方式写入到存有numRows行string的list中，然后按行读取就行了.
    """
    if numRows == 0 or numRows == 1:
        return s
    l = ['' for i in range(numRows)]
    index, step = 0, 1
    for c in s:
        l[index] += c
        if index == numRows - 1:
            step = -1
        elif index == 0:
            step = 1
        index += step
    return ''.join(l)
