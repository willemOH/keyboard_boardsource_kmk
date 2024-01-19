from kb import KMKKeyboard
from kmk.extensions.media_keys import MediaKeys
from kmk.keys import KC


from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap

modtap = ModTap()

keyboard = KMKKeyboard()

media = MediaKeys()
layers_ext = Layers()

keyboard.extensions = [media]
keyboard.modules = [layers_ext]
keyboard.modules.append(modtap)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

MAIN = KC.TO(0) 
NAV = KC.MO(1)
SYMBOL = KC.LT(2, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=None)
PAD = KC.TG(2)                                                 
SYS = KC.MO(3)

UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)             

keyboard.keymap = [

     # Layer _MAIN
     # ,-----------------------------------------------------------------------------------.
     # | Tab  |   Q  |   W  |   E  |   R  |   T  |   Y  |   U  |   I  |   O  |   P  | Bksp |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # | Esc  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   ;  |  '   |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # | PAD  |   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   .  |  /   |  \   |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # | SYS  | Caps |      |  Ctrl|  NAV | GUI  |enter |Sp/SYM| Shift| Alt  |Insert|PrnScn|
     # `-----------------------------------------------------------------------------------' 
    [  #MAIN
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R, KC.T,    KC.Y,   KC.U,   KC.I,     KC.O,    KC.P,    KC.BSPC,
        KC.ESC,  KC.A,    KC.S,    KC.D,    KC.F, KC.G,    KC.H,   KC.J,   KC.K,     KC.L,    KC.SCLN, KC.QUOT,
        PAD,     KC.Z,    KC.X,    KC.C,    KC.V, KC.B,    KC.N,   KC.M,   KC.COMM,  KC.DOT,  KC.SLSH, KC.BSLS,      
        SYS,     KC.CAPS, XXXXXXX, KC.LCTL, NAV,  KC.LGUI, KC.ENT, SYMBOL, KC.LSFT,  KC.LALT, KC.INS,  KC.PSCR 
    ],                              
                                                                                            
     # Layer _NAV
     # ,-----------------------------------------------------------------------------------.
     # | Tab  |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  | Undo | Cut  | Copy |Paste | Del  |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |  Esc | Home | PgDn | PgUp | End  |      |      | Left | Down | Up   | Right| Bksp |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |  F7  |  F8  |  F9  | F10  | F11  | F12  | vol+ | vol- | mute |plypau|      |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # | SYS  | Caps |      |  Ctrl|  NAV | GUI  |enter |Sp/SYM| Shift| Alt  |Insert|PrnScn|
     # `-----------------------------------------------------------------------------------'
           
    [  #NAV 
        KC.TAB,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   UNDO,    CUT,     COPY,    PASTE,    KC.DEL,
        KC.ESC,  KC.HOME, KC.PGUP, KC.PGDN, KC.END,  XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN,   KC.UP, KC.RIGHT, KC.BSPC,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.VOLU, KC.VOLD, KC.MUTE, KC.MPLY,  XXXXXXX,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,  _______
    ],
    
     # Layer _SYMBOL/PAD
     # ,-----------------------------------------------------------------------------------.
     # |   ~  |   1  |   2  |   3  |   !  |   #  |   $  |   %  |   [  |   ]  |   {  |  }   |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |   `  |   4  |   5  |   6  |   =  |   *  |   +  |   -  |   (  |   )  |   :  |  "   |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # | MAIN |   7  |   8  |  9   |   0  |   &  |   |  |   _  |   <  |   >  |   ?  |  @   |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # | SYS  | Caps |   ^  |  Ctrl|  NAV | GUI  |enter |Sp/SYM| Shift| Alt  |Insert|PrnScn|
     # `-----------------------------------------------------------------------------------'
     
    [  #PAD                                                     
       KC.TILD, KC.N1, KC.N2, KC.N3, KC.EXLM, KC.HASH, KC.DLR,  KC.PERC, KC.LBRC, KC.RBRC, KC.LCBR, KC.RCBR,
        KC.GRV, KC.N4, KC.N5, KC.N6, KC.EQL,  KC.ASTR, KC.PLUS, KC.MINS, KC.LPRN, KC.RPRN, KC.COLN, KC.DQUO,
        MAIN,   KC.N7, KC.N8, KC.N9, KC.N0,   KC.AMPR, KC.PIPE, KC.UNDS, KC.LABK, KC.RABK, KC.QUES, KC.AT,
        _______, _______, KC.CIRC, _______, _______, _______, _______, _______, _______, _______, _______,  _______
    ], 
    
     # Layer _SYS
     # ,-----------------------------------------------------------------------------------.
     # | linux|windws| mac  | noop |      |      |      |      |      |      |      |      |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |   W  |      |      |      |      |      |      |      |      |      |      |      |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |      |      |      |      |      |      |      |      |      |      |      |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # |      |      |      |      |      |      |      |      |      |      |      |      |
     # `-----------------------------------------------------------------------------------'
     
    [  #SYS
        KC.UC_MODE_LINUX, KC.UC_MODE_WINC, KC.UC_MODE_MACOS, KC.UC_MODE_NOOP, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        KC.W,             XXXXXXX,         XXXXXXX,          XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,          XXXXXXX,         XXXXXXX,          XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX,          XXXXXXX,         XXXXXXX,          XXXXXXX,         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    ]  
]  
   
if __name__ == '__main__':
    keyboard.go()
