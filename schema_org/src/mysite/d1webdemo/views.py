from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Site
from schema_org.web_demo import WebDemo


def process_site(sitemap_url):
    w = WebDemo(sitemap_url)
    w.run()

    site = Site(sitemap_url, timezone.now())
    site.save()

    for document in w.documents:
        site.document_set.create(**document)

    return site


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'd1webdemo/index.html'
    context_object_name = 'latest_site_list'

    def get_queryset(self):
        """
        Apparently we must override this???
        """
        return Site.objects.all()


def newsite(request):
    try:
        url = request.POST['sitemap_url']
    except KeyError:
        context = {'error_message': "You didn't indicate a site."}
        return render(request, 'd1webdemo/sites.html', context=context)
    else:
        site = process_site(url)
        path = reverse('d1webdemo:site_doc', args=(site.id,))
        return HttpResponseRedirect(path)


def site_no_id(request):
    """
    If someone monkeys with the /site/<int>/ URL, just redirect.
    """
    path = reverse('d1webdemo:index')
    return HttpResponseRedirect(path)


def site_docs(request, site_id):
    text = (
        f"Hello world, you're at the D1 webdemo for site {site_id}."
    )
    return HttpResponse(text)


def document(request, document_id):
    text = (
        f"Hello world, you're at the D1 webdemo overview for document "
        f"{document_id}."
    )
    return HttpResponse(text)


def metadata(request, document_id):
    text = (
        f"Hello world, you're at the D1 webdemo metadata page for "
        f"document {document_id}."
    )
    return HttpResponse(text)


def jsonld(request, document_id):
    text = (
        f"Hello world, you're at the D1 webdemo JSON-LD page for "
        f"document {document_id}."
    )
    return HttpResponse(text)
