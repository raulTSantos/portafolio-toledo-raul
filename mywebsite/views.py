from django.shortcuts import render
from django.views.generic import ListView,CreateView,DeleteView
from django.views.generic import TemplateView
from .models import ProjectItem,VisitorIP
from .forms import ProjectItemForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.http import HttpResponse
from django.views.decorators.cache import cache_control

from django.utils import timezone
# Create your views here.

class IndexPageView(TemplateView):
    template_name= "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["projects"] = ProjectItem.objects.all()[:6]
        
        ip =self.get_client_ip_address(self.request)
        new_visitorIp = VisitorIP(ip_address= ip,create_at=timezone.now(),last_visit=timezone.now())

        found_vip = VisitorIP.objects.filter(ip_address= ip)
        if found_vip.exists():
            found_vip.update(last_visit=timezone.now())
        else:
            new_visitorIp.save()

        return context

    def get_client_ip_address(self,request):
        req_headers = request.META
        x_forwarded_for_value = req_headers.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for_value:
            ip_addr = x_forwarded_for_value.split(',')[-1].strip()
        else:
            ip_addr = req_headers.get('REMOTE_ADDR')
        return ip_addr


class PortFolioCreateView(LoginRequiredMixin,CreateView):
    template_name= "portfolio/create.html"
    form_class = ProjectItemForm
    success_url = reverse_lazy('projectpage')

class ProjectsPaginateView(ListView):
    #model =ProjectItem
    template_name= "frontend/projects.html"
    queryset = ProjectItem.objects.all()
    paginate_by=3

class PortFolioDeleteView(SuccessMessageMixin,DeleteView,LoginRequiredMixin):
    model = ProjectItem
    template_name = "portfolio/delete.html"
    success_message = "Registro eliminado con exito !"
    success_url = reverse_lazy("projectpage")

    


