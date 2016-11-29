from django.shortcuts import render
from immigrantApp.sqlFunctions import filterImmigrants, deleteImmigrant
from main.forms import ImmFilterForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


# Create your views here.
def home_page(request):
    data = {
        'firstname':request.GET.get('firstname',''),
        'lastname':request.GET.get('lastname',''),
        'gender':request.GET.get('gender',''),
        'country':request.GET.get('country',''),
        'ethnicity':request.GET.get('ethnicity',''),
        'spokenlang':request.GET.get('spokenlang',''),
        'processLocation':request.GET.get('processLocation',''),
    }

    form = ImmFilterForm(data)
    immigrants = filterImmigrants(firstName=data['firstname'], lastName=data['lastname'], gender=data['gender'], country=data['country'], 
    	ethnicity=data['ethnicity'], spokenLang=data['spokenlang'], procLoc=data['processLocation'])
    return render(request, 'index.html', {'immigrants': immigrants, 'form' : form})


def delete_imm(request, id):

	deleteImmigrant(id)
	return HttpResponseRedirect(reverse(home_page))
