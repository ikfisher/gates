from django.contrib import admin
from cs.models import author
from cs.models import paper
from cs.models import remark

# Register your models here.

admin.site.register(author)
admin.site.register(paper)
admin.site.register(remark)

