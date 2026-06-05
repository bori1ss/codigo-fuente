saldo=5
total_prodeuctos=0
a=0
while a==0 and saldo>=1.50 and total_prodeuctos<3:
    opcion=int(input('MAQUINA EXPENDEDORA \n 1.-PAPAS (1.50) \n 2.-CHOCOLATE (2.00) \n 3.- REFRESCO (2.50) \n 4.- SALIR \n'))
    if opcion==1 or (opcion==2 and saldo>=2.00) or (opcion==3 and saldo>=2.50):
        if opcion==1:
            saldo-=1.50
        elif opcion==2: 
            saldo-=2.00
        else:
            saldo -=2.50
        total_prodeuctos+=1
        print(f'Comprado \n Saldo restante: {saldo}')
    elif opcion==4:
        print('Saliendo')
        a+=1
    else :
        print('Opcion invalida')
print(f'Total de productos comprados: {total_prodeuctos}')
