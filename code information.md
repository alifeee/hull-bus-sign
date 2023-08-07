# Code information

Code taken from <https://github.com/ConnectedHumber/Bus-Terminal-Signs/>

## Code

### `Scrolling Text Demo.ino`

demo of scrolling text

<https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/master/Code/Examples/Scrolling%20Text%20Demo.ino>

### `CH_AS1100.h`

description of class (which you have to inherit from):

<https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/master/Code/CH_AS1100.h>

### `CH_AS1100.cpp`

C++ code which inherits from class (to implement working behaviour):

<https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/master/Code/CH_AS1100.cpp>

## Information

- There are three pins of interest:
  - load
  - clk (clock)
  - data
- When changing pixels (with e.g., [`setPixel`]), it changes only the [internal pixel array].

  You must call [`Panel.display`] to update the pixels.
  This calls `sendPixels`, which:

  - calls `writeDigit` for each pixel
    - calls `write16`
      - writes to data pin (sends "the lower 12 bits of the word" - not sure what this means. I think it is leftover from copied code, and it actually just sends 0 or 1 (on or off))
  - calls `load`, which writes to load pin. "load pulse causes data to be loaded and displayed if display is on"

[`setPixel`]: https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/924d6c9f16a497d58154f33e4dc9a63ff28e7344/Code/CH_AS1100.cpp#L390-L404
[internal pixel array]: https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/924d6c9f16a497d58154f33e4dc9a63ff28e7344/Code/CH_AS1100.h#L67
[`Panel.display`]: https://github.com/ConnectedHumber/Bus-Terminal-Signs/blob/924d6c9f16a497d58154f33e4dc9a63ff28e7344/Code/Examples/Scrolling%20Text%20Demo.ino#L71
