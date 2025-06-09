
from django.contrib import admin
from django.urls import path, include
from .import views, user_login
from django.conf import settings
from django.conf.urls.static import static
admin.site.site_header = "Welcome To Progromming Library"
admin.site.site_title = "Welcome To Progromming Library"
admin.site.index_title = "Welcome To Progromming Library"
urlpatterns = [
    path('admin/', admin.site.urls),

    path('base', views.BASE, name='base'),

    #Main page (first page )
    path('', views.HOME, name='home'),

    path('contact', views.CONTACT_US, name='contact'),
    path('about', views.ABOUT_US, name='about'),

    path('accounts/register', user_login.REGISTER, name='register'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('doLogin', user_login.DO_LOGIN, name='doLogin'),
    path('course-single-v5', views.COURSESINGLE, name='course-single-v5'),
    path('course-list-v6', views.COURSEPAGE, name='course-list-v6'),

    path('accounts/profile', user_login.PROFILE,  name='profile'),
    path('accounts/profile/update', user_login.PROFILE_UPDATE, name='profile_update'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
