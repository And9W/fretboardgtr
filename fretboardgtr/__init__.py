"""Top-level package for FretBoardGtr."""
from fretboardgtr._version import version_str
from fretboardgtr.elements.background import Background, BackgroundConfig
from fretboardgtr.elements.fret_number import FretNumber, FretNumberConfig
from fretboardgtr.elements.frets import Fret, FretConfig
from fretboardgtr.elements.neck_dots import NeckDot, NeckDotConfig
from fretboardgtr.elements.notes import (
    FrettedNote,
    FrettedNoteConfig,
    OpenNote,
    OpenNoteConfig,
)
from fretboardgtr.elements.nut import Nut, NutConfig
from fretboardgtr.elements.strings import String, StringConfig
from fretboardgtr.elements.tuning import Tuning, TuningConfig
from fretboardgtr.fretboard import (
    FretBoard,
    FretBoardConfig,
    FretBoardContainer,
    FretboardDrawer,
    FretBoardMainConfig,
)
from fretboardgtr.note_colors import NoteColors
from fretboardgtr.notes_creators import NotesContainer

__author__ = "Antoine Gibek"
__email__ = "antoine.gibek@gmail.com"
__version__ = version_str
