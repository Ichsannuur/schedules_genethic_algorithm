from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^lecturers/', include("penjadwalan_genetika.backoffice.lecturers.urls",
                                namespace='lecturers')),
    url(r'^classrooms/', include("penjadwalan_genetika.backoffice.classrooms.urls",
                                 namespace='classrooms')),
    url(r'^study-programs/', include("penjadwalan_genetika.backoffice.study_programs.urls",
                                     namespace='study_programs'))
]
