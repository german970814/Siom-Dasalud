<template lang="html">
    <div v-if="formato">
        <v-layout>
            <h1 class="title">Formato para el Laboratorio <strong>{{ formato.laboratorio.nombre.toUpperCase() }}({{ formato.laboratorio.codigo.toUpperCase() }})</strong></h1>
        </v-layout>
        <v-layout wrap>
            <v-flex md6 class="mb-5" v-for="(item, id) of items" :key="id">
                <v-expansion-panel expand class="white">
                    <v-expansion-panel-content>
                        <div slot="header">{{ item.nombre }}</div>
                        <v-card>
                            <v-card-title>
                            </v-card-title>
                            <v-card-text class="grey lighten-5">
                                <v-alert error hide-icon :value="['checkbox', 'radio'].indexOf(item.tipo.name) !== -1 && item.choices.length <= 1">
                                    Asegurate de crear varias opciones.
                                </v-alert>
                                <v-select
                                    label="Tipo"
                                    :hint="item.tipo.help"
                                    :items="tipoOpciones"
                                    v-model="item.tipo"
                                    item-value="text"
                                    :rules="[item.tipo !== '' || 'Este campo es obligatorio']"
                                    required
                                    return-object
                                    persistent-hint
                                    dark
                                ></v-select>
                                <br>
                                <v-text-field
                                    label="Nombre del Campo"
                                    v-model="item.nombre"
                                    hint="Con este nombre se identificará el campo"
                                    :rules="[item.nombre !== '' || 'Este campo es obligatorio']"
                                    required
                                ></v-text-field>
                                <br>
                                <v-text-field
                                    label="Texto de ayuda"
                                    v-model="item.help"
                                    hint="Ayuda textual que acompaña el campo"
                                ></v-text-field>
                                <br>
                                <v-text-field
                                    label="Valores de referencia"
                                    v-model="item.referencia"
                                    hint="Texto de referencia para el momento de poner el resultado"
                                ></v-text-field>
                                <br>
                                <v-text-field
                                    label="Unidades"
                                    v-model="item.unidades"
                                    hint="Medida en unidades de el resultado"
                                ></v-text-field>
                                <br>
                                <v-text-field
                                    v-if="item.tipo.name == 'text' || item.tipo.name == 'textarea'"
                                    :multi-line="item.tipo.name == 'textarea'"
                                    :label="item.nombre"
                                    :hint="item.help"
                                    v-model="item.model_text"
                                    persistent-hint
                                ></v-text-field>
                                <div v-else-if="item.tipo.name == 'select'">
                                    <v-layout>
                                        <v-flex md10 xs10>
                                            <v-select
                                                :label="item.nombre"
                                                :hint="item.help"
                                                v-model="item.model_text"
                                                :items="item.choices_select"
                                                :rules="[item.choices_select.length >= 1 || 'Debes escoger una caracteristica', item.choices_select.length == 1 ? 'Asegurate que la caracteristica tenga varias especificaciones': true]"
                                                item-value="text"
                                                persistent-hint
                                            ></v-select>
                                        </v-flex>
                                        <v-flex md2 xs2>
                                            <v-btn
                                                v-tooltip:top="{html: 'Agregar Opciones'}"
                                                class="green--text darken-1" icon="icon"
                                                @click.native.stop="dialog = true; lastItem = item">
                                                <v-icon>add</v-icon>
                                            </v-btn>
                                        </v-flex>
                                    </v-layout>
                                </div>
                                <div v-else-if="item.tipo.name == 'checkbox'">
                                    <v-layout v-for="(choice, choiceId) of item.choices" :key="choiceId">
                                        <v-flex xs7 md7>
                                            <v-checkbox
                                              v-if="!choice.edit"
                                              :label="choice.name"
                                              v-model="item.model_check"
                                              :value="choice.id"
                                              primary
                                            ></v-checkbox>
                                            <v-text-field
                                              v-else
                                              label="Texto para mostrar"
                                              v-model="choice.name"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs5 md5>
                                          <v-btn v-tooltip:top="{html: 'Editar opción'}" icon="icon" class="indigo--text" @click.native="toggleValueEditCheckBox(choice)">
                                              <v-icon>mode_edit</v-icon>
                                          </v-btn>
                                          <v-btn v-tooltip:top="{html: 'Remover opción'}" icon="icon" class="red--text" @click.native="deleteChoiceItem(item, choiceId)" v-show="item.choices.length != 1">
                                              <v-icon>delete</v-icon>
                                          </v-btn>
                                          <v-btn v-tooltip:top="{html: 'Agregar opción'}" icon="icon" class="yellow--text" @click.native="addChoiceItem(item)" v-show="choiceId == item.choices.length - 1">
                                              <v-icon>add</v-icon>
                                          </v-btn>
                                        </v-flex>
                                    </v-layout>
                                </div>
                                <div v-else-if="item.tipo.name == 'radio'">
                                    <v-layout v-for="(choice, choiceId) of item.choices" :key="choiceId">
                                        <v-flex xs7 md7>
                                            <v-radio
                                              v-if="!choice.edit"
                                              :label="choice.name"
                                              v-model="item.model_text"
                                              :value="choice.name"
                                              primary
                                            ></v-radio>
                                            <v-text-field
                                              v-else
                                              label="Texto para mostrar"
                                              v-model="choice.name"
                                            ></v-text-field>
                                        </v-flex>
                                        <v-flex xs5 md5>
                                          <v-btn v-tooltip:top="{html: 'Editar opción'}" icon="icon" class="indigo--text" @click.native="toggleValueEditCheckBox(choice)">
                                              <v-icon>mode_edit</v-icon>
                                          </v-btn>
                                          <v-btn v-tooltip:top="{html: 'Remover opción'}" icon="icon" class="red--text" @click.native="deleteChoiceItem(item, choiceId)" v-show="item.choices.length != 1">
                                              <v-icon>delete</v-icon>
                                          </v-btn>
                                          <v-btn v-tooltip:top="{html: 'Agregar una nueva opción'}" icon="icon" class="yellow--text" @click.native="addChoiceItem(item)" v-show="choiceId == item.choices.length - 1">
                                              <v-icon>add</v-icon>
                                          </v-btn>
                                        </v-flex>
                                    </v-layout>
                                </div>
                            </v-card-text>
                            <v-card-actions>
                                <v-btn
                                  v-show="items.length > 1"
                                  flat
                                  class="red--text darken-1"
                                  @click.native="removeItem(id)"
                                >Eliminar Campo</v-btn>
                            </v-card-actions>
                        </v-card>
                    </v-expansion-panel-content>
                </v-expansion-panel>
                <br>
            </v-flex>
        </v-layout>
        <floating-button>
            <template slot="child">
                <v-btn floating warning small @click.native="addItem" v-tooltip:left="{html: 'Agregar Campo'}">
                    <v-icon light>add</v-icon>
                </v-btn>
                <v-btn floating success small @click.native="saveFormato" v-tooltip:left="{html: 'Guardar Formato'}">
                    <v-icon light>save</v-icon>
                </v-btn>
                <v-btn floating info small @click.native.stop="preview = true" v-tooltip:left="{html: 'Previsualizar el Formulario'}">
                    <v-icon light>photo</v-icon>
                </v-btn>
            </template>
            <v-btn floating error v-tooltip:left="{html: 'Opciones'}">
                <v-icon light>settings</v-icon>
            </v-btn>
        </floating-button>
        <v-dialog v-model="preview" fullscreen transition="v-dialog-bottom-transition" :overlay="false">
            <v-card>
                <v-card-row>
                    <v-toolbar class="orange darken-2">
                        <v-btn icon="icon" @click.native="preview = false">
                            <v-icon class="white--text">close</v-icon>
                        </v-btn>
                        <v-toolbar-title class="white--text">Settings</v-toolbar-title>
                        <!-- <v-btn class="white--text" flat="flat" @click.native="preview = false">Save</v-btn> -->
                    </v-toolbar>
                </v-card-row>
                <formulario-resultado :value="$data"></formulario-resultado>
            </v-card>
        </v-dialog>
        <v-dialog v-model="dialog" scrollable>
            <v-card>
                <v-card-title>Selecciona una Caracteristica</v-card-title>
                <v-divider></v-divider>
                <v-card-row height="300px">
                    <v-card-text>
                      <v-radio
                      v-for="(caracteristica, caracteristicaId) of caracteristicas"
                      :key="caracteristica.id"
                      :label="caracteristica.codigo.toUpperCase()"
                      v-model="modalchoice"
                      :value="caracteristica.id"
                      primary></v-radio>
                    </v-card-text>
                </v-card-row>
                <v-divider></v-divider>
                <v-card-actions>
                    <v-btn class="blue--text darken-1" flat @click.native="dialog = false">Cerrar</v-btn>
                    <v-btn class="blue--text darken-1" flat @click.native="llenarCaracteristicas">Escoger</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>
    </div>
