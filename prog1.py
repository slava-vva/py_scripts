from types import SimpleNamespace

print("Hu PY!")

class Calc:
    res = 0
    def calculation(self, val1, val2, type):
        if type == "mult":
            res = val1 * val2
        if type == "sum":
            res = val1 + val2
        if type == "sub":
            res = val1 - val2
        if type == "div":
            res = val1 / val2
        if type == "pow":
            res = val1**val2

        print(f"result of {type} is {res}")


mathtypes = SimpleNamespace(mult="mult", sum="sum", sub="sub", div="div", pow="pow")

class Optypes:
    mult = "mult"
    sum = "sum"
    sub = "sub"
    div = "div"
    pow = "pow"

clc = Calc()
while True:
    val1 = float(input("Enter the first val1:"))
    val2 = float(input("Enter the second val2:"))
    optype = input("Enter the type of operation:")

    clc.calculation(val1=val1, val2=val2, type=optype)
    
    if (input('Do you want to continue? y/n: ') == 'n'):
        break
