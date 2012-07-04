# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live 
from MIDI_Fighter_APC import MIDI_Fighter_APC 

def create_instance(c_instance):
    ' Creates and returns the APC20 script '
    return MIDI_Fighter_APC(c_instance)


# local variables:
# tab-width: 4

