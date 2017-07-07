import _ from 'underscore';

import Vue from 'vue/dist/vue.js';
import Vuetify from 'vuetify';
import VueResource from 'vue-resource';
import VueRouter from 'vue-router';

import MenuComponent from './components/menu.vue';
import TableComponent from './components/table.vue';
import FormComponent from './components/form.vue';

import IgMixin from './mixins/igmixin.js';
import router from './routes';

import URL from './urls.js';

Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(Vuetify);

const BASE_URL = URL.BASE;

const app = new Vue({
    el: '#app',
    delimiters: ['{[', ']}'],
    data: {
        snackbar: false,
        snackbarText: '',
        sidebar: false,
        contentLoaded: false,
        http403: false,
    },
    mounted: function () {
        this.contentLoaded = true;
    },
    components: {
        igMenu: MenuComponent,
        igTable: TableComponent,
        igForm: FormComponent,
    },
    methods: {
        mostrarSnackBar: function (value) {
            this.snackbarText = value;
            this.snackbar = true;
        },
        eventoObjetoCreado: function (value) {
            value.selected = false;
            this.elements.push(value);
            this.selected = value;
        },
        eventoFormularioActualizado: function (value) {
            this.selected = value;
        },
    },
    router: router
})//.$mount();
