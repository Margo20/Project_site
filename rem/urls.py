from django.conf.urls import url
from django.urls import path
from .views import indexOur_work_html, indexOur_work_bd, indexPrice, indexReviews, indexContacts, indexServices, index, footer_form, \
    saveuser_db, RegisterView, change_password, LogoutUserView, profile_user,  discount_form, \
    indexOrderCalculation, indexKapRem, indexEuroRem, LoginUserView
from . import views

app_name = 'rem'

urlpatterns = [
    path('', index, name='rem'),
    path('price/', indexPrice, name='price'),
    path('reviews/', indexReviews, name='reviews'),
    path('contacts/', indexContacts, name='contacts'),
    path('services/', indexServices, name='services'),
    path('order_calculation/', indexOrderCalculation, name='order_calculation'),
    path('kap_rem/', indexKapRem, name='kap_rem'),
    path('euro_rem/', indexEuroRem, name='euro_rem'),
    path('work_html/', indexOur_work_html, name='our_work_html'),
    path('accounts/send/', footer_form, name='footersend'),
    path('accounts/main/', discount_form, name='discount'),
    path('saveuser/', saveuser_db, name='saveuser'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/change_password/', change_password, name='change_password'),
    path('accounts/logout/', LogoutUserView.as_view(), name='logout'),
    path('accounts/profile/', profile_user, name='profile'),
    path('accounts/login/', LoginUserView.as_view(), name='login'),
    path('work_bd/', views.indexOur_work_bd, name='product_list'),
    path('work_bd/', views.indexOur_work_bd, name='ourwork_list'),
    path(r'^(?P<repair_slug>[-\w]+)/$', views.indexOur_work_bd, name='ourwork_list_by_repair'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='ourwork_detail'),
]

