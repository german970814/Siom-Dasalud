/*

ErrorMixin

Mixin usado para manejar los errores de cada componente,
el cual valida a un elemento 'x' que cumpla una serie de
condiciones y recibe objetos como parametros, de la siguiente
forma:

var x = {
  target: document.getElementById('test'),
  validations: [
    x => true,
    false,
    0 === false,
  ]
}
*/
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
        addValidationIfNotExists: function (obj) {
            if (!'target' in obj) {
                throw new Error ('No hay un objetivo definido a partir de el cual buscar validaciones.')
            }
            let exists = this.validations.find(x => x.target == obj)
            if (!exists) {
                this.addValidation(obj)
            }
        },
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
                if (validate) {
                    let validations = validate.validations;
                    for (let validation of validations) {
                        const valid = typeof validation === 'function' ? validation(validate.target): validation;
                            if (!valid || typeof valid == 'string') {
                                return true;
                            }
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
                    const valid = typeof validation === 'function' ? validation(error.target): validation;
                    if (!valid || typeof valid == 'string') {
                        errors.push(error)
                    }
                });
            });
            return errors.length >= 1;
        }
    }
}
