import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D1, board.D2, board.D4, board.D5, board.D6, board.D7, board.D8]

keyboard.matrix = KeysScanner(
    pins = PINS,
    value_when_pressed = False
)

# keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
# Most of these shortcuts are for VSCode
keyboard.keymap = [
    [
        KC.MACRO([Press(KC.LCMD), Tap(KC.S), Release(KC.LCMD)]), 
        KC.MACRO([Press(KC.LCMD), Tap(KC.P), Release(KC.LCMD)]),
        KC.MACRO([Press(KC.LCMD), Press(KC.LSFT), Tap(KC.P), Release(KC.LSFT), Release(KC.LCMD)]),
        KC.MACRO([Press(KC.LCMD), Tap(KC.SLASH), Release(KC.LCMD)]),
        KC.MACRO([Press(KC.LCMD), Tap(KC.J), Release(KC.LCMD)]),
        KC.MACRO([Press(KC.LCMD), Tap(KC.N), Release(KC.LCMD)]),
        KC.MACRO([Press(KC.LCMD), Tap(KC.RBRK), Release(KC.LCMD)]),
        KC.MACRO([Press(KC.LCMD), Tap(KC.B), Release(KC.LCMD)]),
        KC.MACRO([Press(KC.LCMD), Press(KC.LSFT), Tap(KC.O), Release(KC.LSFT), Release(KC.LCMD)]),
    ]
]

if __name__ == '__main__':
    keyboard.go()
