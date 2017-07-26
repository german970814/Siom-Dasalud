<template lang="html">
    <div class="">
        <v-layout>
            <v-breadcrumbs icons divider="forward">
                <v-breadcrumbs-item :disabled="false" href="/laboratorios/#/ordenes_laboratorios/">
                    Lista ordenes
                </v-breadcrumbs-item>
                <v-breadcrumbs-item :disabled="true">
                    Resultado
                </v-breadcrumbs-item>
            </v-breadcrumbs>
        </v-layout>
        <div v-if="items.length">
            <v-tabs
                id="tabs"
                grow scroll-bars
                v-model="tab"
                dark>
                <v-tabs-bar slot="activators">
                    <v-tabs-item
                        class="cyan darken-2"
                        v-for="(item, id) of items" :key="id"
                        :href="'#tabs-' + id"
                        :id="'tabItem-' + id"
                        ripple>
                        {{ item.laboratorio.nombre }}
                    </v-tabs-item>
                    <v-tabs-slider class="cyan accent-4"></v-tabs-slider>
                </v-tabs-bar>
                <v-tabs-content
                    v-for="(item, id) of items" :key="id" :id="'tabs-' + id">
                    <v-card flat>
                        <v-card-title>
                        </v-card-title>
                        <v-card-text class="grey lighten-5">
                            <formulario-resultado
                              @input="error = hasError()"
                              @empty="toggleClass($event, id)"
                              :gender="orden.paciente.genero"
                              :value="{item, items: 'formato' in item ? item.formato: item.resultado}"
                              :disabled="formDisabled(item)"
                              >
                            </formulario-resultado>
                        </v-card-text>
                        <v-card-actions v-if="'resultado' in item ? !item.resultado.cerrado: true">
                            <v-spacer></v-spacer>
                            <v-btn
                                :class="{'green--text': !someError(item), 'red--text': someError(item), 'darken-1': true}"
                                flat
                                @click.native="someError(item) ? () => undefined: saveItem(item)">
                                Guardar
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                </v-tabs-content>
            </v-tabs>
            <v-layout></v-layout>
            <v-dialog v-model="dialog" width="80%">
                <v-card>
                    <v-card-title>Seguro que quiere finalizar esta prueba de laboratorio?</v-card-title>
                    <v-card-text>Al finalizar la prueba, se mostrará adecuadamente la firma de el bacteriologo en el resultado de la prueba.</v-card-text>
                    <v-card-text>
                        <v-layout>
                            <v-flex md6 xs12>
                                <v-subheader>Insumos</v-subheader>
                                <ig-producto :plantillas="plantillas_insumos" tipo="i"></ig-producto>
                            </v-flex>
                            <v-flex md6 xs12>
                                <v-subheader>Reactivos</v-subheader>
                                <ig-producto :plantillas="plantillas_reactivos" tipo="r"></ig-producto>
                            </v-flex>
                        </v-layout>
                    </v-card-text>
                    <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn class="green--text darken-1" flat="flat" @click.native="cerrarPrueba">Aceptar</v-btn>
                        <v-btn class="green--text darken-1" flat="flat" @click.native="dialog = false">Cancelar</v-btn>
                    </v-card-actions>
                </v-card>
            </v-dialog>
            <v-dialog v-model="preview" fullscreen transition="v-dialog-bottom-transition" :overlay="false">
                <v-card>
                    <v-toolbar class="cyan darken-4">
                        <v-btn icon="icon" @click.native="preview = false">
                            <v-icon class="white--text">close</v-icon>
                        </v-btn>
                        <v-toolbar-title class="white--text">Previsualización</v-toolbar-title>
                        <v-spacer></v-spacer>
                        <!-- <a class="white--text btn btn--dark btn--flat" :href="url_impresion">
                            <span class="btn__content">Imprimir</span>
                        </a> -->
                    </v-toolbar>
                    <v-container>
                        <div class="wrap__all" v-if="!contentLoaded">
                            <div class="preloader">
                                <v-progress-circular indeterminate class="blue--text" :size="50"></v-progress-circular>
                            </div>
                        </div>
                        <!-- <canvas id="the-canvas" style="border: 1px solid black"></canvas> -->
                        <object id="object-visor" width="100%" height="800px" :data="url_impresion" type="application/pdf"></object>
                    </v-container>
                </v-card>
            </v-dialog>
        </div>
        <v-container v-else>
           <!-- <h5>403 Forbidden</h5>
           <br> -->
           <p>Es posible que si no logras visualizar nada, no tengas permisos necesarios para acceder aquí.</p>
        </v-container>
        <floating-button v-if="items.length">
            <template slot="child">
                <v-btn fab dark info small @click.native.stop="showModalCerrarPrueba" v-tooltip:left="{html: 'Cerrar Prueba'}">
                    <v-icon dark>check</v-icon>
                </v-btn>
                <v-btn fab dark warning small @click.native.stop="showSingleResult" v-tooltip:left="{html: 'Imprimir individual'}">
                    <v-icon dark>fingerprint</v-icon>
                </v-btn>
                <v-btn fab dark success small @click.native.stop="showAllResults" v-tooltip:left="{html: 'Imprimir terminados'}">
                    <v-icon dark>print</v-icon>
                </v-btn>
            </template>
            <v-btn fab dark error v-tooltip:left="{html: Boolean(error) ? 'Aun hay errores': 'Opciones'}">
                <v-icon dark>settings</v-icon>
            </v-btn>
        </floating-button>
    </div>