</template>

<script>
import URL from './../urls.js';
import IgMixin from './../mixins/igmixin.js';
import ErrorMixin from './../mixins/errormixin.js';
import FloattingButton from './../components/floating-button.vue';
import FormularioResultado from './../components/formulario-resultado.vue';
import _ from 'underscore';

export default {
    mixins: [IgMixin, ErrorMixin],
    components: {
        floatingButton: FloattingButton,
        formularioResultado: FormularioResultado,
    },
    created: function () {
        this.getFormato()
    },
    data: function () {
        return {
            formato: {laboratorio: {nombre: '', codigo: '', id: ''}},
            dialog: false,
            preview: false,
            caracteristicas: [],
            modalchoice: '',
            items: [],
            lastItem: {},
            tipoHelpText: 'Escoja un tipo de campo para los resultados.',
            tipoOpciones: [
                {
                  text: 'Texto',
                  name: 'text',
                  help: 'Con este campo se puede dar un resultado libre corto y conciso.'
                },
                {
                  text: 'Selección Unica',
                  name: 'radio',
                  help: 'Con este campo se proveen varias opciones y solo podrá ser escogida 1.'
                },
                {
                  text: 'Multiple Selección',
                  name: 'checkbox',
                  help: 'Con este campo se proveen varias opciones y podrán ser escogidas 1 o todas.'
                },
                {
                  text: 'Caracteristicas',
                  name: 'select',
                  help: 'Con este campo se muestran solo las opciones a partir de una caracteristica escogida.'
                },
                {
                  text: 'Libre',
                  name: 'textarea',
                  help: 'Con este campo se puede escribir libremente, bajo ciertos formatos.'
                }
            ]
        }
    },
    watch: {
        dialog: function () {
            if (this.dialog) {
                this.$http.get(URL.caracteristicas)
                  .then(response => {
                      this.caracteristicas = response.body;
                  }, response => {
                      this.showSnackBar('No se pueden mostrar las caracteristicas, vuelva a intentarlo.')
                  });
            }
        },
        '$route': 'getFormato',
    },
    methods: {
        genValidationsForItem: function (item) {
            return {
                target: item,
                validations: [
                    i => ['checkbox', 'radio'].indexOf(i.tipo.name) === -1 || i.choices.length > 1,
                    i => i.tipo !== '',
                    i => i.nombre !== '',
                    i => ['select'].indexOf(i.tipo.name) === -1 || i.choices_select.length > 1
                ]
            }
        },
        addItem: function () {
            let length = (this.items.length + 1).toString();
            let item = {
                nombre: 'Campo ' + length,
                help: '',
                choices: [{edit: false, name: 'Option 1', id: 0}],
                choices_select: [],
                choices_count: 0,
                model_text: '',
                model_check: [],
                unidades: '',
                tipo: '',
                referencia: '',
            }
            this.items.push(item);
            this.addValidation(this.genValidationsForItem(item));
        },
        deleteChoiceItem: function (item, choice) {
            item.choices.splice(choice, 1);
        },
        addChoiceItem: function (item) {
            let length = (item.choices.length + 1).toString();
            item.choices_count++;
            item.choices.push(
                {edit: false, name: 'Option ' + length, id: item.choices_count}
            );
        },
        toggleValueEditCheckBox: function (item) {
            // item es un choice
            if (!'edit' in item) {
                console.warning('No hay una propiedad ¨edit¨ de la opcion, por lo que no sera reactiva.');
            }
            item.edit = !item.edit;
        },
        removeItem: function (item) {
            let deleted = this.items.splice(item, 1);
            let error = this.validations.find(i => i.target == deleted);
            this.removeValidation(error);
        },
        llenarCaracteristicas: function () {
            let item = this.lastItem;
            if (this.modalchoice) {
                this.$http.get(URL.especificaciones_por_carateristica + this.modalchoice.toString() + '/')
                  .then(response => {
                      item.choices_select = [];
                      for (let choice of response.body) {
                          choice.text = choice.nombre;
                          item.choices_select.push(choice);
                      }
                  }, response => {
                      this.showSnackBar('Ha ocurrido un error al intentar obtener las caracteristicas, por favor vuelva a intentarlo mas tarde.');
                  });
            }
            this.dialog = false;
        },
        getFormato: function () {
            let idLaboratorio = this.$route.params.id;
            this.$http.get(URL.formatos.concat(idLaboratorio.toString()).concat('/'))
              .then(response => {
                  this.formato = response.body;
                  this.items = !_.isEmpty(this.formato.formato) ? this.formato.formato: [];
                  if (this.items.length === 0) {
                      this.addItem();
                  } else {
                      this.validateNewPossibleErrors();
                  }
              }, response => {
                  this.showSnackBar('Formato Solicitado no encontrado.');
                  this.formato = undefined;
              })
        },
        saveFormato: function () {
            this._validated = true;
            let idLaboratorio = this.$route.params.id;
            let token = document.getElementsByName('csrfmiddlewaretoken')[0];
            let data = {formato: JSON.stringify(this.items), laboratorio: this.formato.laboratorio}
            if (!this.hasError()) {
                this.$http.post(URL.formatos.concat(idLaboratorio.toString()).concat('/'), data, {headers: {'X-CSRFToken': token.value}})
                  .then(response => {
                      this.showSnackBar('Se ha guardado el formato con exito.');
                  }, response => {
                      if (typeof response == 'object' && 'detail' in response) {
                          this.showSnackBar(response.detail);
                      } else {
                          this.showSnackBar('Ha ocurrido un error al guardar el formato, por favor vuelva a intentarlo.');
                      }
                  })
            } else {
                this.showSnackBar('Aun hay campo con errores, verifique antes de guardar');
            }
        },
        validateNewPossibleErrors: function () {
            let toDelete = [];
            this.validations.forEach(item => {
                let find = this.items.find(i => i == item.target);
                if (!find) {
                    toDelete.push(item);
                }
            })
            if (toDelete.length) {
                for (let index of toDelete) {
                    this.validations.splice(this.validations.indexOf(index), 1)
                }
            }
            this.items.forEach(item => {
                let inValidations = this.validations.find(i => i.target === item);
                if (!inValidations) {
                    this.addValidation(this.genValidationsForItem(item));
                }
            })
        }
    }
}
</script>

<style lang="css">
</style>
