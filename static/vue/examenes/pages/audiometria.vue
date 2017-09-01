<template>
    <div>
        <v-layout>
            <v-breadcrumbs icons divider="forward">
                <v-breadcrumbs-item :disabled="false" href="/examenes/#/ordenes/audiometria/">
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
                        <h1 class="title">Formato "Certificado de aptitud auditiva"</h1>
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
                        <h3 class="title">Antecedentes De Exposición a Ruidos Historias Ocupacional</h3>
                        <v-layout wrap>
                            <v-flex md6>
                                <v-layout>
                                    <v-flex md6 x12>
                                        <v-text-field label="Tiempo Exposición" v-model="tiempo_exposicion"></v-text-field>
                                    </v-flex>
                                    <v-flex md6 x12>
                                        <v-text-field label="Frecuencia" v-model="frecuencia"></v-text-field>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                            <v-flex md6>
                                <v-layout>
                                    <v-flex md6 x12>
                                        <v-checkbox label="Protección Auditiva" v-model="proteccion_auditiva"></v-checkbox>
                                    </v-flex>
                                    <v-flex md6 x12>
                                        <v-text-field label="Tipo" v-model="tipo_proteccion"></v-text-field>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                        </v-layout>
                        <v-layout wrap>
                            <v-flex md6>
                                <div class="table__overflow">
                                    <table class="table datatable examen-table">
                                        <thead>
                                            <tr>
                                                <th>ANTECEDENTES EXTRA LABORAL</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td><v-checkbox label="Prestó servicio militar" v-model="servicio_militar"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Practica o practicaba polígono" v-model="practica_poligono"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Utiliza motocicleta" v-model="usa_motocicleta"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Ha estado cerca de explosiones" v-model="cerca_explociones"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Escucha música a alto volumen" v-model="musica_volumen"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Usa audifonos/walman" v-model="usa_audifonos"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Practica tejo, caza, entre otras" v-model="practica_tejo"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-text-field label="Otros" v-model="otros_antecedentes"></v-text-field></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </v-flex>
                            <v-flex md6>
                                <div class="table__overflow">
                                    <table class="table datatable examen-table">
                                        <thead>
                                            <tr>
                                                <th>ANTECEDENTES PATOLOGICOS</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <td><v-checkbox label="Cirugía de oído" v-model="cirugia_oido"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Trauma" v-model="trauma"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Medicamentos ototóxicos" v-model="medicamentos_ototoxicos"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Hipoacusia" v-model="hipoacusia"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Vértigo" v-model="vertigo"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Acufeno" v-model="acufeno"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Otitis" v-model="otitis"></v-checkbox></td>
                                            </tr>
                                            <tr>
                                                <td><v-checkbox label="Otorrea" v-model="otorrea"></v-checkbox></td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </v-flex>
                        </v-layout>
                        <br>
                        <v-layout wrap>
                            <v-flex md12>
                                <div class="table__overflow">
                                    <table class="table datatable examen-table">
                                        <thead>
                                            <tr>
                                                <th colspan="9">TAMIZAJE AUDITIVO</th>
                                            </tr>
                                            <tr>
                                                <th class="column">OIDO/FRECUENCIA</th>
                                                <th class="column">250HZ</th>
                                                <th class="column">500HZ</th></th>
                                                <th class="column">1000HZ</th>
                                                <th class="column">2000HZ</th>
                                                <th class="column">3000HZ</th>
                                                <th class="column">4000HZ</th>
                                                <th class="column">6000HZ</th>
                                                <th class="column">8000HZ</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr>
                                                <th class="text-xs-center">DERECHO</th>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz250_d"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz500_d"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz1000_d"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz2000_d"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz3000_d"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz4000_d"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz6000_d"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz8000_d"></v-text-field>
                                                </td>
                                            </tr>
                                            <tr>
                                                <th class="text-xs-center">IZQUIERDO</th>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz250_i"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz500_i"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz1000_i"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz2000_i"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz3000_i"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz4000_i"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz6000_i"></v-text-field>
                                                </td>
                                                <td class="text-xs-center">
                                                    <v-text-field label="" type="number" v-model="cphz8000_i"></v-text-field>
                                                </td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </v-flex>
                        </v-layout>
                        <v-layout wrap>
                            <v-flex md12>
                                <v-layout wrap>
                                    <v-flex md6>
                                        <div class="table__overflow">
                                            <table class="table datatable examen-table">
                                                <thead>
                                                    <tr>
                                                        <th colspan="2" class="column">OTOSCOPIA</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <th class="text-xs-center">OIDO DERECHO</th>
                                                        <td class="text-xs-center">
                                                            <v-text-field label="" v-model="otoscopia_od"></v-text-field>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th class="text-xs-center">OIDO IZQUIERDO</th>
                                                        <td class="text-xs-center">
                                                            <v-text-field label="" v-model="otoscopia_id"></v-text-field>
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </v-flex>
                                    <v-flex md6>
                                        <div class="table__overflow">
                                            <table class="table datatable examen-table">
                                                <thead>
                                                    <tr>
                                                        <th colspan="2" class="column">PROMEDIO AUDITIVO</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <th class="text-xs-center">OIDO DERECHO</th>
                                                        <td class="text-xs-center">
                                                            {{ od_avg }}
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th class="text-xs-center">OIDO IZQUIERDO</th>
                                                        <td class="text-xs-center">
                                                            {{ oi_avg }}
                                                        </td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </v-flex>
                                </v-layout>
                            </v-flex>
                        </v-layout>
                        <v-layout wrap>
                            <v-flex md6>
                                <chart-audiometria :chartData="chartDataCopy" :options="chartOptions"></chart-audiometria>
                            </v-flex>
                            <v-flex md6>
                                <chart-audiometria :chartData="chartData" :options="chartOptions"></chart-audiometria>
                                <v-spacer></v-spacer>
                                <v-btn v-show="'id' in audiometria && audiometria.id && audiometria.estado !== 'RE'" flat outline success @click.native="saveGraph">Guardar gráfico actual</v-btn>
                            </v-flex>
                        </v-layout>
                        <br>
                        <h3 class="title">RECOMENDACIONES</h3>
                        <v-layout wrap>
                            <v-flex md6 x12>
                                <v-checkbox label="Uso de protectores auditivos" v-model="uso_protectores_auditivos"></v-checkbox>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-checkbox label="Complementar con audiología clínica" v-model="complementar_audiometria_clinica"></v-checkbox>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-checkbox label="Control periódico" v-model="control_periodico"></v-checkbox>
                            </v-flex>
                            <v-flex md6 x12>
                                <v-text-field label="Otras" v-model="otras" multi-line></v-text-field>
                            </v-flex>
                        </v-layout>
                    </v-card-text>
                    <v-card-actions>
                        <!-- <v-spacer></v-spacer> -->
                        <v-btn v-show="audiometria.estado !== 'RE'" flat outline success @click.native="submit">{{ 'id' in this.audiometria && this.audiometria.id ? 'Editar': 'Crear'}}</v-btn>
                    </v-card-actions>
                </v-card>
            </v-flex>
        </v-layout>
        <ig-fab v-show="'id' in audiometria && audiometria.id && audiometria.estado !== 'RE'">
            <v-btn class="pink" dark fab v-tooltip:left="{html: 'Cerrar'}" @click.native="cerrarPrueba">
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
import ChartAudiometria from './../components/chart_audiometria';

