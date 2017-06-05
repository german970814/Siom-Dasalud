<template lang="html">
    <div>
        <v-container>
          <v-layout>
            <v-flex xs12 md12>
              <ig-table
              table-title="Equipos"
              :headers="headers"
              :data="elements"
              :fields="['codigo', 'nombre', 'tecnica.codigo']"
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

const BASE_URL = URL.BASE;

export default {
    mixins: [IgMixin],
    data: function () {
          return {
              urlForm: URL.equipos,
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
                  text: 'Técnica',
                  value: 'tecnica',
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
                  hint: 'Este es el nombre del equipo.',
                },
                {
                  name: 'tecnica',
                  verbose_name: 'Técnica',
                  type: Array,
                  hint: 'Este es el código de representacion internacional del laboratorio.',
                  url: URL.tecnicas,
                  key: 'codigo'
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
        this.getElements(URL.equipos);
    }
}
</script>

<style lang="css">
</style>
