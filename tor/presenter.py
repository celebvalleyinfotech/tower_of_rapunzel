#!/usr/bin/env python3
# encoding: utf-8

# This file is part of Tower of Rapunzel.
#
# Tower of Rapunzel is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Tower of Rapunzel is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Tower of Rapunzel.  If not, see <http://www.gnu.org/licenses/>.

from collections import deque
from collections import namedtuple
import copy
import sys

from turberfield.dialogue.matcher import Matcher
from turberfield.dialogue.model import Model
from turberfield.dialogue.performer import Performer

import tor
import tor.story
from tor.story import Narrator


class Presenter:

    Element = namedtuple(
        "Element",
        ["source", "dialogue", "shot", "offset", "duration"]
    )

    @staticmethod
    def build_frames(source, seq, dwell, pause):
        """Generate a new Frame on each Shot and FX item"""
        shot = None
        frame = []
        offset = 0
        for item in seq:
            if isinstance(item, (Model.Audio, Model.Shot)):
                if frame and shot and shot != item:
                    yield frame
                    frame = []
                    offset = 0

                if isinstance(item, Model.Shot):
                    shot = item
                else:
                    frame.append(Presenter.Element(
                        source, item, shot,
                        item.offset / 1000,
                        item.duration / 1000
                    ))

            elif isinstance(item, Model.Line):
                durn = pause + dwell * item.text.count(" ")
                frame.append(Presenter.Element(
                    source, item, shot, offset, durn
                ))
                offset += durn
            elif not isinstance(item, Model.Condition):
                frame.append(Presenter.Element(
                    source, item, shot, offset, 0
                ))
        else:
            if any(
                isinstance(
                    i.dialogue, (Model.Audio, Model.Line)
                )
                for i in frame
            ):
                yield frame

    @staticmethod
    def react(frame):
        for element in frame:
            event = element.dialogue
            if (
                isinstance(event, Model.Property) and
                event.object is not None
            ):
                setattr(event.object, event.attr, event.val)

            yield element

    @staticmethod
    def refresh(frame, min_val=8):
        try:
            return max(
                [min_val] +
                [i.offset + i.duration for i in frame if i.duration]
            )
        except ValueError:
            return None

    def __init__(self, ensemble, frames=None):
        self.ensemble = copy.deepcopy(ensemble)
        self.frames = frames if frames is not None else deque([])

    @property
    def narrator(self):
        return next((i for i in self.ensemble if isinstance(i, Narrator)), None)

    def next_frame(self, entities, dwell=0.3, pause=1):
        while not self.frames:
            matcher = Matcher(tor.story.folders)
            selector = {"area": self.narrator.state.area}
            folders = list(matcher.options(selector))
            performer = Performer(folders, entities)
            try:
                folder, index, script, selection, interlude = performer.next(
                    folders, entities
                )
            except TypeError:
                raise
            scene = performer.run(react=False)
            frames = list(Presenter.build_frames(
                folder.paths[index], scene,
                dwell=dwell, pause=pause
            ))
            self.frames.extend(frames)

        return self.frames.popleft()
