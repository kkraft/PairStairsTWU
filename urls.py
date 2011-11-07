from django.conf.urls.defaults import patterns, include, url
from pairstairs import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^add_programmer/', views.add_programmer),
    url(r'^pairstairs/', views.pairstairs),
    url(r'^add_count/(?P<pair1_id>.+?)/(?P<pair2_id>.+?)$', views.add_count),
    url(r'^delete_programmers/', views.delete_programmers),
    url(r'^delete_programmer/(?P<person_id>.+?)', views.delete_programmer),
    url(r'^reset_counts/', views.reset_counts)


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
