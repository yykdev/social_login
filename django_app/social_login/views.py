from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login as auth_login, logout as django_logout
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers
from django.conf import settings
from django.shortcuts import render, redirect

from social_login.forms import LoginForm


@login_required
def profile(request):
    print('profile')
    return render(request, 'profile.html')


def login(request):
    providers = []
    for provider in get_providers():
        try:
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    return auth_login(
        request,
        authentication_form=LoginForm,
        template_name='login.html',
        extra_context={'providers': providers}
    )

def logout(request):
    django_logout(request)
    return redirect('index')