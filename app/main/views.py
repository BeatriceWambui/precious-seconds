from flask import render_template,redirect,url_for
from flask_login import login_required,current_user
from . import main
from .. import db
from app.models import Pitch
from .forms import PitchForm

@main.route('/')
def index():
    all_pitches = Pitch.query.all()
    return render_template('index.html',all_pitches =all_pitches )

@main.route('/pitches/new',methods = ['GET','POST'])
@login_required
def new_pitch(): 
    form = PitchForm()
    if form.validate_on_submit():
        user_id= current_user._get_current_object().id
        pitch = Pitch(category = form.category.data,title=form.title.data,description=form.description.data,user_id=user_id)
        pitch.save()
        return redirect(url_for('main.index'))
    return render_template('pitch.html',form=form)