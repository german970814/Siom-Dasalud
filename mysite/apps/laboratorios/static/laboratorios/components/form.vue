<template lang="html">
    <v-card>
        <v-card-title>
            <!-- <span>{[ selected ? 'Editar Laboratorio '.concat(codigo.toUpperCase()): 'Crear Laboratorio' ]}</span> -->
            <v-spacer></v-spacer>
            <v-btn flat @click.native="cleanFields()" v-show="selected"><v-icon>clear_all</v-icon>Limpiar</v-btn>
        </v-card-title>
        <v-card-text>
          <br>
            <v-container>
                <!--<template v-for="f in fields.length">-->
                    <v-row>
                        <v-col md6 xs12 v-for="field in fields" :key="field.name">
                            <template v-if="field.type == String"><!---->
                                <v-text-field
                                :label="field.verbose_name || ''"
                                :hint="field.hint || ''"
                                :required="fieldIsRequired(field)"
                                :rules="getRules(field)"
                                v-model="models[field.name]"
                                ></v-text-field>
                            </template>
                            <template v-else>
                                <v-select
                                :label="field.verbose_name || ''"
                                :hint="field.hint || ''"
                                :items="items[field.name]"
                                :required="fieldIsRequired(field)"
                                :rules="getRules(field)"
                                v-model="models[field.name]"
                                item-value="text"
                                light
                                ></v-select>
                            </template>
                        </v-col>
                    </v-row>
                <!--</template>-->
            </v-container>
            <small>* Campos requeridos.</small>
            <br>
        </v-card-text>
        <v-card-row actions>
            <v-btn flat @click.native="submitForm()">
                {{ !selected ? 'Crear': 'Editar' }}
                <v-icon>check_circle</v-icon>
            </v-btn>
        </v-card-row>
    </v-card>
</template>

<script>
import Vue from 'vue/dist/vue.js';
import VueResource from 'vue-resource';
import _ from 'underscore';

Vue.use(VueResource);

export default {
    name: 'igForm',
    props: {
        fields: {
            type: Array,
            required: true
        },
        url: {
            type: String,
            required: true
        },
        selected: {}
    },
    created: function () {
        this._getFetchData();
    },
    data: function () {
        return {
            models: {},
            items: {},
            _validated: false
        }
    },
    watch: {
        selected: function () {
            if (this.selected) {
                for (let attr in this.selected) {
                    if (attr in this.models) {  // si esta en los campos
                        if (attr in this.items) {  // si esta en los items que ya fueron fetched
                            let key;
                            for (let obj of this.items[attr]) {
                                if (obj.id == this.selected[attr].id) {
                                    key = obj;
                                    break;
                                }
                            }
                            if (key) {
                                this.models[attr] = key;
                            } else {
                                this.$emit('showsnack', 'No se encuentra el ' + attr.toString() + ' deseado.');
                            }
                        } else {
                            this.models[attr] = this.selected[attr];
                        }
                    }
                }
            }
        }
    },
    methods: {
        cleanFields: function () {
            for (let field of this.fields) {
                this.models[field.name] = '';
            }
            // this.selected = false;
            this.$emit('clearselected');
            this._validated = false;
        },
        fieldIsRequired: function (field) {
            return field.required === undefined || field.required;
        },
        _getFetchData: function () {
            for (let field of this.fields) {
                if ('url' in field) {
                    Vue.set(this.items, field.name, []);  // Se setean las propiedades de acuerdo a la documentacion, de forma reactiva
                    this.$http.get(field.url)
                        .then(response => {
                          for (let _item of response.body) {
                            _item.text = _item[field.key];
                            this.items[field.name].push(_item);
                          }
                        }, response => {
                            if ('detail' in response.body) {
                                this.snackbarText = response.body.detail;
                                this.snackbar = true;
                            } else {
                                this.snackbarText = 'Han ocurrido errores';
                                this.snackbar = true
                            }
                        });
                }
                Vue.set(this.models, field.name, field.type == String ? '': {});
            }
        },
        getRules: function (field) {
            let rules = new Array();
            if ('rules' in field) {
                let customRules = field.rules();
                if (typeof customRules === 'boolean' || typeof customRules === 'string') {
                    rules.push(customRules);
                } else {
                    for (let rule of customRules) {
                        rules.push(rule);
                    }
                }
            } else {
                if (this.fieldIsRequired(field)) {
                    rules.push(!this._validated || !_.isEmpty(this.models[field.name]) || 'Este campo es obligatorio');
                }
            }
            return rules
        },
        submitForm: function () {
            this._validated = true;
            let url = this.url;
            let method = 'post';
            let message;
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            console.log(this.models);
            if (this.selected) {
                url += this.selected.id + '/';
                method = 'put';
            }
            console.log(this.models);
            this.$http[method](url, this.models, {headers: {'X-CSRFToken': token.value}})
                .then(response => {
                    if (response.status == 201) {
                        // this.selected_before = response.body;
                        // this.laboratorios.push(this.selected_before);
                        message = 'Laboratorio Creado Correctamente';
                        this.$emit('objectcreated', response.body);
                    } else {
                        message = 'Laboratorio Editado Correctamente';
                    }
                    if (message) {
                        this.$emit('showsnack', message);
                    }
                }, response => {
                    if (response.status == 400) {
                        message = 'Han ocurrido Errores';
                        for (let res in response.body) {

                        }
                    } else if ('detail' in response.body) {
                        message = response.body.detail;
                    } else {
                        console.error(response);
                    }
                    if (message) {
                        this.$emit('showsnack', message);
                    }
                });
        }
    }
}
</script>

<style lang="css">
</style>
