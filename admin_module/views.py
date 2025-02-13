from django.contrib import messages
from django.shortcuts import render, redirect

from admin_module.forms import *
from admin_module.models import *


def adminlogin(request):
    return render(request, "admin_panel/login.html")


def admin_check(request):
    ausername = request.POST.get("admin_username")
    apassword = request.POST.get("admin_password")
    try:
        AdminLoginModel.objects.get(username=ausername, password=apassword)
        request.session['status'] = True
        return redirect('admin_dashboard')

    except AdminLoginModel.DoesNotExist:
        messages.error(request, "Sorry Invalid Details")
        return redirect('adminlogin')


def admin_dashboard(request):
    return render(request, "admin_panel/dashboard.html")


def admin_logout(request):
    request.session['status'] = False
    return redirect('admin_login')


def open_state(request):
    return render(request, 'admin_panel/open_state.html', {"sf": StateForm(), "sdata": StateModel.objects.all()})


def save_state(request):
    sf = StateForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_state')
    else:
        return render(request, "admin_panel/open_state.html", {"sf": sf})


def update_state(request):
    sno = request.GET.get("sno")
    sname = request.GET.get("sname")
    d1 = {"sno": sno, "sname": sname}
    return render(request, "admin_panel/open_state.html", {"update_data": d1, "sdata": StateModel.objects.all()})


def update_state_data(request):
    sno = request.POST.get("s1")
    sname = request.POST.get("s2")
    StateModel.objects.filter(state_no=sno).update(state_name=sname)
    return redirect('open_state')


def delete_state(request):
    sno = request.GET.get("sno")
    StateModel.objects.filter(state_no=sno).delete()
    return redirect('open_state')


def open_city(request):
    return render(request, 'admin_panel/open_city.html', {"sf": CityForm(), "sdata": CityModel.objects.all()})


def save_city(request):
    sf = CityForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_city')
    else:
        return render(request, "admin_panel/open_city.html", {"sf": sf})


def update_city(request):
    cno = request.GET.get("cno")
    cname = request.GET.get("cname")
    d1 = {"cno": cno, "cname": cname}
    return render(request, "admin_panel/open_city.html", {"update_data": d1, "cdata": CityModel.objects.all()})


def update_city_data(request):
    cno = request.POST.get("c1")
    cname = request.POST.get("c2")
    CityModel.objects.filter(city_no=cno).update(city_name=cname)
    return redirect('open_city')


def delete_city(request):
    cno = request.GET.get("cno")
    CityModel.objects.filter(city_no=cno).delete()
    return redirect('open_city')


def open_area(request):
    return render(request, 'admin_panel/open_area.html', {"sf": AreaForm(), "sdata": AreaModel.objects.all()})


def save_area(request):
    sf = AreaForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_area')
    else:
        return render(request, "admin_panel/open_area.html", {"sf": sf})


def update_area(request):
    ano = request.GET.get("ano")
    aname = request.GET.get("aname")
    d1 = {"ano": ano, "aname": aname}
    return render(request, "admin_panel/open_area.html", {"update_data": d1, "cdata": AreaModel.objects.all()})


def update_area_data(request):
    ano = request.POST.get("a1")
    aname = request.POST.get("a2")
    AreaModel.objects.filter(area_no=ano).update(area_name=aname)
    return redirect('open_area')


def delete_area(request):
    ano = request.GET.get("ano")
    AreaModel.objects.filter(area_no=ano).delete()
    return redirect('open_area')


def open_type(request):
    return render(request, 'admin_panel/open_type.html', {"sf": RestaurantTypeForm(), "sdata": RestaurantTypeModel.objects.all()})


def save_type(request):
    sf = RestaurantTypeForm(request.POST)
    if sf.is_valid():
        sf.save()
        return redirect('open_type')
    else:
        return render(request, "admin_panel/open_type.html", {"sf": sf})


def update_type(request):
    tno = request.GET.get("tno")
    tname = request.GET.get("tname")
    d1 = {"tno": tno, "tname": tname}
    return render(request, "admin_panel/open_type.html", {"update_data": d1, "cdata": RestaurantTypeModel.objects.all()})


def update_type_data(request):
    tno = request.POST.get("t1")
    tname = request.POST.get("t2")
    AreaModel.objects.filter(no=tno).update(type_name=tname)
    return redirect('open_type')


def delete_type(request):
    tno = request.GET.get("tno")
    RestaurantTypeForm.objects.filter(no=tno).delete()
    return redirect('open_type')
