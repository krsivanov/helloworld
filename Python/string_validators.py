str = str(input())
def f(x,str):
    res = False
    for i in str:
        res = res or getattr(i,x)()
    return res

print(f("isalnum",str))
print(f("isalpha",str))
print(f("isdigit",str))
print(f("islower",str))
print(f("isupper",str))

