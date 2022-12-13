def calcular_par_impar(num1, num2):
    num1 = num1
    num2 = num2
    soma = num1 + num2
    resultado = soma%2
    par_impar = ""
    if resultado == 0:
        par_impar = "par"
    elif resultado == 1:
        par_impar = "impar"
    
    return par_impar 
