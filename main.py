import pyxel

SCREEN_X = 20
SCREEN_Y = 6

class App:
    def __init__(self):
        #変数たちを定義
        self.VALUE_1 = 0
        self.VALUE_2 = 0
        self.VALUE_3 = 0
        self.SPACE_COUNT = 0
        self.ALLOW_SLOT_1 = False
        self.ALLOW_SLOT_2 = False
        self.ALLOW_SLOT_3 = False
        #画面サイズとか重要なやつ定義
        pyxel.init(SCREEN_X,SCREEN_Y)
        pyxel.run(self.update, self.draw)
    def update(self):
        if self.ALLOW_SLOT_1:
            self.VALUE_1 = self.VALUE_1 + 1
        if self.VALUE_1 == 10:
            self.VALUE_1 = self.VALUE_1 -10
        if self.ALLOW_SLOT_2:
            self.VALUE_2 = self.VALUE_2 + 1
        if self.VALUE_2 == 10:
            self.VALUE_2 = self.VALUE_2 -10
        if self.ALLOW_SLOT_3:
            self.VALUE_3 = self.VALUE_3 + 1
        if self.VALUE_3 == 10:
            self.VALUE_3 = self.VALUE_3 -10
        if pyxel.btnp(pyxel.KEY_SPACE):
            if self.SPACE_COUNT == 0:
                self.ALLOW_SLOT_1 = not self.ALLOW_SLOT_1
                self.ALLOW_SLOT_2 = not self.ALLOW_SLOT_2
                self.ALLOW_SLOT_3 = not self.ALLOW_SLOT_3
                self.SPACE_COUNT = self.SPACE_COUNT + 1
            elif self.SPACE_COUNT == 1:
                self.ALLOW_SLOT_1 = not self.ALLOW_SLOT_1
                self.SPACE_COUNT = self.SPACE_COUNT + 1
            elif self.SPACE_COUNT == 2:
                self.ALLOW_SLOT_2 = not self.ALLOW_SLOT_2
                self.SPACE_COUNT = self.SPACE_COUNT + 1
            elif self.SPACE_COUNT == 3:
                self.ALLOW_SLOT_3 = not self.ALLOW_SLOT_3
                self.SPACE_COUNT = 0       
    def draw(self):
        pyxel.cls(0)
        pyxel.text(2,0,str(self.VALUE_1),7)
        pyxel.text(8,0,str(self.VALUE_2),7)
        pyxel.text(14,0,str(self.VALUE_3),7)
App()
