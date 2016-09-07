from django.contrib import admin

from .models import Author, Quote


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    base_fields = ('text', 'author')
    admin_fields = ('user',)

    def get_fields(self, request, obj=None):
        fields = self.base_fields
        if request.user.is_superuser:
            fields += self.admin_fields
        return fields

    def get_queryset(self, request):
        qs = super(QuoteAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not change and not request.user.is_superuser:
            obj.user = request.user
        obj.save()
