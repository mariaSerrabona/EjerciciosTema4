#Escriba, usando comparaciones, un algoritmo que muestre
# el estado del agua (hielo, líquido, vapor) en función de su temperatura.

#definimos un método que evalúe los casos dependiendo de la temperatura
def estado_agua (temperatura):
    if temperatura <=0:
        return ('el agua se encuentra en estado sólido')
    elif temperatura >0 and temperatura <100:
        return ('el agua se encuentra en estado líquido')
    else:
        return ('el agua se encuentra en estado gaseoso')


temperatura=input('introduzca la temperatura del agua: ')
temperatura=int(temperatura)
estado_agua(temperatura)

