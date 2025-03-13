from flask import Blueprint , render_template, redirect, request

supply_app = Blueprint('supply_app', __name__)

# 비품 : 비품번호, 입고일, 이름, 개수로 구성된 dict
supplies = []
sno = 1

# 비품 목록 : GET
@supply_app.route("/supply/list")
def index():
    return render_template("supply/list.html", supplies=supplies)

# 비품 작성 : GET으로 작성화면 보기, POST로 작성 후 비품 목록으로 이동
@supply_app.route("/supply/add", methods=['GET', 'POST'])
def write():
    if request.method=='GET':
        return render_template("supply/add.html")
    elif request.method=='POST':
        global sno
        name = request.form.get('name')
        date = request.form.get('date')
        count = int(request.form.get('count'))
        new_supply = {'sno':sno, 'date':date, 'name':name, 'count':count}
        supplies.append(new_supply)
        sno+=1
        return redirect("/supply/list")

# 비품 번호로 찾아 비품 항목 출력
@supply_app.route("/supply/read")
def read() :
    sno = int(request.args.get('sno'))
    print(sno)
    for s in supplies:
        print(s['sno'])
        if s['sno']==sno:
            return render_template("supply/read.html", supply=s)
    return redirect("/supply/list")        

# 비품 개수 증가
@supply_app.route("/supply/inc", methods=['post'])
def inc():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno:
            s['count']=s['count']+1
    return redirect(f"/supply/read?sno={sno}")

# 비품 개수 감소
@supply_app.route("/supply/dec", methods=['post'])
def desc():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno and s['count']>1:
            s['count']=s['count']-1
    return redirect(f"/supply/read?sno={sno}")

# 비품 삭제 : 비품 번호를 받아와 번호에 해당하는 지출을 지운다
@supply_app.route("/supply/delete", methods=['post'])
def delete():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno:
            supplies.remove(s)
    return redirect("/supply/list")