from __future__ import annotations

from django.forms.widgets import ClearableFileInput


class BatonAiImageInput(ClearableFileInput):
    template_name: str = "baton/widgets/ai_image.html"
