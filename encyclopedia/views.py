from django.shortcuts import redirect, render
from . import util
from markdown import markdown
import re
from django.contrib import messages
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def title(request, title):
    # if there is none we return an error page 
    if util.get_entry(title) is None:
        return render(request, "encyclopedia/error.html",{
            "title": title.capitalize()
        })
    # if the title from url is valid we render the page with markdown
    return render(request, "encyclopedia/wiki.html", {
        "title": title.capitalize(),
        "entry": markdown(util.get_entry(title))
    })


def search(request):
    """
    Here we check to see if the util function from util.py returned anything. If test did not return anything then we 
    check if the user inputed any potential substrings to the strings. We check through the python re.search.
    Else if test did return something we just redirect them to our title function. 
    """
    search = request.GET.get('q')
    test = util.get_entry(search)
    entries = util.list_entries()
    if test is None:
        found = []
        for entry in entries:
            if re.search(search.lower(), entry.lower()):
                found.append(entry)
        return render(request, "encyclopedia/search.html", {
            "search": search,
            "found" : found
        })
    return redirect('title', search)

def newpage(request):
    """
    Here we render a form when you click the link. Once form is submitted we check if the title of the wiki page
    already exists. If the title exists we return an error message that prompts them to edit the page if they want.
    If the title is new then we save the new entry and redirect them to the new page they created.
    """
    if request.method == "GET":
        return render(request, "encyclopedia/new.html" )
    if request.method == "POST":
        content = request.POST.get('text')
        pagetitle = request.POST.get('title')
        if util.get_entry(pagetitle) is None:
            util.save_entry(pagetitle, content)
            return title(request, pagetitle)
        else:
            messages.info(request, 'This page already exists! You can either change the title of your new Wiki Page or ')
            return render(request, "encyclopedia/new.html", {
                "title": pagetitle,
                "content": content,
            })

def editpage(request, title):
    """
    When you click the edit button or link you will be shown the current markdown content. After you finish editing
    it you can click Save Page. Once clicked you are redirected back to the title function so you can see the same page
    but with the changes you made.
    """
    if request.method == "GET":
        entry = util.get_entry(title)
        return render(request, "encyclopedia/editpage.html", {
            "title": title, 
            "content": entry
        })
    if request.method == "POST":
        content = request.POST.get('text')
        util.save_entry(title, content)
        return redirect('title', title)

def randompage(request):
    # In this function we just randomly pick from our current wiki pages. Once elected we redirect you back to the title function
    entries = util.list_entries()
    elected = random.choice(entries)
    return redirect('title', elected)

