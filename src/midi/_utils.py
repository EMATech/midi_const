# SPDX-FileCopyrightText: 2021 Raphaël Doursenaud <rdoursenaud@gmail.com>
#
# SPDX-License-Identifier: CC0-1.0 OR MIT OR Unlicense

"""
Utilities to help dealing with MIDI.

TODO: Move into mido?
"""

import datetime

from . import SMF_DEFAULT_TEMPO, _MS2US


def compute_delta_time(
        delta_time: int,
        division: int,
        tempo: float = SMF_DEFAULT_TEMPO
) -> datetime.timedelta:
    """Computes natural delta-time in milliseconds
     from MIDI delta-time expressed in ticks.

    :param delta_time: SMF Track Event delta-time
     (in ticks)

    :param division: SMF Header Chunk division
     (in delta ticks per quarter-note)

    :param tempo: SMF Track non-MIDI data Meta Event Tempo
    (in microseconds per quarter-note).
    Assumed to be 120.0 if not provided.

    :return: A time delta object.
    """
    return datetime.timedelta(
        milliseconds=delta_time * (tempo / division) / _MS2US
    )
