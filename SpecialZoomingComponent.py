# emacs-mode: -*- python-*-
# -*- coding: utf-8 -*-

import Live 
from _Framework.SessionZoomingComponent import SessionZoomingComponent 
from _Framework.ButtonElement import ButtonElement 
class SpecialZoomingComponent(SessionZoomingComponent):
    ' Special ZoomingComponent that uses clip stop buttons for stop all when zoomed '
    __module__ = __name__

    def __init__(self, session):
        SessionZoomingComponent.__init__(self, session)
        
        
    def _nav_up_value(self, value):
        assert (self._nav_up_button != None)
        assert (value in range(128))
        if (self.is_enabled()): # and self._is_zoomed_out):
            if ((value != 0) or (not self._nav_up_button.is_momentary())):
                height = self._session.height()
                track_offset = self._session.track_offset()
                scene_offset = self._session.scene_offset()
                if (scene_offset > 0):
                    new_scene_offset = scene_offset
                    if ((scene_offset % height) > 0):
                        new_scene_offset -= (scene_offset % height)
                    else:
                        new_scene_offset = max(0, (scene_offset - height))
                    self._session.set_offsets(track_offset, new_scene_offset)



    def _nav_down_value(self, value):
        assert (self._nav_down_button != None)
        assert (value in range(128))
        if (self.is_enabled()): # and self._is_zoomed_out):
            if ((value != 0) or (not self._nav_down_button.is_momentary())):
                height = self._session.height()
                track_offset = self._session.track_offset()
                scene_offset = self._session.scene_offset()
                new_scene_offset = ((scene_offset + height) - (scene_offset % height))
                self._session.set_offsets(track_offset, new_scene_offset)



    def _nav_left_value(self, value):
        assert (self._nav_left_button != None)
        assert (value in range(128))
        if (self.is_enabled()): # and self._is_zoomed_out):
            if ((value != 0) or (not self._nav_left_button.is_momentary())):
                width = self._session.width()
                track_offset = self._session.track_offset()
                scene_offset = self._session.scene_offset()
                if (track_offset > 0):
                    new_track_offset = track_offset
                    if ((track_offset % width) > 0):
                        new_track_offset -= (track_offset % width)
                    else:
                        new_track_offset = max(0, (track_offset - width))
                    self._session.set_offsets(new_track_offset, scene_offset)



    def _nav_right_value(self, value):
        assert (self._nav_right_button != None)
        assert (value in range(128))
        if (self.is_enabled()): # and self._is_zoomed_out):
            if ((value != 0) or (not self._nav_right_button.is_momentary())):
                width = self._session.width()
                track_offset = self._session.track_offset()
                scene_offset = self._session.scene_offset()
                new_track_offset = ((track_offset + width) - (track_offset % width))
                self._session.set_offsets(new_track_offset, scene_offset)


# local variables:
# tab-width: 4
