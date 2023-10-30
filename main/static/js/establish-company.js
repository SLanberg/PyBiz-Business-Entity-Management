$(document).ready(function () {
  var formsetPrefix = $("#shareholder-forms").data("prefix"); // Get the formset prefix from a data attribute

  function addRemoveButton(container) {
    container.append(
      '<button style="margin: 20px 0 20px 0; display: block;" type="button" class="remove-form">Remove</button>'
    );
  }

  $("#add-shareholder").click(function () {
    var formIdx = $("#id_" + formsetPrefix + "-TOTAL_FORMS").val();
    var newForm = $("#empty-form")
      .html()
      .replace(/__prefix__/g, formIdx);
    var formContainer = $('<div class="form-container"></div>');
    formContainer.append(newForm);
    $("#shareholder-forms").append(formContainer);

    // Add the "Remove" button for the new form
    addRemoveButton(formContainer);

    formContainer.append("<hr>");

    $("#id_" + formsetPrefix + "-TOTAL_FORMS").val(parseInt(formIdx) + 1);
  });

  function updateTotalForms() {
    var totalFormsInput = $("#id_shareholder_set-TOTAL_FORMS");
    var currentTotalForms = parseInt(totalFormsInput.val());
    totalFormsInput.val(currentTotalForms - 1);
  }

  $(document).on("click", ".remove-form", function () {
    $(this).closest(".form-container").remove();
    updateTotalForms();
  });


  function toggleShareholderFields() {
    var entitySelect = $("#id_shareholder_set-0-entity_type");
    var founderStatus = entitySelect.val();
    var naturalFields = $("#id_shareholder_set-0-natural_person, label[for='id_shareholder_set-0-natural_person']");
    var legalEntityFields = $("#id_shareholder_set-0-legal_entity, label[for='id_shareholder_set-0-legal_entity']");

    if (founderStatus === "natural_person") {
        naturalFields.css("display", "block");
        legalEntityFields.css("display", "none");
        // Clear the values of the legal entity fields
        $("#id_shareholder_set-0-legal_entity").val("");
    } else {
        naturalFields.css("display", "none");
        legalEntityFields.css("display", "block");
        // Clear the values of the natural person fields
        $("#id_shareholder_set-0-natural_person").val("");
    }
}

// Initial state on page load
toggleShareholderFields();

// Listen for changes in founder status dropdown
$("#id_shareholder_set-0-entity_type").on("change", function () {
    toggleShareholderFields();
});


  
});
