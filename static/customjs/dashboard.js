$(document).ready(function() {
 session_comparison()
});


function session_comparison() {
    $.ajax({
        type: "GET",
        url: "/session-comparison/",
        'data': { },
        success: function(response) {
            if (response.success == 'true') {
                barchart(response.ukSessionData,response.englandSessionData,response.walesSessionData,response.scotlandSessionData)
            $('#coolest_lbl').text(response.coolest)
            $('#hotest_lbl').text(response.hotest)


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


 // Bar chart

function barchart(ukSessionData,englandSessionData,walesSessionData,scotlandSessionData){

      var ctx = document.getElementById("mybarChart");
      var mybarChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ["Winter", "Spring", "Summer", "Autumn"],
          datasets: [{
            label: 'UK',
            backgroundColor: "#26B99A",
            data: ukSessionData
          }, {
            label: 'England',
            backgroundColor: "#6EFF70",
            data: englandSessionData
          },{
            label: 'Wales',
            backgroundColor: "#03586B",
            data: walesSessionData
          },{
            label: 'Scotland',
            backgroundColor: "#00AF33",
            data: scotlandSessionData
          }

          ]
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
}