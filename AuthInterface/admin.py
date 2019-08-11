from django.contrib import admin
from .models import User
from django.utils.translation import ugettext_lazy as _

admin.site.site_header = _('Voo Shop')
admin.site.site_title = _('Voo Shop')
# Register your models here.

admin.site.register(User)
