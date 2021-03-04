from jinja2 import Template
from markupsafe import Markup


class Renderable:
    """An object that can be rendered."""

    template = ''

    def __post_init__(self):
        self._template = Template(self.template)

    def render(self) -> Markup:
        """Render template into :class:`Markup` object.

        :return: rendering result as Markup
        :rtype: Markup
        """
        return Markup(self._template.render(obj=self))
