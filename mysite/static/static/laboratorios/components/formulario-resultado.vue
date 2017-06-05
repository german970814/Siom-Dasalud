<template lang="html">
    <div>
        <v-container>
            <v-layout>
                <h1 class="title">Formulario de Resultado</h1>
            </v-layout>
            <v-layout v-for="(item, id) of value.items" :key="id">
                <v-flex md8>
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
                        dark
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
                        <v-layout v-for="(choice, choiceId) of item.choices" :key="choiceId">
                            <v-flex xs7 md7>
                                <!--v-if="!choice.edit"-->
                                <v-checkbox
                                    :label="choice.name"
                                    v-model="item.model_check"
                                    :value="choice.id"
                                    :disabled="disabled"
                                    primary
                                    @input="$emit('input', $event)"
                                ></v-checkbox>
                            </v-flex>
                        </v-layout>
                    </div>
                    <div v-else-if="item.tipo.name == 'radio'">
                        <dl class="section-text section-text--def">
                            <dt>{{ item.nombre }}</dt>
                            <dd>{{ item.help }}</dd>
                        </dl>
                        <v-layout v-for="(choice, choiceId) of item.choices" :key="choiceId">
                            <v-flex xs7 md7>
                                <v-radio
                                    v-if="!choice.edit"
                                    :label="choice.name"
                                    v-model="item.model_text"
                                    :value="choice.name"
                                    :disabled="disabled"
                                    primary
                                    @input="$emit('input', $event)"
                                ></v-radio>
                            </v-flex>
                        </v-layout>
                    </div>
                </v-flex>
                <v-flex md2 v-if="Boolean(item.referencia)">
                  <h6 class="title">Referencia:</h6> {{ item.referencia }}
                </v-flex>
                <v-flex md2 v-if="Boolean(item.unidades)">
                  <h6 class="title">Unidades:</h6> {{ item.unidades }}
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
export default {
    name: 'formulario-resultado',
    mounted: function () {

    },
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
