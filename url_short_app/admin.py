from django.contrib import admin

from url_short_app.models import Click, Bookmark

admin.site.register([Bookmark, Click])
