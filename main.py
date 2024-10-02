from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField("Cafe Location (URL)", validators=[DataRequired(), URL()])
    opening = StringField("Opening Time", validators=[DataRequired()])
    closing = StringField("Closing Time", validators=[DataRequired()])
    coffee = SelectField("Coffee Rating", choices=[("☕️"), ("☕️☕️"), ("☕️☕️☕️"), ("☕️☕️☕️☕️"), ("☕️☕️☕️☕️☕️")])
    wifi = SelectField("Wifi Strength Rating", choices=[("✘"), ("💪"), ("💪💪"), ("💪💪💪"), ("💪💪💪💪"), ("💪💪💪💪💪")])
    power = SelectField("Power Socket Availability", choices=[("🔌"), ("🔌🔌"), ("🔌🔌🔌"), ("🔌🔌🔌🔌"), ("🔌🔌🔌🔌🔌")])

    submit = SubmitField('Submit')




# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["POST","GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv","a",encoding="utf-8") as file:
            file.write(f"\n{form.cafe.data},{form.location.data},{form.opening.data}AM,{form.closing.data}PM,{form.coffee.data},{form.wifi.data},{form.power.data}")
            return render_template("index.html")
    return render_template('add.html', form=form)

    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
# Cafe Name,Location,Open,Close,Coffee,Wifi,Power
