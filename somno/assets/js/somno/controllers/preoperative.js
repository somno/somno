angular.module('opal.controllers').controller('preoperative', function($scope, slugifyFilter){
  $scope.tab = "preop";

  var showRisks = function(procedure){
    if (procedure != undefined){
      var riskybusyness = _.find($scope.metadata.Risks, procedure);
      alert(riskybusyness);
    }
    debugger


  };


  $scope.$watch('editing.anaesthetic_plan.Proposed_Procedure', showRisks);
});
