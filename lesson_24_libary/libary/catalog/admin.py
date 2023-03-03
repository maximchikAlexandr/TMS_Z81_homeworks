from django.contrib import admin
from catalog.models import Genre, Language, Author, BookInstance, Book


class BookInline(admin.TabularInline):
    model = Book


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "display_genre"]
    search_fields = ["title", "author__pseudonym"]
    inlines = [BookInstanceInline]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "pseudonym",
                    "date_of_birth", "date_of_death"]
    search_fields = ["pseudonym", "first_name", "last_name"]
    inlines = [BookInline]


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ["book", "status", "borrower", "due_back"]
    fieldsets = (
        ("Availability", {
            "fields": ("book", "status", "borrower")
        }),
        (None, {
            "fields": ("due_back",)
        })
    )


admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Author, AuthorAdmin)