</template>

<script>
import _ from 'underscore';

import Vue from 'vue/dist/vue.js';

import FormularioResultado from './../components/formulario-resultado.vue';
import FloattingButton from './../components/floating-button.vue';
import ProductoComponent from './../components/productos.vue';
// import FormComponent from './../components/form.vue';
import ErrorMixin from './../mixins/errormixin.js';

import URL from './../urls.js';

export default {
    components: {
        formularioResultado: FormularioResultado,
        floatingButton: FloattingButton,
        igProducto: ProductoComponent,
    },
    mixins: [ErrorMixin],
    created: function () {
        this._fetchData();
        this.error = this.hasError();
    },
    mounted: function () {
        setTimeout(() => {
            this.tab = 'tabs-0'
        }, 1000)
    },
    computed: {
        selected_tab: function () {
            let sub = this.tab.substring(this.tab.length, this.tab.length - 1);
            return sub;
        }
    },
    data: function () {
        return {
          items: [],
          error: true,
          tab: null,
          orden: '',
          bacteriologo: '',
          preview: false,
          dialog: false,
          contentLoaded: true,
          url_impresion: '',
          plantillas_insumos: [],
          plantillas_reactivos: []
        }
    },
    watch: {
        '$route': '_fetchData',
        tab: function () {
        },
        preview: function () {
        },
        dialog: function () {
            if (this.dialog) {
                let laboratorio = this.items[parseInt(this.selected_tab)];
                this.$http.get(URL.plantillasOrdenes.concat(this.$route.params.id.toString() + `/${laboratorio.laboratorio.id.toString()}/?tipo=R`))
                  .then(response => {
                      this.plantillas_reactivos = response.body;
                  }, response => {
                    console.error(response);
                  })
            }
        }
    },
    props: {

    },
    methods: {
        toggleClass: function (event, id) {
            let element = document.getElementById('tabItem-'.concat(id));
            if (event) {
                element.classList.add('yellow');
                element.classList.remove('cyan');
            } else {
                element.classList.add('cyan');
                element.classList.remove('yellow');
            }
        },
        showModalCerrarPrueba: function () {
            let actualItem = this.items[parseInt(this.selected_tab)];
            if (!('cerrado' in actualItem && actualItem.cerrado)) {
                this.dialog = true;
            } else {
                this.$emit('mostrarsnackbar', 'La prueba actual ya se encuentra cerrada')
            }
        },
        cerrarPrueba: function () {
            let laboratorio = this.items[parseInt(this.selected_tab)];
            laboratorio.cerrado = true;
            this.saveItem(laboratorio);
            this.dialog = false;
        },
        showSingleResult: function (event) {
            let sub = this.tab.substring(this.tab.length, this.tab.length - 1);
            let laboratorio = this.items[parseInt(sub)];
            if ('resultado' in laboratorio) {
                return this.showAllResults(event, `&laboratorio=${laboratorio.id}`);
            }
            this.$emit('mostrarsnackbar', 'No se puede imprimir el laboratorio sin resultado.');
        },
        showAllResults: function (event, add = '') {
            let validated = false;
            for (var item of this.items) {
                if ('resultado' in item) {
                    validated = true;
                    break;
                }
            }

            if (validated) {
                this.preview = true;
                this.contentLoaded = true;
                var url = `/laboratorios/imprimir/${this.orden.id}/?inline=true` + add;
                this.url_impresion = url;
                let visor = document.getElementById('object-visor');
                // PDFJS.workerSrc = '/static/js/pdfjs/pdf.worker.js';

                // var loadingTask = PDFJS.getDocument(url);

                // loadingTask.promise.then((pdf) => {
                //     // Fetch the first page
                //     var pageNumber = 1;
                //     pdf.getPage(pageNumber).then((page) => {
                //         var scale = 1.5;
                //         var viewport = page.getViewport(scale);
                //         // Prepare canvas using PDF page dimensions
                //         var canvas = document.getElementById('the-canvas');
                //         var context = canvas.getContext('2d');

                //         canvas.height = viewport.height;
                //         canvas.width = viewport.width;

                //         // Render PDF page into canvas context
                //         var renderContext = {
                //             canvasContext: context,
                //             viewport: viewport
                //         };
                //         var renderTask = page.render(renderContext);
                //         renderTask.then(() => {
                //             this.contentLoaded = true;
                //         });
                //     });
                // }, function (reason) {
                //     // PDF loading error
                //     console.error(reason);
                // });
            } else {
                this.$emit('mostrarsnackbar', 'No hay resultados para imprimir');
                return undefined;
            }
        },
        formDisabled: function (item) {
            let areas = this.bacteriologo.areas.map(x => {return x.id});
            let laboratorio = item.laboratorio.seccion_trabajo.id;

            if ('resultado' in item) {
                if (item.cerrado) {
                    return true;
                }
                return areas.indexOf(laboratorio) == -1;
            }
            return areas.indexOf(laboratorio) == -1;
        },
        someError: function (item) {
            let formato = 'formato' in item ? item.formato: item.resultado;
            for (let field of formato) {
                if (this.hasError(field)) {
                    return true;
                }
            }
            return false;
        },
        genValidationsForItem: function (item) {
            let formato = 'formato' in item ? item.formato: item.resultado;
            for (let field of formato) {
                this.addValidation({
                    target: field,
                    validations: [
                        // i => ['select', 'radio', 'textarea', 'text'].indexOf(i.tipo.name) !== -1 ? i.model_text !== '': true,
                        // i => ['checkbox'].indexOf(i.tipo.name) !== -1 ? i.model_check.length > 1: true,
                    ]
                })
            }
        },
        _fetchData: function () {
            this.$http.get(URL.resultados.concat(this.$route.params.id.toString() + '/'))
              .then(response => {
                  this.items = [];
                  if ('resultados' in response.body && response.body.resultados) {
                      this.items.push.apply(this.items, response.body.resultados);
                      for (let items of response.body.resultados) {
                          // this.items(items)
                          this.genValidationsForItem(items);
                      }
                  }
                  if ('formatos' in response.body && response.body.formatos) {
                      this.items.push.apply(this.items, response.body.formatos)
                      for (let items of response.body.formatos) {
                          // this.items(items)
                          this.genValidationsForItem(items);
                      }
                  }
                  this.orden = response.body.orden;
                  this.bacteriologo = response.body.bacteriologo;
              }, response => {
                  console.error(response);
              })
        },
        saveItem: function (item, showsnack = true) {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            let data = {
                laboratorio: item.laboratorio,
                orden: {id: this.$route.params.id},
                resultado: JSON.stringify('formato' in item ? item.formato: item.resultado),
                cerrado: 'cerrado' in item ? item.cerrado : false
            };
            let productos = [];
            if ('resultado' in item) {
                data.id = item.id;
            }
            let error;

            if ('cerrado' in item && item.cerrado) {
                productos.push.apply(productos, this.plantillas_insumos);
                productos.push.apply(productos, this.plantillas_reactivos);
            }

            if (!this.someError(item)) {
                // console.log(item)
                this.$http.post(URL.resultados.concat(this.$route.params.id.toString() + '/'), {resultado: data, productos: productos}, {headers: {'X-CSRFToken': token.value}})
                    .then(response => {
                        if (showsnack) {
                            this.$emit('mostrarsnackbar', 'Se ha guardado el resultado de el laboratorio '.concat(item.laboratorio.nombre.toString()));
                            error = false;
                        }
                        if (!('resultado' in item)) {
                            item.resultado = item.formato;
                            // Vue.set(this.items, 'resultado', item.formato);
                            delete item['formato'];
                        }
                        item.id = response.body.id;
                    }, response => {
                        if (showsnack) {
                            this.$emit('mostrarsnackbar', 'Ha ocurrido un error al guardar el resultado');
                            error = true;
                        }
                    })
            } else {
                error = true;
                if (showsnack) {
                    this.$emit('mostrarsnackbar', 'No se puede guardar el resultado con campos vacios')
                }
            }
            if (error) {
              return error
            }
        },
        saveAll: function () {
            if (this.error) {
                return undefined;
            } else {
                let error;
                for (let item of this.items) {
                    error = this.saveItem(item, false);
                    if (error) {
                        this.$emit('mostrarsnackbar', 'Ha ocurrido un error al guardar los resultados.');
                        break;
                    }
                }
                if (!error) {
                    this.$emit('mostrarsnackbar', 'Se han guardado los resultados con exito.')
                }
            }
        }
    }
}
</script>

<style lang="css">
</style>
