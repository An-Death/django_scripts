from django.contrib import admin
from .models import Project, Server, Server_connection_info, Project_info


# Register your models here.
admin.site.register(Server)
admin.site.register(Project)
admin.site.register(Server_connection_info)
admin.site.register(Project_info)