# You import all the IOs of your board
import board
import busio

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.display import Display, TextEntry, ImageEntry

# For SSD1306
from kmk.extensions.display.ssd1306 import SSD1306

# This is the encoder handler
encoder_handler = EncoderHandler()

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules = [layers, holdtap, encoder_handler]
keyboard.modules.append(macros)

# Add the MediaKeys extension
keyboard.extensions.append(MediaKeys())

# Define your pins here!
PINS = [board.D7, board.D8, board.D9, board.D10]
encoder_handler.pins = ((board.D1,board.D2,None),)

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Configuring the OLED
# I2C Bus for the OLED
i2c_bus = busio.I2C(board.GP_SCL, board.GP_SDA)

driver = SSD1306(i2c=i2c_bus)

display = Display(
    display=driver,
    width=128,
    height=64,
    brightness=0.8, 
)

display.entries = [
        TextEntry(text="Music Playing..."  , x=0, y=0, x_anchor="M"),
        TextEntry(text="Untitled", x=0, y=12, x_anchor="M"),
        TextEntry(text="00:02/02:36", x=0, y=24, x_anchor="M")
]

# TODO: Connect Spotify/ YT Music

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.MPRV, KC.MPLY, KC.MNXT, KC.MUTE,]
]
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),),
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()