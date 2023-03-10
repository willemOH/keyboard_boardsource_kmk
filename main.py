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
NAV = KC.TT(1)
SYMBOL = KC.LT(2, KC.SPC, prefer_hold=True, tap_interrupted=False, tap_time=None)                                                
PAD = KC.TT(3) 
SYS = KC.TG(4)

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
     # | Caps |L_Ctrl|  Alt |  GUI |NavLr |      |  Pad |Sc/Sym|      |PrntSc|Insert| sys  |
     # `-----------------------------------------------------------------------------------' 
    [  #MAIN
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R, KC.T,   KC.Y, KC.U, KC.I,     KC.O,    KC.P,    KC.BSPC,
        KC.ESC,  KC.A,    KC.S,    KC.D,    KC.F, KC.G,   KC.H, KC.J, KC.K,     KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V, KC.B,   KC.N, KC.M, KC.COMM,  KC.DOT,  KC.SLSH, KC.ENT ,
        KC.CAPS, KC.LCTL, KC.LALT, KC.LGUI, NAV,  XXXXXXX, PAD, SYMBOL, XXXXXXX, KC.PSCR, KC.INS,  SYS
    ],                              
                                                                                            
     # Layer _NAV
     # ,-----------------------------------------------------------------------------------.
     # |   `  |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  | Undo | Cut  | Copy |Paste | Bksp |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |  Esc | Home | PgDn | PgUp | End  |      |      | Left | Up   | Down | Right|  Del |   
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |  F7  |  F8  |  F9  | F10  | F11  | F12  | vol+ | vol- | mute |plypau|Enter |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # |      |      |      |      |LCtrl |MainLr| Shift| Space| Left |  Up  | Down | Right|      
     # `-----------------------------------------------------------------------------------'
           
    [  #NAV 
        KC.GRV,  KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,   KC.F6,   UNDO,    CUT,     COPY,    PASTE,    KC.BSPC,
        KC.ESC, KC.HOME, KC.PGDN, KC.PGUP, KC.END,  XXXXXXX, XXXXXXX, KC.LEFT, KC.UP,   KC.DOWN, KC.RIGHT, KC.DEL,
        XXXXXXX, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,  KC.VOLU, KC.VOLD, KC.MUTE, KC.MPLY,  KC.ENT,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.LCTL, MAIN,    KC.RSFT, KC.SPC,  KC.LEFT, KC.UP,   KC.DOWN,  KC.RIGHT
    ],
    
     # Layer _SYMBOL
     # ,-----------------------------------------------------------------------------------.
     # |   ~  |   !  |   @  |   #  |   $  |  %   |   ^  |   &  |   *  |   (  |   )  |      |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |      |   {  |   }  |   +  |   _  |      |      |   -  |   =  |   [  |   ]  |  \   |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |      |      |      |      |      |      |      |      |      |      |      |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # |      |      |      |      |      |      |      |      |      |      |      |      | 
     # `-----------------------------------------------------------------------------------'
     
    [  #SYMBOL
        KC.TILD, KC.EXLM, KC.AT,   KC.HASH, KC.DLR,  KC.PERC, KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, XXXXXXX,
        XXXXXXX, KC.LCBR, KC.RCBR, KC.PLUS, KC.UNDS, KC.F5,   KC.F6,   KC.MINS, KC.EQL, KC.LBRC, KC.RBRC, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, 
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,
    ],
    
     # Layer _PAD
     # ,-----------------------------------------------------------------------------------.
     # |      |      |   1  |   2  |   3  |      |      |   +  |      |      |      |  del |
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |      |      |   4  |   5  |   6  |      |      |   -  |   =  |   *  |   /  |bckspc|
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |      |   7  |  8   |   9  |      |      |      |      |      |      |      |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # |      |      |   *  |   0  |   #  | Main |      |      |      |      |      |      |
     # `-----------------------------------------------------------------------------------'
     
    [  #PAD
        XXXXXXX, XXXXXXX    , KC.N1,   KC.N2, KC.N3,   XXXXXXX, XXXXXXX, KC.PLUS, KC.ASTR, KC.LPRN, KC.RPRN, KC.DEL,
        XXXXXXX, XXXXXXX, KC.N4,   KC.N5, KC.N6,   XXXXXXX, XXXXXXX, KC.MINS, KC.EQL, KC.PAST, KC.SLSH, KC.BSPC,
        XXXXXXX, XXXXXXX, KC.N7,   KC.N8, KC.N9,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX, KC.PAST, KC.N0, KC.HASH, MAIN,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    ],
    
    # Layer _SYS
     # ,-----------------------------------------------------------------------------------.
     # | linux|windws| mac  | noop |      |      |      |   +  |      |      |      |bckspc|
     # |------+------+------+------+------+-------------+------+------+------+------+------|
     # |      |      |   4  |   5  |   6  |      |      |   -  |   =  |   *  |   /  |  del |
     # |------+------+------+------+------+------|------+------+------+------+------+------|
     # |      |      |   7  |  8   |   9  |      |      |      |      |      |      |      |
     # |------+------+------+------+------+------+------+------+------+------+------+------|
     # |      |      |   *  |   0  |   #  | Main |      |      |      |      |      |      |
     # `-----------------------------------------------------------------------------------'
     
    [  #SYS
        KC.UC_MODE_LINUX, KC.UC_MODE_WINC, KC.UC_MODE_MACOS,   KC.UC_MODE_NOOP, XXXXXXX,   XXXXXXX, XXXXXXX, KC.PLUS, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,
        XXXXXXX, XXXXXXX, KC.P4,   KC.P5, KC.P6,   XXXXXXX, XXXXXXX, KC.MINS, KC.EQL, KC.PAST, KC.SLSH, KC.DEL,
        XXXXXXX, XXXXXXX, KC.P7,   KC.P8, KC.P9,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX,
        XXXXXXX, XXXXXXX, KC.PAST, KC.P0, KC.HASH, MAIN,    XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX
    ]  
]  
   
if __name__ == '__main__':
    keyboard.go()