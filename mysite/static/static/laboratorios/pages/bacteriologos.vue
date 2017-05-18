<template lang="html">
    <div>
        <v-container>
          <v-row>
            <v-col xs12 md12>
              <ig-table
              table-title="Bacteriologos"
              :headers="headers"
              :data="elements"
              :fields="['usuario.username', 'nombre', 'usuario.email', 'codigo', 'registro', 'areas.codigo']"
              @selectedrow="eventUpdatedForm"
              :loading="loading"
              ></ig-table>
            </v-col>
          </v-row>
        </v-container>
        <br>
        <v-container>
          <v-row>
            <v-col xs12 md12>
              <ig-form
              :fields="fields"
              :url="urlForm"
              @showsnack="showSnackBar"
              @objectcreated="eventCreatedObject"
              @clearselected="selected = false"
              :selected="selected"
              >
            </ig-form>
          </v-col>
        </v-row>
        <br>
      </v-container>
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
              urlForm: URL.bacteriologos,
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
                  text: 'Codigo',
                  value: 'codigo',
                  left: true,
                  sortable: false,
                },
                {
                  text: 'Registro',
                  value: 'registro',
                  left: true,
                  sortable: false,
                },
                {
                  text: 'Areas',
                  value: 'areas-nombre',
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
                  name: 'nombre',
                  verbose_name: 'Nombre',
                  type: String,
                  hint: 'Nombre de el bacteriologo.',
                },
                {
                  name: 'codigo',
                  verbose_name: 'Codigo',
                  type: String,
                  hint: 'Código de el bacteriologo.',
                },
                {
                  name: 'registro',
                  verbose_name: 'Registro',
                  type: Number,
                  hint: 'Registro de el bacteriologo.',
                },
                {
                  name: 'areas',
                  verbose_name: 'Areas',
                  type: Array,
                  hint: 'Este es el código de representacion internacional del laboratorio.',
                  url: URL.secciones_trabajo,
                  key: 'codigo',
                  kwargs: {
                    multiple: true
                  }
                },
            ]
          }
    },
    mounted: function () {
        this.getElements(URL.bacteriologos);
    }
}
</script>

<style lang="css">
</style>
