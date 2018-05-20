Pure Data (the version I use is called "Purr Data" because Sometimes Projects Change Hands) is a visual language for synthesizing and directing sound using a combination of raw DSP widgets and MIDI and MIDI-like signaling between objects and to other programs such as VSTs.

puredata-extras is my personal collection of patches, which I use as a way to re-use my effort when building larger patches.  Pure Data lets you add to the default search path for patches, so "installing" puredata-extras means copying it to your computer then telling Pure Data that you want it in your search path.

Contents:

env: Envelope functions, ADSR, Trapezoid, etc.

fx: Effects like reverb, sample/hold, panning, clipping...

python: Python files for interfacing the Akai LPD8 on Linux.  Pure Data's MIDI interface can be a little fiddly so I found it easier to just write an external streaming app that pipes the data to Pure Data over a socket.

route: Routing such as mux/demux.

samples: Patches for managing .wav samples.

seq: Patches for generating, using, and modifying Messages.

synths: Synthesizers.

vis: Visualizers such as scopes and UV meters.

In the root directory you will also find stdout.pd, my standard output function, although you might prefer to use other features.  The save function makes a new random file name every time so it won't copy over its own stuff.
