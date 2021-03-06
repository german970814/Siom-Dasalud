<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <v-card>
                    <v-card-title>
                        Visiometrías
                        <v-spacer></v-spacer>
                        <v-text-field append-icon="search" label="Buscar" single-line hide-details v-model="buscador"></v-text-field>
                    </v-card-title>
                    <v-data-table
                        :pagination.sync="pagination"
                        :total-items="totalItems"
                        :loading="loading"
                        v-bind:headers="headers"
                        :items="elements"
                        v-bind:search="buscador"
                        :rows-per-page-items="[10]"
                        :filter="filter"
                        rows-per-page-text="Filas por Página"
                        no-results-text="No se encontraron resultados">
                        <template slot="headers" scope="props">
                            <tr>
                                <th v-for="header in props.headers" :key="header"
                                :class="['column sortable', pagination.descending ? 'desc' : 'asc', header.value === pagination.sortBy ? 'active' : '']"
                                    @click="changeSort(header)"
                                >
                                    <v-icon>arrow_upward</v-icon>
                                    {{ header.text }}
                                </th>
                            </tr>
                        </template>
                        <template slot="items" scope="props">
                            <template v-for="field of fields">
                                <td :class="{'text-xs-center': true, 'light-green lighten-4': props.item.estado == 'RE' ? true: false}" @click="updateForm(props.item)" v-if="typeof field != 'object'">{{ getattr(props.item, field) }}</td>
                                <td :class="{'text-xs-center': true, 'light-green lighten-4': props.item.estado == 'RE' ? true: false}" v-else>
                                    <v-btn fab dark small router class="cyan darken-1" :href="field.href.replace(':id', props.item.id)">
                                        <v-icon dark>content_paste</v-icon>
                                    </v-btn>
                                </td>
                            </template>
                        </template>
                    </v-data-table>
                </v-card>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import _ from 'underscore';

import Vue from 'vue/dist/vue.js';
import Vuetify from 'vuetify';
import VueResource from 'vue-resource';

import TableComponent from './../components/table.vue';
// import FormComponent from './../components/form.vue';

import IgMixin from './../mixins/igmixin.js';

import URL from './../urls.js';

// Vue.use(VueRouter);
Vue.use(VueResource);
Vue.use(Vuetify);


export default {
    mixins: [IgMixin],
    data: function () {
        return {
            buscador: '',
            loading: false,
            fields: [
              'id', 'orden.paciente.cedula', 'orden.paciente.nombre_completo',
              'orden.institucion.razon', 'orden.empresa.razon',
              'orden.empresa_cliente', 'orden.fecha',
              {href: '/formulario/:id/', patrons: [{identifier: 'id', replace: item => item.id}]}
            ],
            totalItems: 0,
            pagination: {
                page: 1,
                rowsPerPage: 10,
                descending: false,
                totalItems: 0
            },
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
                {
                  text: 'Accion', left: true, sortable: false
                },
            ],
        }
    },
    watch: {
        pagination: {
            handler () {
                if (this.buscador !== '') {
                    this._getElements(URL.visiometria.concat(`?param=${this.buscador}&page=${this.pagination.page}`));
                } else {
                    this._getElements(URL.visiometria.concat(`?page=${this.pagination.page}`));
                }
            },
            deep: true
        },
        buscador: function () {
            if (this.buscador !== '') {
                this.pagination.page = 1;
                this._getElements(URL.visiometria.concat(`?param=${this.buscador}&page=${this.pagination.page}`));
            } else {
                this._getElements(URL.visiometria.concat(`?page=${this.pagination.page}`));
            }
        }
    },
    components: {
        igTable: TableComponent,
        // igForm: FormComponent,
    },
    mounted: function () {
        this._getElements(URL.visiometria.concat('?page=1'));
    },
    methods: {
        _getElements () {
            if ('loading' in this) {
                if (!this.loading) {
                  this.toggleLoading()
                }
            }
            let url = this.url || arguments[0];
            if (!url) {
                throw new Error('URL no provehida para hacer consulta de elementos');
            }
            this.$http.get(url)
                .then(response => {
                    this.elements = response.body.results;
                    this.totalItems = response.body.count;
                    this.toggleLoading()
                }, response => {
                    this.showSnackBar(response.body.detail || 'Ha ocurrido un error inesperado.')
                    this.toggleLoading()
                });
        },
        _validValue: function (val) {
            return val !== null && ['undefined', 'boolean'].indexOf(typeof val) === -1
        },
        customFilter: function (val, search) {
            return val.toString().toLowerCase().indexOf(search) !== -1;
        },
        filter: function (val, search) {
            var valid = this._validValue(val);
            if (valid) {
                valid = valid && this.customFilter(val, search);
                if (['object'].indexOf(typeof val) === 0 && !valid) {
                    valid = Object.keys(val).some(j => this._validValue(val[j]) && this.customFilter(val[j], search));
                }
            }
            return valid;
        },
        getattr: function (obj, attr) {
            let attrs = attr.split('.');
            for (let at of attrs) {
                if (at in obj) {
                    obj = obj[at];
                }
                if (obj instanceof Array) {
                    var mix = '';
                    for (let elem of obj) {
                        attr = attrs[attrs.length - 1];
                        if (mix) {
                            mix += ', ';
                        }
                        mix += elem[attr];
                    }
                    return mix;
                }
            }
            return obj;
        },
        updateForm: function (item) {
            this.$emit('selectedrow', item);
        },
        changeSort (column) {
            if ('sortable' in column && !(column.sortable)) {
                return;
            }
            column = column.value;
            if (this.pagination.sortBy === column) {
                this.pagination.descending = !this.pagination.descending;
            } else {
                this.pagination.sortBy = column;
                this.pagination.descending = false;
            }
        }
    }
}
</script>

<style lang="css">
</style>
