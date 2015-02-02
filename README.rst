#####
Gipsy
#####

Set of libraries used for the gipsy project. Those librairies are only compatible with django >= 1.6.

*******
Install
*******

It is strongly recommanded to install this theme from GIT with PIP onto you project virtualenv.

From PyPi

.. code-block::  shell-session

    pip install django-gipsy

From Github

.. code-block::  shell-session

    https://github.com/RevSquare/gipsy#egg=gipsy


*************
GISPY TOOLBAR
*************

This Django app manages a toolbar for admins with shortcuts to easily navigate to most relevant admin features.

setup
=====

Simply add the app in your installed apps list in settings.py

.. code-block::  python

    INSTALLED_APPS = (
        ...
        'gipsy.toolbar'
        ...
    )

Then install your model with 

.. code-block::  shell

    python manage.py syncdb

In case you are using South, you can alternatively do:

.. code-block::  shell

    python manage.py migrate gipsy.toolbar
    
    
Setup your menu items in the admin.

And finaly, install the toolbar in your templates with a template tag:

.. code-block::  html

    {% load gipsy_toolbar %}
    
    {% gipsy_toolbar %}

For the admin part, you will need to overwrite templates with the same code as above: {templates}/admin/base.html 

If you are using a cache engine such as Varnish, you can use a bundled middleware in order to set a cookie that you can use to deactivate cache to display the toolkbar for staff admins. Happy to hear abotu a cleaner solution.

.. code-block::  python

    MIDDLEWARE_CLASSES = (
        ...
        'gipsy.toolbar.middleware.GipsyToolbarMiddleware',
        ...
    )


***************
GISPY DASHBOARD
***************

This Django app adds tons of cool features in the django admin. For now it works only with grappelli, so make sure you have it installed.

setup
=====

Simply add the app in your installed apps list in settings.py.

IMPORTANT! You need to install it BEFORE any other admin library such as grappelli or django admin.

.. code-block::  python

    INSTALLED_APPS = (
        'gipsy.dashboard',
        ...
        'grappelli',
        ...
        'django.contrib.admin',
    )

Then install your model with 

.. code-block::  shell

    python manage.py syncdb

In case you are using South, you can alternatively do:

.. code-block::  shell

    python manage.py migrate gipsy.dashboard
    

Menu items
==========

Setup your menu items in the admin. Each menu entry have parent and children. You can add icons to the parents by using font awesome classes: http://fortawesome.github.io/Font-Awesome/

Urls
====

By default Gipsy Dashboard overrides the admin urls to display the dashboard as the default admin homepage. It still keeps the default index of django or grappelli by hosts this page on a different url: 'admin:all_tables'

To do so, Gipsy Dashboard overrides the django.contrib.admin.sites.AdminSite. If you are using your own AdminSite class, you can inherit it from the gispy.dashboard.admin.GipsyAdminSite. You can also remove this behaviour by using the following constant in your settings:

.. code-block::  python

    GIPSY_ENABLE_ADMINSITE = False

You will then need to use your own url redirections and settings.

Additionnaly you can define in the settings the url pattern you want to use for each of those pages:

.. code-block::  python

    GIPSY_DASHBOARD_URL = 'admin:index'
    GIPSY_VANILLA_INDEX_URL = 'admin:all_apps'

Widgets
=======

The philosophy behind the widget is flexibility. Gipsy Dashboard integrate a set of pre-written template tags. You can include those template tags by overwriting the gipsy.dashboard.templates.dashboard.html file. 

Then feel free to add you own widgets by copying the html of each templatetags. Or you can use existing templatetags and fill them with appropriate objects.


Themes
======

You can add your own stylesheet theme file to the admin by using the GIPSY_THEME constant in your settings.py.

By default the theme is from grappelli. However it doesnt match the toolbar and left menu well. A more accurate theme is available but still under developpment so it might have some unstabilities. You can still use it by adding this command line in your settings.py:

.. code-block::  python

    GIPSY_THEME = STATIC_URL + 'gipsy_dashboard/css/gipsy.css'

Dashboard
=========

The dashboard system is greatly inspired from the awesome Grappelli library. In order to setup your dashboard, you will need to create a setting class and let your django settings know about it by setting up the settings.GIPSY_DASHBOARD constant.

For exemple:

.. code-block::  python

    GIPSY_DASHBOARD = 'gipsy.dashboard.presets.default.DashboardDefault'

In your class you will just need to create a render method and declare each element of it by appending its widgets property list. You can find exemple of widgets in:

* gipsy.dashboard.widgets.widgets
* gipsy.dashboard.widgets.widgets_google_analytics

