<template lang="html">
    <div class="">
        <v-container>
            <v-row></v-row>
            <div v-for="(item, id) of items" :key="item">
                <v-row>
                    <v-col md12 xs12>
                        <v-card>
                            <v-card-title>
                            </v-card-title>
                            <v-card-text class="grey lighten-5">
                                <!-- <v-alert error hide-icon :value="['checkbox', 'radio'].indexOf(item.tipo.name) !== -1 && item.choices.length <= 1">
                                Asegurate de crear varias opciones.
                              </v-alert> -->
                                <formulario-resultado @input="error = hasError()" :value="{item, items: 'formato' in item ? item.formato: item.resultado}" :disabled="false"></formulario-resultado>
                            </v-card-text>
                            <v-card-row actions>
                              <v-btn :class="{'green--text': !someError(item), 'red--text': someError(item), 'darken-1': true}" flat @click.native="someError(item) ? () => undefined: saveItem(item)">Guardar</v-btn>
                            </v-card-row>
                        </v-card>
                    </v-col>
                </v-row>
                <br>
            </div>
        </v-container>
        <floating-button>
            <v-btn
              floating
              :error="error"
              :success="!error"
              v-tooltip:left="{html: Boolean(error) ? 'Aun hay errores': 'Confirmar y Guardar'}"
              @click.native="saveAll">
                <v-icon>{{ Boolean(error) ? 'clear': 'done' }}</v-icon>
            </v-btn>
        </floating-button>
    </div>
</template>

<script>
import _ from 'underscore';

import Vue from 'vue/dist/vue.js';

import FormularioResultado from './../components/formulario-resultado.vue';
import FloattingButton from './../components/floating-button.vue';
// import FormComponent from './../components/form.vue';
import ErrorMixin from './../mixins/errormixin.js';

import URL from './../urls.js';

export default {
    components: {
        formularioResultado: FormularioResultado,
        floatingButton: FloattingButton,
    },
    mixins: [ErrorMixin],
    created: function () {
        this._fetchData();
        this.error = this.hasError();
    },
    data: function () {
        return {
          items: [],
          error: true,
        }
    },
    watch: {
        '$route': '_fetchData',
    },
    props: {

    },
    methods: {
        someError: function (item) {
            let formato = 'formato' in item ? item.formato: item.resultado;
            for (let field of formato) {
                if (this.hasError(field)) {
                    return true;
                }
            }
            return false;
        },
        genValidationsForItem: function (item) {
            let formato = 'formato' in item ? item.formato: item.resultado;
            for (let field of formato) {
                this.addValidation({
                    target: field,
                    validations: [
                        i => ['select', 'radio', 'textarea', 'text'].indexOf(i.tipo.name) !== -1 ? i.model_text !== '': true,
                        i => ['checkbox'].indexOf(i.tipo.name) !== -1 ? i.model_check.length > 1: true,
                    ]
                })
            }
        },
        _fetchData: function () {
            this.$http.get(URL.resultados.concat(this.$route.params.id.toString() + '/'))
              .then(response => {
                  this.items = [];
                  if ('resultados' in response.body && response.body.resultados) {
                      this.items.push.apply(this.items, response.body.resultados);
                      for (let items of response.body.resultados) {
                          // this.items(items)
                          this.genValidationsForItem(items);
                      }
                  }
                  if ('formatos' in response.body && response.body.formatos) {
                      this.items.push.apply(this.items, response.body.formatos)
                      for (let items of response.body.formatos) {
                          // this.items(items)
                          this.genValidationsForItem(items);
                      }
                  }
              }, response => {
                  console.error(response);
              })
        },
        saveItem: function (item, showsnack = true) {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            let data = {
                laboratorio: item.laboratorio,
                orden: {id: this.$route.params.id},
                resultado: JSON.stringify('formato' in item ? item.formato: item.resultado)
            };
            if ('resultado' in item) {
                data.id = item.id;
            }
            let error;
            if (!this.someError(item)) {
                this.$http.post(URL.resultados.concat(this.$route.params.id.toString() + '/'), data, {headers: {'X-CSRFToken': token.value}})
                    .then(response => {
                        if (showsnack) {
                            this.$emit('mostrarsnackbar', 'Se ha guardado el resultado de el laboratorio '.concat(item.laboratorio.nombre.toString()));
                            error = false;
                        }
                    }, response => {
                        if (showsnack) {
                            this.$emit('mostrarsnackbar', 'Ha ocurrido un error al guardar el resultado');
                            error = true;
                        }
                    })
            } else {
                error = true;
                if (showsnack) {
                    this.$emit('mostrarsnackbar', 'No se puede guardar el resultado con campos vacios')
                }
            }
            if (error) {
              return error
            }
        },
        saveAll: function () {
            if (this.error) {
                return undefined;
            } else {
                let error;
                for (let item of this.items) {
                    error = this.saveItem(item, false);
                    if (error) {
                        this.$emit('mostrarsnackbar', 'Ha ocurrido un error al guardar los resultados.');
                        break;
                    }
                }
                if (!error) {
                    this.$emit('mostrarsnackbar', 'Se han guardado los resultados con exito.')
                }
            }
        }
    }
}
</script>

<style lang="css">
</style>
