# Setup

How to set up the screen.

## Attach wires (logic) to unit

![Overview of setup](images/setup_initial.png)

### Arduino (1)

![Zoom of Arduino, showing three wires plugged into the digital output pins.](images/setup_arduino.png)

### Breadboard (3)

![Zoom of breadboard, showing ground cable and ISET table from ribbon cable, and power going out to panel.](images/setup_breadboard.png)

### Ribbon cable (4)

Also see [unit information](./unit%20information.md#pins)

![Zoom of ribbon connector, showing soldered cables 2, 3, 5, 7, and 8.](images/setup_ribbon-connector.png)

### Power connection (5)

![Zoom of power connection, showing positive to positive and neg to neg.](images/setup_power-connection.png)

## Setup code

- Download the [Arduino IDE 2](https://docs.arduino.cc/software/ide-v2).
- Copy [`CH_AS1100.h`] and [`CH_AS1100.cpp`][`CH_AS1100.h`] to `C:\Users\<user>\Documents\Arduino\libraries\ConnectedHumber` or similar
- Create a Sketchbook with the [example code]
- Change [pins] and number of chips to your setup. Pins should match where you put them [above](#arduino-1), and there are 2 chips per LED panel, so 16 across the width of a full sign.
- Upload code to Arduino
- Power on display

[`CH_AS1100.h`]: https://github.com/ConnectedHumber/Bus-Terminal-Signs/tree/master/Code
[example code]: https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/master/Code/Examples/Scrolling%20Text%20Demo.ino
[pins]: https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/e6338adccdb4e44680c86468fa18fadd92395694/Code/Examples/Scrolling%20Text%20Demo.ino#L10-L20
