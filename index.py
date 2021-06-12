mil=[1000,4000,"M"]
ncientos=[900,1000,"CM"]
qinientos=[500,900,"D"]
cuacientos=[400,500,"CD"]
cien=[100,400,"C"]
nventa=[90,100,"XC"]
cncuenta=[50,90,"L"]
cuarenta=[40,50,"XL"]
diez=[10,40,"X"]
nueve=[9,10,"IX"]
cinco=[5,9,"V"]
cuatro=[4,5,"IV"]
uno=[1,4,"I"]

restricciones=[[1000,4000,"M"],[900,1000,"CM"],[500,900,"D"],[400,500,"CD"],[100,400,"C"],[90,100,"XC"],[50,90,"L"],[40,50,"XL"],[10,40,"X"],[9,10,"IX"],[5,9,"V"],[4,5,"IV"],[1,4,"I"]]

numero=[3999,""]

def romaconv(numero,restriccion):
    if(numero[0]>=restriccion[0] and numero[0]<restriccion[1]):
        n=int(numero[0]/restriccion[0])
        numero[0]=numero[0]-n*restriccion[0]
        numero[1]=numero[1]+restriccion[2]*n
        return (numero)
    else:
        return(numero)

def romaconvp(num):
    numero=[num,""]
    restricciones=[[1000,4000,"M"],[900,1000,"CM"],[500,900,"D"],[400,500,"CD"],[100,400,"C"],[90,100,"XC"],[50,90,"L"],[40,50,"XL"],[10,40,"X"],[9,10,"IX"],[5,9,"V"],[4,5,"IV"],[1,4,"I"]]
    for i in restricciones:
        restriccion=i
        if(numero[0]>=restriccion[0] and numero[0]<restriccion[1]):
            n=int(numero[0]/restriccion[0])
            numero[0]=numero[0]-n*restriccion[0]
            numero[1]=numero[1]+restriccion[2]*n
        else:
            numero=numero
    num=numero[1]
    return(numero[1])

restricciones=[[1000,4000,"M"],[900,1000,"CM"],[500,900,"D"],[400,500,"CD"],[100,400,"C"],[90,100,"XC"],[50,90,"L"],[40,50,"XL"],[10,40,"X"],[9,10,"IX"],[5,9,"V"],[4,5,"IV"],[1,4,"I"]]
for i in restricciones:
        print(i)