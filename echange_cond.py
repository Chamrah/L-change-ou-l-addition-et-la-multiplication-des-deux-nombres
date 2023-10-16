#Programme qui échange les contenus de deux données numérique si elles sont de même signe, sinon il met la somme des deux dans la première donnée et leur produit dans la seconde.
n1=int(input("Entrer le premier nombre :"))
n2=int(input("Entrer le deuxieme nombre :"))
a=0
c=0
d=0
if(n1>0 and n2>0 or n1<0 and n2<0):
    a=n1
    n1=n2
    n2=a
    print(f"le premier nombre est {n1} et le deuxieme nombre est {n2}")
else:
    c=n1+n2
    d=n2*n1
    n1=c
    n2=d
    print(f"L'addition des deux nombres est : {n1} et le produit des deux nombres est : {n2}")


