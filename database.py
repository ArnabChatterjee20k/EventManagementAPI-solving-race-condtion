from sqlalchemy import create_engine , String
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Date , ForeignKey
from datetime import date
from sqlalchemy.orm import mapped_column , Mapped , relationship
SQL_Logging = True
engine = create_engine("mysql+pymysql://root@localhost:3306/test", echo=SQL_Logging)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


class Attendee(Base):
    __tablename__ = "attendee"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    user: Mapped[int] = mapped_column(ForeignKey("user.id"))
    event: Mapped[int] = mapped_column(ForeignKey("events.id"))


class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(30))
    attendees: Mapped["Attendee"] = relationship(backref="attendees") #we can call .attendees in the child

class Events(Base):
    __tablename__ = "events"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str] = mapped_column(String(30))
    date:Mapped[date]
    entries:Mapped[int]
    fee:Mapped[float]
    attendees:Mapped["Attendee"] = relationship(backref="events") #we can call .events in the child

Base.metadata.create_all(engine)