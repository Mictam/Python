from operator import or_, and_, not_, xor, eq
import string


VARS = string.ascii_lowercase + string.ascii_uppercase
OPS = "|&>^=~"
PRIO = {'~': 6, '^': 5, '&': 4, '|': 3, '>': 2, '=': 1}

def Implication(a, b):
    return not(a) or b

OPExec = {"|": or_, "&": and_, ">": Implication, "~": not_, "^": xor, "=": eq  }


def ValidateExpr(expr):
    
    testVar = "".join(expr.split())
    
    brackets = 0
    k = 1
    k1 = 1

    if (((testVar[0].islower)==False and testVar[0] != '(') or ((testVar[len(testVar)-1].islower)==False and testVar[len(testVar)-1] != ')')):
        k = 0

    state = 0


    for x in range(0, len(testVar)):

        
     
        if ( testVar[x] == '(' ):
            brackets+=1
            if ( state == 1 ):
                k = 0 
            state = 3

        elif ( testVar[x] == ')' ):
            brackets-=1
            if ( state == 2 ):
                k =  0
            if ( state == 5 ):
                k = 0
            state = 4

        elif ( testVar[x] == "&" or testVar[x] == '|' or testVar[x] == '>' or testVar[x] == '=' or testVar[x] == '^' ):

            if ( state == 3 ):
                k = 0
            if ( state == 2 ):
                k = 0
            if ( state == 5 ):
                k = 0
            state = 2
            
        elif ( testVar[x] == "~" ):
            if ( state == 4):
                k = 0
            if ( state == 1):
                k = 0
            if ( state == 5 ):
                k = 0
            state = 5

        elif ( testVar[x].islower or testVar[x].isUpper):
            if ( state == 4):
                k = 0
            if ( state == 1):
                k = 0
            state = 1


        if ( brackets < 0 ):
            k=0


    if ( brackets > 0):
        k=0 


    if ( k == 1 ):
        return True
    else:
        return False
    

def ToRPN(expr):
    
    out = []
    stack = []

    for el in expr:
        
        if el in string.ascii_lowercase or el in "01~" or el in string.ascii_uppercase:
            out.append(el)

        elif el == "(":
            stack.append(el)

        elif el == ")":
            while (stack[-1] != "("):
                out.append(stack.pop())

            stack.pop()

            
        elif el in "|&>^=":

            if stack and stack[-1] != "(":
                priority = PRIO[el]
                TopElPrio = PRIO[stack[-1]]

                while (stack and stack[-1] != "(" and TopElPrio > priority ):

                    out.append(stack.pop())

                    if stack and stack[-1] != "(":
                        TopElPrio = PRIO[stack[-1]]

            stack.append(el)
           
  
    while stack:
        out.append(stack.pop())

    return out

def CreateProperList(bin_num, res_digits):
    
    return "".join([str('0') for _ in range(res_digits+1 - len(bin_num))]) + bin_num;



def SeparateVarOp(expr):
    tab = list("".join(expr.split()))
    vartab = []
    for x in tab:
        if(x in VARS):
            vartab.append(x)
    optab = []
    for x in tab:
        if(x in OPS):
            optab.append(x)
    
    return sorted(vartab), sorted(optab)

def Int2bin(i):
    if i == 0: return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s


def Generator(var):
    
    longest = len(var)
    binTab = [bin(i)[2:] for i in range(2**longest)]  # tablica liczb binarnych
    return list(map(list, map(lambda i: CreateProperList(i, len(binTab[-1])), binTab)))


    
def ToBool(expr):
     if expr == "1": 
        return True
     else:
        return False
    
def ToStr(expr):
     if expr == True: 
        return "1"
     else:
        return "0"
    
    
    
def Eval(expr):
    
    var, ops = SeparateVarOp(expr)
    GeneratedArrays = Generator(variables)
    
    for SingleArray in GeneratedArrays:

        RPN = ToRPN(expr)
        stack = []
        BoolRPN = RPN
        stri = ""
        
        i = 1
        j = 0
        for el in RPN:
            if el in VARS:
                indx2=var.index(el)
                BoolRPN[j]=SingleArray[indx2+1]  
            j+=1  
      
        ifneg = 0
        for i in BoolRPN:

            w = i
            
            if i in OPS:
                k1 = ToBool(stack.pop())
                k2 = ToBool(stack.pop())
                if(ifneg): k2= not k2
                w = ToStr(OPExec[i](k1, k2))
                
            if i == "~":
                ifneg = 1
                continue
                
            if i in VARS:
                if(ifneg): 
                    if(i == "1"): 
                        i = "0" 
                    else: 
                        i = "1"
                w = i
        
            ifneg = 0
            stack.append(w)

        SingleArray[0] = stack.pop()
    var.insert(0,'wynik')
    return GeneratedArrays,var

def Taut(expr):
    tab, var=Eval(expr)
    t = True
    for i in tab:
        if(i[0]=='0'): 
            t=False
    return t
