from django.urls import path
from .views import *
from .views import user_login, user_logout, signup, home, base,service1,show_category
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('home/', home, name='home'),
    path('base/', base, name='base'),
    path('service/', service1, name='service1'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
     path('category/<int:category_id>/', show_category, name='category'),
      path('mobels_by_category/<int:category_id>/', views.mobels_by_category, name='mobels_by_category'),
     path('postdetail/<int:Mobels_id>/', views.post_detail, name='postdetail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

