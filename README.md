MIDI constants for Python
=========================

midi_const
----------

This very simple package provides useful constants derived from official 
MIDI specifications available at:
- MIDI Association, ex MIDI Manufacturers Association (MMA) [US]:
  https://midi.org
- Association of Musical Electronics Industry (AMEI) [JP]:
  https://www.amei.or.jp/
- MIDI Standard Committee (MSC) [JP]:
  http://amei.or.jp/midistandardcommittee

### Status

Already covers most of the MIDI 1.0 Detailed Specification v4.2.1 from 
February 1996.

Other specifications will be added along the way.

Contributions welcome!

### License

To allow maximal re-usability, these constants are offered,
at your option, under any of the following licenses:
 - CC0-1.0
 - MIT (OSI and FSF compatible)
 - Unlicense

### Installation

```shell
pip install midi_const
```

### Usage

Interactively:

```pycon
>>> import midi_const as midi

>>> midi.STATUS_BYTES.get(0x80)
'Note Off'

>>> midi.CONTROLLER_NUMBERS.get(7)
'Channel Volume'

>>> midi.SMF_DEFAULT_TEMPO
500000.0

>>> help(midi)
```
Within a program:

```python
from midi_const import GENERAL_MIDI_SOUND_SET, GENERAL_MIDI_SOUND_SET_GROUPINGS

index = GENERAL_MIDI_SOUND_SET.index('Banjo')
# index = 105
group = GENERAL_MIDI_SOUND_SET_GROUPINGS.get(index)
# group = 'Ethnic'
```
