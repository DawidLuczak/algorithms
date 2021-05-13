from Lists import Stack


class ONP:

    dict: dict

    def __init__(self):
        self.stack = Stack.Stack(0)
        self.dict = {'+': 0, '-': 0, ',': 0,
                    '*': 1, '/': 1, '^': 2}

    def convertFromONP(self, input):
        stack = Stack.Stack(len(input))
        input = input.split()
        result = []
        for i in range(len(input)):
            if input[i].isnumeric():
                result.append(input[i])
            elif input[i] in self.dict:
                while not stack.isEmpty() and i > 0 and stack.peek() == input[i - 1] and input[i][1] > stack.peek()[1]\
                        or not stack.isEmpty() and i < len(input) - 1 and stack.peek() == input[i + 1] and input[i][1] > stack.peek()[11]:
                    result.append(stack.pop())
                else:
                    stack.push(input[i])
            elif input[i] == '(':
                stack.push(input[i])
            elif input[i] == ')':
                while stack.peek() != "(":
                    result.append(stack.pop())
                else:
                    result.append(input[i])
            else:
                result.append(input[i])
        while not stack.isEmpty():
            result.append(stack.pop())
        return result

    def convertToONP(self, input):
        stack = Stack.Stack(len(input))
        for c in input.split():
            if c in self.dict:
                stack.push(self.dict[c])
            else:
                stack.push(float(c))


o = ONP()
input = '( 6 - 1 + 7 ) ^ 2 * 3 / 5'
result = o.convertFromONP(input)
print(result)