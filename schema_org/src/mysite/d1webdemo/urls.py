from django.urls import path

from . import views

app_name = 'd1webdemo'
urlpatterns = [
    # ex: /d1webdemo/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /d1webdemo/site/
    path('site/', views.sites, name='site'),
    # ex: /d1webdemo/site/5/
    path('site/<int:site_id>/', views.site_docs, name='sitedocs'),
    # ex: /d1webdemo/doc/5/
    path('doc/<int:document_id>/', views.document, name='document'),
    # ex: /d1webdemo/metadata/5/
    path('metadata/<int:document_id>/', views.metadata, name='metadata'),
    # ex: /d1webdemo/jsonld/5/
    path('jsonld/<int:document_id>/', views.jsonld, name='jsonld'),
]
