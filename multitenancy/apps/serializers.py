from rest_framework import serializers
from multitenancy.subscriptions.serializers import (
    PlanSerialiser,
    SubscriptionSerializer,
)
from .models import Tenant, Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = "__all__"


class TenantSerializer(serializers.ModelSerializer):
    subscription = SubscriptionSerializer(many=False)
    plan = PlanSerialiser(many=False, required=False)
    domain = DomainSerializer(many=True, required=False)

    class Meta:
        model = Tenant
        fields = [
            "id",
            "name",
            "slug",
            "type",
            "is_template",
            "plan",
            "domain",
            "description",
            "subscription",
            "trail_duration",
            "on_trial",
            "created",
            "modified",
        ]
