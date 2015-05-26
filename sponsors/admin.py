# -*- coding: utf-8 -*-
from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Sponsor


class CustomSponsor(admin.ModelAdmin):
    list_display = ['id', 'enabled', 'name', 'width', 'height', 'does_expire', 'expires_on', 'type', ]
    list_editable = ['enabled', 'name', 'width', 'height', 'does_expire', 'expires_on', 'type', ]
    list_filter = ['enabled', 'does_expire', 'type', ]
    list_display_links = ['id', ]
    # readonly_fields = ['', ]
    # search_fields = ['', ]

admin.site.register(Sponsor, CustomSponsor)
