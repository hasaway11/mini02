from flask import Blueprint , render_template, redirect, request
import datetime as dt

contact_app = Blueprint('contact_app', __name__)

contacts = []
cno = 1

@contact_app.route("/contact/list")
def index():
    return render_template("contact/list.html", contacts=contacts)

@contact_app.route("/contact/write", methods=['get', 'post'])
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

@contact_app.route("/contact/read")
def read() :
    cno = int(request.args.get('cno'))
    for contact in contacts:
        if contact['cno']==cno:
            return render_template("contact/read.html", contact=contact)
    return redirect("/contact/list")
    
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

@contact_app.route("/contact/delete", methods=['post'])
def delete():
    cno = int(request.form.get('cno'))
    for contact in contacts:
        if contact['cno']==cno:
            contacts.remove(contact)
    return redirect("/contact/list")
