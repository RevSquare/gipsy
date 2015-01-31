import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from django.conf import settings


class GoogleAnalyticsConnector(object):
    """
    Connector class for the google API. This is a very implementation using
    the method described in http://blog.iambob.me/accessing-google-analytics-from-django/
    and in the official API documentation
    https://developers.google.com/analytics/solutions/articles/hello-analytics-api
    """
    CLIENT_SECRETS = settings.GOOGLE_ANALYTICS_CLIENT_SECRETS
    VIEW_ID = settings.GOOGLE_ANALYTICS_VIEW_ID
    TOKEN_FILE_NAME = settings.GOOGLE_ANALYTICS_TOKEN_FILE_NAME
    FLOW = flow_from_clientsecrets(CLIENT_SECRETS, scope='https://www.googleapis.com/auth/analytics.readonly')

    def __init__(self):
        self.service = None

    def _authenticate(self):
        # Retrieve existing credendials
        storage = Storage(self.TOKEN_FILE_NAME)
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            credentials = run_flow(self.FLOW, storage, self.GAFlags())

        return credentials

    def _create_service(self):
        # 1. Create an http object
        http = httplib2.Http()

        # 2. Authorize the http object
        credentials = self._authenticate()
        http = credentials.authorize(http)

        # 3. Build the Analytics Service Object with the authorized http object
        return build('analytics', 'v3', http=http)

    def start_service(self):
        """
        :return: ``this`` Google analytics object with the service set

        start the service which may be used to query the google analytics api
        """
        if not self.service:
            self.service = self._create_service()
        return self

    def query(self, **kwargs):
        kwargs.update({
            'ids': "ga:{id}".format(id=self.VIEW_ID),
        })

        result = self.service.data().ga().get(**kwargs)
        return result

    class GAFlags():
        """
        total hack. If you want to see why, examine apiclient.sample_tools.
        The python bindings as well as the documentation kind've forgot to
        mention this... Which is a big deal... But actually though.
        """
        noauth_local_webserver = True
        logging_level = "DEBUG"
