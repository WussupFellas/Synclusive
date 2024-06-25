
class Elevador:

    def __init__(self,andar_atual,capacidade_atual,andar_limite,capacidade_limite):
        self.andar_atual = andar_atual
        self.capacidade_atual = capacidade_atual
        self.andar_limite = andar_limite
        self.capacidade_limite = capacidade_limite

    def subir(self,andar):
        if andar < self.andar_atual:
           print("Erro: O elevador não pode subir para um andar inferior ao atual")
        elif andar > self.andar_limite:
            print("Erro: O elevador não pode subir para um andar superior ao limite")
        else:
            self.andar_atual = andar

    def descer(self,andar):
        if andar > self.andar_atual:
           print("Erro: O elevador não pode descer para um andar superior ao atual")
        elif andar < 0:
            print("Erro: O elevador não pode descer para um andar inferior ao limite")
        else:
            self.andar_atual = andar
    
    def entra(self):
        if self.capacidade_atual < self.capacidade_limite:
            self.capacidade_atual += 1
        else:
            print("Erro: O elevador está cheio")

    def sai(self):
        if self.capacidade_atual > 0:
            self.capacidade_atual -= 1
        else:
            print("Erro: O elevador está vazio")


elevadorGloria = Elevador(0,0,10,5)
elevadorEmpireState = Elevador(0,0,100,10)

for i in range(7):
    elevadorGloria.entra()

for i in range(3):
    elevadorGloria.sai()

for i in range(2):
    elevadorGloria.entra()

elevadorGloria.subir(10)
elevadorGloria.descer(5)
elevadorGloria.descer(7)
