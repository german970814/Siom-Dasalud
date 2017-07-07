<script>
import _ from 'underscore';
import IGSlotInput from './slot-input.vue';

export default {
    name: 'formulario-resultado',
    components: {'ig-slot-input': IGSlotInput},
    mounted: function () {

    },
    data: function () {
        return {
            headers: [
                {
                    text: 'Concepto', value: 'id', left: true,
                },
                {
                    text: 'Valor Resultado', value: 'tabla-cedula', left: true,
                },
                {
                    text: 'Medida', value: 'paciente-pnombre', left: true,
                },
                {
                    text: 'Abreviatura', value: 'tipo', left: true,
                },
                {
                    text: 'Referencia Minima', value: 'paciente-pnombre', left: true,
                },
                {
                    text: 'Referencia Maxima', value: 'paciente-pnombre', left: true,
                },
            ],
        }
    },
    props: {
        value: {},
        gender: '',
        disabled: {
            type: Boolean,
            default: true
        },
    },
    methods: {
        validateErrorItem (item) {
            let gender = this.gender.toUpperCase();
            if (item.tipo.name == 'number' && 'referencias' in item) {
                let refMin = item.referencias[gender].minima;
                let refMax = item.referencias[gender].maxima;
                return Boolean(item.model_text.toString()) ? !(parseInt(item.model_text) >= refMin && parseInt(item.model_text) <= refMax): false;
            }
            return false;
        },
        _genTd (item, slot) {
            return this.$createElement(
              'td',
              {'class': {'text-xs-center': true, 'yellow lighten-1': this.validateErrorItem(item)}}, [slot]
            )
        },
        _genHeader () {
            return this.$createElement('v-layout', [
                this.$createElement('h1', {'class': 'title'}, ['Formulario de Resultado'])
            ])
        },
        _genBody () {
            let childs = this.$createElement('v-data-table', {
                  props: {
                      headers: this.headers, items: this.value.items,
                      rowsPerPageItems: [100],
                      pagination: {
                          page: 1,
                          rowsPerPage: 100,
                          descending: false,
                          totalItems: 0
                      }
                  },
                  scopedSlots: {
                      items: (props) => {
                          let tds = [];
                          if (props.item.tipo.name != 'title') {
                              return [
                                  this._genTd(props.item, props.item.nombre),
                                  this._genTd(props.item, this.createTdWithProp(props.item)),
                                  this._genTd(props.item, props.item.unidades),
                                  this._genTd(props.item, props.item.nombre),
                                  ...this.calculaReferencias(props.item),
                              ]
                          }
                          return [
                              this.$createElement('td', {'class': 'text-xs-left', attrs: {colspan: 6}}, [
                                  this.$createElement('strong', {attrs: {style: 'font-size: 20px'}} , [props.item.nombre.toUpperCase()])
                              ])
                          ]
                      }
                  }
                },
                []
            );

            return childs;
        },
        calculaReferencias (item) {
            /*
             * Calcula las referencias del modo
             * referencias {
             *   M: {
             *     minima: 12,
             *     maxima: 15,
             *   },
             *   F: {
             *     minima: 12,
             *     maxima: 15,
             *   }
             * }
            */
            let childs = [];
            let gender = this.gender.toUpperCase();
            let unidades = item.unidades;
            if (item.tipo.name != 'number') {
                unidades = '';
            }
            if ('referencias' in item) {
                childs.push(
                    this._genTd(item, item.referencias[gender].minima.toString().concat(' ') + unidades)
                )
                childs.push(
                    this._genTd(item, item.referencias[gender].maxima.toString().concat(' ') + unidades)
                )
            } else {
                childs.push(
                    this._genTd(item, 'undefined')
                )
                childs.push(
                    this._genTd(item, 'undefined')
                )
            }
            return childs;
        },
        createTdWithProp (item) {
            const MATCH = {
                'text': 'v-text-field',
                'textarea': 'v-text-field',
                'select': 'v-select',
                'checkbox': 'v-checkbox',
                'radio': 'v-radio',
                'number': 'v-text-field',
                'title': '',
            }

            let dialog = 'v-edit-dialog';
            if (this.disabled) {
                dialog = 'ig-slot-input';
            }

            if (MATCH[item.tipo.name] == 'v-text-field') {
                let unidades = '';
                if (item.tipo.name == 'number') {
                    unidades = ' '.concat(item.unidades)
                }
                return this.$createElement(dialog,
                  {
                    'class': 'text-xs-center',
                    on: {
                        open: () => {
                            item._model_text = item.model_text
                        },
                        cancel: () => {
                            item.model_text = item._model_text || item.model_text
                        }
                    },
                    props: {large: true, 'cancel-text': 'Cancelar', 'save-text': 'Guardar'}
                  },
                  [
                    Boolean(item.model_text) ? item.model_text + unidades: this.$createElement('div', {'class': 'teal--text'}, ['Agregar Resultado']),
                    this.$createElement(MATCH[item.tipo.name], {
                        slot: 'input',
                        props: {
                            label: 'Resultado', 'multi-line': item.tipo.name == 'textarea',
                            type: item.tipo.name == 'number' ? 'number': 'text',
                            hint: item.help, 'persistent-hint': true
                        },
                        on: {
                            input: (event) => {
                                item.model_text = event;
                                this.$emit('input', event);
                            },
                            blur: (event) => {
                                item.model_text = item.model_text;
                                this.$emit('blur', event);
                            }
                        },
                      }, [])
                  ]
                )
            } else if (MATCH[item.tipo.name] == 'v-select') {
                return this.$createElement(dialog, {
                    'class': 'text-xs-center',
                    props: {large: true, 'cancel-text': 'Cancelar', 'save-text': 'Guardar'},
                    on: {
                        open: () => {
                            item._model_text = item.model_text;
                            // fix z-index
                            if (!_.isEmpty(this.$refs.select)) {
                                if (this.$refs.select instanceof Array) {
                                    this.$refs.select.forEach(select => {
                                        select.$refs.menu.$el.classList.add('fixindex');
                                    })
                                } else {
                                    // console.log(this.$refs.select.$refs.menu.$ refs.content)
                                    this.$refs.select.$refs.menu.$refs.content.classList.add('fixindex');
                                }
                            }
                        },
                        cancel: () => {
                            item.model_text = item._model_text || item.model_text;
                            // fix z-index
                            if (!_.isEmpty(this.$refs.select)) {
                                if (this.$refs.select instanceof Array) {
                                    this.$refs.select.forEach(select => {
                                        select.$refs.menu.$el.classList.add('fixindex');
                                    })
                                } else {
                                    // console.log(this.$refs.select.$refs.menu.$ refs.content)
                                    this.$refs.select.$refs.menu.$refs.content.classList.add('fixindex');
                                }
                            }
                        }
                    }
                  },
                  [
                    !_.isEmpty(item.model_text) ? item.model_text.text: this.$createElement('div', {'class': 'teal--text'}, ['Agregar Resultado']),
                    this.$createElement(MATCH[item.tipo.name], {
                        slot: 'input',
                        ref: 'select',
                        props: {
                            label: 'Resultado', 'item-value': 'text',
                            hint: item.help, 'persistent-hint': true,
                            items: item.choices, 'return-object': true
                        },
                        on: {
                            input: (event) => {
                                item.model_text = event;
                                this.$emit('input', event);
                            },
                            blur: (event) => {
                                item.model_text = item.model_text;
                                this.$emit('blur', event);
                            }
                        },
                      }, [])
                  ]
                )
            }
            return 'hola';
        },
    },
    render () {
        return this.$createElement('div', [
            this._genHeader(),
            this._genBody(),
        ])
    }
}
</script>

<style lang="css">
.fixindex {
    z-index: 7 !important;
}
</style>
