<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <v-card>
                    <v-card-title>
                        <p class="title">Productos</p>
                        <v-spacer></v-spacer>
                        <v-text-field append-icon="search" label="Buscar" single-line hide-details v-model="buscador"></v-text-field>
                    </v-card-title>
                    <v-data-table
                        :pagination.sync="pagination"
                        :loading="loading"
                        v-bind:headers="headers"
                        :items="elements"
                        v-bind:search="buscador"
                        :customSort="customSortFunction"
                        :rows-per-page-items="[10]"
                        rows-per-page-text="Filas por Página"
                        no-results-text="No se encontraron resultados">
                        <!--:filter="filter"-->
                        <template slot="headers" scope="props">
                            <!--<span style="text-align:before: center !important">{{ props.item.text }}</span>-->
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
                            <template v-for="field of table_fields">
                                <td :class="itemClasses(props.item)" @click="updateForm(props.item)" v-if="typeof field != 'object'">{{ getattr(props.item, field) }}</td>
                                <td :class="itemClasses(props.item)" v-else>
                                    <v-btn fab dark small router class="cyan darken-1" @click.native.stop="openModalRecarga(props.item)">
                                        <v-icon dark>content_paste</v-icon>
                                    </v-btn>
                                </td>
                            </template>
                        </template>
                    </v-data-table>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn flat outline warning @click.native.stop="controlDialog = true">Controles</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
        <v-dialog v-model="dialog" width="80%" scrollable>
            <v-card class="lol">
                <v-card-title>Realizar Recarga para {{ selected.nombre }}</v-card-title>
                <v-card-text>
                    <v-layout>
                        <ig-form
                            :flat="true"
                            :fields="recarga_fields"
                            :url="urlRecarga.concat(selected ? selected.id.toString(): '') + '/'"
                            ref="formRecarga"
                            @showsnack="showSnackBar"
                            @clearselected="selectedRecarga = false"
                            @objectcreated="updateCantidadObjectCreated"
                            :selected="selectedRecarga"
                        ></ig-form>
                    </v-layout>
                </v-card-text>
                <v-card-actions>
                    <v-btn class="red--text darken-1" flat="flat" @click.native="dialog = false">Cancelar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
        <v-dialog v-model="controlDialog" width="80%" scrollable>
            <v-card class="lol">
                <v-card-title><p class="title">Realizar Control</p></v-card-title>
                <v-card-text>
                    <v-layout>
                        <v-flex md6 xs12>
                            <v-subheader>Insumos</v-subheader>
                            <ig-producto :ref="'producto_i'" :plantillas="[]" tipo="i" :urlSend="urlSend"></ig-producto>
                        </v-flex>
                        <v-flex md6 xs12>
                            <v-subheader>Reactivos</v-subheader>
                            <ig-producto :ref="'producto_r'" :plantillas="[]" tipo="r" :urlSend="urlSend"></ig-producto>
                        </v-flex>
                    </v-layout>
                </v-card-text>
                <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn outline class="red--text darken-1" flat="flat" @click.native="controlDialog = false">Cancelar</v-btn>
                    <v-btn outline class="green--text darken-1" flat="flat" @click.native="saveControl">Aceptar</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
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
import ProductoComponent from './../components/productos.vue';

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
            urlRecarga: URL.recarga,
            selectedRecarga: false,
            selected: false,
            dialog: false,
            buscador: '',
            controlDialog: false,
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
                    value: 'cantidad',
                    left: true,
                },
                {
                    text: 'Recargar',
                    left: true,
                    sortable: false
                }
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
            ],
            table_fields: [
                'producto.codigo', 'producto.nombre', 'produto.tipo_display',
                'producto.cantidad', {}
            ],
            pagination: {
                page: 1,
                rowsPerPage: 10,
                descending: false,
                totalItems: 0
            },
            recarga_fields: [
                {
                    name: 'cantidad',
                    verbose_name: 'Cantidad',
                    type: Number,
                    kwargs: {
                        type: 'number'
                    },
                    hint: 'Cantidad de unidades del producto para la recarga'
                },
                {
                    name: 'fecha_vencimiento',
                    verbose_name: 'Fecha de Vencimiento',
                    required: false,
                    type: Date,
                    kwargs: {
                        type: 'date'
                    },
                    hint: 'Fecha de vencimiento del producto'
                },
                {
                  name: 'lote',
                  verbose_name: 'Lote',
                  required: false,
                  type: String,
                  hint: 'Este es el lote del producto.'
                },
                {
                  name: 'distribuidor',
                  verbose_name: 'Distribuidor',
                  required: false,
                  type: String,
                  hint: 'Este es el distribuidor del producto.'
                },
                {
                  name: 'fabricante',
                  verbose_name: 'Fabricante',
                  required: false,
                  type: String,
                  hint: 'Este es el fabricante del producto.'
                },
                {
                  name: 'marca',
                  verbose_name: 'Marca',
                  required: false,
                  type: String,
                  hint: 'Este es el marca del producto.'
                },
                {
                    name: 'fecha_distribucion',
                    verbose_name: 'Fecha de Distribución',
                    required: false,
                    type: Date,
                    kwargs: {
                        type: 'date'
                    },
                    hint: 'Fecha de vencimiento del producto'
                },
                {
                    name: 'presentacion',
                    verbose_name: 'Presentación',
                    required: false,
                    type: String,
                    hint: 'Esta es la presentacion en la que viene el producto'
                },
                {
                    name: 'invima',
                    verbose_name: 'Invima',
                    required: false,
                    type: String,
                    hint: 'Este es el invima del producto.'
                },
                {
                    name: 'casa_comercial',
                    verbose_name: 'Casa comercial',
                    required: false,
                    type: String,
                    hint: 'Esta es la casa comercial del producto.'
                },
            ]
        }
    },
    computed: {
        urlSend: function () {
            return URL.controlProductos;
        }
    },
    components: {
        igMenu: MenuComponent,
        igTable: TableComponent,
        igForm: FormComponent,
        igProducto: ProductoComponent,
    },
    mounted: function () {
        this.getElements(URL.reactivos);
    },
    methods: {
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
        updateForm: function (item) {
            // this.$emit('selectedrow', item);
            this.selected = item;
        },
        itemClasses: function (item) {
            /* Avisa cuando un elemento necesita una recarga */
            return {
                'text-xs-center': true,
                'yellow lighten-1': item.cantidad < item.alarma_media && item.cantidad >= item.alarma_inferior,
                'orange lighten-1': item.cantidad < item.alarma_inferior
            }
        },
        openModalRecarga: function (item) {
            this.selected = item;
            this.dialog = true;
        },
        updateCantidadObjectCreated: function (event) {
            let created = event;
            let item = this.elements.find(x => {return _.isNumber(created.producto) ? x.id == created.producto: x.id == created.producto.id});
            if (item) {
                item.cantidad += created.cantidad;
            }
            this.dialog = false;
            // console.log(this.$refs.formRecarga)
            for (let field in this.$refs.formRecarga.models) {
                this.$refs.formRecarga.models[field] = '';
            }
        },
        saveControl() {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];

            let productos = [...this.$refs.producto_i.plantillas, ...this.$refs.producto_r.plantillas];

            if (productos) {
                this.$http.post(URL.controlProductos, {'productos': productos}, {headers: {'X-CSRFToken': token.value}})
                    .then(response => {
                        this.getElements(URL.reactivos);
                        this.controlDialog = false;
                        this.$refs.producto_i.plantillas = this.$refs.producto_r.plantillas = [];
                    }, response => {
                        this.$emit('showsnack', 'Ocurrió un error al intentar crear un control.')
                    })
            }
        },
        customSortFunction (items, index, descending) {
            return items;
        },
    }
}
</script>

<style lang="css">
.dialog:not(.dialog--fullscreen) {
    overflow: scroll;
}
</style>
