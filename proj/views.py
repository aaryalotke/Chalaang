from django.shortcuts import render, redirect
# import your predictor model here
# Ex
# from predictor import model
# if predictor file in the current folder
from app.models import Admin, User

def home(request):
    msg = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phnno = request.POST.get('phnno')
        loanamount = request.POST.get('loanamount')
        university = request.POST.get('university')
        course = request.POST.get('course')
        workexp = request.POST.get('workexp')
        # answer = model(name, age, email, phnno, loanamount, university, course, workexp)
        #print(name, age, email, phnno, loanamount, university, course, workexp)
        msg = {
            "flg": 1,
            "name": name,
            "age": age,
            "email": email,
            "answer": "Not Known for now"
        }
        user = User(name=name, age=age, email=email, phnno=phnno, loanamount=loanamount, 
                    university=university, course=course, workexp=workexp)
        user.save()
        print("User Saved")
        msg['flg'] = 1
    return render(request, 'index.html', msg)

def adminlog(request):
    msg = {}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        admins = Admin.objects.filter(email=email)
        for admin in admins:
            if admin.password == password:
                msg['flg'] = 1
                request.session['admin_id'] = admin.id
                return redirect(adminhome)
        msg['flg'] = 0
    return render(request, 'adminlog.html', msg)

def adminhome(request):
    msg = {}
    if request.session.get('admin_id'):
        users = User.objects.all()
        lst = []
        for user in users:
            lvl = {
                "name": user.name,
                "age": user.age,
                "email": user.email,
                "phnno": user.phnno,
                "loanamount": user.loanamount,
                "university": user.university,
                "course": user.course,
                "workexp": user.workexp
            }
            lst.append(lvl)
        msg['data'] = lst 
        return render(request, 'adminhome.html', msg)
    return redirect(home)
