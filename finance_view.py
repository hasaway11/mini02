from flask import Blueprint , render_template, redirect, request
import datetime as dt

finance_app = Blueprint('finance_app', __name__)

finances= []
fno = 1

@finance_app.route("/finance/list")
def index():
    hap = sum(item["price"] for item in finances)
    return render_template("finance/list.html", finances=finances, sum=hap)

@finance_app.route("/finance/write", methods=['get', 'post'])
def write():
    global fno
    if request.method=='GET':
        return render_template("finance/write.html")
    elif request.method=='POST':
        item = request.form.get('item')
        price = int(request.form.get('price'))
        date = request.form.get('date')
        new_finance = {'fno':fno, 'item':item, 'price':price, 'date':date}
        finances.append(new_finance)
        fno+=1
        return redirect("/finance/list")


@finance_app.route("/finance/read")
def read() :
    fno = int(request.args.get('fno'))
    for finance in finances:
        if finance['fno']==fno:
            return render_template("finance/read.html", finance=finance)
    return redirect("/finance/list")
    
@finance_app.route("/finance/update", methods=['post'])
def update() :
    fno = int(request.form.get('fno'))
    price = int(request.form.get('price'))
    for finance in finances:
         if finance['fno']==fno:
            finance['price']=price
    return redirect(f"/finance/read?fno={fno}")

@finance_app.route("/finance/delete", methods=['post'])
def delete():
    fno = int(request.form.get('fno'))
    for finance in finances:
        if finance['fno']==fno:
            finances.remove(finance)
    return redirect("/finance/list")