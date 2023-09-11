from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path ('', views.index, name = "index"),
    path ('about/', views.about, name = "about"),
    path ('contact/', views.contact, name = "contact"),
    path ('contact_us/', views.contact_us, name = "contact-us"),
    path ('education/', views.education, name = "education"),
    path ('faq/', views.faq, name = "faq"),
    path ('news/', views.news, name = "news"),
    path ('privacy_policy/', views.privacy_policy, name = "privacy-policy"),
    path ('privacy/', views.privacy, name = "privacy"),
    path ('register/', views.register, name = "register"),
    path ('login/', views.loginPage, name = "login"),
    path ('logout/', views.logoutUser, name = "logout"),
    path ('terms_and_condition/', views.terms_and_condition, name = "terms-and-condition"),
    path ('support/', views.support, name = "support"),
    path ('investments/', views.investments, name = "investments"),
    path ('change_avatar/', views.change_avatar, name = "change-avatar"),
    path ('change_password/', views.change_password, name = "change-password"),
    path ('crypto/', views.crypto, name = "crypto"),
    path ('dashboard/', views.dashboard, name = "dashboard"),
    path ('deposit/', views.deposit, name = "deposit"),
    path ('fund_transfer/', views.fund_transfer, name = "fund-transfer"),
    path ('kyc_form/', views.kyc_form, name = "kyc-form"),
    path ('kyc/', views.kyc, name = "kyc"),
    path ('market/', views.market, name = "market"),
    path ('settings/', views.settings, name = "settings"),
    path ('signal/', views.signal, name = "signal"),
    path ('trade_history/', views.trade_history, name = "trade-history"),
    path ('verify/', views.verify, name = "verify"),
    path ('withdrawal_info/', views.withdrawal_info, name = "withdrawal-info"),
    path ('withdrawal/', views.withdrawal, name = "withdrawal"),
    ]