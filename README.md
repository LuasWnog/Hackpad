# Hackpad
This my hackpad for listening to music

## Cad Model:
The whole hackpad comes together with 4 M3 heatset inserts and M3 bolts. The PCB fits snugly inside the case, with 2 pegs holding it still. The case comes in two parts, the top and the bottom. The top has holes to allow the rotary encoder, switches, LEDs, and the OLED screen to poke through.
![[Hackpad Case.png]]

## PCB:
This is the schematic for the PCB,
![[Schematic.png]]
and this is the PCB itself.
![[PCB.png]]

## Firmware and Functions
* The 4 buttons have different functions:
*Previous Track, Pause/Play, Next Track, Mute*
* The rotary encoder will increase and decrease the volume.
* The OLED screen will display the current song, the length of the song, and the next song. (TODO when hardware is received)
* The LEDs will light up according how much of the song that is finished (25%, 50%, 75%, 100%).

The firmware is coded in python with kmk.

## BOM:
Here are all the materials for the hackpad.
* 1x Seeed XIAO RP2040
* 4x MX-Style switches
* 1x EC11 rotary encoder
* 1x 0.91 inch OLED display
* 4x Blank DSA keycaps
* 4x SK6812 MINI-E LEDs
* 4x M3x16mm screws
* 4x - M3x5mx4mm heatset inserts
* 1x 3D printed case