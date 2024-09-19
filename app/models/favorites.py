from .db import db, environment, SCHEMA

class Favorite(db.Model):
    __tablename__ = "favorites"

    if environment == "production":
        __table_args__ = {"schema": SCHEMA}

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    image_id = db.Column(db.Integer, db.ForeignKey("images.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

# # Will be in the user.py model soon
# images = db.relationship("Image", secondary=favorites, back_populates="users")

# # Will be in the image.py model soon
# users = db.relationship("User", secondary=favorites, back_populates="images")