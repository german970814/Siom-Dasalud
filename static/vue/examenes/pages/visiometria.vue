<template>
    <div>
        <v-layout>
            <v-breadcrumbs icons divider="forward">
                <v-breadcrumbs-item :disabled="false" href="/examenes/#/ordenes/visiometria/">
                    Lista ordenes
                </v-breadcrumbs-item>
                <v-breadcrumbs-item :disabled="true">
                    Resultado
                </v-breadcrumbs-item>
            </v-breadcrumbs>
        </v-layout>
        <v-layout>
            <v-flex xs12 md12>
                <v-card>
                    <v-card-title>
                        <h1 class="title">Formato "Certificado de aptitud visual"</h1>
                    </v-card-title>
                    <v-card-text>
                        <v-layout wrap>
                            <v-flex md3>
                                <div style="margin-bottom: 7px">
                                    <strong>Nombre del paciente</strong>
                                    <div v-if="'paciente' in recepcion">{{ recepcion.paciente.nombre_completo }}</div>
                                </div>
                            </v-flex>
                            <v-flex md3>
                                <div style="margin-bottom: 7px">
                                    <strong>Identificación</strong>
                                    <div v-if="'paciente' in recepcion">{{ recepcion.paciente.cedula }}</div>
                                </div>
                            </v-flex>
                            <v-flex md3>
                                <div style="margin-bottom: 7px">
                                    <strong>Edad del paciente</strong>
                                    <div v-if="'paciente' in recepcion">{{ recepcion.paciente.edad + ' ' + recepcion.paciente.unidad_edad }}</div>
                                </div>
                            </v-flex>
                            <v-flex md3>
                                <div style="margin-bottom: 7px">
                                    <strong>Empresa cliente</strong>
                                    <div v-if="'paciente' in recepcion">{{ recepcion.empresa_cliente }}</div>
                                </div>
                            </v-flex>
                            <v-flex md3>
                                <div style="margin-bottom: 7px">
                                    <strong>Orden</strong>
                                    <div v-if="'paciente' in recepcion">{{ recepcion.id }}</div>
                                </div>
                            </v-flex>
                        </v-layout>
                    </v-card-text>
                    <v-card-text>
                        <v-layout wrap>
                            <v-flex md6 x12>
                                <v-checkbox label="Usa Lentes Correctivos?" v-model="lentes_correctivos"></v-checkbox>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-text-field label="Hace cuanto tiempo" v-model="hace_cuanto"></v-text-field>
                            </v-flex>
                        </v-layout>
                        <h3 class="title">Antecedentes Oftalmológicos</h3>
                        <v-layout wrap>
                            <v-flex md6 x12>
                                <v-text-field label="Cirugía" v-model="cirugia"></v-text-field>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-text-field label="Trauma Ocular" v-model="trauma_ocular"></v-text-field>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-text-field label="Pterigio" v-model="pterigio"></v-text-field>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-text-field label="Colores" v-model="colores"></v-text-field>
                            </v-flex>
                        </v-layout>
                        <v-layout wrap>
                            <div class="table__overflow">
                                <table class="table datatable examen-table">
                                    <thead>
                                        <tr>
                                            <th></th>
                                            <th>OD</th>
                                            <th>OI</th>
                                            <th>AO</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>Visión Lejana</td>
                                            <td><v-text-field label="" v-model="vision_lejana_od"></v-text-field></td>
                                            <td><v-text-field label="" v-model="vision_lejana_oi"></v-text-field></td>
                                            <td><v-text-field label="" v-model="vision_lejana_ao"></v-text-field></td>
                                        </tr>
                                        <tr>
                                            <td>Visión Cercana</td>
                                            <td><v-text-field label="" v-model="vision_cercana_od"></v-text-field></td>
                                            <td><v-text-field label="" v-model="vision_cercana_oi"></v-text-field></td>
                                            <td><v-text-field label="" v-model="vision_cercana_ao"></v-text-field></td>
                                        </tr>
                                        <tr>
                                            <td>AV</td>
                                            <td><v-text-field label="" v-model="av_od"></v-text-field></td>
                                            <td><v-text-field label="" v-model="av_oi"></v-text-field></td>
                                            <td><v-text-field label="" v-model="av_ao"></v-text-field></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </v-layout>
                        <br>
                        <h3 class="title">Refracción Final</h3>
                        <v-layout>
                            <div class="table__overflow">
                                <table class="table datatable examen-table">
                                    <thead>
                                        <tr>
                                            <th class="column"></th>
                                            <th class="column">ESF</th>
                                            <th class="column">CIL</th>
                                            <th class="column">EJE</th>
                                            <th class="column">ADD</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td class="text-xs-center">OJO DERECHO</td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="esf_od"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="cil_od"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="eje_od"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="add_od"></v-text-field></td>
                                        </tr>
                                        <tr>
                                            <td class="text-xs-center">OJO IZQUIERDO</td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="esf_oi"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="cil_oi"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="eje_oi"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="add_oi"></v-text-field></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </v-layout>
                        <v-layout>
                            <div class="table__overflow">
                                <table class="table datatable examen-table">
                                    <thead>
                                        <tr>
                                            <th class="column"></th>
                                            <th class="column">D.P</th>
                                            <th class="column">N.P</th>
                                            <th class="column">ALT</th>
                                            <th class="column">PRISMA</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td class="text-xs-center">OJO DERECHO</td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="dp_od"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="np_od"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="alt_od"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="prisma_od"></v-text-field></td>
                                        </tr>
                                        <tr>
                                            <td class="text-xs-center">OJO IZQUIERDO</td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="dp_oi"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="np_oi"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="alt_oi"></v-text-field></td>
                                            <td class="text-xs-center"><v-text-field label="" v-model="prisma_oi"></v-text-field></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </v-layout>
                        <br>
                        <v-layout wrap>
                            <v-flex md6 x12>
                                <v-text-field label="Foria" v-model="foria"></v-text-field>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-text-field label="Campimetría" v-model="campimetria"></v-text-field>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-text-field label="Recomendaciones" v-model="recomendaciones" multi-line></v-text-field>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-checkbox label="Remitir a Oftamología" v-model="remitir_oftamologia"></v-checkbox>
                            </v-flex>
                        </v-layout>
                    </v-card-text>
                    <v-card-actions>
                        <!-- <v-spacer></v-spacer> -->
                        <v-btn v-show="visiometria.estado !== 'RE'" flat outline success @click.native="submit">{{ 'id' in this.visiometria && this.visiometria.id ? 'Editar': 'Crear'}}</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
        <ig-fab v-show="'id' in visiometria && visiometria.id && visiometria.estado !== 'RE'">
            <v-btn
                class="pink"
                dark
                fab
                v-tooltip:left="{html: 'Cerrar'}"
                @click.native="cerrarPrueba"
            >
                <v-icon>save</v-icon>
            </v-btn>
        </ig-fab>
    </div>
