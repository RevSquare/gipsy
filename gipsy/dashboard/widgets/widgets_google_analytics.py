from datetime import date, datetime, timedelta

from django.core.cache import cache

from .widgets import WidgetMetricsEvolution, WidgetLineChart
from gipsy.dashboard.services.google_analytics_connector import GoogleAnalyticsConnector


class WidgetGAEvolution(WidgetMetricsEvolution):
    cache_time = 3600

    def __init__(self, metrics, **kwargs):
        cache_name = 'gipsy.dashboard.widgets.widgets_google_analytics.' + metrics
        cached_objects = cache.get(cache_name)
        if cached_objects is None:
            ga_connector = GoogleAnalyticsConnector()
            query_date = str((datetime.now() - timedelta(days=1)).date())
            result = ga_connector.start_service()\
                .query(start_date=query_date, end_date=query_date, metrics=metrics).execute()
            previous_date = str((datetime.now() - timedelta(days=2)).date())
            previous_result = ga_connector.start_service()\
                .query(start_date=previous_date, end_date=previous_date, metrics='ga:pageviews').execute()

            try:
                result = result['rows'][0][0]
            except KeyError:
                result = 0
            try:
                previous_result = previous_result['rows'][0][0]
            except KeyError:
                previous_result = 0

            cached_objects = {'result': result, 'previous_result': previous_result}
            cache.set(cache_name, cached_objects, self.cache_time)

        super(WidgetGAEvolution, self)\
            .__init__(cached_objects['result'], cached_objects['previous_result'], **kwargs)


class WidgetGAPageViewsEvolution(WidgetGAEvolution):
    title = 'page views'
    label = 'page viewed today'
    label_bottom = 'pages viewed difference since yesterday'

    def __init__(self, **kwargs):
        super(WidgetGAPageViewsEvolution, self)\
            .__init__('ga:pageviews', **kwargs)


class WidgetGASessionsEvolution(WidgetGAEvolution):
    title = 'daily unique visitors'
    label = 'unique visitors today'
    label_bottom = 'unique visitors difference since yesterday'

    def __init__(self, **kwargs):
        super(WidgetGASessionsEvolution, self)\
            .__init__('ga:sessions', **kwargs)


class WidgetGALineChart(WidgetLineChart):
    title = 'our traffic overview'
    cache_time = 86400

    def __init__(self, **kwargs):
        labels = []
        values = []
        cache_name = 'gipsy.dashboard.widgets.widgets_google_analytics.WidgetGALineChart'
        cached_objects = cache.get(cache_name)
        if cached_objects is None:
            ga_connector = GoogleAnalyticsConnector()
            today = date.today()
            start_day = date(today.year, today.month, 1)
            month_start = today
            for num in range(0, 6):
                if num == 0:
                    month_start = start_day
                    month_end = today
                else:
                    month_end = month_start + timedelta(days=-1)
                    month_start = date(month_end.year, month_end.month, 1)
                start = month_start.strftime("%Y-%m-%d")
                end = month_end.strftime("%Y-%m-%d")
                labels.append(month_start.strftime("%b"))
                result = ga_connector.start_service()\
                    .query(start_date=start, end_date=end, metrics='ga:pageviews').execute()
                values.append(result['totalsForAllResults']['ga:pageviews'])
            cached_objects = {'labels': labels[::-1], 'values': values[::-1]}
            cache.set(cache_name, cached_objects, self.cache_time)
        self.labels = cached_objects['labels']
        self.values = cached_objects['values']

