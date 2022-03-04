import animales

menu = {
    '1':'Loro',
    '2':'Perro',
    '0':'Exit'
}

class Animal:
    loro=0
    perro=0
    
    animales_lista = {
        1:animales.loro,
        2:animales.perro
    }
    
    def __init__(self,loro,perro):
        self.loro = loro
        self.perro = perro

    def mostrar_animal(self,op):
        print(self.animales_lista[op])

#Ejecución principal
if __name__ == '__main__':
    
    for k,i in menu.items():
        print(f'{k}:{i}')
    
    op = int(input('Elige qué animal quieres ver: ')) #building function
    
    while True:
        
        if op == 0:
            #El usuario quiere dejar de jugar
            print("Que el código te acompañe")
            break
        elif op == 1:
            #Imprimir animal
            print(animales.loro)
        elif op == 2:
            print(animales.perro)
        else:
            #Opcion invalida
            print('Opción inválida, intentelo nuevamente')
            for k,i in menu.items():
                print(f'{k}:{i}')
            
        op = int(input('Elige qué animal quieres ver: '))