"""
Somno - Our Opal Application
"""
from opal.core import application

class Application(application.OpalApplication):
    schema_module = 'somno.schema'
    flow_module   = 'somno.flow'
    javascripts   = [
        'js/somno/routes.js',
        'js/somno/filters.js',
        'js/somno/controllers/drug_controller.js',
        'js/somno/services/records/observation_record.js',
        'js/somno/services/infusion.js',
        'js/somno/controllers/newgraph.js',
        'js/somno/controllers/induction_drug_controller.js',
        'js/somno/controllers/new_infusions.js',
    ]
    styles = [
        "css/somno.css",
        "css/anaesthetic_drug_colours.css",
        "css/anaesthetic_drug_colours.scss"
    ]
