import TemplateParser

class ItemParser(TemplateParser):

    def get_template_name():
        return "Infobox Item"

    def get_template_parameters():
        lines = []
        with open("data/parameters-item.txt") as fp:
            lines = fp.readLines()
        return lines
    

    def parse(text):

