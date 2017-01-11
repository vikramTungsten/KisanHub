$(document).ready(function() {
    get_table_initilize();
    set_temprature_trend('All');
    set_rainfall_paichart('All');
    $('#year_select').val('All');
    $("#region_lbl").text($("#region_select option:selected").text());
    $("#datatype_lbl").text($("#datatype_data_select option:selected").text());


});

function download() {
    $.ajax({
        type: "GET",
        url: "/download/",
        'data': {
            'region': $('#region_select').val(),
            'datatype': $('#datatype_select').val()
        },
        success: function(response) {
            if (response.success == 'true') {
                alert('Downloaded successfully!')
                get_table_initilize();
                set_temprature_trend('All');
                set_rainfall_paichart('All');
                $('#year_select').val('All');
            } else {
                alert('Server Error !')
            }

        },
        error: function(response) {
            console.log('error');
            console.log('response', response);
        },
       beforeSend: function() {
            $("#processing").show();
            },
            complete: function() {
            $("#processing").hide();
            }
    });
}

function select_nochange() {
    get_table_initilize();
    set_temprature_trend('All');
    set_rainfall_paichart('All');
    $('#year_select').val('All');
    $("#region_lbl").text($("#region_select option:selected").text());
}

function year_select_nochange() {
    set_temprature_trend($('#year_select').val())
    set_rainfall_paichart($('#year_select').val());
}

function datatype_nochange() {
    set_rainfall_paichart($('#year_select').val());
    $("#datatype_lbl").text($("#datatype_data_select option:selected").text());
}




function get_table_initilize() {
    var table = $('#datatable').dataTable({
        "processing": true,
        "serverSide": true,
        "destroy": true,
        "ajax": "/get-region-datalist/?region=" + $('#region_select').val() + '&datatype=' + $('#datatype_select').val(),
        "searching": false,
        "ordering": false,
        "paging": true,
        "columnDefs": [{
            "targets": 7,
            "orderable": false
        }, ]
    });
}


function set_temprature_trend(year) {
    $.ajax({
        type: "GET",
        url: "/get-temprature/",
        'data': {
            'region': $('#region_select').val(),
            'datatype': $('#datatype_select').val(),
            'year':year
        },
        success: function(response) {           
            if (response.success == 'true') {
                console.log(response.maxTemp)
                LineChart(response.maxTemp,response.minTemp,response.meanTemp);
            } else {
                alert('Server Error !')
            }
        },
        error: function(response) {
            console.log('error');
            console.log('response', response);
        },
           beforeSend: function() {
            $("#processing").show();
            },
            complete: function() {
            $("#processing").hide();
            }
    });
}



function set_rainfall_paichart(year){
    $.ajax({
        type: "GET",
        url: "/get-rainfall-data/",
        'data': {
            'region': $('#region_select').val(),
            'datatype': $('#datatype_data_select').val(),
            'year':year
        },
        success: function(response) {
            if (response.success == 'true') {
                PaiChart(response.sessionData);
            } else {
                alert('Server Error !')
            }
        },
        error: function(response) {
            console.log('error');
            console.log('response', response);
        },
           beforeSend: function() {
            $("#processing").show();
            },
            complete: function() {
            $("#processing").hide();
            }
    });
}




Chart.defaults.global.legend = {
    enabled: false
};

// Line chart
function LineChart(maxTemp, minTemp, meanTemp) {
    var ctx = document.getElementById("lineChart");
    var lineChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
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


function PaiChart(sessionData) {
  // Pie chart
      var ctx = document.getElementById("pieChart");
      var data = {
        datasets: [{
          data: sessionData,
          backgroundColor: [
            "#455C73",
            "#9B59B6",
            "#BDC3C7",
            "#26B99A"
          ],
          label: 'Session Data' // for legend
        }],
        labels: [
          "Winter",
          "Spring",
          "Summer",
          "Autumn"
        ]
      };

      var pieChart = new Chart(ctx, {
        data: data,
        type: 'pie',
        otpions: {
          legend: true
        }
      });
}
