angular.module('opal.records').factory('InfusionRecord', function(){
    return function(record){
        if(!record.start_time && !record.id){ record.start_time = moment()}
        return record;
    }
});
