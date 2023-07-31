from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
# path_wkhtmltopdf = r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'

# config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# pdfkit.from_url("http://google.com", "out.pdf", configuration=config)
import io

# Create your views here.
def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        school=request.POST.get("school","")
        degree=request.POST.get("degree","")
        university=request.POST.get("university","")
        skills=request.POST.get("skills","")
        about_you=request.POST.get("about_you","")
        previous_work=request.POST.get("previous_work","")

        profile=Profile(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skills=skills,about_you=about_you,previous_work=previous_work)
        profile.save()
    return render(request, "accept.html")

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template("resume.html")
    html=template.render({'user_profile':user_profile})
    # option={
    #     'page-size':'Letter',
    #     'encoding':'UTF-8'
    # }
    pdf=pdfkit.from_string(html,False)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request,'list.html',{'profile':profile})
