
function convertToRoman() {
    let num = document.getElementById("entrada")
    console.log(num)
    let restricciones = [[1000, 4000, "M"], [900, 1000, "CM"], [500, 900, "D"], [400, 500, "CD"], [100, 400, "C"], [90, 100, "XC"], [50, 90, "L"], [40, 50, "XL"], [10, 40, "X"], [9, 10, "IX"], [5, 9, "V"], [4, 5, "IV"], [1, 4, "I"]]
    let numero=[num.value,""]
    let restriccion=[]
    let n

//let numero=map()

    for (var i in restricciones) {
        restriccion=restricciones[i]
        if (numero[0] >= restriccion[0] && numero[0] < restriccion[1] ) {
            n = parseInt(numero[0]/restriccion[0]); 
            numero[0]=numero[0]-n*restriccion[0];
            numero[1]=numero[1].concat(restriccion[2].repeat(n))  ;
        }
    }
    console.log(numero[1]);
    setTimeout(function(){
        document.getElementById("salida").innerHTML=numero[1].toString();
    },3000)
    

 return numero[1];
}



convertToRoman(3444)