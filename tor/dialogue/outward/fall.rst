
..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: tor.story.version

:author: D Haynes
:date: 2019-09-24
:project: tor
:version: |VERSION|

.. entity:: NARRATOR
   :types: tor.story.Narrator

.. entity:: RAPUNZEL
   :types: tor.story.Rapunzel
   :states: tor.story.At.crib

.. This dialogue uses Rapunzel's random state to select lines.
   It should be aligned to player health instead.

Fall
~~~~

Splat 0
-------

.. condition:: NARRATOR.damage_bars 0

[NARRATOR]_

    That was easy!

Splat 1
-------

.. condition:: NARRATOR.damage_bars 1

[NARRATOR]_

    You have taken a fall.

Splat 2
-------

.. condition:: NARRATOR.damage_bars 2

[NARRATOR]_

    Must remember not to cut off so much next time.

Splat 3
-------

.. condition:: NARRATOR.damage_bars 3

[NARRATOR]_

    A bit of rope burn. Could be worse.

Splat 4
-------

.. condition:: NARRATOR.damage_bars 4

[NARRATOR]_

    Luckily, you landed on a small animal.

Splat 5
-------

.. condition:: NARRATOR.damage_bars 5

[NARRATOR]_

    After the initial shock of the landing, you are happy
    to discover only minor abrasions.

Splat 6
-------

.. condition:: NARRATOR.damage_bars 6

[NARRATOR]_

    Your mobility has been somewhat impaired.

Splat 7
-------

.. condition:: NARRATOR.damage_bars 7

[NARRATOR]_

    It's difficult, despite your natural optimism, to
    ignore a suspicion that you might have internal
    bleeding.

Splat 8
-------

.. condition:: NARRATOR.damage_bars 8

[NARRATOR]_

    There seems to be a lot of blood.

Splat 9
-------

.. condition:: NARRATOR.damage_bars 9

[NARRATOR]_

    One of your shoes has come off.

    It still has your foot in it.
