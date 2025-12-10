from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0])
        else:
            operators = ["+", "-", "*", "/"]
            idx1 = 0
            idx2 = 1
            i = 2
            while i < len(tokens):
                if tokens[i] not in operators:
                    idx1 = idx2
                    idx2 = i
                else:
                    match tokens[i]:
                        case "+": tokens[i] = int(tokens[idx1]) + int(tokens[idx2])
                        case "-": tokens[i] = int(tokens[idx1]) - int(tokens[idx2])
                        case "*": tokens[i] = int(tokens[idx1]) * int(tokens[idx2])
                        case "/": tokens[i] = int(int(tokens[idx1]) / int(tokens[idx2]))
                    tokens[idx1] = tokens[idx2] = "x"
                    if i + 1 < len(tokens):
                        if tokens[i + 1] not in operators:
                            idx1 = i
                            idx2 = i + 1
                            i += 1
                        else:
                            idx2 = i
                            for j in range(idx1 - 1, -1, -1):
                                if tokens[j] != "x":
                                    idx1 = j
                                    break
                    else:
                        return tokens[-1]
                i += 1
    
    def evalRPN_solution2(self, tokens: List[str]) -> int:
        prev_idxes = [i - 1 for i in range(len(tokens))]
        if len(tokens) == 0:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0])
        else:
            operators = ["+", "-", "*", "/"]
            idx1 = 0
            idx2 = 1
            i = 2
            while i < len(tokens):
                if tokens[i] not in operators:
                    idx1 = idx2
                    idx2 = i
                else:
                    match tokens[i]:
                        case "+": tokens[i] = int(tokens[idx1]) + int(tokens[idx2])
                        case "-": tokens[i] = int(tokens[idx1]) - int(tokens[idx2])
                        case "*": tokens[i] = int(tokens[idx1]) * int(tokens[idx2])
                        case "/": tokens[i] = int(int(tokens[idx1]) / int(tokens[idx2]))
                    tokens[idx1] = tokens[idx2] = "x"
                    if i + 1 < len(tokens):
                        prev_idxes[i] = prev_idxes[idx1]
                        if tokens[i + 1] not in operators:
                            idx1 = i
                            idx2 = i + 1
                            i += 1
                        else:
                            idx2 = i
                            idx1 = prev_idxes[idx1]
                    else:
                        return tokens[-1]
                i += 1
    
    def evalRPN_solution3(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return 0
        elif len(tokens) == 1:
            return int(tokens[0])
        else:
            stack = []
            operators = ["+", "-", "*", "/"]
            for token in tokens:
                if token not in operators:
                    stack.append(token)
                else:
                    operand2 = int(stack.pop())
                    operand1 = int(stack.pop())
                    match token:
                        case "+": stack.append(operand1 + operand2)
                        case "-": stack.append(operand1 - operand2)
                        case "*": stack.append(operand1 * operand2)
                        case "/": stack.append(int(operand1 / operand2))
            return stack.pop()
                
case1 = ["2","1","+","3","*"]
case2 = ["4","13","5","/","+"]
case3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
solution = Solution
print(solution.evalRPN_solution3(solution, case3))