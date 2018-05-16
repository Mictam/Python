from operator import or_, and_, not_, xor, eq
import string


VARS = string.ascii_lowercase + string.ascii_uppercase + "01"
OPS = "|&>^="
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
        if(x in VARS and x not in vartab):
            vartab.append(x)
    optab = []
    for x in tab:
        if(x in OPS and x not in optab): 
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
    GeneratedArrays = Generator(var)
    
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
               # if(ifneg): k1= not k1
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

def CreateMArray(expr):
    tab, var = Eval(expr)
    res = []
    k = 0
    for i in tab:
        if( i[0] == '1'):
            res.append(i)
            bin_no = ""
            k=0
            suma=0
            for var in reversed(i):
                if(k!=4):
                    bin_no+=var
                    if(var=='1'):
                        suma+=1
                if(k==4):
                    i.insert(0,'False')
                    i.insert(0,int(bin_no,2))
                    i.insert(0,bin_no)
                    i.insert(0,suma)
                k+=1       
    return sorted(res)

expr3=[]

def proceed(expr):
    
    expr2=[]
    for x in expr:
        for i in expr:
            k=0
            l=0
            new=""
            new1=""
            newt=[]
            old=[]
            
            if(int(i[0])==int(x[0])+1):
                for j in range(0, len(i[1])):
                    if(x[1][j]!=i[1][j]):
                        k+=1
                        new+='-'
                    else:
                        new+=x[1][j]
                if(k<2):
                    x[3]="True"
                    i[3]="True"
                    new1=str(x[2])+"-"+str(i[2])
                  #  print(i, x)
                  #  print(new,new1)
                    su=0
                    for iii in new:
                        if(iii=='1'):
                            su+=1
                    newt.append(su)
                    newt.append(new)
                    newt.append(new1)
                    newt.append("False")
                    t=0
                    for iii in new:
                        newt.insert(len(newt)-t,iii)
                        t+=1
                    expr2.append(newt)
                  #  print(newt)
                  #  new[2]+=i[2]
                  #  print(new)
    return expr2

def proceed2(expr):
    
    tt=0
    for x in expr:
        for i in expr:
            k=0
            l=0
            new=""
            new1=""
            newt=[]
            old=[]
            if(int(i[0])==int(x[0])+1):
                for j in range(0, len(i[1])):
                    if(x[1][j]!=i[1][j]):
                        k+=1
                        tt+=1
                        new+='-'
                    else:
                        new+=x[1][j]
               # print(k)
                if(k==1):
                    x[3]="True"
                    i[3]="True"
                    new1=str(x[2])+"-"+str(i[2])
                  #  print(i, x)
                  #  print(new,new1)
                    su=0
                    for iii in new:
                        if(iii=='1'):
                            su+=1
                    newt.append(su)
                    newt.append(new)
                    newt.append(new1)
                    newt.append("False")
                    t=0
                    for iii in new:
                        newt.insert(len(newt)-t,iii)
                        t+=1
                 #   print(newt)
                    expr3.append(newt)
        
   # print(expr)
    if(tt>0): proceed2(expr3)
                  #  print(newt)
                  #  new[2]+=i[2]
                  #  print(new)
    
    return sorted(expr3)
        
def proceed3(expr):
    expr4 = []
    pre = CreateMArray(expr)
    pre2 = proceed(pre)
    pre3 = proceed2(pre2)
    expr4.append(pre)
    expr4.append(pre2)
    expr4.append(pre3)
    return expr4
    
    
def isolate(expr):
    expr2 = []
    for j in expr:
        for k in j:
            if(k[3]=="False"):
                expr2.append(k)
    return expr2

def create_final_array(P,K):
    
    k=0
    k1=0
    E=[]
    for i in P:
        k+=1
    for i in K:
        if( i[1] in E):
            ;
        else:
            E.append(i[1])
            k1+=1
              
    h = 2
    m=0
    Matrix = [[0 for x in range(k+2)] for y in range(k1+1)] 
    for i in P:
        Matrix[0][h]=i[2]
        h+=1
    for jj in E:
        if(m%2==0): Matrix[int(m/2)+1][0]=jj
        else: Matrix[int(m/2)+1][1]=jj
        m+=1
    
    
    
    return E

def LastButNotLeast(E,var):
    f=""
    for i in E:
        k=0
        while(k<len(var)-1):
            if( i[k] == '1' ):
                f+=var[k]
                f+='&'
            k+=1
        if(i[len(var)-1]=='1'):
            f+=var[k]
        f+='|'
    f = f[:-1]
    return f

def shorten_expr(expr):
    
    if not ValidateExpr(expr):
        print("Invalid expression!")
        return
    
    var, ops = SeparateVarOp(expr)
    
    table1 = CreateMArray(expr)
    
    table2 = proceed3(expr)
    
    table3 = create_final_array(table1,table2)    
    
    return LastButNotLeast(table3,var)
