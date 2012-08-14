from django.db import models
from mezzanine.pages.models import Page
from django.forms import *

class ContactUs(Form):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=164)
    phone_number = CharField(max_length=255, required=False)
    message = models.TextField()
    created = models.DateField(auto_created=True)
    confirm_message = models.TextField(help_text="Skriv en 'Tak for besked tekst'")
    send_to_email = models.EmailField(max_length=255, help_text="Email addresse som besked skal sendes til")


    class Meta:
        verbose_name = "Kontakt os"

    def __unicode__(self):
        return 's%, s%' % (self.name, self.email)



