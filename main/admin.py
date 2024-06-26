from django.contrib import admin
from .models import QAPair,fetch_transformer_answer

class QAPairAdmin(admin.ModelAdmin):
    list_display = ('question',)
    search_fields = ('question',)

    def save_model(self, request, obj, form, change):
        if not obj.answer:
            obj.answer = fetch_transformer_answer(obj.question)
        super().save_model(request, obj, form, change)

admin.site.register(QAPair, QAPairAdmin)
