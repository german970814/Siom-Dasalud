<template lang="html">
    <v-card>
        <v-card-title>
            {{ tableTitle }}
            <v-spacer></v-spacer>
            <v-text-field append-icon="search" label="Buscar" single-line hide-details v-model="buscador"></v-text-field>
        </v-card-title>
        <v-data-table
            v-bind:headers="headers"
            v-model="data"
            v-bind:search="buscador" select-all
            :rows-per-page-items="[10]"
            rowsPerPage="10"
            rows-per-page-text="Filas por Página"
            no-results-text="No se encontraron resultados"
            ref="dataTable">
            <template slot="items" scope="props">
                <td @click="updateForm(props.item)">
                    <v-checkbox primary v-model="props.item.selected" ></v-checkbox>
                </td>
                <template v-for="field of fields">
                    <td class="text-xs-center" @click="updateForm(props.item)">{{ getattr(props.item, field) }}</td>
                </template>
            </template>
        </v-data-table>
    </v-card>
</template>

<script>
export default {
    name: 'igTable',
    props: {
        tableTitle: {
            type: String,
            default: 'Lista',
            required: false
        },
        headers: {
            type: Array,
            required: true
        },
        data: {
            type: Array,
            default: () => [],
            required: false
        },
        fields: {
            type: Array,
            required: true
        }
    },
    data: function () {
        return {
            buscador: ''
        }
    },
    mounted: function () {
        this.$refs.dataTable.rowsPerPage = 10;
    },
    methods: {
        getattr: function (obj, attr) {
            let attrs = attr.split('.');
            for (let at of attrs) {
                if (at in obj) {
                    obj = obj[at];
                }
            }
            return obj;
        },
        updateForm: function (item) {
            this.$emit('selectedrow', item);
        }
    }
}
</script>

<style lang="css">
</style>
