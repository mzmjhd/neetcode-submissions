class Solution:
    def isValid(self, s: str) -> bool:
        stack = collections.deque() #LIFO
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.appendleft(c)
                print(stack)
            else:
                if len(stack)<=0:
                    return False
                match c:
                    case ']':
                        if stack.popleft() != '[':
                            return False
                    case '}':
                        if stack.popleft() != '{':
                            return False
                    case ')':
                        if stack.popleft() != '(':
                            return False
                    case _: continue
        return len(stack) == 0