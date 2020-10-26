$( document ).ready(function() {

    // open form
    function open_form() {
        $("#data-form").show();
    }

    // add command
    $(".btn-toggle-data-form").click(function() {
        $("#id_name").prop("readonly", false);
        $("#id_name").val("");
        $("#id_output").val("");
        $("#id_brief").val("");
        $("#id_description").val("");

        open_form();
    });

    // edit command
    $(".edit").click(function() {
        let tr = $(this).closest("tr");

        let name = tr.find("td.name").text();
        let output = tr.find("td.output").text();
        let brief = tr.find("td.brief").text();
        let description = tr.find("td.description").text();

        $("#id_name").prop("readonly", true);
        $("#id_name").val(name);
        $("#id_output").val(output);
        $("#id_brief").val(brief);
        $("#id_description").val(description);

        open_form();
    });

});