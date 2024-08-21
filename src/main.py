print('oi')
bolas = "https://i.imgur.com/rgTSap6.png"
amarelo = 'https://i.imgur.com/FwCTxwE.png'
azul = 'https://i.imgur.com/ERl5wQU.png'
rosa = 'https://i.imgur.com/goMGtsi.png'
vermelho = 'https://i.imgur.com/hNCB7v3.png'
palito = 'https://imgur.com/20BUCM6.png'
from browser import html

class Palito:
    def __init__(self):
        def movepa(ev):
            self.destino <= dpa

        pa = html.IMG(src=palito, width="40px").bind("click", movepa)
        dpa = html.DIV(src=pa, style="position:absolute; left:105px; top:100px;")
    def mostrap(self):
        return [self.destino, self.palito]
class Torre:
    def __init__(self):

        #movimento dos palitos
        def move2(ev):
            self.palito2 <= bl
            self.palito2 <= bla
            self.palito2 <= blz
            self.palito2 <= blr

        def move3(ev):
            self.origem <= bl
            self.origem2 <= bla
            self.origem3 <= blz
            self.origem4 <= blr

        def move4(ev):
            self.palito3 <=bl
            self.palito3 <=bla
            self.palito3 <=blz
            self.palito3 <=blr

        #movimento das bolas de volta a origem, no primeiro palito
        def move(ev):
            self.destino <= bl
        def movea(ev):
            self.destino <= bla
        def movez(ev):
            self.destino <= blz
        def mover(ev):
            self.destino <= blr


        #posição mão
        dm = html.DIV(Id="a_mao", style="position:absolute; left:155px; top:10px;")

#criar classe mão para verificar se está cheia

        #palitos
        pa = html.IMG(src=palito, width="40px").bind("click", move3)
        dpa = html.DIV(src=pa, style="position:absolute; left:105px; top:100px;")
        pa2 = html.IMG(src=palito, width="30px").bind("click", move2)
        dpa2 = html.DIV(src=pa2, style="position:absolute; left:250px; top:175px;")
        pa3 = html.IMG(src=palito, width="20px").bind("click", move4)
        dpa3 = html.DIV(src=pa3, style="position:absolute; left:375px; top:250px;")

        #bolas
        bl = html.IMG(Id="bola_vermelha", src=vermelho, width="80px").bind("click", move)
        dlv = html.DIV(Id="a_bolav", style="position:absolute; left:85px; top:328px;")
        bla = html.IMG(Id="bola_amarela", src=amarelo, width="80px").bind("click", movea)
        dla = html.DIV(Id="a_bolaa", style="position:absolute; left:85px; top:250px;")
        blz = html.IMG(Id="bola_azul", src=azul, width="80px").bind("click", movez)
        dlz = html.DIV(Id="a_bolaz", style="position:absolute; left:85px; top:174px;")
        blr = html.IMG(Id="bola_rosa", src=rosa, width="80px").bind("click", mover)
        dlr = html.DIV(Id="a_bolar", style="position:absolute; left:85px; top:97px;")


        self.destino = dm
        self.origem = dlv
        self.origem2 = dla
        self.origem3 = dlz
        self.origem4 = dlr
        self.palito = dpa
        self.palito2 = dpa2
        self.palito3 = dpa3
        dpa <= pa
        dpa2 <= pa2
        dpa3 <= pa3
        dlv <= bl
        dla <= bla
        dlz <= blz
        dlr <= blr
    def mostra(self):
        return [self.palito, self.palito2, self.palito3, self.destino, self.origem, self.origem2, self.origem3, self.origem4]


def torre():
    return Torre().mostra()
# def palito():
#     return Palito().mostrap()


