<template lang="html">
    <div>
        <v-container>
          <v-layout>
            <v-flex xs12 md12>
              <ig-table
              table-title="Reactivos"
              :headers="headers"
              :data="elements"
              :fields="['codigo', 'nombre', 'laboratorio.codigo', 'costos']"
              @selectedrow="eventUpdatedForm"
              :loading="loading"
              ></ig-table>
            </v-flex>
          </v-layout>
        </v-container>
        <br>
        <v-container>
          <v-layout>
            <v-flex xs12 md12>
              <ig-form
              :fields="fields"
              :url="urlForm"
              @showsnack="showSnackBar"
              @objectcreated="eventCreatedObject"
              @clearselected="selected = false"
              :selected="selected"
              >
            </ig-form>
          </v-flex>
        </v-layout>
        <br>
      </v-container>
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
                  value: 'tabla-codigo',
                  left: true,
                },
                {
                  text: 'Nombre',
                  value: 'tabla-nombre',
                  left: true,
                },
                {
                  text: 'Laboratorio',
                  value: 'tabla-laboratorio',
                  left: true,
                },
                {
                  text: 'Costo',
                  value: 'tabla-costo',
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
                  name: 'nombre',
                  verbose_name: 'Nombre',
                  type: String,
                  hint: 'Este es el código que identifica a cada equipo.'
                },
                {
                  name: 'laboratorio',
                  verbose_name: 'Laboratorio',
                  type: Array,
                  url: URL.laboratorios,
                  hint: 'Este es el equipo que sera usado en este laboratorio.',
                  key: 'codigo'
                },
                {
                  name: 'alarma_media',
                  verbose_name: 'Alarma Media',
                  type: String,
                  hint: 'Este es el código que identifica a cada equipo.'
                },
                {
                  name: 'alarma_inferior',
                  verbose_name: 'Alarma Inferior',
                  type: String,
                  hint: 'Este es el código que identifica a cada equipo.'
                },
                {
                  name: 'costos',
                  verbose_name: 'Costo',
                  type: String,
                  hint: 'Este es el código que identifica a cada equipo.'
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
