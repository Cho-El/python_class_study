def function_doubleasterix(**keywordargs):

    print("The keys in the kwargs dicionary are -", keywordargs.keys())
    print("The values in the kwargs dicionary are -", keywordargs.values())

    print("--The key value assignment in the 'keywordargs' dictionary are as follows--")
    for key, value in keywordargs.items():
        print ("%s == %s" %(key, value))

function_doubleasterix(SNo001 ='Alex', SNo002 ='Tom')


def functiondef(a,b):
    e = {**a,**b} # **은 딕셔너리 언패킹한 값들을 set에 저장
    print(type(e))
    return e
varlist = ["Tom","John","Alice"]
vardict = {'a':"Tom",'b':"John",'c':"Alice"}
vardict2 = {'d':"Tm",'e':"Jon",'f':"Alic"}

print(functiondef(vardict,vardict2))

def start(a, *args):
    print('sssss')
    return a(args)

print(start(sum, 1, 2))
