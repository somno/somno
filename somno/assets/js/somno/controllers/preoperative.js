angular.module('opal.controllers').controller('preoperative', function($scope, slugifyFilter){
  $scope.tab = "preop";


  function appendrisk(){
    var risk = $(this).val();
    $('textarea').tagsinput('add', risk)
  }

  function addbutton(name) {
    var button = document.createElement("BUTTON");
    var buttondiv = document.getElementById("buttons");
    var label = document.createTextNode(name);
    button.onclick= appendrisk ;
    button.value = name ;
    button.className = "btn btn-warning btn-sm";
    button.appendChild(label);
    buttondiv.appendChild(button);
  }
  var showRisks = function(procedure){
    if (procedure != undefined){
      var riskybusyness = _.find($scope.metadata.Risks, function(x, y){
        return y == procedure
      });
    }
    document.getElementById("buttons").innerHTML = "";
    _.each(riskybusyness, function(r){
      addbutton(r);
    });
  };

  $scope.$watch('editing.anaesthetic_plan.Proposed_Procedure', showRisks);
});
