<script>
import Vue from 'vue/dist/vue.js';
import VueResource from 'vue-resource';
import ErrorMixin from './../mixins/errormixin.js';
import _ from 'underscore';

Vue.use(VueResource);
/* TODO:
  -Corregir el método getRules();
*/
export default {
    name: 'igForm',
    mixins: [ErrorMixin],
    props: {
        fields: {
            type: Array,
            required: true
        },
        url: {
            type: String,
            required: true
        },
        selected: {}
    },
    created: function () {
        this._getFetchData();
    },
    data: function () {
        return {
            models: {},  // los modelos
            items: {},  // los items de los selects
            validateFields: false,
            appended: {},
        }
    },
    watch: {
        selected: function () {
            if (this.selected) {
                for (let attr in this.selected) {
                    if (attr in this.models) {  // si está en los campos
                        if (this._isGroupField(attr)) {
                            for (let subattr in this.models[attr]) {
                                if (attr in this.items) {
                                    let key;
                                    if (this.selected[attr][subattr] instanceof Array) {
                                        let field = this.fields.find(field => field.name == subattr && field.group == attr)
                                        if (field && field.kwargs && field.type == Array && field.kwargs.multiple) {
                                            key = [];
                                            for (let obj of this.selected[attr][subattr]) {
                                                let found = this.items[attr].find(object => object.id == obj.id);
                                                if (found) {
                                                    key.push(found);
                                                }
                                            }
                                            if (!_.isEmpty(key)) {
                                                this.models[attr][subattr] = key;
                                            } else {
                                                this.$emit('showsnack', 'No se encontró el campo múltiple ' + subattr.toString() + ' del grupo ' + attr.toString())
                                                this.models[attr][subattr] = [];
                                            }
                                        }
                                    } else {
                                        for (let obj of this.items[attr]) {
                                            if (obj.id == this.selected[attr][subattr].id) {
                                                key = obj;
                                                break;
                                            }
                                        }
                                        if (key) {
                                            this.models[attr][subattr] = key;
                                        } else {  // support for OneToOneField and GroupField forms (models)
                                            key = this.fields.find(x => x.group == attr && x.name == subattr);
                                            if (key) {
                                                this.selected[attr][subattr].text = this.selected[attr][subattr][key.key];
                                                if (attr in this.appended && this.appended[attr]) {
                                                    this.items[attr].pop();
                                                    this.appended[attr] = false;
                                                }
                                                this.items[attr].push(this.selected[attr][subattr]);
                                                this.appended[attr] = true;
                                                this.models[attr][subattr] = this.selected[attr][subattr];
                                            } else {
                                                this.$emit('showsnack', `No se encuentra el campo "${subattr}" de el grupo "${attr}" deseado.`)
                                            }
                                        }
                                    }
                                }
                                this.models[attr][subattr] = this.selected[attr][subattr];
                            }
                        } else {
                            if (attr in this.items) {  // si esta en los items que ya fueron fetched
                                let key;
                                if (this.selected[attr] instanceof Array) {  // support for ManyToManyField
                                    let field = this.fields.find(field => field.name == attr);
                                    if (field && field.kwargs && field.type == Array && field.kwargs.multiple) {
                                        key = [];
                                        for (let obj of this.selected[attr]) {
                                            let found = this.items[attr].find(object => object.id == obj.id);
                                            if (found) {
                                                key.push(found);
                                            }
                                        }
                                        if (!_.isEmpty(key)) {
                                            this.models[attr] = key;
                                        } else {
                                            this.$emit('showsnack', 'No se encontró el campo múltiple ' + attr.toString());
                                            this.models[attr] = [];
                                        }
                                    }
                                } else {
                                    for (let obj of this.items[attr]) {
                                        if (obj.id == this.selected[attr].id) {
                                            key = obj;
                                            break;
                                        }
                                    }
                                    if (key) {
                                        this.models[attr] = key;
                                    } else {  // support for OneToOneField
                                        key = this.fields.find(x => x.name == attr);
                                        if (key) {
                                            this.selected[attr].text = this.selected[attr][key.key];
                                            if (attr in this.appended && this.appended[attr]) {
                                                this.items[attr].pop();
                                                this.appended[attr] = false;
                                            }
                                            this.items[attr].push(this.selected[attr]);
                                            this.appended[attr] = true;
                                            this.models[attr] = this.selected[attr];
                                        } else {
                                            this.$emit('showsnack', 'No se encuentra el ' + attr.toString() + ' deseado.');
                                            this.models[attr] = '';
                                        }
                                    }
                                }
                            } else {
                                this.models[attr] = this.selected[attr];
                            }
                        }
                    }
                }
            }
        }
    },
    methods: {
        cleanFields: function () {
            for (let field of this.fields) {
                if (field.group) {
                    if (this.models[field.group][field.name] instanceof Array) {
                        this.models[field.group][field.name] = new Array();
                    } else {
                        this.models[field.group][field.name] = '';
                    }
                } else {
                    if (this.models[field.name] instanceof Array) {
                        this.models[field.name] = new Array();
                    } else {
                        this.models[field.name] = '';
                    }
                }

                if (field.name in this.appended) {
                    this.appended[field.name] = false;
                    this.items[field.name].pop();
                }
            }
            // this.selected = false;
            this.$emit('clearselected');
            this.validateFields = false;
        },
        fieldIsRequired: function (field) {
            return field.required === undefined || field.required;
        },
        _getFetchData: function () {
            for (let field of this.fields) {
                if ('url' in field) {  // si tiene una url donde hacer la consulta
                    Vue.set(this.items, field.name, []);  // Se setean las propiedades de acuerdo a la documentacion, de forma reactiva
                    this.$http.get(field.url)
                        .then(response => {
                          for (let _item of response.body) {
                            _item.text = _item[field.key];
                            this.items[field.name].push(_item);
                          }
                        }, response => {
                            if ('detail' in response.body) {
                                this.snackbarText = response.body.detail;
                                this.snackbar = true;
                            } else {
                                this.snackbarText = 'Han ocurrido errores';
                                this.snackbar = true
                            }
                        });
                }
                let fieldType = {};
                if (field.type == String || field.type == Number) {
                    fieldType = '';
                } else if (field.type == Array) {
                    if ('kwargs' in field) {
                        fieldType = field.kwargs.multiple ? []: {};
                    }
                }
                if (field.group) {
                    if (!this.models[field.group]) {
                        Vue.set(this.models, field.group, {});
                    }
                    Vue.set(this.models[field.group], field.name, fieldType)
                    // this.models[field.group][field.name] = fieldType;
                } else {
                    Vue.set(this.models, field.name, fieldType);
                }
            }
        },
        getRules: function (field) {
            let rules = new Array();
            if ('group' in field && field.group && this.fieldIsRequired(field)) {
                rules.push(_field => this.validateFields ? !_.isEmpty(this.models[field.group][field.name]) || 'Este campo es obligatorio': true)
            } else if (this.fieldIsRequired(field)) {
                rules.push(_field => this.validateFields ? !_.isEmpty(this.models[field.name]) || 'Este campo es obligatorio': true)
            }
            if ('rules' in field) {
                if (!field.rules instanceof Array) {
                    console.error('Las reglas de los campos, deben ser un array [' + field.name.toString() + ']');
                }
                rules.push.apply(rules, field.rules);
            }
            return rules
        },
        isValid: function () {
            this.validateFields = true;
            for (let field of this.fields) {
                let rules = this.getRules(field);
                for (let rule of rules) {
                    const valid = typeof rule === 'function' ? rule(field): rule;
                    if (!valid || typeof valid == 'string') {
                        return false;
                    }
                }
            }
            return true;
        },
        submitForm: function () {
            let url = this.url;
            let method = 'post';
            let message;
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            if (this.selected) {
                url += this.selected.id + '/';
                method = 'put';
            }
            if (this.isValid()) {
                this.$http[method](url, this.models, {headers: {'X-CSRFToken': token.value}})
                    .then(response => {
                        if (response.status == 201) {
                            message = 'Laboratorio Creado Correctamente';
                            this.$emit('objectcreated', response.body);
                        } else {
                            message = 'Laboratorio Editado Correctamente';
                        }
                        if (message) {
                            this.$emit('showsnack', message);
                        }
                    }, response => {
                        if (response.status == 400) {
                            message = 'Han ocurrido Errores';
                            for (let res in response.body) {

                            }
                        } else if ('detail' in response.body) {
                            message = response.body.detail;
                        } else {
                            console.error(response);
                        }
                        if (message) {
                            this.$emit('showsnack', message);
                        }
                    });
            } else {
                this.$emit('showsnack', 'El formulario aún tiene errores, verifica antes de enviar.');
            }
        },
        _isGroupField: function (item) {
            if (!_.isArray(this.models[item]) && !_.isObject(this.models[item])) {
                for (let field of this.fields) {
                    if (field.group == item) {
                        return true;
                    }
                }
            }
            return false;
        },
        _genCardHeader: function () {
            let childs = [this.$createElement('v-spacer', [])]
            if (this.selected) {
                childs.push(
                  this.$createElement('v-btn', {
                      nativeOn: {
                        click: () => {
                          this.cleanFields()
                        }
                      },
                      props: {flat: true}
                    },
                    [
                      this.$createElement('v-icon', ['clear_all']),
                      'Limpiar'
                  ])
                )
            }
            return this.$createElement('v-card-title', childs)
        },
        _genCardBody: function() {
            let match = {};
            match[typeof String()] = 'v-text-field';
            match[typeof Number()] = 'v-text-field';
            match[typeof Array()] = 'v-select';

            let childs = [];
            for (let field of this.fields) {
                let defaultProps = {
                    label: field.verbose_name || '',
                    hint: field.hint || '',
                    required: this.fieldIsRequired(field),
                    rules: this.getRules(field),
                }
                if (match[typeof field.type()] == 'v-text-field') {
                    defaultProps.type = _.isEmpty(field.kwargs)? 'text': _.isEmpty(field.kwargs.type)? 'text': field.kwargs.type;
                } else if (match[typeof field.type()] == 'v-select') {
                    defaultProps.items = this.items[field.name];
                    defaultProps['item-value'] = 'text';
                    defaultProps.autocomplete = true;
                    defaultProps.light = true;
                    if ('kwargs' in field) {
                        defaultProps.multiple = field.kwargs.multiple ? true: false;
                    }
                }

                childs.push(this.$createElement('v-col', {attrs: {'md6': true, 'xs12': true}}, [
                    this.$createElement(match[typeof field.type()], {
                        props: Object.assign({

                        }, defaultProps),
                        domProps: {
                          value: field.group ? this.models[field.group][field.name]: this.models[field.name]
                        },
                        on: {
                          input: (event) => {
                            if (field.group) {
                                this.models[field.group][field.name] = event;
                            } else {
                                this.models[field.name] = event;
                            }
                            this.$emit('input', event);
                          }
                        }
                    }, [])
                ]));
            }
            return this.$createElement('v-card-text', [
                this.$createElement('br', []),
                this.$createElement('v-container', [
                    this.$createElement('v-row', childs)
                ]),
                this.$createElement('small', ['*Campos requeridos.']),
                this.$createElement('br', [])
            ]);
        },
        _genCardFooter: function () {
            return this.$createElement('v-card-row', {
              props: {
                actions: true
              }
            }, [
                this.$createElement('v-btn', {
                  props: {
                    flat: true,
                  },
                  nativeOn: {
                    click: (event) => {
                        this.submitForm(event.target.value);
                    }
                  }
                }, [
                  !this.selected ? 'Crear': 'Editar',
                  this.$createElement('v-icon', ['check_circle'])
                ])
            ])
        },
    },
    render: function () {
      return this.$createElement('v-card', [
          this._genCardHeader(),
          this._genCardBody(),
          this._genCardFooter(),
      ]);
    }
}
</script>

<style lang="css">
</style>
