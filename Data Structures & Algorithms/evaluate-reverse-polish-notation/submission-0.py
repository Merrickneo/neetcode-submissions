class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        # if its a number, insert it in
        # operand then pop two elements and evaluate before putting them back
        operands = set(["+", "-", "*", "/"])
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
                continue
            num2 = stack.pop()
            num1 = stack.pop()
            output = 0
            if token == "+":
                output = num1 + num2
            elif token == "-":
                output = num1 - num2
            elif token == "*":
                output = num1 * num2
            elif token == "/":
                output = num1 / num2
            stack.append(int(output))
        return stack.pop()




        