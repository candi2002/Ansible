"""Routes for logged-in application."""
from flask import Blueprint, render_template, session,request, Flask, request, session, url_for, redirect, render_template, g, flash
from flask_login import current_user
from flask import current_app as app
from .assets import compile_auth_assets
from flask_login import login_required
import json
from pathlib import Path


# Blueprint Configuration
main_bp = Blueprint('main_bp', __name__,
                    template_folder='templates',
                    static_folder='static')
compile_auth_assets(app)


@main_bp.route('/', methods=['GET'])
@login_required
def dashboard():
    """Serve logged in Dashboard."""
    session['redis_test'] = 'This is a session variable.'
    return render_template('dashboard.html',
                           title='Flask-Session Tutorial.',
                           template='dashboard-template',
                           current_user=current_user,
                           body="You are now logged in!")


@main_bp.route('/session', methods=['GET'])
@login_required
def session_view():
    """Route which displays session variable value."""
    return render_template('session.html',
                           title='Flask-Session Tutorial.',
                           template='dashboard-template',
                           session_variable=str(session['redis_test']))

@main_bp.route('/calendar',methods=['GET'])
@login_required
def calendar_view():
    return render_template("index.html")

def return_data():
    start_date = request.args.get('start', '')
    end_date = request.args.get('end', '')


    with open("templates/events.json", "r") as input_data:
        return input_data.read()

@main_bp.route('/bus',methods=['GET'])
@login_required
def bus():
    return render_template("bus.html")

@main_bp.route('/map',methods=['GET'])
@login_required
def map():
    return render_template("new_map.html")

@main_bp.route('/yangsan',methods=['GET'])
@login_required
def yangsan():
    return render_template("yangsan.html")

@main_bp.route('/miryang',methods=['GET'])
@login_required
def miryang():
    return render_template("miryang.html")

@main_bp.route("/home", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        req = request.form
        name = req["name"].lower()
        data = read_json('users')
        if not name in data:
            return render_template('user not found.html', username=name)
        return redirect("/home/user/{}".format(name))
    return render_template("home.html")

@main_bp.route("/home/user/<name>/")
@login_required
def getUser(name):
    data = read_json('users')
    if not name in data:
        return render_template('user not found.html', username=name)
    list = data[name]['timetable']
    name = name.title()
    cssList = []
    for item in list:
        if item == "":
            cssList.append("")
        else:
            cssList.append("selected")
    return render_template(
    'timetable template.html', list=list, cssList=cssList, username=name)

@main_bp.route("/register", methods=["GET", "POST"])
@login_required
def register():
    if request.method == "POST":
        req = request.form
        name = req["name"].lower()
        data = read_json('users')
        if not name in data:
            data[name] = {}
        data[name]['timetable'] = []
        for item in req:
            if item not in ['name']:
                data[name]['timetable'].append(req[item])
        write_json(data, 'users')
        return redirect("/home/user/{}".format(name))
    return render_template(
    'input form.html',
    nameList=['월요일', '화요일', '수요일', '목요일', '금요일'],
    idList=['monday8am', 'tuesday8am', 'wednesday8am', 'thursday8am', 'friday8am', 'monday9am', 'tuesday9am', 'wednesday9am', 'thursday9am', 'friday9am', 'monday10am', 'tuesday10am', 'wednesday10am', 'thursday10am', 'friday10am', 'monday11am', 'tuesday11am', 'wednesday11am', 'thursday11am', 'friday11am', 'monday12pm', 'tuesday12pm', 'wednesday12pm', 'thursday12pm', 'friday12pm', 'monday1pm', 'tuesday1pm', 'wednesday1pm', 'thursday1pm', 'friday1pm', 'monday2pm', 'tuesday2pm', 'wednesday2pm', 'thursday2pm', 'friday2pm', 'monday3pm', 'tuesday3pm', 'wednesday3pm', 'thursday3pm', 'friday3pm', 'monday4pm', 'tuesday4pm', 'wednesday4pm', 'thursday4pm', 'friday4pm'],
    typeList=['text', 'text', 'text', 'text', 'text'],
    placeholder=[' 월요일 과목을 입력하세요', ' 화요일 과목을 입력하세요', ' 수요일 과목을 입력하세요', ' 목요일 과목을 입력하세요', ' 금요일 과목을 입력하세요']
    )

def get_path():
    cwd = Path(__file__).parents[0]
    cwd = str(cwd)
    return cwd

def read_json(filename):
    cwd = get_path()
    with open(cwd+'/'+filename+'.json', 'r') as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    cwd = get_path()
    with open(cwd+'/'+filename+'.json', 'w') as file:
        json.dump(data, file, indent=4)
        
@login_required
@main_bp.route('/school')
def school():
    return render_template('school.html')