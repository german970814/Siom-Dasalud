<template lang="html">
    <div>
        <v-layout>
            <v-flex xs12 md12>
                <ig-table
                  table-title="Empleados"
                  :headers="headers"
                  :data="elements"
                  :fields="['usuario.username', 'nombres', 'usuario.email', 'documento']"
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
              urlForm: URL.empleados,
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
                {
                  text: 'Documento',
                  value: 'documento',
                  left: true,
                  sortable: false,
                },
              ],
              fields: [
                {
                  name: 'username',
                  verbose_name: 'Usuario',
                  type: String,
                  hint: 'Este es el nombre de usuario de el bacteriologo.',
                  group: 'usuario',
                },
                {
                  name: 'password',
                  verbose_name: 'Contraseña',
                  type: String,
                  hint: 'Esta es la contraseña de el bacteriologo.',
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
                  hint: 'Este es el email de el bacteriologo.',
                  group: 'usuario',
                  kwargs: {
                    type: 'email'
                  }
                },
                {
                  name: 'nombres',
                  verbose_name: 'Nombre',
                  type: String,
                  hint: 'Nombres del empleado.',
                },
                {
                  name: 'apellidos',
                  verbose_name: 'Apellidos',
                  type: String,
                  hint: 'Apellidos de el empleado.',
                },
                {
                  name: 'documento',
                  verbose_name: 'Documento',
                  type: Number,
                  hint: 'Documento de el empleado.',
                  kwargs: {
                      type: 'number',
                  }
                },
            ]
          }
    },
    mounted: function () {
        this.getElements(URL.empleados);
    }
}
</script>

<style lang="css">
</style>
