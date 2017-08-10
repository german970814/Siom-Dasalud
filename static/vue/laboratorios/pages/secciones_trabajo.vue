<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <ig-table
                  table-title="Areas"
                  :headers="headers"
                  :data="elements"
                  :fields="['codigo', 'descripcion']"
                  @selectedrow="eventUpdatedForm"
                  :loading="loading"
                ></ig-table>
            </v-flex>
        </v-layout>
        <br>
        <v-stepper v-model="stepper">
            <v-stepper-header class="white">
                <v-stepper-step step="1" @click.native="stepper = 1" :complete="validateFirstStep()">Área</v-stepper-step>
                <v-divider></v-divider>
                <v-stepper-step step="2" @click.native="secondStepClick">Plantilla de Gasto</v-stepper-step>
            </v-stepper-header>
            <v-stepper-content step="1" class="white">
                <ig-form
                :fields="fields"
                :url="urlForm"
                @showsnack="showSnackBar"
                @objectcreated="eventCreatedObject"
                @clearselected="selected = false"
                :selected="selected"
                >
                    <v-btn flat @click.native="stepper = 2" dark v-if="validateFirstStep()">
                        Continuar
                    </v-btn>
                </ig-form>
            </v-stepper-content>
            <v-stepper-content step="2" class="white">
                <v-card>
                    <v-card-title>Lista de insumos por área</v-card-title>
                    <v-card-text>
                        <ig-producto :area="area" :plantillas="plantillas"></ig-producto>
                    </v-card-text>
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
import ProductoComponent from './../components/productos.vue';

import IgMixin from './../mixins/igmixin.js';

import URL from './../urls.js';

// Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(Vuetify);


export default {
    mixins: [IgMixin],
    watch: {
        selected: function () {
            if (!this.selected) {
                this.area = {};
            } else {
                this.area = this.selected;
                this.$http.get(URL.plantillaArea.concat('?area=' + this.area.id.toString()))
                  .then(response => {
                      if (response.body instanceof Array) {
                          this.plantillas = response.body;
                      }
                  }, response => {

                  })
            }
        }
    },
    data: function () {
          return {
              area: {},
              plantillas: [],
              stepper: 1,
              urlForm: URL.secciones_trabajo,
              selected: false,
              headers: [
                {
                  text: 'Código',
                  value: 'codigo',
                  left: true,
                },
                {
                  text: 'Nombre',
                  value: 'descripcion',
                  left: true,
                },
              ],
              fields: [
                {
                  name: 'codigo',
                  verbose_name: 'Código',
                  type: String,
                  hint: 'Este es el código que identifica a cada equipo.'
                },
                {
                  name: 'descripcion',
                  verbose_name: 'Descripción',
                  type: String,
                  hint: 'Este es el nombre del equipo.',
                },
            ]
          }
    },
    components: {
        igMenu: MenuComponent,
        igTable: TableComponent,
        igForm: FormComponent,
        igProducto: ProductoComponent,
    },
    mounted: function () {
        this.getElements(URL.secciones_trabajo);
    },
    methods: {
        validateFirstStep: function () {
            return !_.isEmpty(this.area);
        },
        secondStepClick: function () {
            if (this.validateFirstStep()) {
                this.stepper = 2;
            }
        },
    }
}
</script>

<style lang="css">
</style>
