
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

.. entity:: BROOMER
   :types:  tor.types.Character
   :states: tor.types.Occupation.broomer

Brooms
~~~~~~

Chat 0
------

.. condition:: BROOMER.state 0

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    Ah, hello again, how are we now?

Chat 1
------

.. condition:: BROOMER.state 1

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    Do you think you might be ready to buy something?

Chat 2
------

.. condition:: BROOMER.state 2

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    Please be careful stepping over the masonry.

    We had an unfortunate accident in here last week.

Chat 3
------

.. condition:: BROOMER.state 3

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    The trouble with selling to witches is they really know how to exploit
    a situation.

Chat 4
------

.. condition:: BROOMER.state 4

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    I've been getting a lot  of customers coming in recently wanting a
    test drive.

    I strongly suspect it's one single witch in a multitude of disguises.

Chat 5
------

.. condition:: BROOMER.state 5

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    This is our most popular model.

    A modern construction means it's inexpensive.

[BROOMER]_

    Even so, it has a Bronze name tag on the handle. We can engrave that
    for you for a small extra charge.

    Only 10 coins.

Chat 6
------

.. condition:: BROOMER.state 6

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    I would probably steer you towards our Silver model.

[BROOMER]_

    Traditional construction. It's a classic. Sturdy and reliable.

    And we have it on sale at 20 coins. That's the best price anywhere.

Chat 7
------

.. condition:: BROOMER.state 7

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    Ah, I see you are admiring the Excelsior. This is the only model
    with real Gold detailing.

    Would you mind stepping back a little?

Chat 8
------

.. condition:: BROOMER.state 8

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    If you're considering a purchase of the Excelsior, I recommend
    you speak to my colleague in finance.

    For a cash sale, we'd be looking north of 30 coins I think.

    Depending on the options of course.

Chat 9
------

.. condition:: BROOMER.state 9

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[BROOMER]_

    Do you think you might be ready to buy something?

Bronze
------

.. condition:: BROOMER.state 10

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

.. fx:: tor.static.mp3  fly_away.mp3
   :offset: 0
   :duration: 8000
   :loop: 12

[BROOMER]_

    Congratulations on picking our most affordable model.

[BROOMER]_

    And thanks for helping us clear the last of the old stock.

[BROOMER]_

    There's no warranty by the way, before you ask.

[NARRATOR]_

    Restart the server to have another go!

Silver
------

.. condition:: BROOMER.state 20

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

.. fx:: tor.static.mp3  fly_away.mp3
   :offset: 0
   :duration: 8000
   :loop: 12

[BROOMER]_

    Not a bad choice at all.

    I bought this exact model for my son last year.

[BROOMER]_

    I always felt the Excelsior would suit you better in the longer term.

    Do come in soon for another chat.

[NARRATOR]_

    Restart the server to have another go!

Gold
----

.. condition:: BROOMER.state 30

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

.. fx:: tor.static.mp3  fly_away.mp3
   :offset: 0
   :duration: 8000
   :loop: 12

[BROOMER]_

    Well.

    Nothing I can say can add to this moment, so I'll just shut up.

[BROOMER]_

    I am so excited.

    And also somewhat wealthier, due to manufacturer incentives.

[BROOMER]_

    We are both now members of the Excelsior Club!

[NARRATOR]_

    Thanks for playing Tower of Rapunzel.

Status
------

.. fx:: tor.static.img  street.jpg
   :offset: 0
   :duration: 0

[NARRATOR]_

    You have |COINS_N| coins.

.. |COINS_N| property:: NARRATOR.coins_n
.. |HAIR_M| property:: NARRATOR.hair_m
