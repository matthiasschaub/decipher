import logging
import textwrap
from typing import Any, cast

from marko.renderer import Renderer

from decipher import helper
from decipher.template import template


class VimDocRenderer(Renderer):
    def render_paragraph(self, element: "block.Paragraph") -> str:
        text = textwrap.wrap(text=self.render_children(element), width=78)
        return "\n".join(text) + "\n"

    def render_list(self, element: "block.List") -> str:
        return self.render_children(element) + "\n"

    def render_list_item(self, element: "block.ListItem") -> str:
        return "- " + self.render_children(element)

    def render_quote(self, element: "block.Quote") -> str:
        return self.render_children(element) + "\n"

    def render_fenced_code(self, element: "block.FencedCode") -> str:
        indent = " " * 4
        lines = self.render_children(element).splitlines()
        lines = [indent + line for line in lines]
        lines = "\n".join(lines)
        return ">\n{}\n<\n".format(lines)

    def render_code_block(self, element: "block.CodeBlock") -> str:
        indent = " " * 4
        lines = self.render_children(element).splitlines()
        lines = [indent + line for line in lines]
        lines = "\n".join(lines)
        return ">\n{}\n<\n".format(lines)

    def render_html_block(self, element: "block.HTMLBlock") -> str:
        try:
            return helper.parse_html_table(element.children)
        except ValueError:
            logging.warning(
                "Could not parse HTML Block as table. "
                + "This element could not be converted to Vimdoc"
            )
            logging.debug(element.children)
            return "*Error: HTML Block element to Vimdoc is not supported.\n"

    def render_thematic_break(self, element: "block.ThematicBreak") -> str:
        return ""

    def render_heading(self, element: "block.Heading") -> str:
        if element.level == 1:
            return ""
        elif element.level == 2:
            temp = template.get_heading(level=2)
            # Is it a "rune" or "overview"?
            if len(self.render_children(element).split(" ")) == 1:
                return self.render_children(element) + "~\n"
            rune_raw, name_raw, *_ = self.render_children(element).split(" ")
            rune = helper.remove_chars(rune_raw)
            name = helper.remove_chars(name_raw)
            rune_tag = helper.parse_as_tag(rune)
            name_tag = helper.parse_as_tag(name)
            return temp.substitute(
                name_upper=name.upper(),
                name_tag=name_tag,
                rune_tag=rune_tag,
            )
        else:
            return self.render_children(element) + "~\n"

    def render_setext_heading(self, element: "block.SetextHeading") -> str:
        if element.level > 4:
            return self.render_children(element).capitalize()
        else:
            return self.render_children(element) + "~"

    def render_blank_line(self, element: "block.BlankLine") -> str:
        return "\n"

    def render_link_ref_def(self, element: "block.LinkRefDef") -> str:
        message = (
            "*Error: Link Reference Definition element to Vimdoc is not supported."
        )
        logging.warning(message)
        return message + "\n"

    def render_emphasis(self, element: "inline.Emphasis") -> str:
        return self.render_children(element)

    def render_strong_emphasis(self, element: "inline.StrongEmphasis") -> str:
        return self.render_children(element)

    def render_inline_html(self, element: "inline.InlineHTML") -> str:
        message = "Error: Inline HTML element to Vimdoc is not supported."
        logging.warning(message)
        logging.debug(element.children)
        return message + "\n"

    def render_plain_text(self, element: Any) -> str:
        if isinstance(element.children, str):
            return element.children
        return self.render_children(element)

    def render_link(self, element: "inline.Link") -> str:
        return self.render_children(element)

    def render_auto_link(self, element: "inline.AutoLink") -> str:
        return self.render_link(cast("inline.Link", element))

    def render_image(self, element: "inline.Image") -> str:
        message = "*Error: Image element to Vimdoc is not supported."
        logging.warning(message)
        return message + "\n"

    def render_literal(self, element: "inline.Literal") -> str:
        return element.children

    def render_raw_text(self, element: "inline.RawText") -> str:
        return element.children

    def render_line_break(self, element: "inline.LineBreak") -> str:
        return " "

    def render_code_span(self, element: "inline.CodeSpan") -> str:
        return "`{0}`".format(element.children)
