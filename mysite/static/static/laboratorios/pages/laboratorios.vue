<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <ig-table
                  table-title="Laboratorios"
                  :headers="headers"
                  :data="elements"
                  :fields="['codigo', 'nombre', 'codigo_internacional', 'equipo.codigo', 'seccion_trabajo.codigo']"
                  @selectedrow="customEventUpdatedForm"
                  :loading="loading"
                ></ig-table>
            </v-flex>
        </v-layout>
        <br>
        <v-stepper v-model="stepper" non-linear>
            <v-stepper-header class="white">
                <v-stepper-step step="1" @click.native="stepper = 1" :complete="validateFirstStep()">Laboratorio</v-stepper-step>
                <v-divider></v-divider>
                <v-stepper-step step="2" @click.native="secondStepClick" :complete="stepper > 2">Formato</v-stepper-step>
                <v-divider></v-divider>
                <v-stepper-step step="3" @click.native="thirdStepClick">Insumos y Reactivos</v-stepper-step>
            </v-stepper-header>
            <v-stepper-content step="1" class="white">
                <ig-form
                :fields="fields"
                :url="urlForm"
                @showsnack="showSnackBar"
                @objectcreated="_eventCreatedObject"
                @clearselected="selected = false"
                :selected="selected"
                >
                    <v-btn flat @click.native="stepper = 2" dark v-if="validateFirstStep()">
                        Continuar
                    </v-btn>
                </ig-form>
            </v-stepper-content>
            <v-stepper-content step="2" class="white">
                <ig-formato :laboratorio="laboratorio" @mostrarsnackbar="showSnackBar"></ig-formato>
            </v-stepper-content>
            <v-stepper-content step="3" class="white">
                <v-card>
                    <v-card-text>
                        <v-layout>
                            <v-flex md6 xs12>
                              <v-subheader>Insumos</v-subheader>
                              <ig-producto :laboratorio="laboratorio" :plantillas="plantillas_insumos" tipo="i"></ig-producto>
                            </v-flex>
                            <v-flex md6 xs12>
                              <v-subheader>Reactivos</v-subheader>
                              <ig-producto :laboratorio="laboratorio" :plantillas="plantillas_reactivos" tipo="r"></ig-producto>
                            </v-flex>
                        </v-layout>
                    </v-card-text>
                    <!-- <v-card-row actions>
                        <v-btn primary @click.native="stepper = 1" light>Continue</v-btn>
                        <v-btn flat dark>Cancel</v-btn>
                    </v-card-row> -->
                </v-card>
            </v-stepper-content>
        </v-stepper>
    </div>
</template>

<script>
import _ from 'underscore';

import Vue from 'vue/dist/vue.js';
import Vuetify from 'vuetify';
import VueResource from 'vue-resource';

import MenuComponent from './../components/menu.vue';
import TableComponent from './../components/table.vue';
import FormComponent from './../components/form.vue';
import Formato from './../components/formato.vue';
import ProductoComponent from './../components/productos.vue';

import IgMixin from './../mixins/igmixin.js';

import URL from './../urls.js';

// Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(Vuetify);

const BASE_URL = URL.BASE;

export default {
    mixins: [IgMixin],
    data: function () {
          return {
              laboratorio: {},
              stepper: 1,
              urlForm: URL.laboratorios,
              selected: false,
              plantillas_insumos: [],
              plantillas_reactivos: [],
              headers: [
                {
                  text: 'Código',
                  left: true,
                  value: 'codigo'
                },
                {
                  text: 'Nombre', value: 'nombre', left: true,
                },
                {
                  text: 'Código Internacional', value: 'codigo_internacional', left: true,
                },
                {
                  text: 'Equipo', value: 'equipo', left: true,
                },
                {
                  text: 'Sección de Trabajo', value: 'seccion_trabajo', left: true,
                  sortable: false,
                },
              ],
              fields: [
                {
                  name: 'codigo',
                  verbose_name: 'Código',
                  type: String,
                  hint: 'Este es el código que identifica a cada laboratorio.'
                },
                {
                  name: 'nombre',
                  verbose_name: 'Nombre',
                  type: String,
                  hint: 'Este es el nombre del equipo.',
                },
                {
                  name: 'codigo_internacional',
                  verbose_name: 'Código Internacional',
                  type: String,
                  hint: 'Este es el código de representacion internacional del laboratorio.',
                },
                {
                  name: 'equipo',
                  verbose_name: 'Equipo',
                  type: Array,
                  url: URL.equipos,
                  hint: 'Este es el equipo que sera usado en este laboratorio.',
                  key: 'nombre'
                },
                {
                  name: 'seccion_trabajo',
                  verbose_name: 'Sección de Trabajo',
                  type: Array,
                  url: URL.secciones_trabajo,
                  hint: 'Este es el area o sección de trabajo de este laboratorio.',
                  key: 'codigo'
                },
                {
                  name: 'servicio',
                  verbose_name: 'Servicio',
                  type: Array,
                  url: URL.servicios,
                  hint: 'Este es el servicio asociado, con el cual se hará la relación en la orden.',
                  key: 'nombre'
                },
            ]
          }
    },
    components: {
        igMenu: MenuComponent,
        igTable: TableComponent,
        igForm: FormComponent,
        igFormato: Formato,
        igProducto: ProductoComponent,
    },
    watch: {
        selected: function () {
            this.plantillas_insumos = [];
            this.plantillas_reactivos = [];
            if (!this.selected) {
                this.laboratorio = {};
            } else {
                this.laboratorios = this.selected;
                this.$http.get(URL.plantillaLaboratorio.concat('?laboratorio=' + this.laboratorio.id.toString()))
                  .then(response => {
                      if (response.body instanceof Array) {
                          for (let plantilla of response.body) {
                              if (plantilla.producto.tipo.toLowerCase() == 'i') {
                                  this.plantillas_insumos.push(plantilla);
                              } else {
                                  this.plantillas_reactivos.push(plantilla);
                              }
                          }
                      }
                  }, response => {

                  })
            }
        }
    },
    methods: {
        validateFirstStep: function () {
            return !_.isEmpty(this.laboratorio);
        },
        secondStepClick: function () {
            if (this.validateFirstStep()) {
                this.stepper = 2;
            }
        },
        thirdStepClick: function () {
            if (this.validateFirstStep()) {
                this.stepper = 3;
            }
        },
        customEventUpdatedForm: function (value) {
            this.laboratorio = value;
            this.$http.get(URL.servicios.concat(value.servicio.id.toString() + '/'))
                .then(response => {
                    value.servicio = response.body;
                    this.eventUpdatedForm(value);
                }, response => {
                    console.error(response);
                    this.showSnackBar(response.detail || 'Ha ocurrido un error');
                })
        },
        _eventCreatedObject: function (value) {
            this.laboratorio = value;
            value.selected = false;
            let exists = this.elements.find(x => x.id == value.id);
            if (exists) {
                for (let attr in exists) {
                    this.elements[this.elements.indexOf(exists)][attr] = value[attr] || exists[attr];
                }
            } else {
                this.elements.push(value);
            }
            this.selected = value;
            this.stepper = 3;
        }
    },
    mounted: function () {
        this.getElements(URL.laboratorios);
    }
}
</script>

<style lang="css">
.stepper__wrapper .card {
    box-shadow: inherit;
}

.stepper__step--active, .stepper__step--complete {
    cursor: pointer !important;
    transition: ease 1s all;
}

.stepper__step--active:hover, .stepper__step--complete:hover {
    background-color: #f0f0f0;
}
/*.stepper__wrapper .card .card__title{
    display: none;
}*/
</style>
