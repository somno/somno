angular.module('opal.controllers').controller(
  'UnPairMonitorController', function(step, scope, episode){
    "use strict";

    if(!_.isArray(scope.editing.monitor_patient_pairing)){
      scope.editing.monitor_patient_pairing = [scope.editing.monitor_patient_pairing]
    }
    var whichMonitor = function(){
      var result = _.find(scope.editing.monitor_patient_pairing, function(mpp){
        return mpp.start && !mpp.stop
      });

      if(!result){
        return;
      }
      return scope.metadata.monitors[String(result.monitor_id)]
    }

    scope.monitor = whichMonitor();
});
