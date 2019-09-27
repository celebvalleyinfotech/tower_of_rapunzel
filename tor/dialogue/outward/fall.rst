
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

.. condition:: RAPUNZEL.state 0

[NARRATOR]_

    You have taken a fall.

Splat 1
-------

.. condition:: RAPUNZEL.state 1

[NARRATOR]_

    Your mobility has been somewhat impaired.

Splat 2
-------

.. condition:: RAPUNZEL.state 2

[NARRATOR]_

    After the initial shock of the landing, you are happy to discover
    only minor abrasions.

Splat 3
-------

.. condition:: RAPUNZEL.state 3

[NARRATOR]_

    It's difficult, despite your natural optimism, to ignore a suspicion
    that you might have internal bleeding.

Splat 4
-------

.. condition:: RAPUNZEL.state 4

[NARRATOR]_

    One of your shoes has come off.

    It still has your foot in it.

Splat 5
-------

.. condition:: RAPUNZEL.state 5

[NARRATOR]_

    Luckily, you landed on a small animal.

Splat 6
-------

.. condition:: RAPUNZEL.state 6

[NARRATOR]_

    There seems to be a lot of blood.

Splat 7
-------

.. condition:: RAPUNZEL.state 7

[NARRATOR]_

    Must remember not to cut off so much next time.

Splat 8
-------

.. condition:: RAPUNZEL.state 8

[NARRATOR]_

    That was easy!

Splat 9
-------

.. condition:: RAPUNZEL.state 9

[NARRATOR]_

    A bit of rope burn. Could be worse.
