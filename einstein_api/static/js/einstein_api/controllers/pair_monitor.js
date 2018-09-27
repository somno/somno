angular.module('opal.controllers').controller(
  'PairMonitorController', function(step, scope, episode){
    "use strict";
    var currentRunning = _.filter(scope.editing.pairing, function(x){
      return !x.stop;
    });

    if(currentRunning.length){
      scope.currentRunning = currentRunning[0].monitor_id;
    }

    scope.editing.pairing = {};
});
