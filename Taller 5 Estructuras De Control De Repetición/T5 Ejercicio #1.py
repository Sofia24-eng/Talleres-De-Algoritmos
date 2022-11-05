print("K Debe Ser Menor Que N")
K=int(input("Valor De K: "))
N=int(input("Valor De N: "))
i=0
while (K<N):
  if(N>=K):
    i=i+1
  else:
    i=0
  ValorDeK=N-i
  x=N-K
  if(i==x):
    print("En Total Se Hicieron",i,"Repeticiones Para Hallar El Valor De K")
  if(ValorDeK==K):
    print("El Valor De K Es:",ValorDeK)
  if(ValorDeK<K):
    break