
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
from jobs import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home,name='homename'),
    path('<int:job_id>/',views.job_detail,name="job_detail_name"),
    path('blog/',include('blog.urls')),
    path('link/',include('jobs.urls'),name='linkname'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
