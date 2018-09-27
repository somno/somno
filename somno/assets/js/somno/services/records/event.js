angular.module('opal.records').factory('EventRecord', function(){
    return function(record){
        if(!record.datetime && !record.id){ record.datetime = moment()}
        return record;
    }
});
