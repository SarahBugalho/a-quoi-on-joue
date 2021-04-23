from models import Friendship, User

myuser = User(
    id=3,
    status="NEW",
    email="abc@email.com",
    name="pastapouet",
    birthday="1997-05-23",
    creation_date="2021-04-18 12:34:00",
    update_date="2021-04-19 20:45:09",
)

myseconduser = User(
    id=5,
    status="NEW",
    email="pipouet@email.com",
    name="pizzapouet",
    birthday="1992-09-17",
    creation_date="2020-10-18 10:10:00",
    update_date="2021-04-19 20:53:00",
)


myfriendship = Friendship(
    status="ASKED",
    user_id=3,
    friend_id=5,
    lend_game=True,
    creation_date="2000-01-01 23:59:00",
    update_date="2000-01-01 23:59:00",
)

mygame = Game(
    id=456,
    status=""
)