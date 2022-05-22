import copy
from html.parser import HTMLParser


class TableHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.td = False
        self.th = False
        self.table = []
        self.row = []
        self.cell = []

    def handle_starttag(self, tag, attrs):
        if tag == "td":
            self.td = True
        if tag == "th":
            self.th = True

    def handle_endtag(self, tag):
        if self.td or self.th:
            self.td = False
            self.th = False
        if tag in ["td", "th"]:
            self.row.append(" ".join(self.cell).strip())
            self.cell = []
        elif tag == "tr":
            self.table.append(copy.deepcopy(self.row))
            self.row = []

    def handle_data(self, data):
        if self.td or self.th:
            self.cell.append(data.strip())
