<template lang="html">
    <div>
        <v-container fluid>
            <v-layout>
                <v-flex xs12 md12>
                    <v-card>
                        <v-card-title>
                            <p class="title">Ordenes en Recepción</p>
                            <v-spacer></v-spacer>
                            <v-text-field append-icon="search" label="Buscar" single-line hide-details v-model="buscador"></v-text-field>
                        </v-card-title>
                        <v-container>
                            <v-layout wrap>
                                <v-flex xs12 md3>
                                    <v-menu
                                        lazy
                                        :close-on-content-click="true"
                                        v-model="fechaMenu"
                                        offset-y
                                        full-width
                                        :nudge-left="40"
                                        max-width="290px">
                                        <v-text-field
                                            slot="activator"
                                            label="Fecha"
                                            v-model="fecha"
                                            prepend-icon="event"
                                            readonly
                                        ></v-text-field>
                                        <v-date-picker v-model="fecha" no-title scrollable actions locale="es-sp">
                                            <template scope="{ save, cancel }">
                                                <v-card-actions>
                                                    <v-btn flat primary @click.native="cancel()">Cancel</v-btn>
                                                    <v-btn flat primary @click.native="save()">Save</v-btn>
                                                </v-card-actions>
                                            </template>
                                        </v-date-picker>
                                    </v-menu>
                                </v-flex>
                            </v-layout>
                        </v-container>
                        <v-data-table
                          :pagination.sync="pagination"
                          :headers="headers"
                          :items="elements"
                          :loading="loading"
                          :rows-per-page-items="[100]"
                          :rowsPerPage="100"
                          :customSort="customSortFunction"
                          rows-per-page-text="Filas por Página"
                          no-results-text="No se encontraron resultados"
                          >
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
                                <td :class="{'green lighten-4': props.item.toma_muestra}">{{ props.item.id }}</td>
                                <td :class="{'green lighten-4': props.item.toma_muestra}">{{ props.item.paciente.nombre_completo }}</td>
                                <td :class="{'green lighten-4': props.item.toma_muestra}">{{ joinBy(props.item.laboratorios, x => x.codigo.toUpperCase(), ' | ') }}</td>
                                <td :class="{'green lighten-4': props.item.toma_muestra}">{{ props.item.fecha }}</td>
                                <td :class="{'green lighten-4': props.item.toma_muestra}">
                                    <v-btn v-if="!props.item.toma_muestra" fab dark small class="cyan darken-1" @click.native.stop="selectRecepcion(props.item)">
                                        <v-icon dark>content_paste</v-icon>
                                    </v-btn>
                                </td>
                            </template>
                        </v-data-table>
                    </v-card>
                </v-flex>
            </v-layout>
        </v-container>
        <v-dialog width="80%" v-model="modalTomaMuestra">
            <v-card>
                <v-card-title>Recepcion # {{ recepcion.id }}</v-card-title>
                <v-card-text v-if="hasRecepcion">
                    <v-card horizontal flat>
                        <v-container>
                            <v-layout>
                                <v-flex xs4>
                                    <v-card-media
                                    :src="fotoPaciente"
                                    height="345px"
                                    ></v-card-media>
                                </v-flex>
                                <v-flex xs8>
                                    <!--height="100px"-->
                                    <v-card-text>
                                        <v-layout>
                                            <v-flex md6>
                                                <div style="margin-bottom: 7px">
                                                    <strong>Nombre del paciente</strong>
                                                    <div>{{ recepcion.paciente.nombre_completo }}</div>
                                                </div>
                                                <div style="margin-bottom: 7px">
                                                    <strong>Identificación</strong>
                                                    <div>{{ recepcion.paciente.cedula }}</div>
                                                </div>
                                                <div style="margin-bottom: 7px">
                                                    <strong>Edad del paciente</strong>
                                                    <div>{{ recepcion.paciente.edad + ' ' + recepcion.paciente.unidad_edad }}</div>
                                                </div>
                                                <div style="margin-bottom: 7px">
                                                    <strong>Empresa cliente</strong>
                                                    <div>{{ recepcion.empresa_cliente }}</div>
                                                </div>
                                                <div style="margin-bottom: 7px">
                                                    <strong>Contacto</strong>
                                                    <div>{{ recepcion.paciente.telefono }}</div>
                                                </div>
                                                <strong>Laboratorios a realizar</strong>
                                                <div>{{ joinBy(recepcion.laboratorios, x => x.nombre.toUpperCase(), ', ') }}</div>
                                            </v-flex>
                                            <v-flex md6>
                                                <ig-producto :plantillas="plantillas" ref="hojaGasto" filter></ig-producto>
                                            </v-flex>
                                        </v-layout>
                                    </v-card-text>
                                    <v-card-actions class="cyan darken-1">
                                        <v-spacer></v-spacer>
                                        <v-btn flat class="white--text" @click.native="saveRecepcion">
                                            <v-icon left light>rate_review</v-icon>Muestra Tomada
                                        </v-btn>
                                        <v-btn flat class="white--text" @click.native="modalTomaMuestra = false">
                                            Cancelar
                                        </v-btn>
                                    </v-card-actions>
                                </v-flex>
                            </v-layout>
                        </v-container>
                    </v-card>
                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import _ from 'underscore';

