angular.module('opal.controllers').controller(
  'NewInfusionsController', function(step, scope, episode, Infusion){
    "use strict";


    if(!scope.editing.infusion){
      scope.editing.infusion = [new Infusion(episode.patient_id)];
    }
    else if(!_.isArray(scope.editing.infusion)){
      scope.editing.infusion = new Infusion(episode.patient_id, scope.editing.infusion);
    }
    else{
      scope.editing.infusion = _.map(scope.editing.infusion, function(infusion){
        return new Infusion(episode.patient_id, infusion);
      })
    }

    scope.addAnother = function(){
      scope.editing.infusion.push(new Infusion(episode.patient_id));
    };

    scope.hasExisting = _.filter(scope.editing.infusion, function(i){
      return i.currentlyExisting()
    }).length;

    scope.preSave = function(editing){
      var additional = [];
      editing.infusion = _.filter(editing.infusion, function(i){
        return i.complete();
      });
      _.each(editing.infusion, function(i){
        i.preSave();
        var addition = i.getOldChanged();
        if(addition){
          additional.push(addition);
        }
      });
      _.each(additional, function(a){
        editing.infusion.push(a);
      });
    };

    scope.addAnother();
});
