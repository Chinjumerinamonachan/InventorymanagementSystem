from itertools import product
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic as views
from user.forms import UserRegistrationForm
from user.models import Profile
from django.urls import reverse_lazy

from master.forms import FeedbackForm

from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

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


class FeedbackView(views.FormView):
    template_name = "master/feedback.html"
    form_class = FeedbackForm
    success_url = reverse_lazy("master:home")

    def form_valid(self, form):
        data = form.cleaned_data
        subject = "Thank you for your valuable feedback!"
        message = f"""
        Hi {data.get("name")},

        This is an auto generated mail. We will reach you soon.

        Thanks and Regards,
        Learning Team
        """
        from_email = settings.EMAIL_HOST_USER
        to_email = [
            data.get("email"),
        ]
        send_mail(subject=subject, message=message, from_email=from_email, recipient_list=to_email)
        return super().form_valid(form)




