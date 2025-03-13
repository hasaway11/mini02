from flask import Blueprint , render_template, redirect, request
import datetime as dt

finance_app = Blueprint('finance_app', __name__)

# 지출 : 지출번호, 항목, 가격, 지출날짜로 구성된 dict
finances= []
fno = 1

# 지출 목록 : GET
@finance_app.route("/finance/list")
def index():
    hap = sum(item["price"] for item in finances)
    return render_template("finance/list.html", finances=finances, sum=hap)

# 지출 작성 : GET으로 작성화면 보기, POST로 작성 후 지출 목록으로 이동
@finance_app.route("/finance/write", methods=['GET', 'POST'])
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

# 지출 번호로 찾아 지출 항목 출력
@finance_app.route("/finance/read")
def read() :
    fno = int(request.args.get('fno'))
    for finance in finances:
        if finance['fno']==fno:
            return render_template("finance/read.html", finance=finance)
    return redirect("/finance/list")
    
# 지출 금액 변경
# - 사용자에게 지출 번호, 가격을 받아와 지출 번호로 지출 항목을 찾아 금액을 변경한다
@finance_app.route("/finance/update", methods=['post'])
def update() :
    fno = int(request.form.get('fno'))
    price = int(request.form.get('price'))
    for finance in finances:
         if finance['fno']==fno:
            finance['price']=price
    return redirect(f"/finance/read?fno={fno}")

# 지출 삭제 : 지출 번호를 받아와 번호에 해당하는 지출을 지운다
@finance_app.route("/finance/delete", methods=['post'])
def delete():
    fno = int(request.form.get('fno'))
    for finance in finances:
        if finance['fno']==fno:
            finances.remove(finance)
    return redirect("/finance/list")