from django.conf.urls import url
from basic_app import views 


app_name ='basic_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    #url(r'^login/$',views.loginview,name='loginview'),
    #url(r'^logout/$',views.logoutview,name='logoutview'),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^profile/$',views.userprofile,name='profile'),
    url('blogpost/(?P<slug>[^/]+)/$',views.blogpost,name='post'),
    url(r'^logout/$',views.user_logout,name='logout'),    

    #path(r'^blogpost/<str:slug>',views.blogpost,name='blogpost')
    #url(r'^home/$',HomeView.as_view(),name='home')
]


#if settings.DEBUG:
    