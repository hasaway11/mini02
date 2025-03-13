from flask import Blueprint , render_template, redirect, request
import datetime as dt

todo_app = Blueprint('todo_app', __name__)

# 할일 : 할일번호, 할일, 등록일, 마감일, 내용, 완료여부로 구성된 dict
#        사용자에게서 받아오는 데이터는 할일, 마감일, 내용
todos = []
tno = 1

# 할일 목록 : GET
@todo_app.route("/todo/list")
def index():
    return render_template("todo/list.html", todos=todos)

# 할일 작성 : GET으로 작성화면 보기, POST로 작성 후 할일 목록으로 이동
# 할일, 마감일, 내용은 사용자 입력
# 할일번호, 작성일, finish는 백엔드에서 처리
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

# 할일 번호로 찾아 할일 항목 출력
@todo_app.route("/todo/read")
def read() :
    tno = int(request.args.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            return render_template("todo/read.html", todo=todo)
    return redirect("/todo/list")

# 완료 처리 -> 완료 처리 후 읽기 주소로 이동
@todo_app.route("/todo/finish", methods=['post'])
def finish():
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todo['finish']=True
    return redirect(f"/todo/read?tno={tno}")

# 삭제 처리
@todo_app.route("/todo/delete", methods=['post'])
def delete() :
    tno = int(request.form.get('tno'))
    for todo in todos:
        if todo['tno']==tno:
            todos.remove(todo)
    return redirect("/todo/list")
