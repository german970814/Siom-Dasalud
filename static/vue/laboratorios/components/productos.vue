<template lang="html">

</template>

<script>
import Vue from 'vue/dist/vue.js';
import VueResource from 'vue-resource';
import _ from 'underscore';
import URL from './../urls.js';

Vue.use(VueResource);

export default {
    props: {
        plantillas: {
            required: true
        },
        laboratorio: {},
        area: {},
        tipo: {
          default: 'i',
        },
        filter: false,
    },
    watch: {
        plantillas: function () {
            this.self_plantillas = this.plantillas;
        },
        cantidad: function () {
            if (this.cantidad < 0) {
                this.cantidad = 0;
            }
        }
    },
    computed: {
        url: function () {
            if (_.isEmpty(this.laboratorio) && !_.isEmpty(this.area)) {
                return URL.plantillaArea;
            } else if (_.isEmpty(this.area) && !_.isEmpty(this.laboratorio)) {
                return URL.plantillaLaboratorio;
            }
            return false;
        }
    },
    mounted: function () {
        this._fetchProductos();
    },
    data: function () {
        return {
            productos: [],
            cantidad: 1,
            producto: {},
            self_plantillas: [],
            selected: {}
        }
    },
    methods: {
        addPlantilla () {
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            if (this.cantidad > 0 && !_.isEmpty(this.producto)) {
                let exists = this.self_plantillas.find(x => {
                    return x.producto.nombre.toLowerCase() == this.producto.nombre.toLowerCase()
                });
                if (exists) {
                    if (this.url) {
                        this.$http.put(this.url.concat(exists.id.toString() + '/'), {cantidad: this.cantidad, producto: this.producto, area: this.area, laboratorio: this.laboratorio}, {headers: {'X-CSRFToken': token.value}})
                          .then(response => {
                              exists.cantidad = this.cantidad;
                          })
                    } else {
                        exists.cantidad = this.cantidad;
                    }
                } else {
                    if (this.url) {
                        this.$http.post(this.url, {cantidad: this.cantidad, producto: this.producto, area: this.area, laboratorio: this.laboratorio}, {headers: {'X-CSRFToken': token.value}})
                          .then(response => {
                              this.self_plantillas.push({
                                  cantidad: this.cantidad,
                                  producto: this.producto,
                                  laboratorio: this.laboratorio,
                                  area: this.area,
                                  id: response.body.id,
                                  model: true,
                              })
                          }, response => {

                          })
                    } else {
                        this.self_plantillas.push({
                            cantidad: this.cantidad,
                            producto: this.producto,
                            laboratorio: this.laboratorio,
                            area: this.area,
                            model: true,
                        })
                    }
                }
            }
        },
        _fetchProductos () {
            this.$http.get(URL.reactivos.concat(`?tipo=${this.tipo.toUpperCase()}`))
              .then(response => {
                  this.productos = response.body;
              }, response => {

              })
        },
        _renderPresentation () {
            let childs = [];
            for (let plantilla of this.self_plantillas) {
                childs.push(
                    this.$createElement('v-chip', {
                        props: {close: Boolean(this.url)},
                        domProps: {
                            value: plantilla.model,
                        },
                        on: {
                            input: (event) => {
                                this.$emit('input', event);
                                // plantilla.model = event;
                                if (!event) {
                                    let token = document.getElementsByName('csrfmiddlewaretoken')[0];
                                    let item = this.self_plantillas.find(x => {return x.producto.nombre.toLowerCase() == plantilla.producto.nombre.toLowerCase()});
                                    if (item && this.url) {
                                        this.$http.delete(this.url.concat(item.id.toString() + '/'), {headers: {'X-CSRFToken': token.value}})
                                          .then(response => {
                                              this.self_plantillas.splice(this.self_plantillas.indexOf(item), 1);
                                          }, response => {

                                          })
                                    } else {
                                        // item.model = event;
                                        this.self_plantillas.splice(this.self_plantillas.indexOf(item), 1);
                                    }
                                }
                            }
                        },
                        nativeOn: {
                            click: ($event) => {
                                $event.stopPropagation();
                            }
                        }
                    }, [
                        this.$createElement('v-avatar', {'class': 'teal'}, [plantilla.cantidad.toString()]),
                        plantilla.producto.nombre.toUpperCase()
                    ])
                )
            }
            return this.$createElement('v-container', [...childs])
        },
        _renderCreation () {
            let childs = [];
            childs.push(
                this.$createElement('v-flex', {attrs: {'md4': true, 'xs12': true}}, [
                    this.$createElement(
                        'v-text-field', {
                            props: {
                                label: 'Cantidad',
                                hint: '',  // 'Cantidad de unidades usadas por producto.',
                                required: true,
                                type: 'number',
                                // rules: this.getRules(field),
                            },
                            domProps: {value: this.cantidad},
                            on: {
                                input: (event) => {
                                    this.cantidad = event;
                                    this.$emit('input', event);
                                },
                                blur: (event) => {
                                    // this.cantidad = event
                                }
                            },
                        }, []
                    )
                ])
            );
            childs.push(
                this.$createElement('v-flex', {attrs: {'md6': true, 'xs12': true}}, [
                    this.$createElement(
                        'v-select', {
                            props: {
                                label: 'Producto',
                                hint: '',
                                required: true,
                                items: this.productos,
                                itemText: 'nombre'
                            },
                            domProps: {value: this.producto},
                            on: {
                                input: (event) => {
                                    this.$emit('input', event);
                                    this.producto = event;
                                },
                                blur: (event) => {
                                    // this.producto = event;
                                }
                            },
                        }, []
                    )
                ])
            );
            childs.push(
                this.$createElement('v-flex', {attrs: {'md2': true, 'xs12': true}}, [
                    this.$createElement('v-btn', {
                        props: {icon: true},
                        'class': 'green--text',
                        nativeOn: {
                            click: () => {
                                this.addPlantilla();
                                // console.log(this.self_plantillas)
                            }
                        }
                    }, [
                        this.$createElement('v-icon', ['save'])
                    ])
                ])
            );

            return this.$createElement('v-container', [
                this.$createElement('v-layout', [
                    ...childs
                ])
            ])
        }
    },
    render () {
        return this.$createElement('v-card', {props: {flat: true}, 'class': 'productos'}, [
            this._renderCreation(),
            this._renderPresentation()
        ])
    }
}
</script>

<style lang="css">
.productos .container {
  padding: 0;
}
</style>
