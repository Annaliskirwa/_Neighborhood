from django.urls.conf import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('profile/<username>/', views.profile, name='profile'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('hoods/',views.hoods,name='hoods'),
    path('newhood/', views.new_hood, name='newhood'),
    path('my_hood/<id>', views.user_hood, name='my_hood'),
    path('leave-hood/<id>', views.leave_hood, name='leave_hood'),
    path('update_hood/<id>/', views.update_hood, name='update_hood'),
    path('search/', views.search_hood, name='search'),
]