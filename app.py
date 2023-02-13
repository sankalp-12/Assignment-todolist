from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# /// is used for relative paths for sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


# define a class ToDo for the schema of out database
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# to handle the case if database is accessed before creation of table
@app.before_first_request
def create_table():
    db.create_all()

# route to home page of the application
@app.route("/")
def home():
    # return all the exisitng records present using the query
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)

# route to add new tasks to the list
@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")

    # handle case if entered title of the new task is empty
    if title == "":
        flash("Empty input for task detected!", "error")
        return redirect(url_for("home"))

    # create new record
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

# route to toggle competion status of existing tasks
@app.route("/status/<int:todo_id>")
def status(todo_id):
    # obtain first result whose id matches, .one() instead of .first() can also be used 
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))

# route to delete the respective task from the list 
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # obtain first result whose id matches, .one() instead of .first() can also be used 
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

# to update an existing task in the list
@app.route("/update", methods=["POST"])
def update():
    todo_id = request.form.get("id")

    # obtain first result whose id matches, .one() instead of .first() can also be used 
    todo = Todo.query.filter_by(id=todo_id).first()

    # handle case if there exits no such record corresponding to the id entered by the user 
    if todo == None:
        flash("No such task detected!", "error")
        return redirect(url_for("home"))
        
    db.session.delete(todo)
    title = request.form.get("title")

    # handle case if entered title of the updated task is empty
    if title == "":
        flash("Empty input for task detected!", "error")
        return redirect(url_for("home"))

    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
