from gipsy.dashboard.dashboard import Dashboard
from gipsy.dashboard.widgets import widgets_google_analytics


class DashboardDefault(Dashboard):
    def render(self):
        # line chart
        self.widgets.append(widgets_google_analytics.WidgetGALineChart())
