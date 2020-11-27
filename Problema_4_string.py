a=input("Introduceti un sir ")
b=input("Introduceti un sir ")
c=input("Introduceti un sir ")
d=input("Introduceti un sir ")   
if len(a)<3 or len(b)<3 or len(c)<3 or len(d)<3:
    print("Eroare")
elif len(a)>=3 and len(b)>=3 and len(c)>=3 and len(d)>=3:
    if len(d)>=3:
        n=round(len(d)/2)   
    x=a[:2]+b[0]+c[:3]+d[:n]
    y=a+' '+b+' '+c+' '+d+'. '+x
    print(y)
    print(ord('z'))