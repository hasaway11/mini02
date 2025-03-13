from flask import Blueprint , render_template, redirect, request

supply_app = Blueprint('supply_app', __name__)

supplies = []
sno = 1

@supply_app.route("/supply/list")
def index():
    return render_template("supply/list.html", supplies=supplies)

@supply_app.route("/supply/add", methods=['get', 'post'])
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

@supply_app.route("/supply/read")
def read() :
    sno = int(request.args.get('sno'))
    print(sno)
    for s in supplies:
        print(s['sno'])
        if s['sno']==sno:
            return render_template("supply/read.html", supply=s)
    return redirect("/supply/list")        

@supply_app.route("/supply/inc", methods=['post'])
def inc():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno:
            s['count']=s['count']+1
    return redirect(f"/supply/read?sno={sno}")

@supply_app.route("/supply/dec", methods=['post'])
def desc():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno and s['count']>1:
            s['count']=s['count']-1
    return redirect(f"/supply/read?sno={sno}")


@supply_app.route("/supply/delete", methods=['post'])
def delete():
    sno = int(request.form.get('sno'))
    for s in supplies:
        if s['sno']==sno:
            supplies.remove(s)
    return redirect("/supply/list")