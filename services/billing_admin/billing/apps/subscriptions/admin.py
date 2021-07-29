import uuid
from django.contrib import admin
from billing.apps.subscriptions.models.models import (
    Client, Product, Tariff, Discount, Subscription, PaymentInvoice, AuditEvents
)


class BaseAdmin(admin.ModelAdmin):
    exclude = ('id',)

    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.id = uuid.uuid4()
        super().save_model(request, obj, form, change)


@admin.register(Client)
class ClientAdmin(BaseAdmin):
    list_display = ('user_id',)


@admin.register(Product)
class ProductAdmin(BaseAdmin):
    list_display = ('name', 'access_type')
    search_fields = ['name']


@admin.register(Tariff)
class TariffAdmin(BaseAdmin):
    list_display = ('product', 'price', 'period')


@admin.register(Discount)
class DiscountAdmin(BaseAdmin):
    list_display = ('name', 'code', 'value', 'is_active')
    search_fields = ['name', 'code']


@admin.register(Subscription)
class SubscriptionAdmin(BaseAdmin):
    list_display = ('client', 'tariff', 'status')


@admin.register(PaymentInvoice)
class PaymentHistoryAdmin(BaseAdmin):
    list_display = ('subscription', 'amount', 'status', 'payment_system', 'created', 'modified')


@admin.register(AuditEvents)
class AuditEventsAdmin(admin.ModelAdmin):
    exclude = ('id',)
    list_display = ('created', 'who', 'what', 'content_type', 'object_id')
    search_fields = ['who', 'what', 'details', 'content_type__model', 'object_id']
    ordering = ['-created', ]