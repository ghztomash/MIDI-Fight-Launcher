# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

from _Framework.MixerComponent import MixerComponent 
from SpecialChannelStripComponent import SpecialChannelStripComponent 
class SpecialMixerComponent(MixerComponent):
    ' Special mixer class that uses return tracks alongside midi and audio tracks '
    __module__ = __name__

    def __init__(self, num_tracks):
        MixerComponent.__init__(self, num_tracks)



    def tracks_to_use(self):
        return (self.song().visible_tracks + self.song().return_tracks)



    def _create_strip(self):
        return SpecialChannelStripComponent()



# local variables:
# tab-width: 4
