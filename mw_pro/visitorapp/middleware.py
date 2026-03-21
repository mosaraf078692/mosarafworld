from .models import Visitor
from .utils import get_ip, get_country, get_device_info
from datetime import date


class VisitorAnalyticsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = get_ip(request)

        if ip:

            country = get_country(ip)

            browser, device = get_device_info(request)

            path = request.path

            today = date.today()

            is_unique = not Visitor.objects.filter(
                ip_address=ip,
                visit_date=today
            ).exists()

            Visitor.objects.create(
                ip_address=ip,
                country=country,
                browser=browser,
                device=device,
                path=path,
                is_unique=is_unique
            )

        response = self.get_response(request)

        return response