For information you can find exemple of implementation of this class in:

* gipsy.dashboard.presets.defaut
* gipsy.dashboard.presets.google_analytics

An exemple of implementing this class would be:

.. code-block::  python

    from gipsy.dashboard.dashboard import Dashboard
    from gipsy.dashboard.widgets import widgets, widgets_google_analytics


    class DashboardDefault(Dashboard):
        def render(self):
            # metrics evolution
            self.widgets.append(widgets_google_analytics.WidgetGAPageViewsEvolution())

            # metrics evolution
            self.widgets.append(widgets_google_analytics.WidgetGASessionsEvolution())

            # metrics single
            self.widgets.append(widgets.WidgetMetricsSingle(
                title='currently active users',
                label='active users',
                count=2564,
            ))

            # line chart
            self.widgets.append(widgets_google_analytics.WidgetGALineChart())

            # metrics list
            self.widgets.append(widgets.WidgetMetricsList(items=[
                {'icon': 'fa-file-image-o', 'label': 'posts', 'value': 75},
                {'icon': 'fa-comment-o', 'label': 'comments', 'value': 192},
                {'icon': 'fa-files-o', 'label': 'pages', 'value': 12},
                {'icon': 'fa-flag-o', 'label': 'in moderation', 'value': 4},
            ]))

            # model list
            self.widgets.append(widgets.WidgetModelList(items={}))

            # admin logs
            self.widgets.append(widgets.WidgetAdminLog())

You can very easily add google analytics to your dashboard by using the widgets stored in gipsy.dashboard.widgets.widgets_google_analytics
Most of the difficulty will be to integrate the API credentials. In order to do so, you will need to follow the steps described in the google API tutorial https://developers.google.com/analytics/solutions/articles/hello-analytics-api#environment. There is also a very nice tutorial here: http://blog.iambob.me/accessing-google-analytics-from-django/

Once you have completed those steps, you will need to add setup the following constants in your settings:

* GOOGLE_ANALYTICS_CLIENT_SECRETS = '/location/of/your/client_secret.json'
* GOOGLE_ANALYTICS_TOKEN_FILE_NAME = '/location/of/your/analytics.dat'
* GOOGLE_ANALYTICS_VIEW_ID = 'your_view_id'

I recommand to start by using the shell to gain the access and generate the analytics.dat file.

.. code-block::  shell

    python manage.py shell
    
Then
    
.. code-block::  shell

    from gipsy.dashboard.services.google_analytics_connector import GoogleAnalyticsConnector
    GoogleAnalyticsConnector().start_service().query(start_date='2015-01-01', end_date='2015-01-01', metrics='ga:pageviews').execute()

You should be prompted with a link to go to to grant the access. By going on the link with your browser you will get a key to enter in the shell.

Please note that for performances purpose the default dashboard template is cached to 5 minutes. You can change the cache time through the settings.GIPSY_DASHBOARD_CACHE_TIME constant.


Version indicator
=================


Sometimes version information is be very useful. When knowing current version you are able to tell in ticket on which version bug appears. Also it will be easy to check if this is regression (bug reapeared on present version, is not reproductible on prod which has different version). 

.. code-block::  python

    GIPSY_VERSION_INDICATOR = ('<version display info>', '<version hover info>')

.. code-block::  python

    GIPSY_VERSION_INDICATOR = (‘v1.0’, ’ fdb25bb85bdd047689d5845bbc15cdac94d3c9de’).

You can setup this value by any method you want, you might want to populate it automatically during deploy or get it from file or git or hg.

For example:

.. code-block::  python

    GIPSY_VERSION_INDICATOR = open('path/to/version.txt').read().rsplit(',', 1)

or:

.. code-block::  python

    def get_git_version():
        import subprocess

        def call(cmd):
            return subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=BASE_DIR).communicate()[0]

        describe = call(['git', 'describe'])
        branch = call(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        sha = call(['git', 'rev-parse', '--short', 'HEAD'])
        if branch.strip() == 'master':
            return describe, sha
        return branch, describe

    GIPSY_VERSION_INDICATOR = get_git_version()

You can choose indicator position by specifying `GIPSY_VERSION_INDICATOR_LOCATION`. Choices are `'nav'`, `'menu'`. By default its `'nav'`.

Example:

.. code-block::  python

    GIPSY_VERSION_INDICATOR_LOCATION = 'nav'


************
Contribution
************


Please feel free to contribute. Any help and advices are much appreciated.


*****
LINKS
*****

Development:
    https://github.com/RevSquare/gipsy

Package:
    https://pypi.python.org/pypi/django-gipsy
