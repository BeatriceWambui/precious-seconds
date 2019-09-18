from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,TextAreaField,RadioField
from wtforms.validators import Required
from wtforms import ValidationError

class PitchForm(FlaskForm):
    title = StringField('Title',validators=[Required()])
    description = TextAreaField('Would you love to share a pitch?',validators=[Required()])
    category = RadioField('Label', choices=[('pickup lines','pickup lines'),('interview pitch','interview pitch'),('product pitch', 'product pitch'),('promotion pitch','promotion pitch')])
    submit = SubmitField('Submit')