// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: ["예측값", "유저 평균 예측가"],
    datasets: [
      {
        label: "Revenue",
        backgroundColor: ["rgba(255, 99, 132, 0.8)", "rgba(75, 192, 192, 0.8)"],
        borderColor: "rgba(2,117,216,1)",
        data: [price, mean_price],
      },
    ],
  },
  options: {
    scales: {
      xAxes: [
        {
          time: {
            unit: "month",
          },
          gridLines: {
            display: false,
          },
          ticks: {
            maxTicksLimit: 2,
          },
        },
      ],
      yAxes: [
        {
          ticks: {
            min: 0,
            max: 50000000,
            maxTicksLimit: 10,
          },
          gridLines: {
            display: true,
          },
        },
      ],
    },
    legend: {
      display: false,
    },
  },
});
