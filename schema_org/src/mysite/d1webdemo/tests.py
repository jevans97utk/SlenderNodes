# standard library imports
import datetime

# 3rd party library imports
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

# local imports
from .models import Site


def create_site(url, days):
    """
    Create a site with the given URL and harvested the given number of days
    ago.
    """
    time = timezone.now() + datetime.timedelta(days=days)
    site = Site.objects.create(url=url, harvest_date=time)
    return site


class IndexViewTests(TestCase):

    def test_no_site_exists(self):
        """
        If no site exists, an appropriate message is displayed.
        """
        response = self.client.get(reverse('d1webdemo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sites are available.")
        self.assertQuerysetEqual(response.context['latest_site_list'], [])

    def test_one_site_with_past_harvest(self):
        """
        Sites with a harvest date in the past are displayed on the index page.
        """
        create_site(url="http://acme.org/sitemap.xml", days=-30)

        response = self.client.get(reverse('d1webdemo:index'))
        self.assertQuerysetEqual(
            response.context['latest_site_list'],
            ['<Site: http://acme.org/sitemap.xml>']
        )
