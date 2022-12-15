from kb import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC

from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

media = MediaKeys()
layers_ext = Layers()

keyboard.extensions = [media]
keyboard.modules = [layers_ext]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

MAIN = KC.TO(0) 
NAV = KC.TT(1)
SYMBOL = KC.LT(2, KC.SPC)

UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)

keyboard.keymap = [

     # Layer _MAIN
     # ,-----------------------------------------------------------------------------------.
     # | Tab  |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Bksp |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # | Esc  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   ;  |  "   |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # | Shift|   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   .  |  /   |Enter |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # | Caps |L_Ctrl|  Alt |  GUI |NavLr |  cmd?|      |Sc/Sym| PadLr|PrntSc|Insert|  \   |
     # `-----------------------------------------------------------------------------------'
    [  #MAIN
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.BSPC,
        KC.ESC,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.ENT ,
        KC.CAPS, KC.LCTL, KC.LALT, KC.LGUI, NAV,     KC.SPC,  KC.SPC,  SYMBOL,  KC.LEFT, KC.PSCR, KC.INS,  KC.BSLASH
    ],

     # Layer _NAV
     # ,-----------------------------------------------------------------------------------.
     # |   `  |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  | Undo | Cut  | Copy |Paste |  Del |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |      | Home | PgDn | PgUp | End  |      |      | Left | Up   | Down | Right|      |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |  F7  |  F8  |  F9  | F10  | F11  | F12  |      |      |      |      |      |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # |      |      |      |      |LShift|MainLr| Space| Shift| Left |  Up  | Down | Right|      
     # `-----------------------------------------------------------------------------------'
     
    [  #NAV 
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   UNDO, CUT, COPY, PASTE, KC.BSPC,
        XXXXXXX, KC.HOME, KC.PGDN, KC.PGUP, KC.END,  XXXXXXX, XXXXXXX, KC.LEFT,       KC.UP,         KC.DOWN,       KC.RIGHT,      XXXXXXX,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  XXXXXXX,       XXXXXXX,       XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, KC.LCTL, KC.LSFT, MAIN, KC.SPC, KC.RSFT, KC.LEFT, KC.UP, KC.DOWN, KC.RIGHT
    ],
    [  #SYMBOL
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        KC.DEL,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   KC.UNDS, KC.PLUS, KC.LCBR, KC.RCBR, KC.PIPE,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  XXXXXXX, XXXXXXX, KC.HOME, KC.END,  XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.MNXT, KC.VOLD, KC.VOLU, KC.MPLY
    ] 
]  
   
if __name__ == '__main__':
    keyboard.go()