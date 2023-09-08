#########################################################################
#
# Copyright (C) 2023 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################
from django.conf import settings
from subsites.utils import extract_subsite_slug_from_request
from geonode.themes.context_processors import custom_theme as geonode_custom_theme


def custom_theme(request, *args, **kwargs):
    custom_theme_payload = geonode_custom_theme(request)
    if settings.ENABLE_SUBSITE_CUSTOM_THEMES:
        subsite_obj = extract_subsite_slug_from_request(request)
        if subsite_obj:
            theme = subsite_obj.theme
            slides = theme.jumbotron_slide_show.filter(is_enabled=True)
            theme.is_enabled = True
            custom_theme_payload = {
                "custom_theme": theme or {},
                "slides": slides if slides.exists() else [],
            }

    return custom_theme_payload