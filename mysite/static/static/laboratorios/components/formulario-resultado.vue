<!-- <template lang="html">
    <div>
        <v-container>
            <v-layout>
                <h1 class="title">Formulario de Resultado</h1>
            </v-layout>
            <v-layout v-for="(item, id) of value.items" :key="id">
                <v-flex md8>
                    <v-text-field
                        v-if="item.tipo.name == 'text' || item.tipo.name == 'textarea'"
                        :multi-line="item.tipo.name == 'textarea'"
                        :label="item.nombre"
                        :hint="item.help"
                        v-model="item.model_text"
                        :disabled="disabled"
                        persistent-hint
                        @input="$emit('input', $event)"
                    ></v-text-field>
                    <v-select
                        v-else-if="item.tipo.name == 'select'"
                        dark
                        :label="item.nombre"
                        :hint="item.help"
                        v-model="item.model_text"
                        :items="item.choices_select"
                        item-value="text"
                        :disabled="disabled"
                        persistent-hint
                        @input="$emit('input', $event)"
                    ></v-select>
                    <div v-else-if="item.tipo.name == 'checkbox'">
                        <dl class="section-text section-text--def">
                            <dt>{{ item.nombre }}</dt>
                            <dd>{{ item.help }}</dd>
                        </dl>
                        <v-layout v-for="(choice, choiceId) of item.choices" :key="choiceId">
                            <v-flex xs7 md7>
                                <!--v-if="!choice.edit"-- !> esto esta comentado
                                <v-checkbox
                                    :label="choice.name"
                                    v-model="item.model_check"
                                    :value="choice.id"
                                    :disabled="disabled"
                                    primary
                                    @input="$emit('input', $event)"
                                ></v-checkbox>
                            </v-flex>
                        </v-layout>
                    </div>
                    <div v-else-if="item.tipo.name == 'radio'">
                        <dl class="section-text section-text--def">
                            <dt>{{ item.nombre }}</dt>
                            <dd>{{ item.help }}</dd>
                        </dl>
                        <v-layout v-for="(choice, choiceId) of item.choices" :key="choiceId">
                            <v-flex xs7 md7>
                                <v-radio
                                    v-if="!choice.edit"
                                    :label="choice.name"
                                    v-model="item.model_text"
                                    :value="choice.name"
                                    :disabled="disabled"
                                    primary
                                    @input="$emit('input', $event)"
                                ></v-radio>
                            </v-flex>
                        </v-layout>
                    </div>
                </v-flex>
                <v-flex md2 v-if="Boolean(item.referencia)">
                  <h6 class="title">Referencia:</h6> {{ item.referencia }}
                </v-flex>
                <v-flex md2 v-if="Boolean(item.unidades)">
                  <h6 class="title">Unidades:</h6> {{ item.unidades }}
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template> -->

<script>
import _ from 'underscore';

export default {
    name: 'formulario-resultado',
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
        disabled: {
            type: Boolean,
            default: true
        },
    },
    methods: {
        validateErrorItem (item) {
            let gender = 'M';
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
                  props: {headers: this.headers, items: this.value.items},
                  scopedSlots: {
                      items: (props) => {
                          let tds = [];
                          return [
                              this._genTd(props.item, props.item.nombre),
                              this._genTd(props.item, this.createTdWithProp(props.item)),
                              this._genTd(props.item, props.item.unidades),
                              this._genTd(props.item, props.item.nombre),
                              ...this.calculaReferencias(props.item),
                          ]
                      }
                  }
                },
                []
            );
            // console.log(this.$refs.select)
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
            let gender = 'M';
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
                    on: {
                        open: () => {
                            item._model_text = item.model_text
                        },
                        cancel: () => {
                            item.model_text = item._model_text || item.model_text
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
                            items: item.choices_select
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
        return this.$createElement('v-container', [
            this._genHeader(),
            this._genBody(),
        ])
    }
}
</script>

<style lang="css">
ul.list:parent {
    z-index: 14!important;
}
</style>
