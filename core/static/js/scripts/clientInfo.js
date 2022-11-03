"use strict";
    
// * user info from control
class UserFormControl {

    constructor(kwargs) {

        // <-- get elements from DOM
        this.kwargs = kwargs;

        // <-- get elements from DOM
        this.form = this._getElem(kwargs.form);
        this.inputs = this._getElems(kwargs.inputs, this.form);
        this.labels = this._getElems(kwargs.labels, this.form);
        this.buttons = this._getElems(kwargs.buttons, this.form);
        this.edit = this._getElem(kwargs.edit, this.form);

        // * init edit event
        this.editEvent();

    }

    // debug
    debug(info = this) {
        console.log(info);
        return this;
    }

    // get elem
    _getElem(selector, parent = document) {
        const elem = parent.querySelector(selector);
        return elem;
    }

    // get elems
    _getElems(selector, parent = document) {
        const elems = [...parent.querySelectorAll(selector)];
        return elems;
    }

    // edit button
    editEvent() {

        this.edit.onclick = () => {

            if (this.edit.dataset.edit == "hide") {
                this.inputs.map(input => { input.removeAttribute('disabled'); });
                this.labels.map(label => { label.classList.add('active'); })
                this.buttons.map(btn => { btn.removeAttribute('disabled'); btn.classList.add('active'); })
                this.edit.dataset.edit = "show"
            }
            else if (this.edit.dataset.edit == "show") {
                this.inputs.map(input => { input.setAttribute('disabled', ''); });
                this.labels.map(label => { label.classList.remove('active'); })
                this.buttons.map(btn => { btn.setAttribute('disabled', ''); btn.classList.remove('active'); })
                this.edit.dataset.edit = "hide"
            }
            
        };

    }

    // update object
    update() {
        this.form = this._getElem(this.kwargs.form);
        this.inputs = this._getElems(this.kwargs.inputs, this.form);
        this.labels = this._getElems(this.kwargs.labels, this.form);
        this.buttons = this._getElems(this.kwargs.buttons, this.form);
        this.edit = this._getElem(this.kwargs.edit, this.form);

        // * init edit event
        this.editEvent();
    }
}

// * add shipping
class AddShipping {
    constructor(kwargs) {

        // * get form
        this.form = this._getElem(kwargs.form);

        // * get add button
        this.button = this._getElem(kwargs.button);

        // * shipping
        this.shipping = this._getElems(kwargs.shipping, this.form);

        // * counter
        this.counter = this.shipping.length;

        // * form control object
        this.formControl = kwargs.formControl;

        // --> create
        this._create(kwargs);

    }

    // create object
    _create(kwargs) {
        this.createNewForm(kwargs);
    }

    // debug
    debug(info = this) {
        console.log(this);
        return this;
    }

    // get elem
    _getElem(selector, parent = document) {
        const elem = parent.querySelector(selector);
        return elem;
    }

    // get elems
    _getElems(selector, parent = document) {
        const elems = [...parent.querySelectorAll(selector)];
        return elems;
    }

    // set new value \ name \ id to input
    slacer(clone) {

        // * get inputs
        let inputs = this._getElems('input', clone);
        inputs = inputs.filter(input => { if (input.getAttribute('type') !== 'hidden') { return input }; })
        
        inputs.map(input => {

            // * get input clone name \ id
            let cloneId = input.getAttribute('id');
            let cloneName = input.getAttribute('name');
            
            // * create new name
            let newId = cloneId.replace(0, this.counter);
            let newName = cloneName.replace(0, this.counter);

            // --> update id \ name
            input.setAttribute('id', newId);
            input.setAttribute('name', newName);

            input.value = '';
        });
    }

    // create new form
    createNewForm(kwargs) {
        this.button.onclick = () => {
            
            // * create clone of form
            const clone = this.shipping[0].cloneNode(true);

            // * update counter
            this.counter += 1;
            
            // --> insert clone in to the form
            this.form.insertAdjacentElement('beforeend', clone);

            // * get total forms
            this.totalForms = this._getElems(kwargs.total, this.form);

            // --> update total forms
            this.totalForms.map(total => {total.value = this.counter});

            // * set new data value
            clone.dataset.shipping = this.counter;

            // --> update counter for title
            const title = this._getElem(kwargs.title, clone).textContent = this.counter;

            // --> set toggle for new form
            const clientInfoDrop = new ElementsControl({
                manager: '.client-info-manager',
                managed: '.client-info-managed'
            });
            clientInfoDrop.toggler({});


            // --> set new input values
            this.slacer(clone);

            this.formControl.update();

        };
    }

}

// --> DOM on load
document.addEventListener("DOMContentLoaded", () => {

    // * toggle client info item
    const clientInfoDrop = new ElementsControl({
        manager: '.client-info-manager',
        managed: '.client-info-managed'
    });
    clientInfoDrop.toggler({});

    // --> user form control
    const formControl = new UserFormControl({
        form: '#client-info-form',
        edit: '[data-edit]',
        labels: '.client-info__input-group--name',
        inputs: '.form-control-client-info',
        buttons: '[data-hide-btn]'
    });
    

    // --> add new shipping address
    const addShipping = new AddShipping({
        form: '#client-info-form',
        button: '#add-shipping-address',
        shipping: '[data-shipping]',
        total: '#id_form-TOTAL_FORMS',
        title: '[data-shipping-title]',
        formControl: formControl
    });

});