# taskmate
Django Project : A simple todolist, explaining basic CRUD operations.
Gives a brief understanding about: 
1) virtual environment
2) how to start project in Django, how to make apps
3) MVT => Models, Views, Templates
4) URL Mapping
5) Migrations and Migrate
   python manage.py makemigrations -> after making model this is the first step we to do. As we are now just having those fields in models.py file. We want these fields in our db.
                                      It convert our file to sql queries and a new file can be seen in migration folder.
   python manage.py migrate -> to make all those migrations. convert sql queries to tables.
6) How to connect    url -> views ---use model(if req.)--> render template
7) Why do we need Jinja 2?
    Sandboxed Execution: It provides a protected framework for automation of testing programs, whose behaviour is unknown and must be investigated.
    HTML Escaping: Jinja 2 has a powerful automatic HTML Escaping, which helps preventing Cross-site Scripting (XSS Attack). There are special characters like >,<,&, etc. which carry special meanings in the templates. So, if you want to use them as regular text in your documents then, replace them with entities. Not doing so might lead to XSS-Attack.
    Template Inheritance: This is the most important feature. If we having many templates to render and we notice that all these templates share a common section among them so it's
    better to make a basic common file for that section which will be inherited by all other templates.
8) Adding a form and accepting the i/p.
9) Django Authentication & Autherisation => Authentication means to check that you are u and authorisation means what you can do.



