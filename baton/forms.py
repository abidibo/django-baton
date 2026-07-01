from __future__ import annotations

from typing import Any

from django.forms.fields import ImageField
from django.forms.widgets import Widget
from .widgets import BatonAiImageInput
from .config import get_config


class BatonAiImageFormField(ImageField):
    widget = BatonAiImageInput

    def __init__(
        self,
        subject_location_field: str | None = None,
        alt_field: str | None = None,
        alt_chars: int = 20,
        alt_language: str = 'en',
        *args: Any,
        **kwargs: Any,
    ) -> None:
        self.subject_location_field = subject_location_field
        self.alt_field = alt_field
        self.alt_chars = alt_chars
        self.alt_language = alt_language
        return super().__init__(*args, **kwargs)

    def widget_attrs(self, widget: Widget) -> dict[str, Any]:
        attrs = super().widget_attrs(widget)
        attrs['subject_location_field'] = self.subject_location_field
        attrs['alt_field'] = self.alt_field
        attrs['alt_chars'] = self.alt_chars
        attrs['alt_language'] = self.alt_language
        attrs['preview_width'] = get_config('IMAGE_PREVIEW_WIDTH')
        return attrs
