class Cuadrado:
    def __init__(self,dimension):
        self.dimension = dimension

    def ingresodatos(self):
        self.dimension = int(input("Ingrese la dimensión N >= 2 del cuadrado a dibujar: "))

    def grafico(self):
        #Lado superior
        n = self.dimension
        for i in range(n+1):
            print('* ', end='')
        print()

        #Partes laterales
        j = 1
        while j <= n - 2:
            for k in range(n):
                if k == 0:
                    print('* ', end='')
                elif k == n-1:
                    print('  *', end='')
                else:
                    print('  ', end='')
            print()
            j += 1

        #Lado inferior
        i = 0
        while i < n + 1:
            print('* ', end='')
            i += 1

