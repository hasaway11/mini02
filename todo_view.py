from flask import Blueprint , render_template, redirect, request
import datetime as dt

todo_app = Blueprint('todo_app', __name__)

todos = []
tno = 1

@todo_app.route("/todo/list")
def index():
    return render_template("todo/list.html", todos=todos)

@todo_app.route("/todo/write", methods=['get','post'])
def write():
    if request.method=='GET':
        return render_template("todo/write.html")
    elif request.method=='POST':
        global tno
        title = request.form.get('title')
        reg_date = dt.datetime.now().strftime('%Y-%m-%d')
        deadline = request.form.get('date')
        content = request.form.get('content')
        new_todo = {'tno':tno, 'title':title, 'reg_date':reg_date, 'deadline':deadline, 'content':content, 'finish':False}
        todos.append(new_todo)
        tno+=1
        return redirect("/todo/list")

@todo_app.route("/todo/read")
def read() :
    tno = int(request.args.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            return render_template("todo/read.html", todo=todo)
    return redirect("/todo/list")

@todo_app.route("/todo/finish", methods=['post'])
def finish():
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todo['finish']=True
    return redirect(f"/todo/read?tno={tno}")


@todo_app.route("/todo/delete", methods=['post'])
def delete() :
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todos.remove(todo)
    return redirect("/todo/list")
