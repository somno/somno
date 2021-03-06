directives.directive("somnoTimeline", function () {
  return {
    link: function(scope, element, attrs){
      d3.bullet = function() {
        var orient = "left", // TODO top & bottom
            reverse = false,
            duration = 0,
            ranges = bulletRanges,
            markers = bulletMarkers,
            measures = bulletMeasures,
            width = 380,
            height = 30,
            tickFormat = null;

        // For each small multiple…
        function bullet(g) {
          g.each(function(d, i) {
            var rangez = ranges.call(this, d, i).slice().sort(d3.descending),
                markerz = markers.call(this, d, i).slice().sort(d3.descending),
                measurez = measures.call(this, d, i).slice().sort(d3.descending),
                g = d3.select(this);

            // Compute the new x-scale.
            var x1 = d3.scale.linear()
                .domain([0, 300])
                .range(reverse ? [width, 0] : [0, width]);

            // Retrieve the old x-scale, if this is an update.
            var x0 = this.__chart__ || d3.scale.linear()
                .domain([0, Infinity])
                .range(x1.range());

            // Stash the new scale.
            this.__chart__ = x1;

            // Derive width-scales from the x-scales.
            var w0 = bulletWidth(x0),
                w1 = bulletWidth(x1);

            // Update the range rects.
            var range = g.selectAll("rect.range")
                .data(rangez);

            var start = 50;

            range.enter().append("rect")
                .attr("class", function(d, i) { return "range s" + i; })
                .attr("width", w0)
                .attr("height", height)
                .attr("x", reverse ? x0 : start)
              .transition()
                .duration(duration)
                .attr("width", w1)
                .attr("x", reverse ? x1 : start);

            range.transition()
                .duration(duration)
                .attr("x", reverse ? x1 : start)
                .attr("width", w1)
                .attr("height", height);

            // Update the measure rects.
            var measure = g.selectAll("rect.measure")
                .data(measurez);

            measure.enter().append("rect")
                .attr("class", function(d, i) { return "measure s" + i; })
                .attr("width", w0)
                .attr("height", height / 3)
                .attr("x", reverse ? x0 : start)
                .attr("y", height / 3)
                .transition()
                .duration(duration)
                .attr("width", w1)
                .attr("x", reverse ? x1 : start);

            measure.transition()
                .duration(duration)
                .attr("width", w1)
                .attr("height", height / 3)
                .attr("x", reverse ? x1 : start)
                .attr("y", height / 3);

            // Update the marker lines.
            var marker = g.selectAll("line.marker")
                .data(markerz);

            marker.enter().append("rect")
                .attr("class", "marker")
                .attr("x", 50 + 100 * Math.random())
                .attr("y", 15)
                .attr("width", 10)
                .attr("height", height / 3)
              .transition()
                .duration(duration)
                .attr("x1", x1)
                .attr("x2", x1);

            marker.transition()
                .duration(duration)
                .attr("x1", x1)
                .attr("x2", x1)
                .attr("y1", height / 6)
                .attr("y2", height * 5 / 6);
          });
          d3.timer.flush();
        }

        // left, right, top, bottom
        bullet.orient = function(x) {
          if (!arguments.length) return orient;
          orient = x;
          reverse = orient == "right" || orient == "bottom";
          return bullet;
        };

        // ranges (bad, satisfactory, good)
        bullet.ranges = function(x) {
          if (!arguments.length) return ranges;
          ranges = x;
          return bullet;
        };

        // markers (previous, goal)
        bullet.markers = function(x) {
          if (!arguments.length) return markers;
          markers = x;
          return bullet;
        };

        // measures (actual, forecast)
        bullet.measures = function(x) {
          if (!arguments.length) return measures;
          measures = x;
          return bullet;
        };

        bullet.width = function(x) {
          if (!arguments.length) return width;
          width = x;
          return bullet;
        };

        bullet.height = function(x) {
          if (!arguments.length) return height;
          height = x;
          return bullet;
        };

        bullet.tickFormat = function(x) {
          if (!arguments.length) return tickFormat;
          tickFormat = x;
          return bullet;
        };

        bullet.duration = function(x) {
          if (!arguments.length) return duration;
          duration = x;
          return bullet;
        };

        return bullet;
      };

      function bulletRanges(d) {
        return d.ranges;
      }

      function bulletMarkers(d) {
        return d.markers;
      }

      function bulletMeasures(d) {
        return d.measures;
      }

      function bulletTranslate(x) {
        return function(d) {
          return "translate(" + x(d) + ",0)";
        };
      }

      function bulletWidth(x) {
        var x0 = x(0);
        return function(d) {
          return Math.abs(x(d) - x0);
        };
      }

      var margin = {top: 0, right: 40, bottom: 0, left: 120},
          width = Math.max($(element).width() - 180, 0),
          height = 50 - margin.top - margin.bottom;

      var chart = d3.bullet()
          .width(width)
          .height(height);

      var bulletLoader = function(data) {
        var svg = d3.select(element[0]).selectAll("svg")
            .data(data)
          .enter().append("svg")
            .attr("class", "bullet")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
          .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")")
            .call(chart);

        var title = svg.append("g")
            .style("text-anchor", "end")
            .attr("transform", "translate(-6," + height / 2 + ")");

        title.append("text")
            .attr("class", "title")
            .attr("x", "0")
            .text(function(d) { return d.title; });

        title.append("text")
            .attr("class", "subtitle")
            .attr("x", "0")
            .attr("dy", "1em")
            .text(function(d) { return d.subtitle; });
      };

      var ranges = [0, 0, 300];

      var bullets = [
        {"title":"Proprofol","subtitle":"200","ranges":ranges,"measures":[],"markers":[250]},
        {"title":"Fentanyl","subtitle":"100","ranges":ranges,"measures":[],"markers":[26]},
        {"title":"Doxamethosone","subtitle":"","ranges":ranges,"measures":[],"markers":[]},
        {"title":"CO-amixiclav","subtitle":"","ranges":ranges,"measures":[],"markers":[]},
        {"title":"Paracetomol","subtitle":"1mg","ranges":ranges,"measures":[],"markers":[]},
        {"title":"Hartmann's","subtitle":"10mg/ml/hour","ranges":ranges,"measures":[220,270],"markers":[]},
        {"title":"Blood products","subtitle":"10mg/ml/hour","ranges":ranges,"measures":[220,270],"markers":[]}
      ]


      bulletLoader(bullets);
    }
  }
});
