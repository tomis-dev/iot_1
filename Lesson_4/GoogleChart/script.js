const url =
  "https://api.thingspeak.com/channels/3086231/feeds.json?api_key=0NTBB700WRE7W74S";

let chartData = [["Time", "Temperature"]]; // Chart header

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    const feeds = data.feeds;

    // Prepare data for Google Chart
    feeds.forEach((feed) => {
      if (feed.field1) {
        chartData.push([
          feed.created_at.substring(11, 16), // Show only HH:MM
          parseFloat(feed.field1),
        ]);
      }
    });

    document.getElementById("output").textContent = JSON.stringify(chartData);

    // Draw chart after data is ready
    drawChart();
  })
  .catch((error) => {
    console.error("Error fetching data", error);
    document.getElementById("output").textContent = "Error loading data";
  });

google.charts.load("current", { packages: ["corechart"] });

function drawChart() {
  var data = google.visualization.arrayToDataTable(chartData);

  var options = {
    title: "Temperature",
    curveType: "function",
    legend: { position: "bottom" },
  };

  var chart = new google.visualization.LineChart(
    document.getElementById("curve_chart")
  );

  chart.draw(data, options);
}
