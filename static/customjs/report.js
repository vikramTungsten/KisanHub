
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





