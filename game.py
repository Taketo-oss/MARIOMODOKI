import pyxel

class App:
    def __init__(self):
        # 画面サイズの設定 (マリオ風に少し横長)
        pyxel.init(160, 120, title="Pyxel Mario Baseline")
        
        # プレイヤーの初期状態
        self.x = 20
        self.y = 100
        self.dy = 0
        self.is_jumping = False
        
        # スコア (一時的なもの)
        self.score = 0
        
        # 敵やコインの代わり（簡易的）
        self.coin_x = 80
        self.coin_y = 90
        self.is_coin_active = True

        pyxel.run(self.update, self.draw)

    def update(self):
        # 1. 左右移動
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x = max(self.x - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x = min(self.x + 2, pyxel.width - 8)

        # 2. ジャンプ処理
        if pyxel.btnp(pyxel.KEY_SPACE) and not self.is_jumping:
            self.dy = -6
            self.is_jumping = True

        # 3. 重力計算
        self.y += self.dy
        self.dy = min(self.dy + 0.5, 8) # 落下速度の制限

        # 4. 床との当たり判定 (y=100を床とする)
        if self.y >= 100:
            self.y = 100
            self.dy = 0
            self.is_jumping = False

        # 5. コイン取得判定
        if (self.is_coin_active and 
            abs(self.x - self.coin_x) < 8 and 
            abs(self.y - self.coin_y) < 8):
            self.score += 100
            self.is_coin_active = False # 一度取ったら消える

    def draw(self):
        pyxel.cls(12) # 背景色 (水色)

        # 床の描画
        pyxel.rect(0, 108, 160, 12, 3) 

        # プレイヤーの描画 (マリオの代わり)
        # 本来はpyxel.bltでドット絵を表示しますが、一旦四角形で
        pyxel.rect(self.x, self.y, 8, 8, 9) 

        # コインの描画
        if self.is_coin_active:
            pyxel.circ(self.coin_x, self.coin_y, 3, 10)

        # スコア表示
        pyxel.text(5, 5, f"SCORE: {self.score}", 7)
        pyxel.text(5, 15, "SPACE: JUMP / LEFT,RIGHT: MOVE", 7)

if __name__ == "__main__":
    App()
