from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "is_published", "created_at", "updated_at")
    list_filter = ("is_published", "created_at", "updated_at")
    search_fields = ("title", "content", "author__email", "author__full_name")
    list_editable = ("is_published",)
    ordering = ("-created_at",)
    actions = ("publish_selected", "unpublish_selected")

    @admin.action(description="Publish selected articles")
    def publish_selected(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description="Unpublish selected articles")
    def unpublish_selected(self, request, queryset):
        queryset.update(is_published=False)

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)
