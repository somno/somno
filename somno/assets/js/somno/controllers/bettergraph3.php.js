angular.module('opal.controllers').controller(
    'bettergraph',
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

        var createColumns = function(anaesthetics){
            var columns = [
                ["bp_systolic"], ["bp_diastolic"], ["pulse"], ["Sp02"], ["datetime"]
            ];
            anaesthetics = _.map(anaesthetics.reverse(), function(a){
                a.datetime =  a.datetime.format("DD/MM/YYYY HH:mm:ss");
                return a;
            });


            _.each(columns, function(column){
                _.each(anaesthetics, function(anaesthetic){
                    column.push(anaesthetic[column[0].toLowerCase()]);
                });
            });

            return columns;
        }

        var creategasses = function(anaesthetics){
            var columns = [
                ["expired_oxygen"], ["inspired_oxygen"], ["expired_aa"], ["expired_carbon_dioxide"], ["datetime"]
            ];
            anaesthetics = _.map(anaesthetics.reverse(), function(a){
                a.datetime =  a.datetime.format("DD/MM/YYYY HH:mm:ss");
                return a;
            });


            _.each(columns, function(column){
                _.each(anaesthetics, function(anaesthetic){
                    column.push(anaesthetic[column[0].toLowerCase()]);
                });
            });

            return columns;
        }

        var ventsettings = function(anaesthetics){
            var columns = [
                ["peak_airway_pressure"], ["peep_airway_pressure"], ["tidal_volume"], ["rate"], ["datetime"]
            ];
            anaesthetics = _.map(anaesthetics.reverse(), function(a){
                a.datetime =  a.datetime.format("DD/MM/YYYY HH:mm:ss");
                return a;
            });


            _.each(columns, function(column){
                _.each(anaesthetics, function(anaesthetic){
                    column.push(anaesthetic[column[0].toLowerCase()]);
                });
            });

            return columns;
        }

        var gridlines = function(events){

            events = _.map(events, function(a){
                a.datetime =  a.datetime.format("DD/MM/YYYY HH:mm:ss");
                function newline(time, title){
                    this.value = time;
                    this.text = title;
                }
                var lines2 = new newline(a.datetime, a.Title);
                return lines2;
            });

            var line = {
                x:{
                    lines: events,
                },
            };

            return line;

        }

        var chart;

        function drawlabels(chartInternal){
            var textLayer = drugchart.internal.main.select('.' + c3.chart.internal.fn.CLASS.chartTexts);
            _.each(drugchart.internal.mainCircle, function(a){
                _.each(a, function(){
                    textLayer.select('text').remove();
                })
            })
            _.each(drugchart.internal.mainCircle, function(point){
                _.each(point, function(p){
                    var d3point = d3.select(p);
                    var ind = _.findIndex(drugchart.internal.mainCircle, point);
                    textLayer
                        .append('text')
                    // center horizontally and vertically
                        .style('text-anchor', 'middle').attr('dy', '.2em')
                        .text($scope.labels[ind])
                    // same as at the point
                        .attr('x', d3point.attr('cx') ).attr('y', d3point.attr('cy'));
                })
            })
        }

        patientLoader().then(function(patient){
            newColumns = createColumns(patient.episodes[0].observation);
            newlines = gridlines(patient.episodes[0].anaesthetic_note);

            chart_padding = 75;
            chart = c3.generate({

                bindto: '#chart',
                legend: {
                    show: false
                },
                padding:{
                    left: chart_padding,
                },

                data : {
                    x: 'datetime',
                    xFormat: '%d/%m/%Y %H:%M:%S',
                    columns: newColumns,

                    colors: {
                        bp_systolic: '#DA291C' ,
                        bp_diastolic: '#DA291C' ,
                        pulse: '#78BE20' ,
                        Sp02: '#FAE100' ,
                    },

                    axes: {
                        Sp02: 'y2',
                    },

                },

                grid: newlines,

                axis: {
                    x: {
                        type: 'timeseries',
                        tick: {
                            fit: false,
                            format: '%d/%m %H:%M'
                        },
                    },
                    y: {
                        min: 35,
                        max: 240,
                        show: true,
                    },

                    y2: {
                        show: true,
                        min: 40,
                        max: 100,
                        padding: {
                            top: 0,
                            bottom: 0,
                        },
                        tick: {
                            values: [100, 90, 80, 60]
                        },
                    },
                },

                line :{
                    show: false,
                },
            })
        })

        interval = setInterval(function () {
            if($scope.monitorPairing()){
                patientLoader().then(function(patient){
                    newColumns = createColumns(patient.episodes[0].observation);

                    //set first and last time for x axis
                    $scope.firstobs = newColumns[4][1];
                    $scope.lastobs = newColumns[4][newColumns[4].length-1];

                    chart.load({
                        columns: newColumns,
                        grid: newlines,
                    });
                });
            }
        }, 1000);

        $scope.$on("$routeChangeStart", function(){
            if(interval){
                clearInterval(interval);
            }
        });

    });
