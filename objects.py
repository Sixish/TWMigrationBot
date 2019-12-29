from osutils import data_filepath
from twtemplate import TWTemplate
import summary

class ObjectTemplate(TWTemplate):
    # Generate a list of object parameters from the data file.
    PNAME_ORDER = open(data_filepath("parameters-object.txt"),
        "r").read().splitlines()

    SUPPORTED_PARAMETERS = set(PNAME_ORDER)

    # Determines padleft behavior
    PNAME_DEFAULT_PADLEFT = True
    PNAME_OVERRIDE_PADLEFT = {
        'list': False,
        'getvalue': False
    }

    # Determines padright behavior
    PNAME_DEFAULT_PADRIGHT = True
    PNAME_OVERRIDE_PADRIGHT = {
        'list': False,
        'getvalue': False
    }

    PNAME_NORM2RAW = {
        'list': 'List',
        'getvalue': 'GetValue'
    }

    MAX_LENGTH_PARAMETER_NAME = len(max(PNAME_ORDER, key=len))
    
    def __init__(self):
        super().__init__()
        self.name = "Infobox Object"

    def is_valid_parameter(self, pname):
        return (pname in self.SUPPORTED_PARAMETERS)

    def get_valid_parameters(self):
        return self.PNAME_ORDER

    def construct(self):
        obj = Object()

    def is_valid(self):
        valid = True
        # TODO
        return valid

    def get_pname_padright(self, spname):
        return self.PNAME_OVERRIDE_PADRIGHT.get(spname,
            self.PNAME_DEFAULT_PADRIGHT)

    def get_pname_padleft(self, spname):
        return self.PNAME_OVERRIDE_PADLEFT.get(spname,
            self.PNAME_DEFAULT_PADLEFT)

    def denormalise_pname(self, norm_pname):
        return self.PNAME_NORM2RAW.get(norm_pname, norm_pname)

    def format_parameter(self, pname, pvalue):
        spname = str(pname)
        spvalue = str(pvalue)

        t = "|"

        if (self.get_pname_padleft(spname)):
            # Only want one space left of parameter name.
            t += " "

        t += self.denormalise_pname(spname)

        if (self.get_pname_padright(spname)):
            # Pad right until MAX_LENGTH_PARAMETER_NAME is reached,
            # plus one to avoid parameters being immediately followed by '='.
            t += " " * (self.MAX_LENGTH_PARAMETER_NAME - len(str(spname)) + 1)

        # Provide the original value for the parameter.
        t += "=" + spvalue

        return t

    def is_supported(self, pname):
        return (pname in self.SUPPORTED_PARAMETERS)

    def get_name(self):
        return 'Infobox Object'
