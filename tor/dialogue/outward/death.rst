
..  This is a Turberfield dialogue file (reStructuredText).
    Scene ~~
    Shot --

.. |VERSION| property:: tor.story.version

:author: D Haynes
:date: 2019-09-24
:project: tor
:version: |VERSION|

.. entity:: NARRATOR
   :types:  tor.story.Narrator

.. entity:: RAPUNZEL
   :types:  tor.story.Character
   :states: tor.story.Occupation.teenager
            tor.story.Hanging.club


Death
~~~~~

RIP 0
-----

[NARRATOR]_

    You are dead.


[NARRATOR]_

    Rapunzel will inherit |COINS_N| coins.


[NARRATOR]_

    Restart the server to try again.

.. |COINS_N| property:: NARRATOR.coins_n
