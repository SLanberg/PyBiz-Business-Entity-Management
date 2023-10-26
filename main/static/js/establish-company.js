$(document).ready(function () {
  var counter = 0;

  function addRemoveButton(container, formIdx) {
    var removeButton = $(
      '<button style="margin: 20px 0 20px 0; display: block; background-color: #8B0000;" type="button" class="remove-form">Remove</button>'
    );
    removeButton.data("form-index", formIdx); // Store the form index in the button's data
    container.append(removeButton);
  }

  $("#add-shareholder").click(function () {
    counter++;

    var newForm = $("#empty-form")
      .html()
      .replace(/__prefix__/, counter);
    var formContainer = $('<div class="form-container"></div>');
    formContainer.append(newForm);

    // Add the "Remove" button for the new form
    addRemoveButton(formContainer, counter);

    // Append the <hr> after the new form container
    formContainer.append("<hr>");

    $("#shareholder-forms").append(formContainer);
  });

  $(document).on("click", ".remove-form", function () {
    $(this).closest(".form-container").remove();
  });
});
