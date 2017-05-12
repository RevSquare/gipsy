from gipsy.dashboard.dashboard import Dashboard
from gipsy.dashboard.widgets import widgets, widgets_google_analytics


class DashboardDefault(Dashboard):
    """
    Defaut and exemple class for dashboards using google analytics specific widgets.
    This class simply uses a render method where widgets are added. The widgets property is a list
    that can be appended as follow.
    The google analytics widgets are plug and play but of course feel free to overwrite them.
    Read the documentation for more information on how to setup google analytics on yourapplication.
    """
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
