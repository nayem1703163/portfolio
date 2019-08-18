from django.shortcuts import render,get_object_or_404
from .models import job
# Create your views here.
def home(request):
    jobs_var=job.objects
    return render(request,'jobs/home.html',{'jobkey':jobs_var})
def link(request):
    return render(request,'jobs/contact.html')
def job_detail(request,job_id):
    detail_job=get_object_or_404(job,pk=job_id)
    return render(request,'jobs/job_detail.html',{'job_detail':detail_job})
