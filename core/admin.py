from django.urls import reverse
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.forms import ModelForm, Textarea
from django import db
from core import models


class PropertyImageInline(admin.TabularInline):
    model = models.PropertyImage
    extra = 0
    classes = ["collapse"]


class PropertyInventoryInline(admin.TabularInline):
    model = models.PropertyInventory
    extra = 0
    classes = ["collapse"]
    verbose_name = "Property Inventory"


class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, PropertyInventoryInline]
    list_display = (
        "name",
        "category",
        "property_value",
        "current_rental_value",
        "rental_revenue",
        "net_revenue",
        "year",
    )
    search_fields = ["category"]
    list_filter = ("category",)


class PropertyInventoryAdmin(admin.ModelAdmin):
    list_display = ("item", "current_state", "original_state", "cost_incurred")
    search_fields = ["item"]
    formfield_overrides = {db.models.TextField: {"widget": Textarea(attrs={"rows": 3, "cols": 30})}}


class PropertyImageAdmin(admin.ModelAdmin):
    list_display = ("tag", "realty")
    search_fields = ["tag"]


class PaymentScheduleInline(admin.TabularInline):
    model = models.PaymentSchedule
    extra = 0
    classes = ["collapse"]
    verbose_name = "Payment Schedule"
    verbose_name_plural = "Payment Schedules"
    readonly_fields = ("amount_due",)


class LettingAdmin(admin.ModelAdmin):
    inlines = [PaymentScheduleInline]


class LettingInline(admin.TabularInline):
    model = models.Letting
    extra = 0
    classes = ["collapse"]
    fields = (
        "type",
        "letting_duration",
        "start_date",
        "end_date",
        "amount_paid",
        "amount_outstanding",
        "cost",
        "schedule_type",
        "changeform_link",
    )
    readonly_fields = (
        "changeform_link",
        "type",
        "letting_duration",
        "start_date",
        "end_date",
        "amount_paid",
        "amount_outstanding",
        "cost",
        "schedule_type",
    )

    def changeform_link(self, instance):
        if instance.id:
            changeform_url = reverse("admin:core_letting_change", args=(instance.id,))
            return mark_safe('<a href="{u}">Details</a>'.format(u=changeform_url))
            # return u'<a href="%s" target="_blank">Details</a>' % changeform_url
        return ""

    def letting_duration(self, instance):
        if instance.duration:
            return f"{instance.duration} month(s)"

    changeform_link.allow_tags = True
    changeform_link.short_description = ""
    letting_duration.short_description = "Duration"


class TenantDocumentInline(admin.TabularInline):
    model = models.TenantDocument
    ordering = ("name",)
    extra = 0
    classes = ["collapse"]


class TenantDocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "date_created", "date_modified", "get_tenant_name")
    search_fields = ["name", "tenant__first_name", "tenant__last_name"]

    def get_tenant_name(self, obj):
        return " ".join([obj.tenant.first_name, obj.tenant.last_name])

    get_tenant_name.short_description = "Tenant Name"
    get_tenant_name.admin_order_field = "tenant"


class LettingAdmin(admin.ModelAdmin):
    inlines = [PaymentScheduleInline]
    list_display = (
        "get_tenant_name",
        "type",
        "letting_duration",
        "start_date",
        "end_date",
        "amount_paid",
        "amount_outstanding",
        "cost",
        "schedule_type",
    )
    search_fields = ["tenant__first_name", "tenant__last_name"]

    def get_tenant_name(self, obj):
        return " ".join([obj.tenant.first_name, obj.tenant.last_name])

    def letting_duration(self, instance):
        if instance.duration:
            return f"{instance.duration} month(s)"

    get_tenant_name.short_description = "Tenant Name"
    get_tenant_name.admin_order_field = "tenant"
    letting_duration.short_description = "Duration"


class BillsAdmin(admin.ModelAdmin):
    list_display = (
        "get_tenant_name",
        "name",
        "amount",
        "billing_cycle",
        "date_paid",
        "transaction_reference",
        "due_date",
        "payment_status",
    )
    list_filter = ("payment_status",)
    search_fields = ["tenant__first_name", "tenant__last_name"]

    def get_tenant_name(self, obj):
        return " ".join([obj.tenant.first_name, obj.tenant.last_name])

    get_tenant_name.short_description = "Tenant Name"


