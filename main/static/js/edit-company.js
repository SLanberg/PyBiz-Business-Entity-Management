$(document).ready(function () {
    const addMoreBtn = document.getElementById('add-more');
    const totalNewForms = document.getElementById('id_shareholder_set-TOTAL_FORMS');
    
    console.log(totalNewForms)

    addMoreBtn.addEventListener('click', add_new_form)

    function add_new_form(event) {
    if (event) {
        event.preventDefault()
    }

    const currentShareholderForms = document.getElementsByClassName('shareholder-form');
    const currentFormCount = currentShareholderForms.length // + 1

    // now add new empty form element to our html form
    const formCopyTarget = document.getElementById('shareholder-form-list');
    const emptyFormEl = document.getElementById('empty-form').cloneNode(true);
    emptyFormEl.setAttribute('class', 'shareholder-form');
    emptyFormEl.setAttribute('id', `form-${currentFormCount}`);
    const regex = new RegExp('__prefix__', 'g')
    emptyFormEl.innerHTML = emptyFormEl.innerHTML.replace(regex, currentFormCount)

    totalNewForms.setAttribute('value', currentFormCount + 1)

    formCopyTarget.append(emptyFormEl)
    }

})


