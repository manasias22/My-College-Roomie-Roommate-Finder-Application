from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    context = {'username': request.session.get('username'), 'so': Vacantroom.objects.all(), 'ab':Vacanthouse.objects.all(), 'cd': Sellroom.objects.all() }
    return render(request,'./app/home.html', context)


def done(request):
    
    return render(request,'./app/done.html', context)

def login(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username= username, password = password)
        request.session['username'] = username

        if (Register.objects.filter(username=username, password = password).exists()):
            # login(request, user)
            context = {'username': request.session.get('username')}
            print(request.session.get('username'))
            return redirect("/",context)
            context = {'successs':False}

        else:
            context= {'success':True, 'soham':"Please enter correct username or password!!!"}
            return render(request, './app/login.html', context)



    return render(request, './app/login.html', context)




def register(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        birthdate = request.POST['birthdate']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        file = request.POST['file']
        try:
            send_mail(
            'Conguratulation!!!',
            'You have been successfully registered to our website',
            'settings.EMAIL_HOST_USER',
            [email], #here it can be also a list of emails
            fail_silently = False)
            print("mail send")
            print("mail is",email)
        except:
            print("mail sendaa")

        if ( len(username) and len(firstname) and len(lastname) and len(birthdate) and len(email) and len(phone) and len(password1) and len(password2)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (password1 != password2 ):
            context={'successs':True,'mssg':"Both passwords are not same!!"}

        elif (Register.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        elif (Roommate.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
    
        
        elif ( Register.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        elif ( Roommate.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}



        else:
            # ins = Customer.objects.create_user(username = username, first_name = first_name, last_name = last_name, email = email, password = password1, state = state, city =city, area = area, pincode = pincode, phone = phone)            
            ins = Register(username = username,firstname =firstname, lastname = lastname, email = email, birthdate = birthdate, phone = phone, file =file)
            ins.save()
            context = {'success': True}
            return render(request,'./app/register.html', context)
            
    return render(request,'./app/register.html', context)

def about(request):
    context = {'username': request.session.get('username') }
    return render(request,'./app/about.html', context)


def contact(request):
    context = {'username': request.session.get('username')}
    return render(request,'./app/contact.html', context)
    
def roommate(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.session.get('username')
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        room_mate_present = request.POST['room_mate_present']
        room_mate_require = request.POST['room_mate_require']
        name1 = request.POST['name1']
        name2 = request.POST['name2']
        name3 = request.POST['name3']
        name4 = request.POST['name4']
        name5 = request.POST['name5']
        name6 = request.POST['name6']
        name7 = request.POST['name7']
        name8 = request.POST['name8']
        name9 = request.POST['name9']
        name10 = request.POST['name10']
        qualification1 = request.POST['qualification1']
        qualification2 = request.POST['qualification2']
        qualification3 = request.POST['qualification3']
        qualification4 = request.POST['qualification4']
        qualification5 = request.POST['qualification5']
        qualification6 = request.POST['qualification6']
        qualification7 = request.POST['qualification7']
        qualification8 = request.POST['qualification8']
        qualification9 = request.POST['qualification9']
        qualification10 = request.POST['qualification10']
        for i in range(1,10):
            if(len(f"name{i}")) == 0 :
                f"name{i}" == 0
        for i in range(1,10):
          if(len(f"qualification{i}")) == 0 :
              f"qualification{i}"(i) == 0

        rent = request.POST['rent']
        file = request.POST['file']
        lastdate = request.POST['lastdate']
        address = state +" "+ city +" "+ area

        if ( len(username) and len(state) and len(city) and len(area) and len(rent) and len(file)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        else:
            ins = Vacantroom(username = username,address = address, state =state, city = city, area = area, room_mate_present = room_mate_present, room_mate_require = room_mate_require, name1 = name1, qualification1 = qualification1, name2 = name2, qualification2 =qualification2, name3 = name3, qualification3 = qualification3, name4 = name4, qualification4 = qualification4, name5 = name5, qualification5 = qualification5, name6 = name6, qualification6 = qualification6, name7 = name7, qualification7 = qualification7, name8 = name8, qualification8 = qualification8, name9 = name9, qualification9 = qualification9, name10 = name10, qualification10 = qualification10, rent =rent, file = file, lastdate = lastdate)
            ins.save()
            context = {'success': True}
            return render(request,'./app/roommate.html', context)
            
    return render(request,'./app/roommate.html', context)


def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('/')


def more(request, obj1, obj2, obj3):
    so = Vacantroom.objects.filter(username = obj1, address = obj2, rent = obj3 )
    ab = Vacanthouse.objects.filter(username = obj1, address = obj2, rent = obj3 )
    cd = Sellroom.objects.filter(username = obj1, address = obj2, sellprice = obj3 )
    context = {'so': so, 'ab': ab, 'cd': cd, 'usersername': request.session.get('username')}
    return render(request, './app/more.html', context)    


def vacanthouse(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.session.get('username')
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        rent = request.POST['rent']
        file = request.POST['file']
        lastdate = request.POST['lastdate']
        address = state +" "+ city +" "+ area

        if ( len(username) and len(state) and len(city) and len(area) and len(rent) and len(file)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        else:
            inss = Vacanthouse(username = username,address = address, state =state, city = city, area = area, rent =rent, file = file, lastdate = lastdate)
            inss.save()
            context = {'success': True}
            return render(request,'./app/vacanthouse.html', context)
            
    return render(request,'./app/vacanthouse.html', context)





def sellroom(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.session.get('username')
        state = request.POST['state']
        city = request.POST['city']
        area = request.POST['area']
        sellprice = request.POST['sellprice']
        file = request.POST['file']
        lastdate = request.POST['lastdate']
        address = state +" "+ city +" "+ area

        if ( len(username) and len(state) and len(city) and len(area) and len(sellprice) and len(file)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        else:
            ins = Sellroom(username = username,address = address, state =state, city = city, area = area, sellprice =sellprice, file = file, lastdate = lastdate)
            ins.save()
            context = {'success': True}
            return render(request,'./app/sellroom.html', context)
            
    return render(request,'./app/sellroom.html', context)


def search(request):
    context = {'nopage': False}
    search = request.GET['search']
    so = Vacanthouse.objects.filter(city = search)
    ab = Vacantroom.objects.filter(city = search)
    cd = Sellroom.objects.filter(city = search)
    context = {'so': so, 'ab':ab, 'cd': cd}
    return render(request, './app/search.html', context)


def final(request):
    if request.method == "POST":
        room_mate_present = request.POST['room_mate_present']
        room_mate_require = request.POST['room_mate_require']
        context = {'i': int(room_mate_present), 'j': int(room_mate_require), 'p':range(0,int(room_mate_present)), 'q':range(0,int(room_mate_require))}
        # return render(request,'./app/roommate.html', context)
        return render(request,'./app/roommate.html', context)
    return render(request, './app/final.html')