import Vue from 'vue/dist/vue.js';
import Vuetify from 'vuetify';
import VueResource from 'vue-resource';

import IgMixin from './../mixins/igmixin.js';
import ProductoComponent from './../components/productos.vue';

import URL from './../urls.js';

Vue.use(VueResource);
Vue.use(Vuetify);

const BASE_URL = URL.BASE;

export default {
    mixins: [IgMixin],
    components: {
      igProducto: ProductoComponent
    },
    data: function () {
        return {
            pagination: {
                page: 1,
                rowsPerPage: 100,
                descending: false,
                totalItems: 0
            },
            modalTomaMuestra: false,
            recepcion: {},
            plantillas: [],
            selected: false,
            buscador: '',
            totalItems: 0, fecha: '', fechaMenu: false,
            fotoPaciente: '/static/profile-none.jpg',
            headers: [
                {
                    text: 'Orden', left: true, value: 'codigo'
                },
                {
                    text: 'Paciente', value: 'nombre', left: true,
                },
                {
                    text: 'Laboratorios', value: 'codigo_internacional', left: true,
                },
                {
                    text: 'Fecha', value: 'fecha', left: true,
                },
                {
                    text: 'Accion', sortable: false, left: true,
                },
            ],
        }
    },
    computed: {
        hasRecepcion: function () {
            return !_.isEmpty(this.recepcion);
        },
    },
    watch: {
        recepcion: function () {
            this.reloadFoto();
        },
        pagination: {
            handler () {
                if (this.buscador !== '') {
                    this._getElements(URL.laboratoriosTomaMuestra.concat(`?param=${this.buscador}&page=${this.pagination.page}`));
                } else {
                    this._getElements(URL.laboratoriosTomaMuestra.concat(`?page=${this.pagination.page}`));
                }
            },
            deep: true
        },
        buscador: {
            handler () {
                this._getElements(URL.laboratoriosTomaMuestra.concat(`?param=${this.buscador}&page=1`));
            },
            depp: true
        },
        fecha: function (val) {
            if (val) {
                this._getElements(URL.laboratoriosTomaMuestra.concat(`?page=1&fecha=${val}`));
            } else {
                this._getElements(URL.laboratoriosTomaMuestra.concat(`?page=1`));
            }
        }
    },
    methods: {
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
        },
        reloadFoto () {
            this.$http.get(this.recepcion.paciente.foto)
              .then(response => {
                  this.fotoPaciente = this.recepcion.paciente.foto;
              }, response => {
                  this.fotoPaciente = '/static/profile-none.jpg';
              })
        },
        saveRecepcion ($event) {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            let plantillas = this.$refs.hojaGasto.self_plantillas;
            let orden = this.recepcion;
            for (let plantilla of plantillas) {
                plantilla.orden = orden;
            }
            this.$http.post(URL.laboratoriosTomaMuestra, {orden: orden, hoja_gasto: plantillas}, {headers: {'X-CSRFToken': token.value}})
              .then(response => {
                  this.modalTomaMuestra = false;
                  this.$emit('mostrarsnackbar', 'Se ha guardado la toma de muestra.');
                  this._getElements(URL.laboratoriosTomaMuestra.concat('?page=1'));
              }, response => {
                  this.$emit('mostrarsnackbar', 'Ocurrió un error al guardar la toma, contacta a administración.');
              })
        },
        joinBy (list, func, param) {
            let string = '';
            for (let x of list) {
                if (!string) {
                    string += func(x);
                    continue;
                }
                string += param.concat(func(x));
            }
            return string;
        },
        selectRecepcion (item) {
            this.modalTomaMuestra = true;
            this.recepcion = item;
            this.$http.get(URL.plantillasOrdenes.concat(this.recepcion.id.toString() + '/?tipo=i'))
              .then(response => {
                  this.plantillas = response.body;
              }, response => {

              })
        },
        _getElements () {
            if ('loading' in this) {
                if (!this.loading) {
                    this.toggleLoading()
                }
            }
            let url = this.url || arguments[0];
            if (!url) {
                throw new Error('URL not provided');
            }

            this.$http.get(url)
                .then(response => {
                    this.elements = response.body.results;
                    this.totalItems = response.body.count;
                    this.toggleLoading();
                }, response => {
                    this.showSnackBar(response.body.detail || 'Ha ocurrido un error inesperado');
                    this.toggleLoading();
                });
        },
        customSortFunction (items, index, descending) {
            return items;
        },
    },
    mounted: function () {
        this._getElements(URL.laboratoriosTomaMuestra.concat('?page=1'));
    }
}
</script>

<style lang="css">
</style>
