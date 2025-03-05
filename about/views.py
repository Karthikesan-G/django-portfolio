from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static


def about(request):
    about_me_details = {
        'experience': '2.5 +',
        'curr_company': 'Sybrant Technologies (P) Ltd.',
        'curr_company_loc': 'Chennai',
    }
    return render(request,"about.html",{"about_me_details": about_me_details})
