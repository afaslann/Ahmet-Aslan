class Tenis():
    turnuva = "wimbeldon"

    def __init__(self, oyuncuadi, yas, galibiyet):
        self.oyuncuadi = oyuncuadi
        self.yas = yas
        self.galibiyet = galibiyet

    def mac_anlatimi(self):
        return "İşte {} geliyor, {} yasindaki oyuncu {} tane wimbeldon final kazandi".format(
            self.oyuncuadi,
            self.yas,
            self.galibiyet)
karsilasma2 = Tenis('alcaraz', 21, 2 )
print(karsilasma2.mac_anlatimi())
