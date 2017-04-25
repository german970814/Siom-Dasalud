<template>
    <div>
        <v-toolbar class="cyan darken-1">
            <v-toolbar-side-icon @click.native.stop="sidebar = !sidebar"></v-toolbar-side-icon>
            <v-toolbar-title>Dasalud</v-toolbar-title>
        </v-toolbar>
        <main>
            <v-sidebar v-model="sidebar" drawer class="mt-0 scroll-y" :mobile-break-point="576">
                <v-list dense>
                    <v-list-item>
                        <v-list-tile>
                            <v-list-tile-avatar>
                                <v-icon>accessibility</v-icon>
                            </v-list-tile-avatar>
                            <v-list-tile-content>
                                <v-list-tile-title>Dashboard</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list-item>
                    <v-list-group>
                        <v-list-item slot="item">
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>people</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Pacientes</v-list-tile-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Lista Paciente</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Crear Paciente</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                    </v-list-group>
                    <v-list-group>
                        <v-list-item slot="item">
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>today</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Agendas</v-list-tile-title>
                                </v-list-tile-content>
                                    <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Agenda del Dia</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Agenda Por Doctor</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                    </v-list-group>
                    <v-list-group>
                        <v-list-item slot="item">
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>open_in_browser</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Ordenes de Servicio</v-list-tile-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Lista de Ordenes</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Filtrar Ordenes</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                    </v-list-group>
                    <v-list-item>
                        <v-list-tile>
                            <v-list-tile-avatar>
                                <v-icon>search</v-icon>
                            </v-list-tile-avatar>
                            <v-list-tile-content>
                                <v-list-tile-title>Buscar Orden</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
                    </v-list-item>
                    <v-divider light></v-divider>
                    <v-subheader>Utilidades</v-subheader>
                    <v-list-group>
                        <v-list-item slot="item">
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>local_hospital</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Medicos e Instituciones</v-list-tile-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Medicos</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Instituciones</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                    </v-list-group>
                    <v-list-group>
                        <v-list-item slot="item">
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>business_center</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Empresas y Planes</v-list-tile-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Empresas</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Planes de Salud</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                    </v-list-group>
                    <v-list-group>
                        <v-list-item slot="item">
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>featured_play_list</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Procedimientos y Plantillas</v-list-tile-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Procedimientos</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Plantillas</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                        <v-list-item>
                            <v-list-tile ripple>
                                <v-list-tile-title>Servicios</v-list-tile-title>
                            </v-list-tile>
                        </v-list-item>
                    </v-list-group>
                    <v-divider light></v-divider>
                </v-list>
            </v-sidebar>
            <div class="main">
                <v-content class="grey lighten-4">
                    <v-container fluid>
                        <br>
                        <v-spacer></v-spacer>
                        <slot></slot>
                    </v-container>
                </v-content>
            </div>
        </main>
    </div>
</template>

<script>
    module.exports = {
        name: 'igMenu',
        props: {

        },
        data: function () {
            return {
                sidebar: false
            };
        }
    }
</script>

<style>
  .main {
    width: 100% !important;
  }
</style>