import IgMixin from './../mixins/igmixin.js';

import URL from './../urls.js';

Vue.use(VueResource);
Vue.use(Vuetify);


export default {
    components: {
        igFab: Fab,
        chartAudiometria: ChartAudiometria
    },
    watch: {
        '$route': 'fetchData',
    },
    mixins: [IgMixin],
    data: function() {
        return {
            selected: false,
            tiempo_exposicion: '',
            frecuencia: '',
            proteccion_auditiva: false,
            tipo_proteccion: '',
            servicio_militar: false,
            practica_poligono: false,
            usa_motocicleta: false,
            cerca_explociones: false,
            musica_volumen: false,
            usa_audifonos: false,
            practica_tejo: false,
            otros_antecedentes: '',
            cirugia_oido: false,
            trauma: false,
            medicamentos_ototoxicos: false,
            hipoacusia: false,
            vertigo: false,
            acufeno: false,
            otitis: false,
            otorrea: false,
            hz250_d: '',
            hz500_d: '',
            hz1000_d: '',
            hz2000_d: '',
            hz3000_d: '',
            hz4000_d: '',
            hz6000_d: '',
            hz8000_d: '',
            hz250_i: '',
            hz500_i: '',
            hz1000_i: '',
            hz2000_i: '',
            hz3000_i: '',
            hz4000_i: '',
            hz6000_i: '',
            hz8000_i: '',
            cphz250_d: '',
            cphz500_d: '',
            cphz1000_d: '',
            cphz2000_d: '',
            cphz3000_d: '',
            cphz4000_d: '',
            cphz6000_d: '',
            cphz8000_d: '',
            cphz250_i: '',
            cphz500_i: '',
            cphz1000_i: '',
            cphz2000_i: '',
            cphz3000_i: '',
            cphz4000_i: '',
            cphz6000_i: '',
            cphz8000_i: '',
            otoscopia_od: '',
            otoscopia_id: '',
            uso_protectores_auditivos: false,
            complementar_audiometria_clinica: false,
            control_periodico: false,
            otras: '',
            recepcion: {},
            audiometria: {},
        }
    },
    computed: {
        chartData: function () {
            let data = {
                labels: ['250HZ', '500HZ', '1000HZ', '2000HZ', '3000HZ', '4000HZ', '6000HZ', '8000HZ'],
                datasets: [
                    {
                        label: 'Oído Derecho',
                        backgroundColor: 'rgba(239,29,26,0.5)',
                        borderColor: 'rgba(239,29,26,0.5)',
                        data: [
                            this.cphz250_d, this.cphz500_d, this.cphz1000_d, this.cphz2000_d, this.cphz3000_d,
                            this.cphz4000_d, this.cphz6000_d, this.cphz8000_d
                        ],
                        fill: false
                    },
                    {
                        label: 'Oído Izquierdo',
                        backgroundColor: 'rgba(26,114,239,0.5)',
                        borderColor: 'rgba(26,114,239,0.5)',
                        data: [
                            this.cphz250_i, this.cphz500_i, this.cphz1000_i, this.cphz2000_i, this.cphz3000_i,
                            this.cphz4000_i, this.cphz6000_i, this.cphz8000_i
                        ],
                        fill: false
                    }
                ],
            }
            return data;
        },
        chartDataCopy: function () {
            let data = {
                labels: ['250HZ', '500HZ', '1000HZ', '2000HZ', '3000HZ', '4000HZ', '6000HZ', '8000HZ'],
                datasets: [
                    {
                        label: 'Oído Derecho',
                        backgroundColor: 'rgba(239,29,26,0.5)',
                        data: [
                            this.hz250_d, this.hz500_d, this.hz1000_d, this.hz2000_d, this.hz3000_d,
                            this.hz4000_d, this.hz6000_d, this.hz8000_d
                        ],
                        fill: false
                    },
                    {
                        label: 'Oído Izquierdo',
                        backgroundColor: 'rgba(26,114,239,0.5)',
                        data: [
                            this.hz250_i, this.hz500_i, this.hz1000_i, this.hz2000_i, this.hz3000_i,
                            this.hz4000_i, this.hz6000_i, this.hz8000_i
                        ],
                        fill: false
                    }
                ],
            }
            return data;
        },
        chartOptions: function () {
            let data = {
                scales: {
                    yAxes: [{
                        ticks: {
                            // beginAtZero: true,
                            reverse: true
                        },
                        gridLines: {
                            display: true
                        },
                        fill: false
                    }],
                    xAxes: [{
                        gridLines: {
                            display: true
                        },
                        position: 'top'
                    }]
                },
                fill: false,
                legend: {
                    display: true
                },
                responsive: true,
                // maintainAspectRatio: false,
                elements: {
                    line: {
                        tension: 0
                    },
                }
            }
            return data;
        },
        oi_avg: function () {
            let list = [
                this.hz250_i, this.hz500_i, this.hz1000_i, this.hz2000_i,
                this.hz3000_i, this.hz4000_i, this.hz6000_i, this.hz8000_i
            ]
            return list.reduce((x, y) => x + y) / list.length
        },
        od_avg: function () {
            let list = [
                this.hz250_d, this.hz500_d, this.hz1000_d, this.hz2000_d,
                this.hz3000_d, this.hz4000_d, this.hz6000_d, this.hz8000_d
            ]
            return list.reduce((x, y) => x + y) / list.length
        }
    },
    mounted: function() {
        this.fetchData();
    },
    methods: {
        fetchData() {
            const properties = [
                'tiempo_exposicion', 'frecuencia', 'proteccion_auditiva', 'tipo_proteccion',
                'servicio_militar', 'practica_poligono', 'usa_motocicleta', 'cerca_explociones',
                'musica_volumen', 'usa_audifonos', 'practica_tejo', 'otros_antecedentes',
                'cirugia_oido', 'trauma', 'medicamentos_ototoxicos', 'hipoacusia', 'vertigo',
                'acufeno', 'otitis', 'otorrea', 'hz250_d', 'hz500_d', 'hz1000_d', 'hz2000_d',
                'hz3000_d', 'hz4000_d', 'hz6000_d', 'hz8000_d', 'hz250_i', 'hz500_i', 'hz1000_i',
                'hz2000_i', 'hz3000_i', 'hz4000_i', 'hz6000_i', 'hz8000_i', 'otoscopia_od',
                'otoscopia_oi', 'uso_protectores_auditivos', 'complementar_audiometria_clinica',
                'control_periodico', 'otras', 'audiometra', 'estado'
            ]
            this.$http.get(URL.audiometria.concat(this.$route.params.id.toString() + '/'))
                .then(response => {
                    this.recepcion = response.body.orden;
                    this.audiometria = response.body;

                    for (let property of properties) {
                        if (property in this.audiometria) {
                            this[property] = this.audiometria[property]
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
        cerrarPrueba() {
            this.submit({ estado: 'RE' });
        },
        submit(payload = {}) {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];

            let { tiempo_exposicion, frecuencia, proteccion_auditiva, tipo_proteccion,
                servicio_militar, practica_poligono, usa_motocicleta, cerca_explociones,
                musica_volumen, usa_audifonos, practica_tejo, otros_antecedentes,
                cirugia_oido, trauma, medicamentos_ototoxicos, hipoacusia, vertigo,
                acufeno, otitis, otorrea, hz250_d, hz500_d, hz1000_d, hz2000_d,
                hz3000_d, hz4000_d, hz6000_d, hz8000_d, hz250_i, hz500_i, hz1000_i,
                hz2000_i, hz3000_i, hz4000_i, hz6000_i, hz8000_i, otoscopia_od,
                otoscopia_oi, uso_protectores_auditivos, complementar_audiometria_clinica,
                control_periodico, otras, audiometra } = this;
            let data = {
                tiempo_exposicion, frecuencia, proteccion_auditiva, tipo_proteccion,
                servicio_militar, practica_poligono, usa_motocicleta, cerca_explociones,
                musica_volumen, usa_audifonos, practica_tejo, otros_antecedentes,
                cirugia_oido, trauma, medicamentos_ototoxicos, hipoacusia, vertigo,
                acufeno, otitis, otorrea, hz250_d, hz500_d, hz1000_d, hz2000_d,
                hz3000_d, hz4000_d, hz6000_d, hz8000_d, hz250_i, hz500_i, hz1000_i,
                hz2000_i, hz3000_i, hz4000_i, hz6000_i, hz8000_i, otoscopia_od,
                otoscopia_oi, uso_protectores_auditivos, complementar_audiometria_clinica,
                control_periodico, otras, audiometra, orden: this.recepcion
            }
            let method = 'id' in this.audiometria && this.audiometria.id ? 'put' : 'post';
            let url = URL.audiometria;
            if (method == 'put') {
                url += this.$route.params.id.toString() + '/'
            }

            data = Object.assign(data, payload);

            this.$http[method](url, data, { headers: { 'X-CSRFToken': token.value } })
                .then(response => {
                    this.audiometria = response.body;
                    this.showSnackBar('Se ha guardado el resultado con exito')
                }, response => {
                    if (response.status == 403) {
                        this.showSnackBar('No tienes permisos para realizar esta acción.')
                    } else {
                        this.showSnackBar('Hubo un error al momento de guardar los datos, recargue la página e intentelo de nuevo')
                    }
                });
        },
        saveGraph() {
            let list = [
                'hz250_d', 'hz500_d', 'hz1000_d', 'hz2000_d',
                'hz3000_d', 'hz4000_d', 'hz6000_d', 'hz8000_d',
                'hz250_i', 'hz500_i', 'hz1000_i', 'hz2000_i',
                'hz3000_i', 'hz4000_i', 'hz6000_i', 'hz8000_i'
            ]

            for (let attr of list) {
                let prop = 'cp'.concat(attr);
                this[attr] = this[prop];
                this[prop] = 0
            }
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
