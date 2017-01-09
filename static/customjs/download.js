

function download(){
alert('vkmchandel');


         $.ajax({
        type: "GET",
        url: "/download/",
        'data':{'region':$('#region_select').val(),'datatype':$('#datatype_select').val()},
        success: function(response) {
            if (response.success=='true'){
               alert('Downloaded successfully!')
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






