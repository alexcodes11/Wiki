from django.shortcuts import render
from . import util
from markdown import markdown

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/error.html",{
            "title": title.capitalize()
        })
        
    return render(request, "encyclopedia/wiki.html", {
        "title": title.capitalize(),
        "entry": markdown(util.get_entry(title))
    })