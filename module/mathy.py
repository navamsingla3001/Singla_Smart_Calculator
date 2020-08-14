responses=["Welcome to Smart Calculator","My Name is Singla Calculator","Thanks","Sorry, this is beyond my ability"]

def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1
def hcf(a,b):
    h=a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def power(a,b):
    return a**b
def end():
    print(responses[2])
    input("Please Enter key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"SUBTRACT":subtract,"MINUS":subtract,
            "MULTIPLY":multiply,"MULTIPLICATION":multiply,"RAISE":power,"POWER":power, "INTO":multiply,"DIVIDE":divide,"DIVIDATION":divide,"BY":divide, "LCM":lcm,"HCF":hcf}
commands={"NAME":myname,"INTRODUCE":myname,"END":end,"CLOSE":end,"EXIT":end}
            
