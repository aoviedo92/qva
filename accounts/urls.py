from django.conf.urls import url
from django.urls import reverse_lazy

from . import views
from django.contrib.auth import views as dj_auth_views
urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^$', views.dashboard, name='dashboard'),
    url(r'^profile/$', views.ProfileView.as_view(), name='signup'),

    # url(r'^register/$', views.register, name='register'),
    url(r'^signup/$', views.signup, name='signup'),
    # url(r'^edit/$', views.edit, name='edit'),

    # login / logout urls
    url(r'^login/$', dj_auth_views.LoginView.as_view(), name='login'),
    url(r'^logout/$', dj_auth_views.LogoutView.as_view(), name='logout'),
    # url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),

    # change password urls
    url(r'^password-change/$', dj_auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change_form.html', success_url=reverse_lazy('accounts:password_change_done')),
        name='password_change'),
    # url(r'^password-change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    # url(r'^password-change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^password-change/done/$', dj_auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'), name='password_change_done'),

    # restore password urls
    # url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    # url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    # url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
    #     'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    # url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete',
    #     name='password_reset_complete'),

    # user profiles
    # url(r'^users/$', views.user_list, name='user_list'),
    # url(r'^users/follow/$', views.user_follow, name='user_follow'),
    # url(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),
]
