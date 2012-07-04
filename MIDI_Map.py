# http://remotescripts.blogspot.com
# hanz.petrov@gmail.com
# Note and CC Mappings for the FCB1020 script (APC emulation) are defined in this file
# Values may be edited with any text editor (but avoid using tabs for indentation)

# Modified by Tomash Ghz for the MIDI Fighter Pro
# www.tomashg.com

# Combination Mode offsets
# ------------------------

TRACK_OFFSET = 0 #offset from the left of linked session origin; set to -1 for auto-joining of multiple instances
SCENE_OFFSET = 0 #offset from the top of linked session origin (no auto-join)

# Buttons / Pads
# -------------
# Valid Note/CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments are permitted

BUTTONCHANNEL = 2 #Channel assignment for all mapped buttons/pads; valid range is 0 to 15
MESSAGETYPE = 0 #Message type for buttons/pads; set to 0 for MIDI Notes, 1 for CCs. 
        #When using CCs for buttons/pads, set BUTTONCHANNEL and SLIDERCHANNEL to different values. 

# General
PLAY = 36 #Global play
STOP = 37 #Global stop
REC = 38 #Global record
TAPTEMPO = 51 #Tap tempo
NUDGEUP = 50 #Tempo Nudge Up
NUDGEDOWN = 49 #Tempo Nudge Down
UNDO = -1 #Undo
REDO = -1 #Redo
LOOP = -1 #Loop on/off
PUNCHIN = -1 #Punch in
PUNCHOUT = -1 #Punch out
OVERDUB = -1 #Overdub on/off
METRONOME = 48 #Metronome on/off
RECQUANT = -1 #Record quantization on/off
DETAILVIEW = 47 #Detail view switch
CLIPTRACKVIEW = 44 #Clip/Track view switch

# Device Control
DEVICELOCK = -1 #Device Lock (lock "blue hand")
DEVICEONOFF = -1 #Device on/off
DEVICENAVLEFT = -1 #Device nav left
DEVICENAVRIGHT = -1 #Device nav right
DEVICEBANKNAVLEFT = -1 #Device bank nav left
DEVICEBANKNAVRIGHT = -1 #Device bank nav right
DEVICEBANK = (-1, #Bank 1 #All 8 banks must be assigned to positive values in order for bank selection to work
              -1, #Bank 2 
              -1, #Bank 3 
              -1, #Bank 4 
              -1, #Bank 5 
              -1, #Bank 6
              -1, #Bank 7
              -1, #Bank 8
              )

# Arrangement View Controls
SEEKFWD = -1 #Seek forward
SEEKRWD = -1 #Seek rewind

# Session Navigation (aka "red box")
SESSIONLEFT = 40 #Session left
SESSIONRIGHT = 41 #Session right
SESSIONUP = -1 #Session up
SESSIONDOWN = -1 #Session down
ZOOMUP = 42 #Session Zoom up
ZOOMDOWN = 43 #Session Zoom down
ZOOMLEFT = -1 #Session Zoom left
ZOOMRIGHT = -1 #Session Zoom right

# Track Navigation
TRACKLEFT = -1 #Track left
TRACKRIGHT = -1 #Track right

# Scene Navigation
SCENEUP = -1 #Scene down
SCENEDN = -1 #Scene up

# Scene Launch
SELSCENELAUNCH = -1 #Selected scene launch
SCENELAUNCH = (-1, #Scene 1 Launch
               -1, #Scene 2 
               -1, #Scene 3 
               -1, #Scene 4 
               -1, #Scene 5 
               )

# Clip Launch / Stop
SELCLIPLAUNCH = -1 #Selected clip launch
STOPALLCLIPS = 39 #Stop all clips

# 8x5 Matrix note assignments
# Track no.:     1   2   3   4   5   6   7   8
CLIPNOTEMAP = ((76, 77, 78, 79), #Row 1
               (72, 73, 74, 75), #Row 2
               (68, 69, 70, 71), #Row 3
               )

# Track Control
MASTERSEL = -1 #Master track select
TRACKSTOP = (80, #Track 1 Clip Stop
             81, #Track 2
             82, #Track 3
             83, #Track 4
             )
TRACKSEL = (64, #Track 1 Select
            65, #Track 2
            66, #Track 3
            67, #Track 4
            )
TRACKMUTE = (60, #Track 1 On/Off
             61, #Track 2
             62, #Track 3
             63, #Track 4
             )
TRACKSOLO = (52, #Track 1 Solo
             53, #Track 2
             54, #Track 3
             55, #Track 4
             )
TRACKREC = (56, #Track 1 Record
            57, #Track 2
            58, #Track 3
            59, #Track 4
            )


# Pad Translations for Drum Rack

PADCHANNEL = 2 # MIDI channel for Drum Rack notes
DRUM_PADS = (96, 97, 98, 99, # MIDI note numbers for 4 x 4 Drum Rack
             92, 93, 94, 95, # Mapping will be disabled if any notes are set to -1
             88, 89, 90, 91, # Notes will be "swallowed" if already mapped elsewhere
             84, 85, 86, 87,
             )

# Sliders / Knobs
# ---------------
# Valid CC assignments are 0 to 127, or -1 for NONE
# Duplicate assignments will be ignored

SLIDERCHANNEL = 2 #Channel assignment for all mapped CCs; valid range is 0 to 15
TEMPO_TOP = 220.0 # Upper limit of tempo control in BPM (max is 999)
TEMPO_BOTTOM = 40.0 # Lower limit of tempo control in BPM (min is 0)

TEMPOCONTROL = -1 #Tempo control CC assignment; control range is set above
MASTERVOLUME = -1 #Master track volume
CUELEVEL = -1 #Cue level control
CROSSFADER = -1 #Crossfader control

TRACKVOL = (-1, #Track 1 Volume
            -1, #Track 2
            -1, #Track 3
            -1, #Track 4
            -1, #Track 5
            -1, #Track 6
            -1, #Track 7
            -1, #Track 8
            )
TRACKPAN = (-1, #Track 1 Pan
            -1, #Track 2
            -1, #Track 3
            -1, #Track 4
            -1, #Track 5
            -1, #Track 6
            -1, #Track 7
            -1, #Track 8
            )
TRACKSENDA = (-1, #Track 1 Send A
              -1, #Track 2
              -1, #Track 3
              -1, #Track 4
              -1, #Track 5
              -1, #Track 6
              -1, #Track 7
              -1, #Track 8
              )
TRACKSENDB = (-1, #Track 1 Send B
              -1, #Track 2
              -1, #Track 3
              -1, #Track 4
              -1, #Track 5
              -1, #Track 6
              -1, #Track 7
              -1, #Track 8
              )
TRACKSENDC = (-1, #Track 1 Send C
              -1, #Track 2
              -1, #Track 3
              -1, #Track 4
              -1, #Track 5
              -1, #Track 6
              -1, #Track 7
              -1, #Track 8
              )
PARAMCONTROL = (16, #Param 1 #All 8 params must be assigned to positive values in order for param control to work
                18, #Param 2
                20, #Param 3
                22, #Param 4
                99, #Param 5
                99, #Param 6
                99, #Param 7
                99, #Param 8
                )