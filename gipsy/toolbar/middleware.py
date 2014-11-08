# -*- coding: utf-8 -*-


class GipsyToolbarMiddleware(object):
    def process_response(self, request, response):
        """
        Adds a cookie when a user is allowed to access the toolbar. This is usefull to deactivate cache engines
        such as Varnish
        """
        if not hasattr(request, 'user'):
            return response
        if request.user.is_active and request.user.is_staff and not request.COOKIES.get('gt_activated'):
            response.set_cookie(key='gt_activated', value=1)

        if (not request.user.is_active or not request.user.is_staff) and request.COOKIES.get('gt_activated'):
            response.delete_cookie('gt_activated')

        return response
