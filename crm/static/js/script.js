$(document).ready(function () {
    $('#touches_table').DataTable();

    var $table_wrapper = $("#touches_table_wrapper");
    $table_wrapper.find('input').attr('class', 'form-control');

    $table_wrapper.find('select').attr('class', 'form-control');


});