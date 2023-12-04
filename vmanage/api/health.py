"""Cisco vManage Health API Endpoints.
"""

import json
import re
from vmanage.api.feature_templates import FeatureTemplates
from vmanage.api.http_methods import HttpMethods
from vmanage.data.parse_methods import ParseMethods
from vmanage.utils import list_to_dict
from vmanage.api.utilities import Utilities

class Health(object):
    """vManage Health Devices API
    
    Responsible for Get methods against vManage Health API.
    
    """
    def __init__(self, session, host, port=443):
        """Initialize Device Templates object with session parameters.

        Args:
            session (obj): Requests Session object
            host (str): hostname or IP address of vManage
            port (int): default HTTPS 443

        """

        self.session = session
        self.host = host
        self.port = port
        self.base_url = f'https://{self.host}:{self.port}/dataservice/'

    def get_devices_health(self, page=None, pageSize=None, sortBy=None, sortOrder=None, startingDeviceId=None, siteId=None, groupId=None, vpnId=None, reachable=None, controlStatus=None, personality=None, health=None):
        """Obtain a list of all devices and their health status.
        
        Returns:
            result (dict): Dictionary of all devices and their health status.
        """

        api = f"health/devices"
        query_string = "?"
        if page:
            query_string += f"page={page}"
        if pageSize:
            query_string += f"pageSize={pageSize}" if query_string == "?" else f"&pageSize={pageSize}"
        if sortBy:
            query_string += f"sortBy={sortBy}" if query_string == "?" else f"&sortBy={sortBy}"
        if sortOrder:
            query_string += f"sortOrder={sortOrder}" if query_string == "?" else f"&sortOrder={sortOrder}"
        if startingDeviceId:
            query_string += f"startingDeviceId={startingDeviceId}" if query_string == "?" else f"&startingDeviceId={startingDeviceId}"
        if siteId:
            query_string += f"siteId={siteId}" if query_string == "?" else f"&siteId={siteId}"
        if groupId:
            query_string += f"groupId={groupId}" if query_string == "?" else f"&groupId={groupId}"
        if vpnId:
            query_string += f"vpnId={vpnId}" if query_string == "?" else f"&vpnId={vpnId}"
        if reachable:
            query_string += f"reachable={reachable}" if query_string == "?" else f"&reachable={reachable}"
        if controlStatus:
            query_string += f"controlStatus={controlStatus}" if query_string == "?" else f"&controlStatus={controlStatus}"
        if personality:
            query_string += f"personality={personality}" if query_string == "?" else f"&personality={personality}"
        if health:
            query_string += f"health={health}" if query_string == "?" else f"&health={health}"
        url = self.base_url + api + query_string if query_string != "?" else self.base_url + api
        response = HttpMethods(self.session, url).request('GET')
        result = ParseMethods.parse_response(response)
        return result

    def get_device_health_overview(self, vpnId=None):
        """Obtain a summary of all devices and their health status.
        
        Returns:
            result (dict): Dictionary of the summed value of all devices by their health status.
        """

        api = f"health/overview"
        query_string = "?"
        if vpnId:
            query_string += f"vpnId={vpnId}" if query_string == "?" else f"&vpnId={vpnId}"
        url = self.base_url + api + query_string if query_string != "?" else self.base_url + api
        response = HttpMethods(self.session).get(url)
        result = ParseMethods.parse_response(response)
        return result

