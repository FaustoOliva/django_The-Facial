from django.conf.urls import url
from api import views 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('alumno/', views.GetAlumno.as_view()),
    url('aula/', views.GetAula.as_view()),
    url('curso/', views.GetCurso.as_view()),
    url('materia/', views.GetMateria.as_view()),
    url('profesora/', views.GetProfesorA.as_view()),
    url('presencia/', views.GetPresencia.as_view()),
    url('cxmxpxa/', views.GetCxmxpxa.as_view()),
    url('related/', views.GetRelated.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)