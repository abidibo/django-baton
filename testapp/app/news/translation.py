from modeltranslation.translator import TranslationOptions, register
from .models import News, Tag


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = (
        "title",
        "body",
        "attachments_summary",
        "videos_summary",
    )
