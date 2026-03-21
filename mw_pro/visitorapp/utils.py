from ipware import get_client_ip
from django.contrib.gis.geoip2 import GeoIP2
from user_agents import parse


def get_ip(request):
    ip, _ = get_client_ip(request)
    return ip


def get_country(ip):

    try:
        g = GeoIP2()
        country = g.country(ip)
        return country["country_name"]
    except:
        return None


def get_device_info(request):

    ua_string = request.META.get('HTTP_USER_AGENT', '')
    user_agent = parse(ua_string)

    browser = user_agent.browser.family

    if user_agent.is_mobile:
        device = "Mobile"
    elif user_agent.is_tablet:
        device = "Tablet"
    elif user_agent.is_pc:
        device = "Desktop"
    else:
        device = "Other"

    return browser, device