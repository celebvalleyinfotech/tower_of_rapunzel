
..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: tor.types.version

:author: D Haynes
:date: 2019-09-24
:project: tor
:version: |VERSION|

.. entity:: NARRATOR
   :types: tor.types.Narrator

.. entity:: RAPUNZEL
   :types:  tor.types.Character
   :states: tor.types.Occupation.teenager
            tor.types.Hanging.crib

Fall
~~~~

Splat 0
-------

.. condition:: NARRATOR.damage_bars 0

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    That was easy!

Splat 1
-------

.. condition:: NARRATOR.damage_bars 1

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    We have taken a slight fall.

Splat 2
-------

.. condition:: NARRATOR.damage_bars 2

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    A bit of rope burn. Could be worse.

Splat 3
-------

.. condition:: NARRATOR.damage_bars 3

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    After the initial shock of the landing
    we discover several significant abrasions.

Splat 4
-------

.. condition:: NARRATOR.damage_bars 4

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    That was a fair drop.

    Our mobility has been somewhat impaired.

Splat 5
-------

.. condition:: NARRATOR.damage_bars 5

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    It has taken a moment to get to our feet.

    And several seconds for the ringing in our ears to die down.

    We have yet to identify familiar objects.

Splat 6
-------

.. condition:: NARRATOR.damage_bars 6

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    Breathing has become difficult.

    We thought we heard some cracked ribs.

Splat 7
-------

.. condition:: NARRATOR.damage_bars 7

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    It has become impossible, despite our natural optimism, to
    ignore a suspicion that we might have severe internal bleeding.

Splat 8
-------

.. condition:: NARRATOR.damage_bars 8

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    There seems to be a lot of blood.

Splat 9
-------

.. condition:: NARRATOR.damage_bars 9

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    One of our shoes has come off.

    It still has a foot in it.

Status
------

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    You have |HEALTH_N| health.

.. |HEALTH_N| property:: NARRATOR.health_n
