# Reverse Words in a String 3
def reverseWords(self, s: str) -> str:
    s = ' ' + s
    stack = []
    str_list = []
    for i in reversed(range(len(s))):
        c = s[i]
        str_list.append(c)
        if c == ' ':
            stack.append(''.join(str_list))
            str_list = []
    
    
    return ''.join(stack[::-1])[:-1]

    # Solution using functional programming
    # return ' '.join(map(lambda x: x[::-1], s.split()))
    
    # Solution using list comprehension
    # return ' '.join([x[::-1] for x in s.split()])