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


@app.route('/user/<int:id>')
def single_user(id):
    data = {
        'id': id
    }

    print(f'obteniendo el usuario de ID {id}')
    user = User.elige_uno(data)

    return render_template('mostrar_usuario.html', user=user)

@app.route('/user/edit/<int:id>')
def edit(id):

    data = {
        'id':id
    }
    user = User.elige_uno(data)
    return render_template('edit.html', user=user)

@app.route('/user/update', methods=["POST"])
def update ():
    User.actualiza(request.form)
    return redirect('/resultados')


@app.route('/user/eliminar/<int:id>')
def eliminar(id):
    data={
        "id":id
    }
    User.delete(data)
    return redirect('/resultados')






if __name__ == "__main__":
    app.run(debug=True)