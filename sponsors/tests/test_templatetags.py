# -*- coding: utf-8 -*-
from model_mommy import mommy

from django.test import TestCase
from django.template import Context, Template


class SponsorsTagTest(TestCase):
    """
    TestCase for templatetag 'show_sponsors'
    """

    TEMPLATE = Template("{% load sponsors_extras %} {% show_sponsors %}")

    def setUp(self):
        mommy.make('Sponsor', _quantity=2)

    def test_tag_show_ok(self):
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn('<div class="sponsors', rendered)

    def test_tag_show_platinum_ok(self):
        mommy.make('Sponsor', type=1)
        rendered = self.TEMPLATE.render(Context({}))
        self.assertIn('<div class="sponsors platinum', rendered)
