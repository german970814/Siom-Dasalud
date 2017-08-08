<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <ig-table
                  table-title="Tecnicas"
                  :headers="headers"
                  :data="elements"
                  :fields="['codigo', 'nombre']"
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
              urlForm: URL.tecnicas,
              selected: false,
              headers: [
                {
                  text: 'Código',
                  value: 'codigo',
                  left: true,
                },
                {
                  text: 'Nombre', value: 'nombre',
                  left: true,
                },
              ],
              fields: [
                {
                  name: 'codigo',
                  verbose_name: 'Código',
                  type: String,
                  hint: 'Este es el código que identifica a cada tecnica.'
                },
                {
                  name: 'nombre',
                  verbose_name: 'Nombre',
                  type: String,
                  hint: 'Este es el nombre de la tecnica.',
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
        this.getElements(URL.tecnicas);
    }
}
</script>

<style lang="css">
</style>
