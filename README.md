# Wiki
Wiki Page Project: is a project by Harvard University CS50’s Web Programming with Python and JavaScript. This is week 3 of the course. Of course, we start counting 
weeks at 0. We are computer scientists after all. 💻 

🚀🚀🚀 

I made an interactive wikipedia. It lets you edit pages that already exists. Doesn't allow any duplicates. Allows you to create a new .md file with such ease and
add it to our page. Search through our wikipedia page which is useful for a big wikipedia page. The more you add you want a simple search to access it quicker.


🚀🚀🚀

## What did I use?
    😤😤😤  I used Django, Html, Bootstrap, and a little bit of CSS to complete this project. 



## Why did you use all your freetime for this project?
    🚀🚀🚀
    Because I need to get that intership by the summer. Toooooo the mooooon we go.
    🚀🚀🚀 

## Now explain the Django functions you used. 


    We created 9 functions total. To describe them brefiely let me explain. 

## The following three functions are in the util.py file

### def list_entries():
    Returns a list of all names of encyclopedia entries.
### def save_entry(title, content):
    Saves an encyclopedia entry, given its title and Markdown content. If an existing entry with the same title already exists, it is replaced.
### def get_entry(title):
    Retrieves an encyclopedia entry by its title. If no such entry exists, the function returns None.

## We use the functions above to create our other 6 functions that makes the Wiki Page very interactive like I explained above

### def index(request):📈📈
    returns all the current wiki pages with the list_entries() function

### def title(request, title): 🎄🎄
    if there is none we return an error page. if the title from url is valid we render the page with markdown

### def search(request): 🛰🛰
    Here we check to see if the util function from util.py returned anything. If test did not return anything then we 
    check if the user inputed any potential substrings to the strings. We check through the python re.search.
    Else if test did return something we just redirect them to our title function. 
### def newpage(request): 🍿🍿
    Here we render a form when you click the link. Once form is submitted we check if the title of the wiki page
    already exists. If the title exists we return an error message that prompts them to edit the page if they want.
    If the title is new then we save the new entry and redirect them to the new page they created.
### def editpage(request, title):🤝🤝
    When you click the edit button or link you will be shown the current markdown content. After you finish editing
    it you can click Save Page. Once clicked you are redirected back to the title function so you can see the same page
    but with the changes you made.
### def randompage(request): 🚀
    In this function we just randomly pick from our current wiki pages. Once elected we redirect you back to the title function
