# -*- coding: utf-8 -*-
from django.views.generic import ListView

from .models import Sponsor


class SponsorsList(ListView):
    model = Sponsor
    template_name = "sponsors/sponsors_list.html"
