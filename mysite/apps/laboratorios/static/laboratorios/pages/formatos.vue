<template lang="html">
    <div>
        <v-container>
            <v-row>
                <h4>Creación de Formatos</h4>
            </v-row>
            <v-row>
                <v-col md6 xs12 class="mb-5" v-for="(item, id) of items" :key="id">
                    <v-expansion-panel expand>
                        <v-expansion-panel-content><!--v-bind:value="item === 1"-->
                            <div slot="header">{{ item.nombre }}</div>
                            <v-card>
                                <v-card-title></v-card-title>
                                <v-card-text class="grey lighten-5">
                                    <v-select
                                        label="Tipo"
                                        :hint="item.tipo.help"
                                        :items="tipoOpciones"
                                        v-model="item.tipo"
                                        item-value="text"
                                        required
                                        persistent-hint
                                        autocomplete
                                        light
                                    ></v-select>
                                    <br>
                                    <v-text-field
                                        label="Nombre del Campo"
                                        v-model="item.nombre"
                                        hint="Con este nombre se identificará el campo"
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
                                        v-if="item.tipo.name == 'text' || item.tipo.name == 'textarea'"
                                        :multi-line="item.tipo.name == 'textarea'"
                                        :label="item.nombre"
                                        :hint="item.help"
                                        v-model="item.model_text"
                                    ></v-text-field>
                                    <v-select
                                        v-else-if="item.tipo.name == 'select'"
                                        :label="item.nombre"
                                        :hint="item.help"
                                        v-model="item.model"
                                    ></v-select>
                                    <div v-else-if="item.tipo.name == 'checkbox'">
                                        <v-row v-for="(choice, choiceId) of item.choices" :key="choiceId">
                                            <v-col xs7 md7>
                                                <v-checkbox
                                                  v-if="!choice.edit"
                                                  :label="choice.name"
                                                  v-model="item.model_check"
                                                  :value="choice"
                                                  primary
                                                ></v-checkbox>
                                                <v-text-field
                                                  v-else
                                                  label="Texto para mostrar"
                                                  v-model="choice.name"
                                                ></v-text-field>
                                            </v-col>
                                            <v-col xs5 md5>
                                              <v-btn v-tooltip:top="{html: 'Editar opción'}" icon="icon" class="indigo--text" @click.native="toggleValueEditCheckBox(choice)">
                                                  <v-icon>mode_edit</v-icon>
                                              </v-btn>
                                              <v-btn v-tooltip:top="{html: 'Remover opción'}" icon="icon" class="red--text" @click.native="deleteChoiceItem(item, choiceId)" v-show="item.choices.length != 1">
                                                  <v-icon>delete</v-icon>
                                              </v-btn>
                                              <v-btn v-tooltip:top="{html: 'Agregar opción'}" icon="icon" class="yellow--text" @click.native="addChoiceItem(item)" v-show="choiceId == item.choices.length - 1">
                                                  <v-icon>add</v-icon>
                                              </v-btn>
                                            </v-col>
                                        </v-row>
                                    </div>
                                    <div v-else-if="item.tipo.name == 'radio'">
                                        <v-row v-for="(choice, choiceId) of item.choices" :key="choiceId">
                                            <v-col xs7 md7>
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
                                            </v-col>
                                            <v-col xs5 md5>
                                              <v-btn v-tooltip:top="{html: 'Editar opción'}" icon="icon" class="indigo--text" @click.native="toggleValueEditCheckBox(choice)">
                                                  <v-icon>mode_edit</v-icon>
                                              </v-btn>
                                              <v-btn v-tooltip:top="{html: 'Remover opción'}" icon="icon" class="red--text" @click.native="deleteChoiceItem(item, choiceId)" v-show="item.choices.length != 1">
                                                  <v-icon>delete</v-icon>
                                              </v-btn>
                                              <v-btn v-tooltip:top="{html: 'Agregar una nueva opción'}" icon="icon" class="yellow--text" @click.native="addChoiceItem(item)" v-show="choiceId == item.choices.length - 1">
                                                  <v-icon>add</v-icon>
                                              </v-btn>
                                            </v-col>
                                        </v-row>
                                    </div>
                                </v-card-text>
                                <v-card-row actions>
                                    <v-btn
                                      v-show="items.length > 1"
                                      flat
                                      class="red--text darken-1"
                                      @click.native="removeItem(id)"
                                    >Eliminar Campo</v-btn>
                                </v-card-row>
                            </v-card>
                        </v-expansion-panel-content>
                    </v-expansion-panel>
                    <br>
                </v-col>
            </v-row>
        </v-container>
        <code><pre>{{ $data }}</pre></code>
        <v-btn floating error @click.native="addItem">
            <v-icon>add</v-icon>
        </v-btn>
    </div>
</template>

<script>
export default {
    props: {

    },
    data: function () {
        return {
            items: [{
                nombre: 'Campo1',
                help: '',
                choices: [{edit: false, name: 'Option 1', checked: false}],
                model_text: '',
                model_check: [],
                tipo: '',
                referencia: '',
            }],
            tipoHelpText: 'Escoja un tipo de campo para los resultados.',
            tipoOpciones: [
                {
                  text: 'Texto',
                  name: 'text',
                  help: 'Con este campo se puede dar un resultado libre corto y consiso.'
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
    methods: {
        addItem: function () {
            let length = (this.items.length + 1).toString();
            this.items.push({
                nombre: 'Campo ' + length,
                help: '',
                choices: [{edit: false, name: 'Option 1', checked: false}],
                model_text: '',
                model_check: [],
                tipo: '',
                referencia: '',
            })
        },
        deleteChoiceItem: function (item, choice) {
            item.choices.splice(choice, 1);
        },
        addChoiceItem: function (item) {
            let length = (item.choices.length + 1).toString();
            item.choices.push(
                {edit: false, name: 'Option ' + length}
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
            this.items.splice(item, 1);
        }
    }
}
</script>

<style lang="css">
</style>
