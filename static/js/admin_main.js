// dependent select dropdown for category and company jquery
$(document).ready(function () {
    $("select#id_company").change(function() {
        $.getJSON("/getCategory/",{id: $(this).val()}, function(j){ 
            var options = '<option value="">---------</option>'; 
            for (var i = 0; i < j.length; i++) { 
                options += '<option value="' + j[i].id + '">' + j[i].name + '</option>'; 
            } 
            // inspect html to check id of category select dropdown.
            $("select#id_category").html(options); 
        }); 
    });
});


// add placeholder to search bar
window.onload = function() {
    document.getElementById("searchbar").placeholder = "search by name, model or code";
};