class PaymentScheduleAdmin(admin.ModelAdmin):
    list_display = ("get_tenant_name", "amount_due", "payment_cycle", "tag", "active_schedule", "payment_status")
    search_fields = ["letting__tenant__first_name", "letting__tenant__last_name"]
    list_filter = ("active_schedule", "tag", "payment_status")
    readonly_fields = ("amount_due", "tag", "payment_cycle")

    def get_tenant_name(self, obj):
        return " ".join([obj.letting.tenant.first_name, obj.letting.tenant.last_name])

    get_tenant_name.short_description = "Tenant Name"
    get_tenant_name.admin_order_field = "tenant"


class AdminUserForm(ModelForm):
    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email", "is_active", "is_superuser")


class TenantCommentAdmin(admin.ModelAdmin):
    list_display = ("get_tenant_name", "comment", "date_added")
    search_fields = ["tenant__first_name", "tenant__last_name"]

    def get_tenant_name(self, obj):
        return " ".join([obj.tenant.first_name, obj.tenant.last_name])


class TenantCommentInline(admin.TabularInline):
    model = models.TenantComment
    extra = 0
    classes = ["collapse"]


class UserAdmin(admin.ModelAdmin):
    inlines = [LettingInline, TenantDocumentInline, TenantCommentInline]
    list_display = ("get_tenant_name", "email", "is_active")
    search_fields = ["first_name", "last_name", "email"]
    list_filter = ("is_active",)
    # form = AdminUserForm
    fieldsets = (

        ("Registration", {"fields": ("first_name", "last_name", "email", "is_active", "is_superuser")}),
        (
            "Bio",
            {
                "fields": (
                    "title",
                    "middle_name",
                    "maiden_name",
                    "nationality",
                    "gender",
                    "telephone",
                    "date_of_birth",
                    "id_number",
                    "mobile_number",
                    "whatsapp_number"
                )
            }
        ),
        (
            "Previous Address",
            {
                "fields": (
                    "previous_address_house_number",
                    "previous_address_house_name",
                    "previous_address_street",
                    "previous_address_town",
                    "previous_address_city",
                    "previous_address_state",
                    "previous_address_duration_of_stay",
                )
            },
        ),
        (
            "Employment Details",
            {
                "fields": (
                    "employment_status",
                    "job_title",
                    "years_at_current_employment",
                    "employer_name",
                    "employer_contact_person",
                    "employer_telephone",
                    "employer_mobile",
                    "employer_email",
                )
            },
        ),
        (
            "Next of Kin",
            {
                "fields": (
                    "next_of_kin_first_name",
                    "next_of_kin_last_name",
                    "next_of_kin_house_number",
                    "next_of_kin_house_name",
                    "next_of_kin_street",
                    "next_of_kin_town",
                    "next_of_kin_city",
                    "next_of_kin_state",
                    "next_of_kin_mobile_1",
                    "next_of_kin_mobile_2",
                    "next_of_kin_email",
                    "next_of_kin_relationship_to_tenant",
                )
            },
        ),
        (
            "Current LandLord / Agent",
            {
                "fields": (
                    "landlord_name",
                    "current_landlord_mobile_1",
                    "current_landlord_mobile_2",
                    "current_landlord_email",
                    "length_of_time_at_last_property",
                )
            },
        ),
        (
            "Personal Referee",
            {
                "fields": (
                    "referee_name",
                    "referee_mobile_number_1",
                    "referee_mobile_number_2",
                    "referee_email",
                    "referee_relationship_to_tenant",
                )
            },
        ),
    )

    def get_tenant_name(self, obj):
        return " ".join([obj.first_name, obj.last_name])

    def change_view(self, request, object_id, form_url="", extra_context=None):
        """
        Change view allows you pass in extra context to an admin template
        :param request:
        :param object_id:
        :param form_url:
        :param extra_context:
        :return:
        """
        extra_context = extra_context or {}
        tenant_comments = models.TenantComment.objects.filter(tenant_id=object_id)
        extra_context["tenant_comments"] = tenant_comments
        extra_context["user"] = request.user
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

    get_tenant_name.short_description = "First Name/Last Name"


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Property, PropertyAdmin)
admin.site.register(models.PropertyImage, PropertyImageAdmin)
admin.site.register(models.TenantDocument, TenantDocumentAdmin)
admin.site.register(models.Letting, LettingAdmin)
admin.site.register(models.PaymentSchedule, PaymentScheduleAdmin)
admin.site.register(models.PropertyDocument)
admin.site.register(models.PropertyRunningCosts)
admin.site.register(models.TenantComment, TenantCommentAdmin)
admin.site.register(models.Bills, BillsAdmin)
admin.site.register(models.PropertyInventory, PropertyInventoryAdmin)

admin.site.site_header = "Pyale Properties"
admin.site.site_title = "Pyale Properties"
admin.site.index_title = "Pyale Properties Administration Portal"
