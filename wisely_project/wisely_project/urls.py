from django.conf.urls import include
from django.http.response import HttpResponse
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from settings import production
from wisely_project import view
from django.conf.urls import patterns, url

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', view.index),
                       url(r'^google46c8e47a069f43cd\.html$',
                           lambda r: HttpResponse("google-site-verification: google46c8e47a069f43cd.html",
                                                  mimetype="text/plain")),
                       url(r'BingSiteAuth\.xml', TemplateView.as_view(template_name='BingSiteAuth.xml')),
                       url(r'^alt$', view.index_alt),
                       url(r'^main$', view.index),
                       url(r'^learn-more$', TemplateView.as_view(template_name='learn-more-alt.html')),
                       url(r'^learn-more/alt$', TemplateView.as_view(template_name='learn-more-alt.html')),
                       url(r'^faq$', TemplateView.as_view(template_name='faq-alt.html')),
                       url(r'^faq/alt$', TemplateView.as_view(template_name='faq-alt.html')),
                       url(r'^about$', TemplateView.as_view(template_name='about-us.html')),
                       url(r'^privacy/$', TemplateView.as_view(template_name='privacy.html')),
                       # Examples:
                       # url(r'^$', 'wisely_project.views.home', name='home'),
                       # url(r'^wisely_project/', include('wisely_project.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r"^payments/", include("payments.urls")),
                       url(r'^users/', include('users.urls', namespace="users")),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^session/', include('studyroom.urls', namespace="studyroom")),
                       url('', include('social.apps.django_app.urls', namespace='social')),
                       url(r'^pledges/', include('pledges.urls', namespace="pledges")),
                       url(r'^blog/', include('cms.urls')),
                       url('activity/', include('actstream.urls')),
                       url(r'^sitemap\.xml$', TemplateView.as_view(template_name='sitemap.xml')),
)

if not production.DEBUG:
    urlpatterns += patterns('',
                            (r'^static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': production.STATIC_ROOT}),
    )