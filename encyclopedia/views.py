from django.shortcuts import redirect, render
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

def search(request):
    search = request.GET.get('q')
    test = util.get_entry(search)
    if test is None:
        return render(request, "encyclopedia/search.html")
    return redirect('title', search)
