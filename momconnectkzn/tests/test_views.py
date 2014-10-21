""" Tests for top-level MomConnect KZN views that aren't test elsewhere. """

from django.contrib.auth import get_user_model
from django.test import TestCase
from tastypie.test import ResourceTestCase
from tastypie.models import ApiKey


class ServiceRatingViewTests(ResourceTestCase):

    def setUp(self):
        super(ServiceRatingViewTests, self).setUp()
        self.user = get_user_model().objects.create_user(
            username='test', email='test@example.com', password='test_pw')
        self.api_key = ApiKey.objects.create(user=self.user)

    def test_top_level(self):
        auth = self.create_apikey(self.user.username, self.api_key.key)
        response = self.api_client.get(
            '/servicerating/api/v1/servicerating/useraccount/',
            format='json', authentication=auth)
        self.assertEqual(response.status_code, 200)
        data = self.deserialize(response)
        self.assertEqual(data['objects'], [])
        self.assertEqual(data['meta']['total_count'], 0)
