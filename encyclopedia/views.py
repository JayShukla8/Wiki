from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import NewPageForm
from . import util
import markdown2
import random

def index(request):
    """
    renders the index (home page)
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def g_entry(request, name):
    """
    function to render a wiki page based on request 
    if GET request, match the query and show results
    else show entry that is clicked on
    """
    
    if 'q' in request.GET:
        query = request.GET.get('q').strip()    
        if query:
            entries = util.list_entries()
            results = [entry for entry in entries if query.lower() in entry.lower()]  
            if (len(results) == 1) and (results[0].lower() == query.lower()):
                return redirect(reverse('wiki:entry', kwargs={'name':results[0]}))
            else:
                return render(request, "encyclopedia/search_results.html", {
                    "title":"Results",
                    "entries":results
                })
        else:
            return render(request, "encyclopedia/search_results.html", {
                "title":"404",
                "entries":results
            })


    entry = util.get_entry(name)

    if entry is None:
        return render(request, "encyclopedia/404.html")
    
    html_content = markdown2.markdown(entry)

    return render(request, "encyclopedia/entry.html", {
        "title": name,
        "content": html_content,
    })

def new_page(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)

        if form.is_valid():
            title=form.cleaned_data['title'].strip()
            content=form.cleaned_data['content'].strip()

            if util.get_entry(title) is not None:
                return render(request, "encyclopedia/new_page.html", {
                    "title": title,
                    "form": form,
                    "error": "An entry with this title already exists."
                })

            util.save_entry(title, content)
            return redirect(reverse('wiki:entry', kwargs={'name':title}))
    else:
        form = NewPageForm()
    return render(request, "encyclopedia/new_page.html", {
        "form":form
    })

def edit_page(request, name):
    entry = util.get_entry(name)
    if entry is None:
        return render(request, "encyclopedia/404.html")
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title'].strip()
            content = form.cleaned_data['content'].strip()
            util.save_entry(title, content)
            return redirect(reverse('wiki:entry', kwargs={'name':name}))
    else:
        form = NewPageForm(initial={'title':name, 'content': entry})
        return render(request, "encyclopedia/edit_page.html", {
            "title": name,
            "form": form,
        })

def random_page(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return g_entry(request, random_entry)