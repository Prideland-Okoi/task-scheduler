from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, ValidationError
from datetime import date


class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[
                                Optional(), Length(max=1000)])
    due_date = DateField('Due Date', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_due_date(self, field):
        today = date.today()
        if field.data < today:
            raise ValidationError('Due date cannot be in the past.')
