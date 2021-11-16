
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

.. entity:: BUTCHER
   :types:  tor.types.Character
   :states: tor.types.Occupation.butcher

Meat
~~~~

Chat 0
------

.. condition:: BUTCHER.state 0

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    There's the mince. It's a little bit over.

Chat 1
------

.. condition:: BUTCHER.state 1

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    One Chicken, madam. Shall I leave the giblets?

Chat 2
------

.. condition:: BUTCHER.state 2

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    No lamb this week, I'm afraid.

    They were a little bit fat, so we sent them back.

Chat 3
------

.. condition:: BUTCHER.state 3

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    Chicken fillets. Skin on or off?

Chat 4
------

.. condition:: BUTCHER.state 4

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    How much would you like?

Chat 5
------

.. condition:: BUTCHER.state 5

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    I'm doing a great offer on packs of sausages.

Chat 6
------

.. condition:: BUTCHER.state 6

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    This sirloin would be beautiful as a Sunday roast.

    It's actually trimmed for steak.

Chat 7
------

.. condition:: BUTCHER.state 7

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    Wild boar has come in.

    May contain shot.

Chat 8
------

.. condition:: BUTCHER.state 8

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    I might have some more in the freezer.

Chat 9
------

.. condition:: BUTCHER.state 9

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BUTCHER]_

    The game.

    It's very gamey.

Status
------

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    You have |COINS_N| coins.

.. |COINS_N| property:: NARRATOR.coins_n
.. |HAIR_M| property:: NARRATOR.hair_m
