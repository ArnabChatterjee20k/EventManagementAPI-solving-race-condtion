from database import Events , engine , User
from datetime import date
from sqlalchemy.orm import Session

def create_fake_events():
    session = Session(bind=engine)
    event1 = Events(
        name='Conference XYZ',
        date=date(2023, 6, 15),
        entries=500,
        fee=99.99
    )
    event2 = Events(
        name='Product Launch',
        date=date(2023, 8, 1),
        entries=200,
        fee=49.99
    )
    event3 = Events(
        name='Networking Event',
        date=date(2023, 10, 20),
        entries=100,
        fee=25.00
    )

    session.add_all([event1, event2, event3])
    session.commit()
def create_fake_users():
    session = Session(bind=engine)

    user1 = User(name='John Doe')
    user2 = User(name='Jane Smith')
    user3 = User(name='Michael Johnson')
    user4 = User(name='Emily Davis')
    user5 = User(name='David Wilson')

    session.add_all([user1, user2, user3, user4, user5])
    session.commit()
    print('Data inserted successfully.')

create_fake_events()
create_fake_users()