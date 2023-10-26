$(document).ready(function () {
    var formsetPrefix = $('#shareholder-forms').data('prefix'); // Get the formset prefix from a data attribute

    function addRemoveButton(container) {
        container.append('<button style="margin: 20px 0 20px 0; display: block;" type="button" class="remove-form">Remove</button>');
    }

    $("#add-shareholder").click(function () {
        var formIdx = $('#id_' + formsetPrefix + '-TOTAL_FORMS').val();
        var newForm = $('#empty-form').html().replace(/__prefix__/g, formIdx);
        var formContainer = $('<div class="form-container"></div>');
        formContainer.append(newForm);
        $('#shareholder-forms').append(formContainer);
        
        // Add the "Remove" button for the new form
        addRemoveButton(formContainer);

        $('#id_' + formsetPrefix + '-TOTAL_FORMS').val(parseInt(formIdx) + 1);
    });

    $(document).on('click', '.remove-form', function () {
        $(this).closest('.form-container').remove();
        updateFormCount();
    });

    function updateFormCount() {
        const forms = $('.form-container');
        $('#id_' + formsetPrefix + '-TOTAL_FORMS').val(forms.length);
    }
});
