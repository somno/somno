"""
Somno - Our Opal Application
"""
from opal.core import application


class Application(application.OpalApplication):
    schema_module = 'somno.schema'
    flow_module   = 'somno.flow'

    core_javascripts = {
        'opal.upstream.deps': [
            "js/lib/modernizr.js",
            "js/lib/c3-0.4.10/c3.js",

            "js/lib/bower_components/angular/angular.js",
            "js/lib/bower_components/angular-route/angular-route.js",
            "js/lib/bower_components/angular-resource/angular-resource.js",
            "js/lib/bower_components/angular-cookies/angular-cookies.js",

            "js/lib/angular-ui-utils-0.1.0/ui-utils.js",
            "js/lib/ui-bootstrap-tpls-0.14.3.js",

            "js/lib/utils/clipboard.js",
            "bootstrap-3.1.0/js/bootstrap.js",
            "js/lib/angulartics-0.17.2/angulartics.min.js",
            "js/lib/angulartics-0.17.2/angulartics-ga.min.js",

            "js/lib/bower_components/ment.io/dist/mentio.js",
            "js/lib/bower_components/ment.io/dist/templates.js",
            # "js/ui-select/dist/select.js",
            "js/lib/bower_components/angular-ui-select/dist/select.js",
            "js/lib/bower_components/ng-idle/angular-idle.js",
            "js/lib/bower_components/angular-local-storage/dist/angular-local-storage.js",  # noqa: E501
            "js/lib/bower_components/ment.io/dist/templates.js",
            "js/lib/bower_components/angular-growl-v2/build/angular-growl.js",
            "js/lib/jquery-plugins/idle-timer.js",
            "js/lib/jquery-plugins/jquery.stickytableheaders.js",
            "js/lib/utils/underscore.js",
            "js/lib/utils/showdown.js",
            "js/lib/utils/moment.js",
            "js/lib/ngprogress-lite/ngprogress-lite.js",
        ],
        'opal.utils': [
            "js/opal/utils.js",
            "js/opal/opaldown.js",
            "js/opal/directives.js",
            "js/opal/filters.js",
        ],
        'opal.services': [
            "js/opal/services_module.js",
            "js/opal/services/flow.js",
            "js/opal/services/user_profile.js",
            "js/opal/services/user.js",
            "js/opal/services/item.js",
            "js/opal/services/http_interceptors.js",
            "js/opal/services/episode.js",
            "js/opal/services/patient.js",
            "js/opal/services/episode_visibility.js",
            "js/opal/services/episode_loader.js",
            "js/opal/services/record_loader.js",
            "js/opal/services/patient_loader.js",
            "js/opal/services/episode_resource.js",
            "js/opal/services/record_editor.js",
            "js/opal/services/copy_to_category.js",
            "js/opal/services/patientlist_loader.js",
            'js/opal/services/fields_translater.js',
            'js/opal/services/referencedata.js',
            'js/opal/services/metadata.js',
            'js/opal/services/patient_consultation_record.js',
        ],
        'opal.controllers': [
            "js/opal/controllers_module.js",
            "js/opal/controllers/patient_list_redirect.js",
            "js/opal/controllers/patient_list.js",
            "js/opal/controllers/patient_detail.js",
            "js/opal/controllers/hospital_number.js",
            "js/opal/controllers/add_episode.js",
            "js/opal/controllers/edit_item.js",
            "js/opal/controllers/edit_teams.js",
            "js/opal/controllers/delete_item_confirmation.js",
            "js/opal/controllers/account.js",
            "js/opal/controllers/discharge.js",
            "js/opal/controllers/undischarge.js",
            "js/opal/controllers/copy_to_category.js",
            "js/opal/controllers/keyboard_shortcuts.js",
            "js/opal/controllers/patient_access_log.js",
            "js/opal/controllers/lookup_list_reference.js"
        ]
    }

    javascripts = [
        'js/somno/routes.js',
        'js/somno/filters.js',
        'js/somno/directives.js',
        'js/somno/controllers/drug_controller.js',
        'js/somno/services/records/infusion.js',
        'js/somno/services/records/event.js',
        'js/somno/services/records/observation_record.js',
        'js/somno/services/infusion.js',
        'js/somno/controllers/newgraph.js',
        'js/somno/controllers/induction_drug_controller.js',
        'js/somno/controllers/new_infusions.js',
        'js/somno/controllers/d3timeline.js',
        'js/somno/d3-timelines.js',
    ]
    styles = [
        "css/somno.css",
        "css/anaesthetic_drug_colours.css",
        "css/anaesthetic_drug_colours.scss"
    ]
