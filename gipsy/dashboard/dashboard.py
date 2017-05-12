from django import forms
from gipsy.dashboard.settings import GIPSY_DASHBOARD_HAS_ROWS, GIPSY_DASHBOARD_DEFAULT_GRID


class Dashboard(object):
    '''
    This class is collecting the widgets setup in the settings.GIPSY_DASHBOARD
    constant.

    It is adding widget in rows in order to display them more efficiently
    in grids and responsive designs. You can disable this functionnality by
    setting settings.GIPSY_DASHBOARD_HAS_ROWS to False. You can also change the
    value of grid by changing settings.GIPSY_DASHBOARD_DEFAULT_GRID (default 12).

    If you want to customize the look of your dashboard and it's modules, you
    can declare css stylesheets and/or javascript files to include when
    rendering the dashboard (these files should be placed in your
    media path), for example::

        from admin_tools.dashboard import Dashboard

        class MyDashboard(Dashboard):
            class Media:
                css = {
                    'all': (
                        'css/mydashboard.css',
                        'css/mystyles.css',
                    ),
                }
                js = (
                    'js/mydashboard.js',
                    'js/myscript.js',
                )
    '''
    # Using Django's Media meta class
    __metaclass__ = forms.MediaDefiningClass

    def _media(self):
        return forms.Media()
    media = property(_media)
    has_rows = True
    rows = [[]]
    widgets = []
    request = None

    def __init__(self, request):
        self.request = request
        self.widgets = []
        self.has_rows = GIPSY_DASHBOARD_HAS_ROWS
        self.rows = [[]]
        self.render()
        if self.has_rows:
            total = 0
            for widget in self.widgets:
                total += widget.grid
                if total > GIPSY_DASHBOARD_DEFAULT_GRID:
                    self.rows.append([])
                    total = widget.grid
                self.rows[-1].append(widget)

    def render(self):
        pass
