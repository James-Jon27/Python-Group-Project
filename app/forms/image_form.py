from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length
from wtforms import  StringField
from app.api.s3_helper import ALLOWED_EXTENSIONS

class ImageForm(FlaskForm):
    image = FileField("Image File", validators=[FileRequired(), FileAllowed(list(ALLOWED_EXTENSIONS))])
    title = StringField("title", validators=[DataRequired()])
    description = StringField("description", validators=[DataRequired()])
    labels = StringField("Labels", validators=[Length(max=50)])

