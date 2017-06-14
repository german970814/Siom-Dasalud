<template lang="html">
    <v-card>
        <v-card-title>
            {{ tableTitle }}
            <v-spacer></v-spacer>
            <v-text-field append-icon="search" label="Buscar" single-line hide-details v-model="buscador"></v-text-field>
        </v-card-title>
        <v-data-table
            :pagination.sync="pagination"
            v-bind:headers="headers"
            :items="data"
            v-bind:search="buscador"
            :rows-per-page-items="[10]"
            :rowsPerPage="10"
            :filter="filter"
            rows-per-page-text="Filas por Página"
            no-results-text="No se encontraron resultados"
            ref="dataTable">
            <template slot="headers" scope="props">
                <span style="text-align:before: center !important">{{ props.item.text }}</span>
            </template>
            <template slot="items" scope="props">
                <!-- <td @click="updateForm(props.item)">
                    <v-checkbox primary v-model="props.item.selected" ></v-checkbox>
                </td> -->
                <template v-for="field of fields">
                    <td class="text-xs-center" @click="updateForm(props.item)" v-if="typeof field != 'object'">{{ getattr(props.item, field) }}</td>
                    <td class="text-xs-center" v-else>
                        <v-btn floating small router class="cyan darken-1" :href="field.href.replace(':id', props.item.id)">
                            <v-icon light>mode_edit</v-icon>
                        </v-btn>
                    </td>
                </template>
            </template>
        </v-data-table>
        <v-progress-linear indeterminate class="red--text" height="3" :active="loading"></v-progress-linear>
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
        },
        loading: true,
    },
    data: function () {
        return {
            buscador: '',
            pagination: {
                page: 1,
                rowsPerPage: 10,
                descending: false,
                totalItems: 0
            }
        }
    },
    mounted: function () {
        // this.$refs.dataTable.rowsPerPage = 10;
    },
    methods: {
        getHrefField: function (field, item) {
            let href;
            if (!'patrons' in field) {
                href = field.href.replace(/\/\:[a-zA-Z]*\//g, '/' + item.id + '/');
            } else {
                href = field.href;
                for (let patron of field.patrons) {
                    href = href.replace(':'.concat(patron.identifier), typeof patron.replace == 'function' ? patron(item): patron);
                }
            }
            return href;
        },
        _validValue: function (val) {
            return val !== null && ['undefined', 'boolean'].indexOf(typeof val) === -1
        },
        customFilter: function (val, search) {
            return val.toString().toLowerCase().indexOf(search) !== -1;
        },
        filter: function (val, search) {
            var valid = this._validValue(val);
            if (valid) {
                valid = valid && this.customFilter(val, search);
                if (['object'].indexOf(typeof val) === 0 && !valid) {
                    valid = Object.keys(val).some(j => this._validValue(val[j]) && this.customFilter(val[j], search));
                }
            }
            return valid;
        },
        getattr: function (obj, attr) {
            let attrs = attr.split('.');
            for (let at of attrs) {
                if (at in obj) {
                    obj = obj[at];
                }
                if (obj instanceof Array) {
                    var mix = '';
                    for (let elem of obj) {
                        attr = attrs[attrs.length - 1];
                        if (mix) {
                            mix += ', ';
                        }
                        mix += elem[attr];
                    }
                    return mix;
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
.text-xs-left {
    text-align: center !important;
}
</style>
