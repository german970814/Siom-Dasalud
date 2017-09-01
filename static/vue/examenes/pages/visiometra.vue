<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <ig-table
                  table-title="Empleados"
                  :headers="headers"
                  :data="elements"
                  :fields="['usuario.username', 'nombre', 'usuario.email']"
                  @selectedrow="eventUpdatedForm"
                  :loading="loading"
                ></ig-table>
            </v-flex>
        </v-layout>
        <br>
        <v-layout>
            <v-flex xs12 md12>
                <ig-form
                :fields="fields"
                :url="urlForm"
                @showsnack="showSnackBar"
                @objectcreated="eventCreatedObject"
                @clearselected="selected = false"
                :selected="selected"
                ></ig-form>
            </v-flex>
        </v-layout>
    </div>
</template>

<script>
import _ from 'underscore';
import IgMixin from './../mixins/igmixin.js';
import TableComponent from './../components/table.vue';
import FormComponent from './../components/form.vue';
import URL from './../urls.js';

export default {
    components: {
        igTable: TableComponent,
        igForm: FormComponent,
    },
    mixins: [IgMixin],
    data: function () {
        return {
            urlForm: URL.visiometra,
            selected: false,
            headers: [
                {
                    text: 'Usuario',
                    value: 'username',
                    left: true,
                },
                {
                    text: 'Nombre',
                    value: 'nombre',
                    left: true,
                },
                {
                    text: 'Email',
                    value: 'usuario.email',
                    left: true,
                },
            ],
            fields: [
                {
                    name: 'username',
                    verbose_name: 'Usuario',
                    type: String,
                    hint: 'Este es el nombre de usuario de el empleado.',
                    group: 'usuario',
                },
                {
                    name: 'password',
                    verbose_name: 'Contraseña',
                    type: String,
                    hint: 'Esta es la contraseña de el empleado.',
                    required: false,
                    group: 'usuario',
                    kwargs: {
                    type: 'password'
                    }
                },
                {
                    name: 'email',
                    verbose_name: 'Email',
                    type: String,
                    hint: 'Este es el email de el empleado.',
                    group: 'usuario',
                    kwargs: {
                    type: 'email'
                    }
                },
                {
                    name: 'nombre',
                    verbose_name: 'Nombre',
                    type: String,
                    hint: 'Nombre de el empleado.',
                },
                {
                    name: 'firma',
                    verbose_name: 'Firma',
                    type: 'file',
                    hint: 'Esta es la firma de el empleado, la cual saldrá en los resultados.',
                    required: false,
                    url_file: '/examenes/api/visiometra/firma/',
                },
            ]
        }
    },
    mounted: function () {
        this.getElements(URL.visiometra);
    }
}
</script>

<style lang="css">
</style>
