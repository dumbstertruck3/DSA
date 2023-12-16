def lengthOfLongestSubstring(s):

    def  helper_func(cursor, s):
        sub = ""
        for position in range(cursor,len(s)):
            if s[position] not in sub:
                sub += s[position]
            else:
                break
        return sub
    subString = []
    for i in range(len(s)):
        subString.append(helper_func(i,s))
    return max(subString, key=len)
