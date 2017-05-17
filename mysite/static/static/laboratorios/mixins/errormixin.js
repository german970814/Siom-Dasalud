import _ from 'underscore';

export default {
    name: 'errorMixin',
    data: function () {
        return {
            validations: [],
            // _validated: false,
            errors: [],
        }
    },
    methods: {
        addValidation: function (error) {
            if (!'validations' in error) {
                throw new Error ('No hay validaciones por hacer.');
            }
            // validations ever will evalue false for errors
            this.validations.push(error);
        },
        removeValidation: function (error) {
            this.validations.slice(this.validations.indexOf(error), 1);
        },
        hasError: function (obj) {
            if (obj !== undefined) {
                let validate = this.validations.find(i => i.target == obj);
                let validations = validate.validations;
                for (let validation of validations) {
                    const error = typeof validation === 'function' ? validation(validate.target): validation;
                    if (error) {
                        return true;
                    }
                }
                return false
            }
            return this.validate();
        },
        validate: function () {
            // this._validated = true;
            let errors = []
            this.validations.forEach(error => {
                error.validations.forEach(validation => {
                    const _error = typeof validation === 'function' ? validation(error.target): validation;
                    if (_error) {
                        errors.push(error)
                    }
                });
            });
            return errors.length >= 1;
        }
    }
}
