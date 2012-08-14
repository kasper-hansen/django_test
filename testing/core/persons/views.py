# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.context import RequestContext
from models import *
from django.shortcuts import render_to_response, get_object_or_404


def staff_members(request):

    staff_list = Staff.objects.all()
    for s in staff_list:
        print s.about
    print "ARRRGH!!!!"
    return render_to_response(
        'persons/index.html',
        {'staff_list': staff_list },
        context_instance=RequestContext(request))

def staff(request, id):
    try:
        s = get_object_or_404(Staff, id)
    except (KeyError, Staff.DoesNotExist):
        return render_to_response('persons/index.html', {'error_message': 'Profil findes ikke'}, context_intance=HttpResponse(request))



#@login_required
def resident_profile(request):
    p = Profile.objects.get(pk=1)
    return render_to_response('persons/details.html',
            {'profiles': p},
        context_instance=RequestContext(request))

