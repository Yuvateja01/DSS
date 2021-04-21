from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,reverse
from .models import Upload
from django.views import generic
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    return  render(request,'userpage/index.html')

class UploadImg(LoginRequiredMixin,CreateView):
    model = Upload
    fields = ["title", "image","description"]


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UploadImg, self).form_valid(form)

    def get_success_url(self):
        return reverse('userpage:index')