from osutils import data_filepath
from twtemplate import TWTemplate
from objects import ObjectTemplate
from mwparserfromhell.nodes.extras import Parameter

class ItemTemplate(TWTemplate):
    # Generate a list of item parameters from the data file.
    SUPPORTED_PARAMETERS = set(
        open(data_filepath("parameters-item.txt"), "r").read().splitlines()
    )

    PARAMETER_NORM_TO_OUTPUT = {
        # TODO "lowercase_normalised": "actual_parameter_name"
    }
    
    def __init__(self):
        super().__init__()

    def get_valid_parameters(self):
        return self.SUPPORTED_PARAMETERS
        
    def is_valid(self):
        valid = True
        # TODO
        return valid

    MAP_EQUIVALENT_OBJECT_PARAMETER = {
        'type': 'weapontype'
    }
    @staticmethod
    def map_item2object_param_name(pname):
        pname = str(pname)
        if pname in ItemTemplate.MAP_EQUIVALENT_OBJECT_PARAMETER:
            pname = ItemTemplate.MAP_EQUIVALENT_OBJECT_PARAMETER[str(pname)]
        return pname

    def to_object(self):
        obj = ObjectTemplate()
        for param in self.parameters:
            pname = self.normalise_parameter(param.name)
            pvalue = str(param.value)

            obj.set(pname, pvalue, showkey=param.showkey)
        return obj

    def get_name(self):
        return 'Infobox Item'
