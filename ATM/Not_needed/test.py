'''
 def  fun_call(str,*fins):
    


    fins=list(fins)

    fins.append([print,"omar"])
    
    fins=tuple(fins)
    p(*fins)
    


def p(*arg):
    for i in arg:
        print(i)

fun_call("mohamed",[print,"mohamed"],[print,"ahmed"],[print,"aaa"])
'''



def call_fun(*arg):
    f=list(arg)
    print(f.pop(0))
    
    
call_fun(print)