from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    return render(request, "entry/index.html", {
        "title": entry,
        "entry": util.get_entry(entry),
    })


def handler404(request, exception):
    return render(request, '404.html', status=404)
