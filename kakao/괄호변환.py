class TransferBracket:
    def is_balanced_bracket(self, bracket):
        return bracket.count("(") == bracket.count(")")
    
    def is_proper_bracket(self, bracket):
        check = 0 # if check < 0 -> not proper bracket
        for b in bracket:
            if b == "(":
                check += 1
            elif b == ')':
                check -= 1
            if check < 0:
                return False
        return True
    
    def transfer(self, brackets):
        if not brackets:
            return ""
        for i in range(2, len(brackets)+1, 2):
            if self.is_balanced_bracket(brackets[:i]):
                u, v = brackets[:i], brackets[i:]
                if self.is_proper_bracket(u):
                    return u + self.transfer(v)
                else:
                    
                    temp = "("
                    temp += self.transfer(v)
                    temp += ')'
                    u = u[1:-1].replace("(", "|").replace(")", "(").replace("|", ")")
                    
                    return temp + u             
        return brackets
        

def solution(ps):
    transferbracket = TransferBracket()
    transfered = transferbracket.transfer(ps)
    return transfered
