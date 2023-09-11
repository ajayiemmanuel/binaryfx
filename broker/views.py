from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *

from .decorators import unauthenticated_user, allowed_users, admin_only




# Create your views here.

def index(request):
    context = {}
    return render (request, "broker/index.html", context)


def about(request):
    context = {}
    return render (request, "broker/about.html", context)


def contact(request):
    context = {}
    return render (request, "broker/contact.html", context)

def contact_us(request):
    context = {}
    return render (request, "broker/contact-us.html", context)

def education(request):
    context = {}
    return render (request, "broker/education.html", context)

def faq(request):
    context = {}
    return render (request, "broker/faq.html", context)

def news(request):
    context = {}
    return render (request, "broker/news.html", context)


def privacy_policy(request):
    context = {}
    return render (request, "broker/privacy-policy.html", context)


def privacy(request):
    context = {}
    return render (request, "broker/privacy.html", context)

@unauthenticated_user
def register(request):
    form = CreateUserForm ()
    if request.method == 'POST':
        form = CreateUserForm (request.POST)
        if form.is_valid ():
            user = form.save ()
            username = form.cleaned_data.get ('username')


            messages.success (request, 'Account was created for ' + username)

            return redirect ('login')

    context = {'form': form}
    return render (request, "broker/register.html", context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect ('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get ('username')
            password = request.POST.get ('password')

            user = authenticate (request, username = username, password = password)

            if user is not None:
                login (request, user)
                return redirect ('dashboard')
            else:
                messages.info (request, 'Username OR password is incorrect')

        context = {}
    return render (request, "broker/login.html", context)

def logoutUser(request):
    logout (request)
    return redirect ('login')


def terms_and_condition(request):
    context = {}
    return render (request, "broker/terms-and-condition.html", context)


def template_activate_account(request):
    context = {}
    return render (request, "broker/template-activate-account.html", context)
    
def support(request):
    context = {}
    return render (request, "broker/support.html", context)

def investments(request):
    context = {}
    return render (request, "broker/investments.html", context)

@login_required (login_url = "login")
def change_avatar(request):
    profile = request.user.profile
    form = ProfileForm (instance = profile)

    if request.method == 'POST':
        form = ProfileForm (request.POST, request.FILES, instance = profile)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/change-avatar.html", context)

@login_required (login_url = "login")
def change_password(request):
    context = {}
    return render (request, "broker/change-password.html", context)

@login_required (login_url = "login")
def crypto(request):
    context = {}
    return render (request, "broker/crypto.html", context)

@login_required (login_url = "login")
def dashboard(request):
    context = {}
    return render (request, "broker/dashboard.html", context)

@login_required (login_url = "login")
def deposit(request):
    context = {}
    return render (request, "broker/deposit.html", context)

@login_required (login_url = "login")
def fund_transfer(request):
    context = {}
    return render (request, "broker/fund-transfer.html", context)

@login_required (login_url = "login")
def kyc_form(request):
    context = {}
    return render (request, "broker/kyc-form.html", context)

@login_required (login_url = "login")
def kyc(request):
    context = {}
    return render (request, "broker/kyc.html", context)

@login_required (login_url = "login")
def market(request):
    context = {}
    return render (request, "broker/market.html", context)

@login_required (login_url = "login")
def settings(request):
    customer = request.user.customer
    form = CustomerForm (instance = customer)

    if request.method == 'POST':
        form = CustomerForm (request.POST, request.FILES, instance = customer)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/settings.html", context)


@login_required (login_url = "login")
def signal(request):
    context = {}
    return render (request, "broker/signal.html", context)

@login_required (login_url = "login")
def trade_history(request):
    context = {}
    return render (request, "broker/trade-history.html", context)


def verify(request):
    context = {}
    return render (request, "broker/verify.html", context)

@login_required (login_url = "login")
def withdrawal_info(request):
    account = request.user.account
    form = AccountForm (instance = account)

    if request.method == 'POST':
        form = AccountForm (request.POST, request.FILES, instance = account)
        if form.is_valid ():
            form.save ()

    context = {'form': form}
    return render (request, "broker/withdrawal-info.html", context)

@login_required (login_url = "login")
def withdrawal(request):
    context = {}
    return render (request, "broker/withdrawal.html", context)