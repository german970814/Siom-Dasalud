<template lang="html">
    <div>
        <v-container>
          <v-layout>
            <v-flex xs12 md12>
              <ig-table
              table-title="Laboratorios"
              :headers="headers"
              :data="elements"
              :fields="['codigo', 'nombre', 'codigo_internacional', 'equipo.codigo', 'seccion_trabajo.codigo', {href: '/formatos/:id/'}]"
              @selectedrow="customEventUpdatedForm"
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
              urlForm: URL.laboratorios,
              selected: false,
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
                {
                  text: 'Accion', left: true, sortable: false
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
    },
    methods: {
        customEventUpdatedForm: function (value) {
            this.$http.get(URL.servicios.concat(value.servicio.id.toString() + '/'))
                .then(response => {
                    value.servicio = response.body;
                    this.eventUpdatedForm(value);
                }, response => {
                    console.error(response);
                    this.showSnackBar(response.detail || 'Ha ocurrido un error');
                })
        },
    },
    mounted: function () {
        this.getElements(URL.laboratorios);
    }
}
</script>

<style lang="css">
</style>
