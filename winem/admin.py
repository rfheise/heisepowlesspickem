from django.contrib import admin
from .models import Weeks,Vote,Student,Team,Game,Pick
from django.contrib.auth.models import Permission

admin.site.register(Weeks)
admin.site.register(Vote)
admin.site.register(Student)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Pick)
admin.site.register(Permission)
