angular.module('opal.controllers').controller(
    'd3timeline',
    function(
        $rootScope, $scope, $window,
        recordLoader, ngProgressLite, $q,
        $cookieStore, patientLoader
    ){

        var dateformat = "DD/MM/YYYY HH:mm:ss";
        var interval;

        $scope.monitorPairing = function(){
            var result = _.find($scope.patient.pairing, function(pairing){
                return pairing.start && !pairing.stop
            });

            if(!result){
                return;
            }
            return $scope.metadata.monitors[String(result.monitor_id)]
        }

        var drugs = function(drug){
            // stuff this still has to do
            // calculate total doses for each drug

            //if new drug create xs and column, if old push to existing.

            $scope.druglist = new Array();
            $scope.drugdata = [] ;

            //set up stuff for infusions


            _.each(drug, function(a){
                var drugname = a.drug_name ;
                var drugtime = a.datetime.format("DD/MM/YYYY HH:mm:ss");
                var drugclass = a.drug_type ;
                var drugdose = a.dose ;

                function capitalizeEachWord(str) {
                    return str.replace(/\w\S*/g, function(txt) {
                        return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
                    });
                }

                drugclass = capitalizeEachWord(drugclass);

                //push dose to array for labels
                $scope.labels.push(drugdose);

                var inlist = _.indexOf($scope.druglist, drugname);
                if (inlist == '-1'){
                    // drug not given before
                    $scope.druglist.push({label: drugname, times: [],});
                  }

                //select the right colour
                //stuff to do
                // 1 find a better way of doing this
                //have some reminder to change this if we change class names

                var colours = [
                    {class: "Antiemetic Drug", colour: "#EFBE7D"},
                    {class: "Induction Agent Drug", colour: '#ffe800'},
                    {class: "Hypnotic Drug", colour: '#FF8200'},
                    {class: "Hypnotic Antagonist Drug", colour: '#FF8200'},
                    {class: "Neuromuscular Blocking Drug", colour: '#ff7477'},
                    {class: "Neuromuscular Blocking Drug Antagonist", colour: '#ff7477'},
                    {class: "Depolarizing Neuromuscular Blocking Drug", colour: '#ff7477'},
                    {class: "Opioid Drug", colour: '#71C5E8'},
                    {class: "Opioid Antagonist", colour: '#71C5E8'},
                    {class: "Vasopressor Drug", colour: '#D6BFDD'},
                    {class: "Local Anaesthetics Drug", colour: '#AFA9A0'},
                    {class: "Anticholinergic Drug", colour: '#A4D65E'},
                    {class: "Other Drug Agents", colour: '#ffffff'},
                ];
                //var nextcolour = _.where(colours, drugclass);
                var something = {class: drugclass};
                var nextcolour = _.findWhere(colours, something);
                //debugger;
                if (nextcolour == null){
                    nextcolour = '#736969';
                } else {
                  nextcolour = nextcolour.colour
                }

                _.each($scope.druglist, function(b){
                	if (drugname == b.label){
                	      b.times.push({
                          "color": nextcolour,
                          "label": drugdose,
                          "starting_time":drugtime,
                          "display": "circle",
                        })
                	    }
                })
            });
        }

        patientLoader().then(function(patient){
            newdrugs = drugs(patient.episodes[0].given_drug);
            // DEBUG:
            console.log($scope.druglist)
            var chart = d3.timeline();
            var svg = d3.select("#timeline1").append("svg").attr("width", 500).datum($scope.druglist).call(chart);

        });

        // interval = setInterval(function () {
        //   patientLoader().then(function(patient){
        //     newColumns = createColumns(patient.episodes[0].observation);
        //     newgasses = creategasses(patient.episodes[0].gases);
        //     newvents = ventsettings(patient.episodes[0].ventilation);
        //     newlines = gridlines(patient.episodes[0].anaesthetic_note);
        //     newdrugs = drugs(patient.episodes[0].given_drug);
        //
        //     //set first and last time for x axis
        //     $scope.firstobs = newColumns[4][1];
        //     $scope.lastobs = newColumns[4][newColumns[4].length-1];
        //
        //     drugchart.axis.range({max: {x: $scope.lastobs}, min: {x: $scope.firstobs}, });
        //     //chart.grid(newlines);
        //     chart.load({
        //         columns: newColumns,
        //         grid: newlines,
        //     });
        //     chart2.load({
        //         columns: newgasses,
        //     });
        //     chart3.load({
        //         columns: newvents,
        //     });
        //     drugchart.load({
        //         columns : newdrugs.columns,
        //         xs: newdrugs.xs,
        //         colors: newdrugs.colors,
        //
        //     });
        //   });
        //   drawlabels(drugchart.interal);
        // }, 1000);
        //
        // $scope.$on("$routeChangeStart", function(){
        //   if(interval){
        //     clearInterval(interval);
        //   }
        // });
        //

    });
