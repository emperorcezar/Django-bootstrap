Django-bootstrap
================

Django-bootstrap is a empty base project to use with Django. It includes [twitter-bootstrap](http://twitter.github.com/bootstrap/) and few utilities to make starting a django project a bit more structured.

Installation
------------

Create a virtual enviroment for your project. By default, the settings assume the virtualenv is the parent directory of the project.

`virtualenv --no-site-packages my_project`

Go into your virtualenv

`cd my_project`

Now clone the repo with `git clone git://github.com/emperorcezar/Django-bootstrap.git my_project`.

Your project should be in `my_project/my_project`

In the virtualenv directory create you static directory

`mkdir static`

Go into the directory when you cloned Django-bootstrap and remove the remote

`git remote rm origin`

Now you can add your own origin.