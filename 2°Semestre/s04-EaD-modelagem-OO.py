# Definição da classe
class Visitante:
 def __init__(self, cpf, nome):
        """
        Construtor
        Args:
        cpf: identificação única do visitante
        nome: nome do visitante
        """
        self.cpf = cpf
        self.nome = nome

# Exemplo de uso
visitante = Visitante(0, "Doctor Who")
print(visitante.nome)

# Definição da classe
class CifradorLinguaDoPê:
    def cifrar(self, mensagem_ptbr):
        """
        Cifra uma mensagem em pt-BR para a língua do Pê
        Args:
        mensagem_ptbr: mensagem em português
        """
        # Faz a cifra da mensagem (não precisa implementar)
        return "PÊJoPÊão PÊgosPÊta PÊde PÊcoPÊmer PÊfeiPÊjão PÊe PÊfaPÊriPÊnha."

# Exemplo de uso
cifradorP = CifradorLinguaDoPê()
print(cifradorP.cifrar("João gosta de comer feijão e farinha."))

"""
A partir dos exemplos acima, fazer a modelagem OO das classes a seguir. REFLITA sobre os atributos e os métodos que cada classe deve ter. Considere somente aquilo que é mais essencial nas classes (você é livre para julgar). NÃO UTILIZE RECURSOS NÃO VISTOS EM AULA COMO DECORATORS E PROPERTIES porque estão fora dos objetivo de aprendizagem deste momento. Não é necessário criar uma implementação para os métodos. Utilize prints e a palavra-chave pass para representar a implementação. É fundamental documentar os métodos. Ofereça uma descrição sucinta para o propósito do método e cada parâmetro. Não é necessário utilizar getters e setters.
"""

class Televisão:
    def __init__(self, canal_atual, volume):
        '''
        Construtor:
        Canal atual
        Volume 
        Ir para o próximo canal
        Voltar ao canal anterior
        aumentar o volume e diminuí-lo
        funções básicas
        '''
        self.canal_atual = 0
        self.volume = 0
    def prox_canal(self, val):
        self.canal_atual += 1
    def canal_anterior(self, val):
        self.canal_atual -= 1
    def aumentar_vol():
        self.volume += 1
    def diminuir_vol():
        self.volume -= 1
    pass
tv = televisao(4, 55)
tv = prox_canal()
tv = canal_anterior()
tv = aumentar_vol()
tv = diminuir_vol()

class HomeTheater:
    def (self, volume):
        self.volume = 0
    def aumentar_vol():
        self.volume += 1
    def diminuir_vol():
        self.volume -= 1
    pass
ht = HomeTheater()
ht = aumentar_vol()
ht = diminuir_vol()
class Microondas:
    def __init__(self, timer, potência):

    pass

class TelaMonitor:
    def __init__(self, brilho, porta_hdmi):
        '''
        Construtor 
        '''
        self.brilho = 50
        self.porta_hdmi = 1


    pass

class Elevador:
    def __init__(self, andar, direção, emergência):

    pass

class ConversorDeTemp:
    def celsius2fahrenheit(self, temp_C):
        '''
        Converte uma temperatura de Celsius para Fahrenheit
        Args:
            temp_C - Temperatura em celsius
        '''
        return (temp_C * 9/5) / 32
convert = ConversorDeTemp()
print(convert.celsius2fahrenheit(30))

class Herói:
    def __init__(self, nome, habilidade):
        '''
        Construtor
        Atributos: 
        Nome do herói
        Habilidade ou poder do herói
        '''
        self.nome = nome
        self.habilidade = habilidade    
    pass
heroi1 = Herói(Batman, dinheiro infinito)
print(heroi1)
class Funcionária:
    def __init__(self, função, nome)

    pass

class Professora:
    def __init__(self, nome, materia):

    pass

class Médica:
    def __init__(self, especialidade, nome )
    pass

class Estudante:
    pass

class Termômetro:

    pass

class Fogão:
    def __int__(self, bocas, nivel_chamas):
        def chama(self, baixa, media, alta):
            self.nivel_chamas = baixa or media or alta
        self.bocas = bocas
        if (bocas < 1):
            raise ValueError('Isso não é um fogão')
        elif(bocas > 6):
            raise ValueError('Quê isso! ')
    pass

class Carro:
    pass

class Impressora:
    pass

class Celular:
    pass

class FoneDeOuvido:
    pass

class RelógioEsperto:
    pass

class MarcaPasso:
    pass

class AferidorDePressãoArterial:
    pass

class ControleRemotoDePortão:
    pass

class TelefoneAnalógico:
    pass

class PianoElétrico:
    pass

class Temperatura:
    pass

class TabelaDePreçoDeCarros:
    pass

class Produto:
    pass

class PesoDeBagagem:
    pass

class Balança:
    pass

class CadeiraDeMassagem:
    pass
