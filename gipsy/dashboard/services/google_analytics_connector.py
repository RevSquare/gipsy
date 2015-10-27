import httplib2
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets, SignedJwtAssertionCredentials
from oauth2client.file import Storage
from oauth2client.tools import run_flow

from django.conf import settings


class GoogleAnalyticsConnector(object):
    """
    Connector class for the google API.
    You could use the auth method described in http://blog.iambob.me/accessing-google-analytics-from-django/
    and in the official API documentation
    https://developers.google.com/analytics/solutions/articles/hello-analytics-api
    Also you could use the type of authenticate credentials "Service account"
    https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/service-py
    For using this method you must define in settings.py follow lines, e.g.:
        GOOGLE_ANALYTICS_CREDENTIAL_TYPE = "oauth2_client_id"  # default value if it's not defined
        GOOGLE_ANALYTICS_TOKEN_FILE_NAME = "path/to/your/analytics.dat"
        GOOGLE_ANALYTICS_CLIENT_SECRETS = "path/to/your/client_secret.json"
        GOOGLE_ANALYTICS_VIEW_ID = "your_view_id"
    or
        GOOGLE_ANALYTICS_CREDENTIAL_TYPE = "service_account"
        GOOGLE_ANALYTICS_PRIVATE_KEY_FILE_NAME = "path/to/privatekey.p12/or/privatekey.pem"
        GOOGLE_ANALYTICS_CLIENT_EMAIL = "your-email-address@developer.gserviceaccount.com"
        GOOGLE_ANALYTICS_VIEW_ID = "your_view_id"
    If you will choose "service_account" credential type, don't forget
    to add your client email "your-email-address@developer.gserviceaccount.com"
    to Google Analytics. See more here:
    http://stackoverflow.com/questions/12837748/analytics-google-api-error-403-user-does-not-have-any-google-analytics-account
    """

    def __init__(self):
        self.service = None
        self.VIEW_ID = settings.GOOGLE_ANALYTICS_VIEW_ID
        self.SCOPE = 'https://www.googleapis.com/auth/analytics.readonly'

    def _credential_type(self):
        if hasattr(settings, 'GOOGLE_ANALYTICS_CREDENTIAL_TYPE'):
            return settings.GOOGLE_ANALYTICS_CREDENTIAL_TYPE
        return "oauth2_client_id"

    def _authenticate(self):
        credentials = None
        if "service_account" == self._credential_type():
            primary_key_file = settings.GOOGLE_ANALYTICS_PRIVATE_KEY_FILE_NAME
            with open(primary_key_file, 'rb') as f:
                private_key = f.read()
            credentials = SignedJwtAssertionCredentials(
                settings.GOOGLE_ANALYTICS_CLIENT_EMAIL, private_key, self.SCOPE)
        else:
            storage = Storage(settings.GOOGLE_ANALYTICS_TOKEN_FILE_NAME)
            credentials = storage.get()
            if credentials is None or credentials.invalid:
                flow = flow_from_clientsecrets(
                    settings.GOOGLE_ANALYTICS_CLIENT_SECRETS, scope=self.SCOPE)
                credentials = run_flow(flow, storage, self.GAFlags())
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
