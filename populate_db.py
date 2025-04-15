from wisdom_nuggets.app import create_app
from wisdom_nuggets.app.database import db
from wisdom_nuggets.app.model import WisdomNugget

app = create_app()

with app.app_context():
    # Optional: Clear existing records
    db.drop_all()
    db.create_all()

    nuggets = [
        WisdomNugget(text="The only way out is through.", author="Robert Frost"),
        WisdomNugget(text="Be the change you wish to see in the world.", author="Mahatma Gandhi"),
        WisdomNugget(text="In the middle of difficulty lies opportunity.", author="Albert Einstein"),
        WisdomNugget(text="What you seek is seeking you.", author="Rumi"),
        WisdomNugget(text="Silence is sometimes the best answer.", author="Dalai Lama"),
    ]

    db.session.add_all(nuggets)
    db.session.commit()
    print("🌱 Database seeded with wisdom nuggets!")
