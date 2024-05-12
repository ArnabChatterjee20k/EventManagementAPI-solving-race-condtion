from sqlalchemy.orm import Session
from database import User,Attendee,Events
from sqlalchemy import select,func,and_
from sqlalchemy.exc import IntegrityError

def book_event(db: Session, user_id: int, event_id: int):
    """
        basically here we are selecting a row for update
        for update means exclusive lock and no one can use the event for referencing it as well till lock is not released
    """
    with db:
        event = db.execute(
            select(Events.entries)
            .where(Events.id == event_id)
            .with_for_update()  # Lock the row for the duration of the transaction
        ).scalar_one()

        allowed_entries = event
        print(allowed_entries)
        # Get the count of attendees for the specific event and user
        attendee_count = db.scalar(
            select(func.count())
            .where(Attendee.event == event_id)
        )

        if attendee_count >= allowed_entries:
            return False
        try:
            db.add(Attendee(user=user_id, event=event_id))
        except IntegrityError:
            db.rollback()
            return False


    # If the transaction was successful, commit it
    db.commit()
    return True