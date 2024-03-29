
from tinymce.widgets import TinyMCE
from django.db import models
from .models import Tutorial


class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["tut_title", "tut_published"]}),
        ("Content", {"fields": ["tut_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


admin.site.register(Tutorial,TutorialAdmin)