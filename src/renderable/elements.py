from dataclasses import dataclass
from typing import ClassVar

from .base import Renderable


@dataclass
class Link(Renderable):
    """HTML link element.
    """

    href: str
    text: str = 'click'

    template: ClassVar[str] = (
        '<a href="{{ obj.href }}">'
        '{{ obj.text }}'
        '</a>'
    )


@dataclass
class ContextButton(Renderable):
    """Contextual button element.
    """

    type_: str = 'submit'
    class_: str = 'primary'
    text: str = 'ok'

    template: ClassVar[str] = (
        '<button type="{{ obj.type_ }}" class="button-{{ obj.class_ }}">'
        '{{ obj.text }}'
        '</button>'
    )


@dataclass
class SVGIconButton(Renderable):
    """HTML button element representation with basic attributes and SVG
    icon loaded from embedded iconset.
    """

    type_: str = 'submit'
    class_: str = 'primary'
    icon: str = 'check'
    text: str = 'ok'

    template: ClassVar[str] = (
        '<button type="{{ obj.type_ }}" class="button-{{ obj.class_ }}">'
        '<span class="icon">'
        '<svg><use xlink:href="#{{ obj.icon }}"></svg>'
        '</span>'
        '&nbsp;'
        '<span>{{ obj.text }}</span>'
        '</button>'
    )
