from flask import Blueprint,render_template,redirect,url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

    
@views.route('/result', methods=['POST'])
def result():
    return render_template('result.html')

@views.route("/go_to_quiz")
def go_to_quiz():
    return redirect(url_for("views.result"))


        

