from mwparserfromhell.nodes.extras import Parameter
from mwparserfromhell.nodes.template import Template

class TWTemplate():
    # TODO add main functionality for templates (to_wikitext etc.)

    def __init__(self):
        self._template = Template(self.get_name())
        self._parameters = []
        self._parameters_map = {}

    def is_supported(self, pname):
        return False

    def has(self):
        return self._parameter

    def to_wikitext(self):
        t = "{{" + self.name
        for param in self.get_valid_parameters():
            if param in self._parameters_map:
                t += self.format_parameter(param, self._parameters_map[param].value)

        for param in self._parameters_map:
            if not self.is_valid_parameter(param):
                raise ValueError("Invalid parameter: " + param)

        t += "}}"
        return t

    def set(self, key, value, showkey=True):
        # Check for uniqueness.
        # Wikicode is not hashable, so we instead use the stringified version
        # as the key and include the Wikicode <parameter name> within the object.
        skey = str(key)
        if not self.is_supported(skey):
            raise ValueError("Not supported: parameter %s" % (skey,))

        if skey not in self._parameters_map:
            o = Parameter(key, value, showkey)
            self._parameters.append(o)
            # Needed for consistency - allow future lookups of this parameter.
            self._parameters_map[skey] = o
        else:
            # Overwrite existing parameter.
            o = self._parameters_map[skey]
            # Don't allow changing parameter names - creates a consistency problem.
            o.value = value
            o.showkey = showkey

    @staticmethod
    def normalise_parameter(parameter):
        return parameter.lower().strip()

    def from_template(self, template):
        for param in template.params:
            self.set(self.normalise_parameter(param.name), param.value)
