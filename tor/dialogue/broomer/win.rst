
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

.. entity:: BROOMER
   :types:  tor.story.Character
   :states: tor.story.Occupation.broomer

Brooms
~~~~~~

Bronze
------

.. condition:: BROOMER.state 10

[BROOMER]_

    Bronze!

Silver
------

.. condition:: BROOMER.state 20

[BROOMER]_

    Silver!

Gold
----

.. condition:: BROOMER.state 30

[BROOMER]_

    Gold!

Restart
-------

[NARRATOR]_

    Restart the server to have another go!

