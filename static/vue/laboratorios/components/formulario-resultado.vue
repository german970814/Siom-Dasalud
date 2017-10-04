<script>
import _ from 'underscore';
import IGSlotInput from './slot-input.vue';
import Vue from 'vue/dist/vue.js';
import IgEditDialog from './edit-dialog';

export default {
    name: 'formulario-resultado',
    components: {'ig-slot-input': IGSlotInput, 'ig-edit-dialog': IgEditDialog},
    mounted: function () {

    },
    data: function () {
        return {
            tabs: [],
            headers: [
                {
                    text: 'Concepto', value: 'id', align: 'left',
                },
                {
                    text: 'Valor Resultado', value: 'tabla-cedula', align: 'left',
                },
                {
                    text: 'Medida', value: 'paciente-pnombre', align: 'left',
                },
                {
                    text: 'Comentarios', value: 'tipo', align: 'left',
                },
                {
                    text: 'Referencias', value: 'paciente-pnombre', align: 'left',
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
    watch: {
        value: {
            handler: function () {
                this.$emit('empty', this._hasEmptyValues());
            },
            deep: true
        }
    },
    methods: {
        customSortFunction (items, index, descending) {
            return items;
        },
        _hasEmptyValues () {
            const MODEL_TEXT = ['select', 'text', 'number', 'textarea'];
            const MODEL_OBJ = [];

            if (!this.value.item.cerrado) {
                for (let item of this.value.items) {
                    if (MODEL_TEXT.indexOf(item.tipo.name.toLowerCase()) !== -1) {
                        let result = typeof item.model_text === "string"? item.model_text.trim(): !_.isEmpty(item.model_text);
                        if (!Boolean(result)) {
                            return true;
                        }
                    } else if (MODEL_OBJ.indexOf(item.tipo.name.toLowerCase()) !== -1) {
                        if (_.isEmpty(item.model_check)) {
                            return true;
                        }
                    }
                }
            }
            return false;
        },
        _genEditDialog (item) {
            let dialog = 'ig-edit-dialog';
            if (this.disabled) {
                dialog = 'ig-slot-input';
            }
            if (!('observaciones' in item)) {
                // item.observaciones = '';
                Vue.set(item, 'observaciones', '');
            }
            return this.$createElement(dialog,
            {
                on: {
                    open: () => {
                        item._observaciones = item.observaciones
                    },
                    cancel: () => {
                        item.observaciones = item._observaciones || item.observaciones
                    }
                },
                props: {large: true, cancelText: 'Cancelar', saveText: 'Guardar'}
            }, [
                Boolean(item.observaciones.trim()) ? item.observaciones: this.$createElement('div', {'class': 'teal--text'}, ['Agregar Comentario']),
                this.$createElement('v-text-field', {
                    slot: 'input',
                    props: {
                        label: 'Comentario', 'multi-line': true, type: 'text', autofocus: true
                    },
                    on: {
                        input: (event) => {
                            item.observaciones = event;
                            this.$emit('input', event);
                        },
                        blur: (event) => {
                            item.observaciones = item.observaciones;
                            this.$emit('blur', event);
                        }
                    },
                }, [])
            ])
        },
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
                    },
                    customSort: this.customSortFunction
                },
                scopedSlots: {
                    items: (props) => {
                        let tds = [];
                        if (props.item.tipo.name != 'title') {
                            return [
                                this._genTd(props.item, props.item.nombre),
                                this._genTd(props.item, this.createTdWithProp(props.item)),
                                this._genTd(props.item, props.item.unidades),
                                this._genTd(props.item, this._genEditDialog(props.item)),
                                ...this.calculaReferencias(props.item),
                            ]
                        }
                        return [
                            this.$createElement('td', {'class': 'text-xs-left', attrs: {colspan: 5}}, [
                                this.$createElement('strong', {attrs: {style: 'font-size: 20px'}} , [props.item.nombre.toUpperCase()])
                            ])
                        ]
                    }
                }
            }, []);
            return childs;
        },
        _genFooter () {
            if (this.value.item.cerrado) {
                return this.$createElement('v-layout', [
                    this.$createElement('p', [
                        this.$createElement('strong', ['Comentarios:'])
                    ]),
                    this.$createElement('p', [this.value.item.comentario])
                ])
            }
            return this.$createElement('v-layout', [
                this.$createElement('v-text-field', {
                    props: {
                        label: 'Comentarios',
                        multiLine: true,
                    },
                    domProps: {
                        value: this.value.item.comentario
                    },
                    on: {
                        input: (event) => {
                            this.value.item.comentario = event;
                            this.$emit('input', event);
                        },
                        blur: (event) => {
                            // this.value.item.comentario = event;
                        }
                    },
                }, [])
            ])
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
            if ('referencias' in item && item.tipo.name == 'number') {
                let refs = item.referencias[gender].minima.toString().concat(' - ') + item.referencias[gender].maxima.toString();
                childs.push(
                    this._genTd(item, refs)
                )
            } else {
                // childs.push(
                //     this._genTd(item, item.referencia)
                // )
                let render = Vue.component('template-x', {
                    props: [],
                    template: '<div>0</div>'.replace('0', item.referencia)
                });
                childs.push(
                    this._genTd(item, this.$createElement('template-x', {}, []))
                )
            }
            return childs;
        },
        createTdWithProp (item) {
            let ref = this.getRefByItem(item)
            let found = this.tabs.find(x => x == ref);
            if (!found) {
                this.tabs.push(ref);
            }

            const MATCH = {
                'text': 'v-text-field',
                'textarea': 'v-text-field',
                'select': 'v-select',
                'checkbox': 'v-checkbox',
                'radio': 'v-radio',
                'number': 'v-text-field',
                'title': '',
            }

            let dialog = 'ig-edit-dialog';
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
                        on: {
                            open: () => {
                                item._model_text = item.model_text
                            },
                            cancel: () => {
                                item.model_text = item._model_text || item.model_text
                            },
                            save: () => {
                                let next = this.tabs.indexOf(ref);
                                next++;
                                next = this.tabs[next];
                                let element = this.$refs[next];
                                if (element) {
                                    window.scrollTo(window.scrollX, window.scrollY + 50)
                                    element.isActive = true;
                                }
                            }
                        },
                        props: {large: false},
                        ref
                    },
                    [
                        Boolean(item.model_text.trim()) ? item.model_text + unidades: this.$createElement('div', {'class': 'teal--text'}, ['Agregar Resultado']),
                        this.$createElement(MATCH[item.tipo.name], {
                            slot: 'input',
                            props: {
                                label: 'Resultado', 'multi-line': item.tipo.name == 'textarea',
                                type: item.tipo.name == 'number' ? 'number': 'text',
                                hint: item.help, 'persistent-hint': true, autofocus: true
                            },
                            domProps: {
                                value: item.model_text.trim()
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
                return this.$createElement(dialog,
                    {
                        props: {large: true, cancelText: 'Cancelar', saveText: 'Guardar'},
                        on: {
                            open: () => {
                                item._model_text = item.model_text;
                            },
                            cancel: () => {
                                item.model_text = item._model_text || item.model_text;
                            }
                        },
                        ref
                    },
                    [
                        !_.isEmpty(item.model_text) && item.model_text.text.trim() ? item.model_text.text: this.$createElement('div', {'class': 'teal--text'}, ['Agregar Resultado']),
                        this.$createElement(
                            MATCH[item.tipo.name],
                            {
                                slot: 'input',
                                ref: 'select',
                                props: {
                                    label: 'Resultado', 'item-value': 'text',
                                    hint: item.help, 'persistent-hint': true,
                                    items: item.choices, 'return-object': true,
                                    autofocus: true
                                },
                                domProps: {
                                    value: item.model_text
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
                            }, []
                        )
                    ]
                )
            }
            return 'hola';
        },
        getRefByItem(item) {
            let type = item.tipo.name.toUpperCase();
            return item.nombre.toUpperCase().replace(/\s*/g, '').concat('_' + type);
        }
    },
    render () {
        return this.$createElement('div', [
            this._genHeader(),
            this._genBody(),
            this._genFooter(),
        ])
    }
}
</script>

<style lang="css">
.fixindex {
    z-index: 7 !important;
}
</style>
