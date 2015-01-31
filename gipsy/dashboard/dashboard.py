from django import forms


class Dashboard(object):
    # Using Django's Media meta class
    __metaclass__ = forms.MediaDefiningClass

    def _media(self):
        return forms.Media()
    media = property(_media)

    has_rows = True
    rows = [[]]
    default_grid = 12
    widgets = []
    request = None

    def __init__(self, request):
        self.request = request
        self.widgets = []
        self.rows = [[]]
        self.render()
        if self.has_rows:
            total = 0
            for widget in self.widgets:
                total += widget.grid
                if total > self.default_grid:
                    self.rows.append([])
                    total = widget.grid
                self.rows[-1].append(widget)

    def render(self):
        pass
