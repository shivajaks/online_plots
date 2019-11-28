from django.shortcuts import render
from .models import Plotmodel,Appmodel,Employeemodel
def login(request):
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def check(request):
    u_id=request.POST.get("t1")
    u_pass=request.POST.get("t2")
    if u_id=='admin' and u_pass=='admin':
        return  index(request)
    else:
        return render(request,'login.html',{'data':"INVALID DATA"})


def about(request):
    return render(request,'about.html')


def newplot(request):
    return render(request,'plot.html',{'newplot':"wow"})


def editplot(request):
    return render(request,'plot.html',{'editplot':"wow2"})


def viewplot(request):
    wow3=Plotmodel.objects.all()
    return render(request,'plot.html',{'viewplot':wow3})


def newapp(request):
    return render(request,'appartment.html',{'newappartment':"wow4"})


def editapp(request):
    return  render(request,'appartment.html',{'editappartment':"wow5"})


def viewapp(request):
    wow6=Appmodel.objects.all()
    return render(request,'appartment.html',{'viewappartment':wow6})



def sales(request):
    return render(request,'sales.html',{'sales':"wow7"})



def payments(request):
    return render(request, 'sales.html', {'payments': "wow8"})


def reports(request):
    return render(request, 'sales.html', {'reports': 'wow9'})


def addemp(request):
    return render(request, 'employee.html', {'addemp': 'wow10'})


def viewemp(request):
    wow11=Employeemodel.objects.all()
    return render(request, 'employee.html', {'viewemp':wow11})


def soldplots(request):
    qs1=Plotmodel.objects.filter(status="Sold")
    qs2=Appmodel.objects.filter(status="Sold")
    wow1={'plot':qs1,'app':qs2}
    return render(request, 'plots.html',{'specific':wow1})


def resplots(request):
    qs1 = Plotmodel.objects.filter(status="Reserved")
    qs2 = Appmodel.objects.filter(status="Reserved")
    wow1 = {'plot': qs1, 'app': qs2}
    return render(request, 'plots.html', {'specific': wow1})


def vacantplots(request):
    qs1 = Plotmodel.objects.filter(status="Vacant")
    qs2 = Appmodel.objects.filter(status="Vacant")
    wow1 = {'plot': qs1, 'app': qs2}
    return render(request, 'plots.html', {'specific': wow1})


def saveplot(request):
    plot_no=request.POST.get("ta1")
    road_no=request.POST.get("ta2")
    survey_no=request.POST.get("ta3")
    c_p_sy=request.POST.get("ta4")
    t_sy=request.POST.get("ta5")
    o_exp=request.POST.get("ta6")
    facing=request.POST.get("ta7")
    status=request.POST.get("ta8")
    t_cost=request.POST.get("ta9")
    image=request.FILES["ta10"]
    Plotmodel(plotno=plot_no,roadno=road_no,surveyno=survey_no,cost_p_sqyard=c_p_sy,total_sqyard=t_sy,other_exp=o_exp,facing=facing,status=status,total_cost=t_cost,image=image).save()
    return render(request,'index.html',{'saveplot':"plot is saved"})


def saveapp(request):
    app_no=request.POST.get("t1")
    f_no=request.POST.get("t2")
    s_no=request.POST.get("t3")
    c_p_sy=request.POST.get("t4")
    t_sy=request.POST.get("t5")
    o_exp=request.POST.get("t6")
    facing=request.POST.get("t7")
    status=request.POST.get("t8")
    t_cost=request.POST.get("t9")
    image=request.FILES['t10']
    Appmodel(appno=app_no,floorno=f_no,surveyno=s_no,cost_p_sqyard=c_p_sy,total_sqyard=t_sy,other_exp=o_exp,facing=facing,status=status,total_cost=t_cost,image=image).save()
    return render(request,'index.html',{'saveapp':"appartment is saved"})


def saveemp(request):
    e_name=request.POST.get("t1")
    e_id=request.POST.get("t2")
    e_email=request.POST.get("t3")
    e_location=request.POST.get("t4")
    e_doj=request.POST.get("t5")
    e_remark=request.POST.get("t6")
    Employeemodel(E_name=e_name,E_id=e_id,E_email=e_email,E_location=e_location,E_doj=e_doj,E_remark=e_remark).save()
    return render(request,'index.html',{'saveemp':"employee saved"})


def delplot(request):
    p_no=request.GET.get("plotno")
    Plotmodel.objects.get(plotno=p_no).delete()
    return render(request,'index.html',{'delplot':'plot got deleted'})


def delemp(request):
    e_no=request.GET.get("idno")
    Employeemodel.objects.get(E_id=e_no).delete()
    return render(request,'index.html',{'delemp':'employee got deleted'})


def delapp(request):
    appno=request.GET.get("appno")
    Appmodel.objects.get(appno=appno).delete()
    return render(request,'index.html',{'delapp':'appartment got deleted'})
