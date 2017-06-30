<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <ig-table
                  table-title="Productos"
                  :headers="headers"
                  :data="elements"
                  :fields="['codigo', 'nombre', 'tipo_display', 'cantidad']"
                  @selectedrow="eventUpdatedForm"
                  :loading="loading"
                ></ig-table>
            </v-flex>
        </v-layout>
        <br>
        <v-layout>
            <v-flex xs12 md12>
                <ig-form
                  :fields="fields"
                  :url="urlForm"
                  @showsnack="showSnackBar"
                  @objectcreated="eventCreatedObject"
                  @clearselected="selected = false"
                  :selected="selected"
                ></ig-form>
            </v-flex>
        </v-layout>
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

import IgMixin from './../mixins/igmixin.js';

import URL from './../urls.js';

// Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(Vuetify);


export default {
    mixins: [IgMixin],
    data: function () {
          return {
              urlForm: URL.reactivos,
              selected: false,
              headers: [
                {
                  text: 'Código',
                  value: 'codigo',
                  left: true,
                },
                {
                  text: 'Nombre',
                  value: 'nombre',
                  left: true,
                },
                {
                  text: 'Tipo',
                  value: 'tipo',
                  left: true,
                },
                {
                  text: 'Cantidad',
                  value: 'tabla-costo',
                  left: true,
                },
              ],
              fields: [
                {
                  name: 'codigo',
                  verbose_name: 'Código',
                  type: String,
                  hint: 'Este es el código que identifica al producto.'
                },
                {
                  name: 'nombre',
                  verbose_name: 'Nombre',
                  type: String,
                  hint: 'Este es el nombre del producto.'
                },
                {
                  name: 'alarma_media',
                  verbose_name: 'Alarma Media',
                  type: Number,
                  kwargs: {
                    type: 'number'
                  },
                  hint: 'Este es el código que identifica a cada equipo.'
                },
                {
                  name: 'alarma_inferior',
                  verbose_name: 'Alarma Inferior',
                  type: Number,
                  kwargs: {
                    type: 'number'
                  },
                  hint: 'Este es el código que identifica a cada equipo.'
                },
                {
                  name: 'cantidad',
                  verbose_name: 'Cantidad',
                  type: Number,
                  kwargs: {
                      type: 'number'
                  },
                  hint: 'Este es cantidad de unidades que se tienen para este producto.'
                },
                {
                  name: 'tipo',
                  verbose_name: 'Tipo',
                  type: Array,
                  hint: 'Este es el tipo de el producto.',
                  choices: [
                      {text: 'INSUMO', value: 'I'},
                      {text: 'REACTIVO', value: 'R'}
                  ]
                },
            ]
          }
    },
    components: {
        igMenu: MenuComponent,
        igTable: TableComponent,
        igForm: FormComponent,
    },
    mounted: function () {
        this.getElements(URL.reactivos);
    }
}
</script>

<style lang="css">
</style>
