from gipsy.dashboard.dashboard import Dashboard
from gipsy.dashboard.widgets import widgets


class DashboardDefault(Dashboard):
    """
    Defaut and static content class for dashboards.
    This class simply uses a render method where widgets are added. The widgets property is a list
    that can be appended as follow.
    """
    def render(self):
        # metrics evolution
        self.widgets.append(widgets.WidgetMetricsEvolution(
            title='daily visitors',
            label='visitors today',
            label_bottom='visitors difference since yesterday',
            result=2564,
            previous_result=2200,
        ))

        # metrics evolution
        self.widgets.append(widgets.WidgetMetricsEvolution(
            title='page views',
            label='page viewed today',
            label_bottom='pages viewed difference since yesterday',
            result=2564,
            previous_result=2200,
        ))

        # metrics single
        self.widgets.append(widgets.WidgetMetricsSingle(
            title='currently active users',
            label='active users',
            count=2564,
        ))

        # metrics single
        self.widgets.append(widgets.WidgetLineChart(
            title='our traffic overview',
            labels=['october', 'november', 'december'],
            values=[1027, 1060, 1500],
        ))

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
