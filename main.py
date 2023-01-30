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
     # | Esc  |   A  |   S  |   D  |   F  |   G  |   H  |   J  |   K  |   L  |   ;  |  "   |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # | PAD  |   Z  |   X  |   C  |   V  |   B  |   N  |   M  |   ,  |   .  |  /   |Enter |
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
     # | Tab  |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  | Undo | Cut  | Copy |Paste | Bksp |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |  Esc | Home | PgDn | PgUp | End  |      |      | Left | Down | Up   | Right|      |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |  F7  |  F8  |  F9  | F10  | F11  | F12  | vol+ | vol- | mute |plypau|      |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # | SYS  | Caps |      |  Ctrl|  NAV | GUI  |enter |Sp/SYM| Shift| Alt  |Insert|PrnScn|
     # `-----------------------------------------------------------------------------------'
           
    [  #NAV 
        KC.TAB,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   UNDO,    CUT,     COPY,    PASTE,    KC.BSPC,
        KC.ESC,  KC.HOME, KC.PGUP, KC.PGDN, KC.END,  XXXXXXX, XXXXXXX, KC.LEFT, KC.DOWN,   KC.UP, KC.RIGHT, XXXXXXX,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.VOLU, KC.VOLD, KC.MUTE, KC.MPLY,  XXXXXXX,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,  _______
    ],
    
     # Layer _SYMBOL/PAD
     # ,-----------------------------------------------------------------------------------.
     # |      |   0  |   1  |   2  |   3  |   $  |   #  |   +  |   *  |   {  |   }  | Bksp |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |  Esc |   ~  |   4  |   5  |   6  |   @  |   !  |   -  |   =  |   (  |   )  |  \   |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |   `  |   7  |  8   |   9  |   %  |   &  |   _  |   /  |   [  |   ]  |Enter |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # | SYS  | Caps |      |  Ctrl|  NAV | GUI  |enter |Sp/SYM| Shift| Alt  |Insert|PrnScn|
     # `-----------------------------------------------------------------------------------'
     
    [  #PAD                                                     
        XXXXXXX, KC.N0,   KC.N1,   KC.N2,   KC.N3, KC.DLR,  KC.HASH, KC.PLUS, KC.ASTR, KC.LCBR, KC.RCBR, KC.BSPC,
        KC.ESC,  KC.TILD, KC.N4,   KC.N5,   KC.N6, KC.AT,   KC.EXLM, KC.MINS, KC.EQL,  KC.LPRN, KC.RPRN, KC.BSLS,
        XXXXXXX, KC.GRV,  KC.N7,   KC.N8,   KC.N9, KC.PERC, KC.AMPR, KC.UNDS, KC.PSLS, KC.LBRC, KC.RBRC, KC.ENT,
        _______, _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,  _______
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
