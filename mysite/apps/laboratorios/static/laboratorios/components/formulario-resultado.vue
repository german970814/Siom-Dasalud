<template lang="html">
    <div>
        <v-container>
            <v-row>
                <h1 class="title">Formulario de Resultado</h1>
            </v-row>
            <v-row v-for="(item, id) of value.items" :key="id">
                <v-col md8>
                    <v-text-field
                        v-if="item.tipo.name == 'text' || item.tipo.name == 'textarea'"
                        :multi-line="item.tipo.name == 'textarea'"
                        :label="item.nombre"
                        :hint="item.help"
                        v-model="item.model_text"
                        :disabled="disabled"
                        persistent-hint
                        @input="$emit('input', $event)"
                    ></v-text-field>
                    <v-select
                        v-else-if="item.tipo.name == 'select'"
                        :label="item.nombre"
                        :hint="item.help"
                        v-model="item.model_text"
                        :items="item.choices_select"
                        item-value="text"
                        :disabled="disabled"
                        persistent-hint
                        @input="$emit('input', $event)"
                    ></v-select>
                    <div v-else-if="item.tipo.name == 'checkbox'">
                        <dl class="section-text section-text--def">
                            <dt>{{ item.nombre }}</dt>
                            <dd>{{ item.help }}</dd>
                        </dl>
                        <v-row v-for="(choice, choiceId) of item.choices" :key="choiceId">
                            <v-col xs7 md7>
                                <v-checkbox
                                    v-if="!choice.edit"
                                    :label="choice.name"
                                    v-model="item.model_check"
                                    :value="choice"
                                    :disabled="disabled"
                                    primary
                                    @input="$emit('input', $event)"
                                ></v-checkbox>
                            </v-col>
                        </v-row>
                    </div>
                    <div v-else-if="item.tipo.name == 'radio'">
                        <dl class="section-text section-text--def">
                            <dt>{{ item.nombre }}</dt>
                            <dd>{{ item.help }}</dd>
                        </dl>
                        <v-row v-for="(choice, choiceId) of item.choices" :key="choiceId">
                            <v-col xs7 md7>
                                <v-radio
                                    v-if="!choice.edit"
                                    :label="choice.name"
                                    v-model="item.model_text"
                                    :value="choice.name"
                                    :disabled="disabled"
                                    primary
                                    @input="$emit('input', $event)"
                                ></v-radio>
                            </v-col>
                        </v-row>
                    </div>
                </v-col>
                <v-col md2 v-if="Boolean(item.referencia)">
                  <h6 class="title">Referencia:</h6> {{ item.referencia }}
                </v-col>
                <v-col md2 v-if="Boolean(item.unidades)">
                  <h6 class="title">Unidades:</h6> {{ item.unidades }}
                </v-col>
            </v-row>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'formulario-resultado',
    data: function () {
        return {

        }
    },
    props: {
        value: {},
        disabled: {
            type: Boolean,
            default: true
        },
    },
    methods: {

    }
}
</script>

<style lang="css">
</style>
