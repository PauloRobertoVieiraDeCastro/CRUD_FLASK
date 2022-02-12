class Oleo:
    def __init__(self,corrente,api,nafta,diesel,gasoleo,s,n,tan,ide=None):
        self.ide = ide
        self.corrente = corrente
        self.api = api
        self.nafta = nafta
        self.diesel = diesel
        self.gasoleo = gasoleo
        self.s = s
        self.n = n
        self.tan = tan

def cria_oleo_com_tupla(tupla):
    return Oleo(tupla[1], tupla[2], tupla[3], tupla[4], tupla[5], tupla[6], tupla[7], tupla[8], ide=tupla[0])

a = ((1,'Alagoano', 40.9, 25.22, 30.08, 44.7, 0.039, 0.039, 0.1),(2,'Alagoano', 40.9, 25.22, 30.08, 44.7, 0.039, 0.039, 0.1))
print(list(map(cria_oleo_com_tupla, a))[0].api)    
