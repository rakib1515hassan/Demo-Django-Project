from django.shortcuts import render
from django.views import generic


# Create your views here.
class Home(generic.TemplateView):
    template_name = "Dashbord/home.html"

    def get(self, request, *args, **kwargs):

        # context = {
            
        # }

        return render(request, self.template_name)