<template lang="html">
    <div>
        <v-container>
            <v-layout>
                <v-flex xs12 md12>
                    <v-card>
                        <v-card-title>
                            Ordenes en Recepción
                            <v-spacer></v-spacer>
                            <v-text-field append-icon="search" label="Buscar" single-line hide-details v-model="buscador"></v-text-field>
                        </v-card-title>
                        <v-data-table
                          :pagination.sync="pagination"
                          :headers="headers"
                          :items="elements"
                          :rows-per-page-items="[10]"
                          :rowsPerPage="10"
                          rows-per-page-text="Filas por Página"
                          no-results-text="No se encontraron resultados"
                          >
                            <template slot="headers" scope="props">
                                <span style="text-align:before: center !important">{{ props.item.text }}</span>
                            </template>
                            <template slot="items" scope="props">
                                <td>{{ props.item.id }}</td>
                                <td>{{ props.item.paciente.nombre_completo }}</td>
                                <td>{{ joinBy(props.item.laboratorios, x => x.codigo, ' | ') }}</td>
                                <td>
                                    <v-btn floating small class="cyan darken-1" @click.native.stop="selectRecepcion(props.item)">
                                        <v-icon light>mode_edit</v-icon>
                                    </v-btn>
                                </td>
                            </template>
                        </v-data-table>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
        <v-dialog width="80%" v-model="modalTomaMuestra">
            <v-card>
                <v-card-row>
                    <v-card-title>Recepcion # {{ recepcion.id }}</v-card-title>
                </v-card-row>
                <v-card-row v-if="hasRecepcion">
                    <v-card-text>
                        <v-card horizontal flat>
                            <v-card-row :img="recepcion.paciente.foto" height="325px"></v-card-row>
                            <v-card-column>
                                <v-card-row height="100px" class="">
                                    <v-card-text>
                                      <v-layout>
                                        <v-flex md6>
                                            <strong>Nombre del paciente</strong>
                                            <div>{{ recepcion.paciente.nombre_completo }}</div>
                                            <br>
                                            <strong>Identificación</strong>
                                            <div>{{ recepcion.paciente.cedula }}</div>
                                            <br>
                                            <strong>Edad del paciente</strong>
                                            <div>{{ recepcion.paciente.edad + ' ' + recepcion.paciente.unidad_edad }}</div>
                                        </v-flex>
                                        <v-flex md6>
                                            <ig-producto :plantillas="plantillas" ref="hojaGasto" filter></ig-producto>
                                        </v-flex>
                                      </v-layout>
                                    </v-card-text>
                                </v-card-row>
                                <v-card-row actions class="cyan darken-1">
                                    <v-btn flat class="white--text" @click.native="saveRecepcion">
                                        <v-icon left light>rate_review</v-icon>Muestra Tomada
                                    </v-btn>
                                </v-card-row>
                            </v-card-column>
                        </v-card>
                    </v-card-text>
                </v-card-row>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import _ from 'underscore';

import Vue from 'vue/dist/vue.js';
import Vuetify from 'vuetify';
import VueResource from 'vue-resource';

import IgMixin from './../mixins/igmixin.js';
import ProductoComponent from './../components/productos.vue';

import URL from './../urls.js';

// Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(Vuetify);

const BASE_URL = URL.BASE;

export default {
    mixins: [IgMixin],
    components: {
      igProducto: ProductoComponent
    },
    data: function () {
          return {
              pagination: {
                  page: 1,
                  rowsPerPage: 10,
                  descending: false,
                  totalItems: 0
              },
              modalTomaMuestra: false,
              recepcion: {},
              plantillas: [],
              selected: false,
              buscador: '',
              headers: [
                  {
                      text: 'Orden', left: true, value: 'codigo'
                  },
                  {
                      text: 'Paciente', value: 'nombre', left: true,
                  },
                  {
                      text: 'Laboratorios', value: 'codigo_internacional', left: true,
                  },
                  {
                      text: 'Accion', value: 'codigo_internacional', left: true,
                  },
              ],
          }
    },
    computed: {
        hasRecepcion: function () {
            return !_.isEmpty(this.recepcion);
        }
    },
    watch: {
    },
    methods: {
        saveRecepcion ($event) {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            let plantillas = this.$refs.hojaGasto.self_plantillas;
            let orden = this.recepcion;
            for (let plantilla of plantillas) {
                plantilla.orden = orden;
            }
            this.$http.post(URL.recepciones, {orden: orden, hoja_gasto: plantillas}, {headers: {'X-CSRFToken': token.value}})
              .then(response => {
                  // console.log(response);
                  let item = this.elements.find(x => {return x.id == this.recepcion.id});
                  if (item) {
                      this.elements.splice(this.elements.indexOf(item), 1);
                  }
                  this.modalTomaMuestra = false;
              }, response => {
                  // console.log(response)
              })
        },
        joinBy (list, func, param) {
            let string = '';
            for (let x of list) {
                if (!string) {
                    string += func(x);
                    continue;
                }
                string += param.concat(func(x));
            }
            return string;
        },
        selectRecepcion (item) {
            this.modalTomaMuestra = true;
            this.recepcion = item;
            this.$http.get(URL.plantillasOrdenes.concat(this.recepcion.id.toString() + '/?tipo=i'))
              .then(response => {
                  this.plantillas = response.body;
              }, response => {

              })
        }
    },
    mounted: function () {
        this.getElements(URL.laboratoriosTomaMuestra);
    }
}
</script>

<style lang="css">
</style>
