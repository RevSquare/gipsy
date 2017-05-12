class Widget(object):
    template = ''
    show_title = True
    title = ''
    grid = 4

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])


class WidgetItems(Widget):
    items = []

    def __init__(self, items, **kwargs):
        self.items = items
        super(WidgetItems, self).__init__(**kwargs)


class WidgetModelList(WidgetItems):
    template = 'gipsy/dashboard/widgets/model_list.html'
    title = 'most recent items'
    grid = 6


class WidgetAdminLog(Widget):
    template = 'gipsy/dashboard/widgets/admin_log.html'
    title = 'recent admin actions'
    grid = 6


class WidgetMetricsList(WidgetItems):
    template = 'gipsy/dashboard/widgets/metrics_list.html'
    title = 'at a glance'
    grid = 4


class WidgetMetricsSingle(Widget):
    template = 'gipsy/dashboard/widgets/metrics_single.html'
    title = 'metrics single'
    grid = 4
    count = 0
    label = 'items'


class WidgetLineChart(Widget):
    template = 'gipsy/dashboard/widgets/line_chart.html'
    title = 'line chart'
    grid = 8
    labels = []
    values = []

    def __init__(self, labels, values, **kwargs):
        self.labels = labels
        self.values = values
        super(WidgetLineChart, self).__init__(**kwargs)


class WidgetMetricsEvolution(Widget):
    template = 'gipsy/dashboard/widgets/metrics_evolution.html'
    title = 'currently active users'
    label = 'active users'
    label_bottom = ''
    grid = 4
    result = 0
    difference = 0
    percentage = 0

    def __init__(self, result, previous_result, **kwargs):
        self.result = result
        self.difference = int(result) - int(previous_result)
        if previous_result == 0:
            self.percentage = 100
        else:
            self.percentage = (int(result) * 100) / int(previous_result)
        super(WidgetMetricsEvolution, self).__init__(**kwargs)
