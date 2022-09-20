from itertools import product
from django.shortcuts import render
from django.views import generic as views

# Create your views here.
def home_view(request):
    template_name = "master/home.html"
    
    return render(request, template_name)


def about_view(request):
    template_name = "master/about.html"
    return render(request, template_name)


def contact_view(request):
    template_name = "master/contact.html"
    return render(request, template_name)


def login_view(request):
    template_name = "master/login.html"
    return render(request, template_name)

class DashboardView(views.View):
    template_name = "user/dashboard.html"

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        pass

    # def get_context_data(self) -> dict:
    #     user = self.request.user
    #     customer = Customer.objects.get(user=user)
    #     products = Product.objects.filter(enroll__student=student)
    #     profile = Profile.objects.filter(student=student).first()
    #     context = {"courses": courses, "profile": profile}

    #     return context



