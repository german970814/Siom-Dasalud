<template lang="html">
    <div>
        <v-container>
          <v-row>
            <v-col xs12 md12>
              <ig-table
              table-title="Ordenes con Laboratorios"
              :headers="headers"
              :data="elements"
              :fields="['id', 'paciente.cedula', 'paciente.nombre_completo', 'laboratorios.nombre', 'institucion.razon', 'empresa.razon', 'empresa_cliente', 'fecha']"
              @selectedrow="eventUpdatedForm"
              ></ig-table>
            </v-col>
          </v-row>
        </v-container>
        <br>
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
            selected: false,
            headers: [
                {
                    text: 'ID',
                    value: 'id',
                    left: true,
                },
                {
                    text: 'Cedula',
                    value: 'tabla-cedula',
                    left: true,
                    sortable: false,
                },
                {
                    text: 'Nombre',
                    value: 'paciente-pnombre',
                    left: true,
                },
                {
                    text: 'Tipo',
                    value: 'tipo',
                    left: true,
                },
                {
                    text: 'IPS',
                    value: 'paciente-pnombre',
                    left: true,
                },
                {
                    text: 'Empresa',
                    value: 'paciente-pnombre',
                    left: true,
                },
                {
                    text: 'Empresa Cliente',
                    value: 'paciente-pnombre',
                    left: true,
                },
                {
                    text: 'Fecha Atención',
                    value: 'paciente-pnombre',
                    left: true,
                },
            ],
        }
    },
    components: {
        igMenu: MenuComponent,
        igTable: TableComponent,
        igForm: FormComponent,
    },
    mounted: function () {
        this.getElements(URL.ordenes_laboratorios);
    }
}
</script>

<style lang="css">
</style>
