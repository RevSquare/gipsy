from datetime import date, datetime, timedelta

from django.core.cache import cache

from oauth2client.client import AccessTokenRefreshError

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
            try:
                result = ga_connector.start_service()\
                    .query(start_date=query_date, end_date=query_date, metrics=metrics).execute()
                previous_date = str((datetime.now() - timedelta(days=2)).date())
                previous_result = ga_connector.start_service()\
                    .query(start_date=previous_date, end_date=previous_date, metrics=metrics).execute()
            except AccessTokenRefreshError:
                result = {}
                previous_result = {}

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
    label = 'page viewed yesterday'
    label_bottom = 'pages viewed difference'

    def __init__(self, **kwargs):
        super(WidgetGAPageViewsEvolution, self)\
            .__init__('ga:pageviews', **kwargs)


class WidgetGASessionsEvolution(WidgetGAEvolution):
    title = 'daily unique visitors'
    label = 'unique visitors yesterday'
    label_bottom = 'unique visitors difference'

    def __init__(self, **kwargs):
        super(WidgetGASessionsEvolution, self)\
            .__init__('ga:sessions', **kwargs)


class WidgetGALineChart(WidgetLineChart):
    title = 'our traffic overview'
    cache_time = 86400

    def __init__(self, **kwargs):
        labels = []
        values = {}
        values['sessions'] = {'label': 'Sessions', 'color': '#abc4e6', 'values': []}
        values['pageviews'] = {'label': 'Page views', 'color': '#ffffff', 'values': []}
        cache_name = 'gipsy.dashboard.widgets.widgets_google_analytics.WidgetGALineChart'
        cached_objects = cache.get(cache_name)
        if cached_objects is None:
            ga_connector = GoogleAnalyticsConnector()
            today = date.today()
            for num in range(0, 10):
                day_date = today - timedelta(days=num)
                day = day_date.strftime("%Y-%m-%d")
                labels.append(day_date.strftime("%m-%d-%Y"))
                try:
                    result = ga_connector.start_service()\
                        .query(start_date=day, end_date=day, metrics='ga:pageviews, ga:sessions').execute()
                except AccessTokenRefreshError:
                    result = {'totalsForAllResults': {'ga:sessions': 0, 'a:pageviews': 0}}

                values['sessions']['values'].append(result['totalsForAllResults']['ga:sessions'])
                values['pageviews']['values'].append(result['totalsForAllResults']['ga:pageviews'])
            values['sessions']['values'] = values['sessions']['values'][::-1]
            values['pageviews']['values'] = values['pageviews']['values'][::-1]
            cached_objects = {'labels': labels[::-1], 'values': [values['sessions'], values['pageviews']]}
            cache.set(cache_name, cached_objects, self.cache_time)
        self.labels = cached_objects['labels']
        self.values = cached_objects['values']
