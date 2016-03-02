from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View, ListView
from datetime import datetime
from hashids import Hashids

from url_short_app.forms import BookmarkForm
from url_short_app.models import Bookmark, Click


class IndexView(ListView):
    model = Click


class CreateView(View):

    def get(self, request):
        bookmark_form = BookmarkForm()
        return render(request, 'create.html', {'form': bookmark_form})

    def post(self, request):
        hashids = Hashids(salt="here is some salt", min_length=5)
        form_instance = BookmarkForm(request.POST)
        if form_instance.is_valid():
            new_bookmark = form_instance.save()
            new_bookmark.shortened = hashids.encode(new_bookmark.pk)
            new_bookmark.save()
            Click.objects.create(bookmark=new_bookmark)

            return render(request, 'shortened.html', {'object': new_bookmark})
        else:
            self.get(request)


class BookmarkView(View):

    def get(self, request, short):
        bookmark = Bookmark.objects.get(shortened=short)
        click = Click.objects.get(bookmark=bookmark)
        click.accessed = datetime.now()
        click.access_count += 1
        click.save()

        return HttpResponseRedirect(bookmark.url)

