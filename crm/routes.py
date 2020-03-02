"""All routes/views are defined here"""

from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required

from crm import app, db, bcrypt
from crm.forms import RegistrationForm, LoginForm, LeadForm, TouchForm
from crm.models import User, Lead, Touch


@app.route('/')
@app.route('/home')
def home():
    """View for main home page"""
    return render_template('home.html',  touches=touches)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """View to register new admin"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created for {}'.format(form.username.data), 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """View to login admin, if he is already logged in redirect to home page"""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            goto = request.args.get('next')
            return redirect(goto) if goto else redirect(url_for('home'))

        else:
            flash('Login unsuccessful', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    """View to logout"""
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
@login_required
def account():
    """View to see info of current logged in admin"""
    return render_template('account.html')


@app.route('/lead', methods=['GET', 'POST'])
@login_required
def lead():
    """View to create new lead"""
    form = LeadForm()
    if form.validate_on_submit():
        new_lead = Lead(name=form.name.data,
                        company=form.company.data,
                        phone=form.phone.data,
                        email=form.email.data)
        db.session.add(new_lead)
        db.session.commit()
        flash('Lead created for {}'.format(form.name.data), 'success')
        return redirect(url_for('leads'))
    return render_template('lead.html', form=form)


@app.route('/leads')
@login_required
def leads():
    """View to see list of all leads"""
    all_leads = Lead.query.filter().all()
    return render_template('leads.html', leads=all_leads)


@app.route('/touch', methods=['GET', 'POST'])
@login_required
def touch():
    """View to create new touch associated with the lead"""
    form = TouchForm()
    form.lead_id.choices = [(l.id, l.name) for l in Lead.query.order_by('name')]
    if form.validate_on_submit():
        new_touch = Touch(description=form.description.data,
                          lead_id=form.lead_id.data)
        db.session.add(new_touch)
        db.session.commit()
        flash('Touch created', 'success')
        return redirect(url_for('touches'))
    return render_template('touch.html', form=form)


@app.route('/touches')
@login_required
def touches():
    """View to see list of all touches"""
    all_touches = Touch.query.filter().all()
    return render_template('touches.html', touches=all_touches)
