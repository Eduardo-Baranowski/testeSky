from django.contrib import admin
from .models import *

admin.site.register(Paper)
admin.site.register(PaperItem)
admin.site.register(PaperItemAssociado)
