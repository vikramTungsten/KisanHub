
$(document).ready(function() {
       get_table_initilize();
 });

function download(){
         $.ajax({
        type: "GET",
        url: "/download/",
        'data':{'region':$('#region_select').val(),'datatype':$('#datatype_select').val()},
        success: function(response) {
            if (response.success=='true'){
               alert('Downloaded successfully!')
               get_table_initilize()
            }
            else{
            alert('Server Error !')
            }

        },
        error: function(response) {
            console.log('error');
            console.log('response', response);
        },
        beforeSend: function() {

        },
        complete: function() {}
    });
}

function select_nochange(){
get_table_initilize()
}

function get_table_initilize() {
        var table = $('#datatable').dataTable({
            "processing": true,
            "serverSide": true,
            "destroy": true,
            "ajax": "/get-region-datalist/?region="+$('#region_select').val()+'&datatype='+$('#datatype_select').val(),
            "searching": false,
            "ordering": false,
            "paging": true,
            "columnDefs": [
                {"targets": 7, "orderable": false},
            ]
        });
 }






 Chart.defaults.global.legend = {
        enabled: false
      };

      // Line chart
  function LineChart(maxTemp,minTemp,meanTemp){

  var ctx = document.getElementById("lineChart");
      var lineChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul","Aug","Sep","Oct","Nov","Dec"],
          datasets: [{
            label: "Max Temp",
            backgroundColor: "rgba(38, 185, 154, 0.31)",
            borderColor: "rgba(38, 185, 154, 0.7)",
            pointBorderColor: "rgba(38, 185, 154, 0.7)",
            pointBackgroundColor: "rgba(38, 185, 154, 0.7)",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointBorderWidth: 1,
            data: maxTemp
          }, {
            label: "Min Temp",
            backgroundColor: "rgba(3, 88, 106, 0.3)",
            borderColor: "rgba(3, 88, 106, 0.70)",
            pointBorderColor: "rgba(3, 88, 106, 0.70)",
            pointBackgroundColor: "rgba(3, 88, 106, 0.70)",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(151,187,205,1)",
            pointBorderWidth: 1,
            data: minTemp
          },
          {
            label: "Mean Temp",
            backgroundColor: "rgba(127, 255, 0, 0.3)",
            borderColor: "rgba(127, 255, 0, 1)",
            pointBorderColor: "rgba(3, 88, 106, 0.70)",
            pointBackgroundColor: "rgba(3, 88, 106, 0.70)",
            pointHoverBackgroundColor: "#fff",
            pointHoverBorderColor: "rgba(151,187,205,1)",
            pointBorderWidth: 1,
            data: meanTemp
          }

          ]
        },
      });




  }

      // Bar chart
      var ctx = document.getElementById("mybarChart");
      var mybarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["January", "February", "March", "April", "May", "June", "July"],
          datasets: [{
            label: '# of Votes',
            backgroundColor: "#26B99A",
            data: [51, 30, 40, 28, 92, 50, 45]
          }, {
            label: '# of Votes',
            backgroundColor: "#03586A",
            data: [41, 56, 25, 48, 72, 34, 12]
          }]
        },

        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });