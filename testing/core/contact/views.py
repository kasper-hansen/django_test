from django.http import HttpResponseRedirect, HttpResponse
from django.template.context import RequestContext
from core.contact.models import ContactUs
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render_to_response

def contact(request):
    if request == "POST":
        form = ContactUs(request.POST)
        if form.is_valid():
            # Opret i kontakt mappe

                if form.send_to_email != '':
                    subject = request.POST.get('subject', '')
                    message = request.POST.get('message', '')
                    from_email = request.POST.get('from_email', '')
                    if subject and message and from_email:
                        try:
                            send_mail(subject, message, from_email, ['admin@example.com'])
                        except BadHeaderError:
                            return HttpResponse('Invalid header found.')
                        return render_to_response('thanks.html',
                                {'confirm_message': form.confirm_message},
                                context_inctance = RequestContext(request))
                    else:
                        # In reality we'd use a form class
                        # to get proper validation errors.
                        return HttpResponse('Make sure all fields are entered and valid.')

def thanks(request):
    form = ContactUs(request)
    if form.confirm_message:
        return  render_to_response()





