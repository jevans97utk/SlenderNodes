from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):

    def test_no_site_exists(self):
        """
        If no site exists, an appropriate message is displayed.
        """
        response = self.client.get(reverse('d1webdemo:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No sites are available.")
        self.assertQuerysetEqual(response.context['latest_site_list'], [])
