Django-bootstrap
================

Django-bootstrap is a empty base project to use with Django. It includes [twitter-bootstrap](http://twitter.github.com/bootstrap/) and few utilities to make starting a django project a bit more structured.

Installation
------------

1. Create a virtual enviroment for your project. By default, the settings assume the virtualenv is the parent directory of the project.

`virtualenv --no-site-packages my_project`

2. Go into your virtualenv

`cd my_project`

3. Now clone the repo with `git clone git://github.com/emperorcezar/Django-bootstrap.git my_project`.

Your project should be in `my_project/my_project`

4. In the virtualenv directory create you static and media directories

`mkdir static`
`mkdir media`

5. Go into the directory when you cloned Django-bootstrap and remove the remote

`git remote rm origin`

Now you can add your own origin.

6. Copy local_settings.py.example to local_settings.py and add admins, site_id, secret_key and whatever else you want not included in your repo.

7. Now edit settings/production.py to setup your production database and whatever else is unique to your production environment. Same for settings/development.py, but it's defaults should be suitable for most local development.

8. Same with settings/development.py.

Development
-----------

Provided are `devmanage.py` and `devserver`. These are wrappers that will use settings.development as your settings file.
settings.development uses sqlite and placed db/dev.db in the directory above your project (the same one that has `static` and `media` directories. So make sure that directory exists.

Production
----------

Whatever you're using for production, it will need to use settings.production instead of settings.