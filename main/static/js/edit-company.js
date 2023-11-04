$(document).ready(function () {
    const addMoreBtn = document.getElementById("add-more");
    const totalNewForms = document.getElementById("id_shareholder_set-TOTAL_FORMS");
  
    addMoreBtn.addEventListener("click", add_new_form);
  
    function add_new_form(event) {
      if (event) {
        event.preventDefault();
      }
  
      const currentShareholderForms = document.getElementsByClassName("shareholder-form");
      const currentFormCount = currentShareholderForms.length;
  
      // Add a new empty form element to the HTML form
      const formCopyTarget = document.getElementById("shareholder-form-list");
      const emptyFormEl = document.getElementById("empty-form").cloneNode(true);
      emptyFormEl.setAttribute("class", "shareholder-form");
      emptyFormEl.setAttribute("id", `form`);
      const regex = new RegExp("__prefix__", "g");
      emptyFormEl.innerHTML = emptyFormEl.innerHTML.replace(regex, currentFormCount);
      
      totalNewForms.setAttribute("value", currentFormCount + 1);
      formCopyTarget.append(emptyFormEl);
    }
  
    function updateTotalForms() {
      var totalFormsInput = $("#id_shareholder_set-TOTAL_FORMS");
      var currentTotalForms = parseInt(totalFormsInput.val());
      totalFormsInput.val(currentTotalForms - 1);
      
      // After removing an element, update the other elements' values
      $(".shareholder-form").each(function (index) {
        const inputFields = $(this).find('input, select'); // Find relevant input/select fields
        inputFields.each(function () {
          // Update the names and IDs of the input/select fields to reflect the new index
          const fieldName = $(this).attr('name');
          const updatedName = fieldName.replace(/\d+/, index);
          $(this).attr('name', updatedName);
          const idAttr = $(this).attr('id');
          const updatedId = idAttr.replace(/\d+/, index);
          $(this).attr('id', updatedId);
        });
      });
    }
  
    $(document).on("click", ".remove-form-button", function () {
      $(this).closest("#form").remove();
      updateTotalForms();
    });
  });
  