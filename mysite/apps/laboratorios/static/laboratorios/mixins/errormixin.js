import _ from 'underscore';

export default {
    data: function () {
        return {
            validations: [],
            _validated: false,
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
                validate.validations.forEach(error => {
                    const valid = typeof error === 'function' ? error(validate): error;
                    if (!valid) {
                        return true;
                    }
                })
                return false;
            }
            return this.validate();
        },
        validate: function () {
            this._validated = true;
            this.errors = []
            this.validations.forEach(error => {
                error.validations.forEach(validation => {
                    const _error = typeof validation === 'function' ? validation(error.target): validation;
                    if (_error) {
                        this.errors.push(error)
                    }
                });
            });
            return this.errors.length >= 1;
        }
    }
}
