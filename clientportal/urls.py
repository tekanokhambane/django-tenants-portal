from . import views
from django.urls import path

urlpatterns = [
    path("dashboard/", views.DashboardView.as_view(), name="customer_dashboard"),
    path("dashboard/websites/", views.WebsitesView.as_view(), name="websites"),
    path("dashboard/domains/", views.DomainsView.as_view(), name="domains"),
]
