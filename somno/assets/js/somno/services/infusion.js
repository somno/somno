angular.module('opal.services').factory('Infusion', function(){
  "use strict";
  var states = {
    NORMAL: "normal",
    STOPPED: "stopped",
    CHANGED: "changed",
  }

  var Infusion = function(patient_id, someArgs){
    if(_.size(someArgs)){
      _.extend(this, someArgs);
    }
    this._client = {
      completed: false,
      id: _.uniqueId("infusion"),
      // stopped is only set if the are stopped in this session
      stopped: false,
      // when they click change, this is set to the old value of
      // rate
      changing: null,
      // used when they've changed the rate
      // as we want to create a new item
      startState: angular.copy(someArgs),
      state: states.NORMAL
    };
    this.patient_id = patient_id;

    if(!this.start_time){
      this.start_time = new Date();
    }
  }

  Infusion.prototype = {
    preSave: function(){
      if(this.id && this.hasChanged()){
        this.id = undefined;
        this.consistency_token = undefined;
      }
    },
    previouslyStopped: function(){
      return this.stopped_time || this._client.stopped;
    },
    complete: function(){
      return this.drug_name && this.rate;
    },
    stop: function(){
      this.stopped_time = new Date();
      this._client.state = states.STOPPED;
    },
    undo: function(){
      _.each(this._client.startState, function(v, k){
        this[k] = v;
      });
      this.stopped_time = null;
      this.state = states.NORMAL;
    },
    change: function(){
      this._client.state = states.CHANGED;
    },
    doneChanging: function(){
      this._client.state = states.NORMAL;
    },
    hasChanged: function(){
      if(!this._client.startState){
        return false;
      }
      var changed = this.rate !== this._client.startState.rate;
      var timeStoppedNow = null;
      if(this.stopped_time){
        timeStoppedNow = this.stopped_time.toGMTString();
      }

      var timeStoppedThen = null;

      if(this._client.startState.stopped_time){
        timeStoppedThen = this._client.startState.stopped_time.toGMTString();
      }

      return changed || timeStoppedNow !== timeStoppedThen
    },
    getOldChanged: function(){
      if(this.hasChanged()){
        var old = angular.copy(this._client.startState);
        old.stopped_time = new Date();
        return old;
      };
    },
    currentlyExisting: function(){
      return this.id && !this._client.startState.stopped_time;
    }
  }

  return Infusion;
});
