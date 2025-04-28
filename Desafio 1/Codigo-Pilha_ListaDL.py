global ops 
ops = ["+", "-", "*", "%", "^", "/"]

class Node_P:
    prox = None
    valor = 0
    def _init_ (self, valor):
        self.prox = None
        self.valor = valor

 
class pilha:
    header = Node_P()
    top = None
    size = 0
    
    def inserir (self, elemento):
        if self.top == None:
            self.top = elemento
            self.top.prox = self.header
            self.size += 1
            return
        else:
            elemento.prox = self.top
            self.top = elemento
            self.size += 1
            return
    
    def pop (self):
        elemento = self.top
        self.top = self.top.prox
        if self.top == self.header:
            self.top = None
        return elemento


class Node_L:
    def __init__(self, val, next, prev):
        self.val = val
        self.next = next
        self.prev = prev


class ListDL:
    def __init__(self):
        self.header = Node_L(-1, None, None)
        self.size = 0
    
    def insert(self, val):
        node = self.header
        while node.next:
            node = node.next
        node.next = Node_L(val, None, node)
        
        self.size += 1


    def search(self):
        node = self.header
        if(node.next):
            node = node.next

        while node.next and not node.val in ops:
            node = node.next
        
        if node.val in ops:
            return node
        else: 
            return None

    def delete(self, element : Node_L):

        element.prev.next = element.next
        if(element.next):
            element.next.prev = element.prev
        
        self.size -= 1

    def Operação(self, operator):
        if(operator):
            operator.prev.prev.val = float(operator.prev.prev.val)
            operator.prev.val = float(operator.prev.val)
            if (operator.val == "+"):
                operator.prev.val = str(operator.prev.prev.val + operator.prev.val)

            elif (operator.val == "-"):
                operator.prev.val = str(operator.prev.prev.val - operator.prev.val)

            elif (operator.val == "/"): 
                operator.prev.val = str(operator.prev.prev.val / operator.prev.val)

            elif (operator.val == "*"):
                operator.prev.val = str(operator.prev.prev.val * operator.prev.val)

            elif (operator.val == "%"):
                operator.prev.val = str(operator.prev.prev.val % operator.prev.val)

            else: #POTENCIAÇÃO
                operator.prev.val = str(operator.prev.prev.val ** operator.prev.val )               
            
            #Fazer no final quando terminar a operação
            operator.prev.prev.prev.next = operator.prev
            operator.prev.next = operator.next
            operator.prev.prev = operator.prev.prev.prev
            if(operator.next):
                operator.next.prev = operator.prev
            
            self.size -= 2

def check_multidigit(expr, i):
    number = str(expr[i])
    while((i+1 < len(expr)) and expr[i+1].isnumeric()):
        number += str(expr[i+1])
        i += 1
    return number
    
    


def main():
    expr = "(" + input() + ")"

    expr_pol = ListDL()
    
    pilha_parenteses = pilha()
    pilha_operação = pilha()

    i = 0
    while i < len(expr):
        if(expr[i].isnumeric()):
            number = check_multidigit(expr, i)
            expr_pol.insert(str(number))
            i += len(number) - 1

        elif(expr[i] == "("):
            parentese = Node_P()
            pilha_parenteses.inserir(parentese)
        
        elif(expr[i] in ops):
            operação = Node_P()
            operação.valor = expr[i]
            pilha_operação.inserir(operação)
        else:
            pilha_parenteses.pop()
            if(pilha_operação.top):
                op = (pilha_operação.pop()).valor
                expr_pol.insert(str(op))
        
        i += 1

    node = expr_pol.header
    print("notação polonesa:", end=" ")
    while node.next:
        node = node.next
        print(node.val, end=" ")
    print("\n")
    
    print("valor da expressão:", end=" ")
    node = expr_pol.header
    while (expr_pol.size > 1):
        expr_pol.Operação(expr_pol.search())

    print(expr_pol.header.next.val)

main()