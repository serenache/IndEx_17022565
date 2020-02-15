from flask import render_template, flash, redirect, url_for, request
from sqlalchemy.exc import IntegrityError
from app.forms import SignupForm
from app import create_app, db
from app.models import User, City, Forecast

app = create_app()


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(username=form.name.data, email=form.email.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash('You are now a registered user!')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('ERROR! Unable to register {}. Please check your details are correct and resubmit'.format(form.email.data), 'error')
    return render_template('signup.html', form=form)

@app.route('/users', methods=['GET'])
def UserInfo():
    user_list = User.query.all()
    return render_template("UserInfo.html", users=user_list)

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        term = request.form['search_term']
        if term == "":
            flash("Enter a city to search for")
            return redirect('/')
        results = City.query.join(Forecast).with_entities(City.city, Forecast.forecast, Forecast.comment).filter(City.city.contains(term)).all()
        if not results:
            flash("No blog post found for the city")
            return redirect('/')
        return render_template('SearchResults.html', results=results)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
