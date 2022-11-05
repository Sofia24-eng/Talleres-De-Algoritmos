while True:
    datos=input()
    (X,M)=datos.split(" ")
    X=int(X)
    M=int(M)
    if(X==0 and M==0):
        break
    print(X*M)