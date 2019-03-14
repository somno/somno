angular
  .module("opal.controllers")
  .controller("d3timeline", function($scope, patientLoader) {
    $scope.monitorPairing = function() {
      var result = _.find($scope.patient.pairing, function(pairing) {
        return pairing.start && !pairing.stop;
      });

      if (!result) {
        return;
      }
      return $scope.metadata.monitors[String(result.monitor_id)];
    };

    var drugs = function(drug) {
      // stuff this still has to do
      // calculate total doses for each drug

      //if new drug create xs and column, if old push to existing.

      $scope.druglist = new Array();
      $scope.drugdata = [];

      //set up stuff for infusions

      _.each(drug, function(a) {
        var drugname = a.drug_name;
        var drugtime = a.datetime.format("DD/MM/YYYY HH:mm:ss");
        var drugclass = a.drug_type;
        var drugdose = a.dose;

        var inlist = _.indexOf($scope.druglist, drugname);
        if (inlist == "-1") {
          // drug not given before
          $scope.druglist.push({ label: drugname, times: [] });
        }

        //select the right colour
        //stuff to do
        // 1 find a better way of doing this
        //have some reminder to change this if we change class names

        var colours = [
          { class: "Antiemetic Drug", colour: "#EFBE7D" },
          { class: "Induction Agent Drug", colour: "#ffe800" },
          { class: "Hypnotic Drug", colour: "#FF8200" },
          { class: "Hypnotic Antagonist Drug", colour: "#FF8200" },
          { class: "Neuromuscular Blocking Drug", colour: "#ff7477" },
          {
            class: "Neuromuscular Blocking Drug Antagonist",
            colour: "#ff7477"
          },
          {
            class: "Depolarizing Neuromuscular Blocking Drug",
            colour: "#ff7477"
          },
          { class: "Opioid Drug", colour: "#71C5E8" },
          { class: "Opioid Antagonist", colour: "#71C5E8" },
          { class: "Vasopressor Drug", colour: "#D6BFDD" },
          { class: "Local Anaesthetics Drug", colour: "#AFA9A0" },
          { class: "Anticholinergic Drug", colour: "#A4D65E" },
          { class: "Other Drug Agents", colour: "#ffffff" }
        ];
        //var nextcolour = _.where(colours, drugclass);
        var something = { class: drugclass };
        var nextcolour = _.findWhere(colours, something);
        //debugger;
        if (nextcolour == null) {
          nextcolour = "#736969";
        } else {
          nextcolour = nextcolour.colour;
        }

        _.each($scope.druglist, function(b) {
          if (drugname == b.label) {
            b.times.push({
              color: nextcolour,
              label: drugdose,
              starting_time: drugtime,
              display: "circle"
            });
          }
        });
      });
    };

    function timelineCircle(drugsList) {
        var width = 500;
        var chart = d3
          .timeline()
          .tickFormat(
            //
            {
              format: d3.time.format("%I %p"),
              tickTime: d3.time.hours,
              tickInterval: 1,
              tickSize: 30
            }
          )
          .display("circle"); // toggle between rectangles and circles
        d3.select("#timeline2").selectAll("svg").remove();
        var svg = d3
          .select("#timeline2")
          .append("svg")
          .attr("width", width)
          .datum(drugsList)
          .call(chart);
      }

    patientLoader().then(function(patient) {
      drugs(patient.episodes[0].given_drug);
      // DEBUG:
      console.log($scope.druglist);
      timelineCircle($scope.druglist);
    });
  });
