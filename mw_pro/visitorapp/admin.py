from django.contrib import admin
from .models import Visitor

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):

    list_display = (
        "ip_address",
        "country",
        "browser",
        "device",
        "path",
        "is_unique",
        "visit_time"
    )

    list_filter = ("country", "device", "browser", "visit_date")