from flask import Blueprint , render_template, redirect, request
import datetime as dt

contact_app = Blueprint('contact_app', __name__)

# 연락처 : 연락처 번호, 이름, 전화번호, 주소로 구성된 dict
contacts = []
cno = 1

# 연락처 목록 : GET
@contact_app.route("/contact/list")
def index():
    return render_template("contact/list.html", contacts=contacts)

# 연락처 작성 : GET으로 작성화면 보기, POST로 작성 후 연락처 목록으로 이동
@contact_app.route("/contact/write", methods=['GET', 'POST'])
def write():
    global cno
    if request.method=='GET':
        return render_template("contact/write.html")
    elif request.method=='POST':
        name = request.form.get('name')
        tel = request.form.get('tel')
        address = request.form.get('address')
        new_contact = {'cno':cno, 'name':name, 'tel':tel, 'address':address}
        contacts.append(new_contact)
        cno+=1
        return redirect("/contact/list")

# 연락처 번호로 찾아 연락처 출력
@contact_app.route("/contact/read")
def read() :
    cno = int(request.args.get('cno'))
    for contact in contacts:
        if contact['cno']==cno:
            return render_template("contact/read.html", contact=contact)
    return redirect("/contact/list")
    
# 연락처 변경
# - 사용자에게 연락처 번호, 전화번호, 주소를 받아온다
# - 연락처 번호로 연락처를 찾아 전화번호와 주소를 변경한다
@contact_app.route("/contact/update", methods=['post'])
def update() :
    cno = int(request.form.get('cno'))
    tel = request.form.get('tel')
    address = request.form.get('address')
    for contact in contacts:
        if contact['cno']==cno:
            contact['tel'] = tel
            contact['address'] = address
    return redirect(f"/contact/read?cno={cno}")

# 연락처 삭제 : 연락처 번호를 받아와 번호에 해당하는 연락처를 지운다
@contact_app.route("/contact/delete", methods=['post'])
def delete():
    cno = int(request.form.get('cno'))
    for contact in contacts:
        if contact['cno']==cno:
            contacts.remove(contact)
    return redirect("/contact/list")
