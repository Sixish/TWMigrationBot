import pywikibot
from pywikibot import pagegenerators
import mwparserfromhell
from mwparserfromhell.parser import Parser

from items import ItemTemplate
from objects import ObjectTemplate
import summary

parser = Parser()
site = pywikibot.Site()

# Map: keys are template names, values are lists of handlers.
registeredHandlers = {}

def create_template_handler(name):
    if name not in registeredHandlers:
        registeredHandlers[name] = []

def trigger_handler(name, template):
    # Just in case it doesn't exist yet.
    create_template_handler(name)

    for handler in registeredHandlers[name]:
        template = handler(template)

    return template

def register_handler(name, handler):
    # Just in case it doesn't exist yet.
    create_template_handler(name)

    registeredHandlers[name].append(handler)

def remove_prefix_if_exists(s, pre):
    # Assume input is normalised so no preprocessing required.
    if s.startswith(pre):
        s = s[len(pre):]
    return s

def normalise_template_name(t):
    return remove_prefix_if_exists(t.lower().replace("_", " "), "template:")

def maintain_wiki(pages):
    for page in pages:
        summary.clear()
        try:
            title = page.title()
            wikitext = mwparserfromhell.parse(page.text)
            new_wikitext = ""

            # We cannot just filter by templates because then we cannot reconstruct
            # the original page.
            #templates = wikitext.filter_templates()

            for node in wikitext.nodes:
                num_items = 0

                if isinstance(node, mwparserfromhell.nodes.template.Template):
                    # Found a template, for handlers of this template.
                    template_name = normalise_template_name(str(node.name))

                    if template_name in registeredHandlers:
                        node = trigger_handler(template_name, node)

                # Add the changes, if necessary.
                new_wikitext += str(node)

            if wikitext != new_wikitext:
                page.text = new_wikitext
                page.save(summary="[bot] %s" % (summary.get(),), asynchronous=True, botflag=True)
        except ValueError as e:
            print("Could not process page %s: %s" % (title, str(e)))

def get_candidate_items():
    # Won't be definitive (can be non-items in this category)
    # Can still use as a filter.

    cat = pywikibot.Category(site, "Category:Items")

    # 
    gen = pagegenerators.CategorizedPageGenerator(cat)

    return gen

def get_candidate_objects():
    return pagegenerators.CategorizedPageGenerator(
        pywikibot.Category(site, "Category:Objects"))

def construct_item(template):
    # Assume input is an infobox item template, otherwise everything breaks.
    # (Check this elsewhere)
    pass


def update_database(template):
    item = ItemTemplate()
    item.from_template(template)

    obj = item.to_object()

    return item.to_object().to_wikitext()

def set_not_pickupable(template):
    obj = ObjectTemplate()
    obj.from_template(template)

    obj.set("pickupable", " no\n", showkey=True)
    summary.put("Enforcing syntax consistency, ensure pickupable=no.")

    # Return wikicode instead of wikitext.
    return parser.parse(obj.to_wikitext())


register_handler('infobox object', set_not_pickupable)
#register_handler('infobox item', update_database)

#maintain_wiki(get_candidate_items())
maintain_wiki(get_candidate_objects())
