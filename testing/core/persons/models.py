from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.files import FileField
from datetime import datetime, timedelta
from mezzanine.pages.models import Page, Orderable

class Profile(Page):
    GENDER_CHOISES = (
        (u'M', u'Mand'),
        (u'K', u'Kvinde'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=2, choices=GENDER_CHOISES)
    address = models.CharField(max_length=100, null=True, default='her')
    zipcode = models.IntegerField(default=0, null=True)
    city = models.CharField(max_length=100, null=True, default='Herrestrup')
    image = models.ImageField(max_length=254, null=True, blank=True, upload_to='profil-billeder')
    email = models.EmailField(max_length=128, null=True)
    phone_number = models.CharField(max_length=64, null=True)
    mobile_number = models.CharField(max_length=64, null=True)
    facebook = models.CharField(max_length=128, null=True, blank=True)
    hello_world_day = models.DateField(default=datetime.now())
    created = models.DateField(null=True, auto_now_add=True, default=datetime.now())
    last_modified = models.DateField(null=True, auto_now=True, default=datetime.now())

    def __unicode__(self):
        return '%s, %s' % (self.full_name(), self.gender)

    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def is_birthday(self):
        return self.hello_world_day == datetime.now().date()

class Resident(Page):
    profile = models.ForeignKey(Profile)
    history = models.TextField()

    class Meta:
        verbose_name = "Beboer"

class Staff(Page):
    STAFF_TITLE_CHOICES = (
        (u'D', u'Direktoer'),
        (u'V', u'Vice Dirktoer'),
        (u'A', u'Ansat'),
        (u'F', u'Flextid'),
    )
    profile = models.ForeignKey(Profile)
    staff_title = models.CharField(max_length=100, choices=STAFF_TITLE_CHOICES)
    about = models.TextField(blank=True)
    employed_since = models.IntegerField(max_length=4, null=True)

    class Meta:
        verbose_name = "Ansat"

class Family(Page):
    FAMILY_CHOICES = (
        (u'F', u'Far'),
        (u'M', u'Mor'),
        (u'B', u'Bror'),
        (u'S', u'Soester')

    )
    profile = models.ForeignKey(Profile)
    family_member = models.CharField(max_length=8, choices=FAMILY_CHOICES)

    class Meta:
        verbose_name = "Foraeldre"


