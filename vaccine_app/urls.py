from django.urls import path
from . import views,urls
from django.conf import settings



urlpatterns = [
    path('', views.index,name="index"),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('register', views.register_user,name="register"),
    # path('centeradd_upload',views.centeradd_upload,name='centeradd_upload'),
    # path('loggedin/<district_or_center>/<name>/',views.loggedin,name='loggedin'),
    path('login',views.login_gen,name='login_gen'),
    path('logout',views.logout,name='logout'),
    path('provideaccess',views.provideaccess,name='provideaccess'),

    path('dashboard/district/<name>/',views.district_dash,name='district_dash'),
    path('district/<str:name>/updateArrivalTimeDistrict/<int:lotId>/',views.updateArrivalTimeDistrict,name='updateArrivalTimeDistrict'),


    path('dashboard/center/<name>/',views.center_dash,name='center_dash'),
    path('dashboard/',views.dashboard,name='dashboard'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)