from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# Create your views here.

from .models import Project, Server, Server_connection_info, Project_info
from .scr.scr import get_project_configs, get_active_wells


def index(request):
    s = Server.objects.all()
    p = Project.objects.filter(supported=1)
    title = Project.__name__
    return render(request, 'param_table_for_customer/index.html', locals())

def wells(request, server_id):

    serv_info = Server_connection_info.objects.filter(pk=server_id)
    server = get_object_or_404(Server, pk=server_id)
    project = get_object_or_404(Project, server_id=server_id)
    title = '{} Server: [{}]'.format(project.name_ru,server.name)
    alchemy_server = get_project_configs(server.name)
    session = alchemy_server.session()
    active_wells = get_active_wells(session, project.network_id )

    return render(request, 'param_table_for_customer/wells.html', locals())

def table(request, well_id):
    well_id = well_id
    title = "IDI NAHUI"
    return render(request, 'param_table_for_customer/table.html', locals())

class IndexView(generic.ListView):
    template_name = 'param_table_for_customer/index.html'
    context_object_name = 'latest_shit_was_happened '

    def get_queryset(self):
        return Project.objects
