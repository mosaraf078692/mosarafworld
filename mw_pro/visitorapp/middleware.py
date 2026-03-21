from .models import Visitor
from .utils import get_ip, get_country, get_device_info
from django.db.models import Q
from datetime import date


class VisitorAnalyticsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip = get_ip(request)

        if ip:

            # Check if the IP address already exists in the database
            if not Visitor.objects.filter(Q(ip_address=ip)).exists():

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