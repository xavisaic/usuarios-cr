from flask import Flask, render_template, request, redirect, session
from users import User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_form', methods=["POST"])
def send_form():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    print(data)
    User.save(data)
    

    return redirect('/resultados')


@app.route('/resultados')
def show():
    users = User.get_all()
    print(users)

    return render_template('resultados.html', usuarios = users)


if __name__ == "__main__":
    app.run(debug=True)