</template>


<script>
import _ from 'underscore';

import Vue from 'vue/dist/vue.js';
import Vuetify from 'vuetify';
import VueResource from 'vue-resource';

import Fab from './../components/fab.vue';

import IgMixin from './../mixins/igmixin.js';

import URL from './../urls.js';

Vue.use(VueResource);
Vue.use(Vuetify);


export default {
    components: {
        igFab: Fab
    },
    watch: {
        '$route': 'fetchData',
    },
    mixins: [IgMixin],
    data: function () {
        return {
            selected: false,
            lentes_correctivos: false,
            hace_cuanto: '',
            cirugia: '',
            trauma_ocular: '',
            pterigio: '',
            colores: '',
            vision_lejana_od: '',
            vision_lejana_oi: '',
            vision_lejana_ao: '',
            vision_cercana_od: '',
            vision_cercana_oi: '',
            vision_cercana_ao: '',
            av_od: '',
            av_oi: '',
            av_ao: '',
            foria: '',
            campimetria: '',
            remitir_oftamologia: '',
            recomendaciones: '',
            esf_od: '',
            cil_od: '',
            eje_od: '',
            add_od: '',
            dp_od: '',
            np_od: '',
            alt_od: '',
            prisma_od: '',
            esf_oi: '',
            cil_oi: '',
            eje_oi: '',
            add_oi: '',
            dp_oi: '',
            np_oi: '',
            alt_oi: '',
            prisma_oi: '',
            recepcion: {},
            visiometria: {},
            OPCIONES_OJOS: [
                {
                    text: 'OJO DERECHO',
                    value: 'OD'
                },
                {
                    text: 'OJO IZQUIERDO',
                    value: 'OI'
                },
                {
                    text: 'AMBOS OJOS',
                    value: 'AO'
                }
            ]
        }
    },
    mounted: function () {
        this.fetchData();
    },
    methods: {
        fetchData () {
            const properties = [
                'lentes_correctivos', 'hace_cuanto', 'cirugia',
                'trauma_ocular', 'pterigio', 'colores', 'vision_lejana_od',
                'vision_lejana_oi', 'vision_lejana_ao', 'vision_cercana_od',
                'vision_cercana_oi', 'vision_cercana_ao', 'av_od', 'av_oi',
                'av_ao', 'foria', 'campimetria', 'remitir_oftamologia',
                'recomendaciones', 'esf_od', 'cil_od', 'eje_od', 'add_od',
                'dp_od', 'np_od', 'alt_od', 'prisma_od', 'esf_oi', 'cil_oi',
                'eje_oi', 'add_oi', 'dp_oi', 'np_oi', 'alt_oi', 'prisma_oi'
            ]
            this.$http.get(URL.visiometria.concat(this.$route.params.id.toString() + '/'))
                .then(response => {
                    this.recepcion = response.body.orden;
                    this.visiometria = response.body;

                    for (let property of properties) {
                        if (property in this.visiometria) {
                            this[property] = this.visiometria[property]
                        }
                    }
                }, response => {
                    if (response.status == 403) {
                       this.showSnackBar('No tienes permisos para estar en esta página.') 
                    } else {
                        this.showSnackBar('Hubo un error al momento de guardar los datos, recargue la página e intentelo de nuevo')
                    }
                })
        },
        cerrarPrueba () {
            this.submit({estado: 'RE'});
        },
        submit (payload = {}) {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];

            let { lentes_correctivos, hace_cuanto, cirugia,
                trauma_ocular, pterigio, colores, vision_lejana_od,
                vision_lejana_oi, vision_lejana_ao, vision_cercana_od,
                vision_cercana_oi, vision_cercana_ao, av_od, av_oi,
                av_ao, foria, campimetria, remitir_oftamologia,
                recomendaciones, esf_od, cil_od, eje_od, add_od,
                dp_od, np_od, alt_od, prisma_od, esf_oi, cil_oi,
                eje_oi, add_oi, dp_oi, np_oi, alt_oi, prisma_oi } = this;
            let data = {
                lentes_correctivos, hace_cuanto, cirugia,
                trauma_ocular, pterigio, colores, vision_lejana_od,
                vision_lejana_oi, vision_lejana_ao, vision_cercana_od,
                vision_cercana_oi, vision_cercana_ao, av_od, av_oi,
                av_ao, foria, campimetria, remitir_oftamologia,
                recomendaciones, esf_od, cil_od, eje_od, add_od,
                dp_od, np_od, alt_od, prisma_od, esf_oi, cil_oi,
                eje_oi, add_oi, dp_oi, np_oi, alt_oi, prisma_oi,
                orden: this.recepcion
            }
            let method = 'id' in this.visiometria && this.visiometria.id ? 'put': 'post';
            let url = URL.visiometria;
            if (method == 'put') {
                url += this.$route.params.id.toString() + '/'
            }

            data = Object.assign(data, payload);

            this.$http[method](url, data, {headers: {'X-CSRFToken': token.value}})
                .then(response => {
                    this.visiometria = response.body;
                    this.showSnackBar('Se ha guardado el resultado con exito')
                }, response => {
                    if (response.status == 403) {
                        this.showSnackBar('No tienes permisos para realizar esta acción.') 
                    } else {
                        this.showSnackBar('Hubo un error al momento de guardar los datos, recargue la página e intentelo de nuevo')
                    }
                });
        }
    }
}
</script>

<style>
table.table.examen-table {
    border-collapse: inherit;
}

table.table.examen-table tbody tr td .input-group {
    margin: 0;
}
</style>
