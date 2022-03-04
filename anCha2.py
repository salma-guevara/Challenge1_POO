import animales

menu = {
    '1':'Loro',
    '2':'Perro',
    '0':'Exit'
}

class Animal:
    dibujo=''
    
    def __init__(self, dibujo):
        self.dibujo = dibujo
        
    def mostrar_animal(self):
        print(self.dibujo)

#Ejecución principal
if __name__ == '__main__':
    
    for k,i in menu.items():
        print(f'{k}:{i}')
    
    loro = Animal(animales.loro)
    perro = Animal(animales.perro)
    
    while True:
        op = int(input('Elige qué animal quieres ver: ')) #building function
        
        if op == 0:
            #El usuario quiere dejar de jugar
            print("Que el código te acompañe")
            break
        elif op == 1:
            #Imprimir animal
            loro.mostrar_animal()
        elif op == 2:
            perro.mostrar_animal()
        else:
            #Opcion invalida
            print('Opción inválida, intentelo nuevamente')
            for k,i in menu.items():
                print(f'{k}:{i}')
      