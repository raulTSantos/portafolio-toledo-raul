from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PortFolioCreateView,IndexPageView,ProjectsPaginateView,PortFolioDeleteView

urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("home", IndexPageView.as_view(), name="index"),
    path("projects", ProjectsPaginateView.as_view(), name="projectpage"),
    path("projects/create", PortFolioCreateView.as_view(), name="create"),
    path("projects/delete/<int:pk>", PortFolioDeleteView.as_view(), name="delete")
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
