
..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: tor.types.version

:author: D Haynes
:date: 2019-09-24
:project: tor
:version: |VERSION|

.. entity:: NARRATOR
   :types:  tor.types.Narrator

.. entity:: RAPUNZEL
   :types:  tor.types.Character
   :states: tor.types.Occupation.teenager
            tor.types.Hanging.club


Death
~~~~~

RIP 0
-----

.. fx:: tor.static.img  tower.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    You are dead.


[NARRATOR]_

    Rapunzel will inherit |COINS_N| coins.


[NARRATOR]_

    Restart the server to try again.

.. |COINS_N| property:: NARRATOR.coins_n
