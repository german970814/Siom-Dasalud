<v-list-group v-else-if="item.children" v-model="item.model" no-action>
    <v-list-tile slot="item">
        <v-list-tile-action>
        <v-icon>{{ item.model ? item.icon : item['icon-alt'] }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
        <v-list-tile-title>
            {{ item.text }}
        </v-list-tile-title>
        </v-list-tile-content>
    </v-list-tile>
    <v-list-tile
        v-for="(child, i) in item.children"
        :key="i"
    >
        <v-list-tile-action v-if="child.icon">
        <v-icon>{{ child.icon }}</v-icon>
        </v-list-tile-action>
        <v-list-tile-content>
        <v-list-tile-title>
            {{ child.text }}
        </v-list-tile-title>
        </v-list-tile-content>
    </v-list-tile>
</v-list-group>
<v-list-tile v-else>
    <v-list-tile-action>
        <v-icon>{{ item.icon }}</v-icon>
    </v-list-tile-action>
    <v-list-tile-content>
        <v-list-tile-title>
        {{ item.text }}
        </v-list-tile-title>
    </v-list-tile-content>
</v-list-tile>


<template>
    <div>
        <v-toolbar class="cyan darken-1">
            <v-toolbar-side-icon @click.native.stop="sidebar = !sidebar"></v-toolbar-side-icon>
            <v-toolbar-title>Dasalud</v-toolbar-title>
        </v-toolbar>
        <main>
            <v-sidebar v-model="sidebar" drawer class="mt-0 scroll-y" :mobile-break-point="576">
                <v-list dense>
                
                        <v-list-tile href="/">
                            <v-list-tile-avatar>
                                <v-icon>accessibility</v-icon>
                            </v-list-tile-avatar>
                            <v-list-tile-content>
                                <v-list-tile-title>Dashboard</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
    
                    <v-list-group>
    
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
        
                    
                            <v-list-tile ripple href="/pacientes/page/1/">
                                <v-list-tile-title>Lista Paciente</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/add/paciente/">
                                <v-list-tile-title>Crear Paciente</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
                    <v-list-group>
    
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
        
                    
                            <v-list-tile ripple href="/agenda/">
                                <v-list-tile-title>Agenda del Dia</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/agenda/doctor/">
                                <v-list-tile-title>Agenda Por Doctor</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
                    <v-list-group>
    
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
        
                    
                            <v-list-tile ripple href="/ordenes/">
                                <v-list-tile-title>Lista de Ordenes</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/ordenesReporte/">
                                <v-list-tile-title>Filtrar Ordenes</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
                
                        <v-list-tile ripple href="/portal_empresas/">
                            <v-list-tile-avatar>
                                <v-icon>search</v-icon>
                            </v-list-tile-avatar>
                            <v-list-tile-content>
                                <v-list-tile-title>Buscar Orden</v-list-tile-title>
                            </v-list-tile-content>
                        </v-list-tile>
    
                    <v-divider light></v-divider>
                    <v-subheader>Utilidades</v-subheader>
                    <v-list-group>
    
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
        
                    
                            <v-list-tile ripple href="/medicos/">
                                <v-list-tile-title>Medicos</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/instituciones/">
                                <v-list-tile-title>Instituciones</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
                    <v-list-group>
    
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
        
                    
                            <v-list-tile ripple href="/empresas/">
                                <v-list-tile-title>Empresas</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/planes/">
                                <v-list-tile-title>Planes de Salud</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
                    <v-list-group>
    
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
        
                    
                            <v-list-tile ripple href="/procedimientos/">
                                <v-list-tile-title>Procedimientos</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/plantillas/">
                                <v-list-tile-title>Plantillas</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/servicios/">
                                <v-list-tile-title>Servicios</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
                    <v-list-group>
    
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>featured_play_list</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Usuarios</v-list-tile-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/usuarios/">
                                <v-list-tile-title>Usuarios del Sistema</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="/usuariosEmpresa/">
                                <v-list-tile-title>Usuarios Empresas</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
                    <v-divider light></v-divider>
                    <v-subheader>Laboratorio</v-subheader>
                
                        <v-list-tile ripple href="#/ordenes_laboratorios/">
                            <v-list-tile-title>Ordenes Laboratorios</v-list-tile-title>
                        </v-list-tile>
    
                    <v-list-group>
    
                            <v-list-tile ripple>
                                <v-list-tile-avatar>
                                    <v-icon>local_hospital</v-icon>
                                </v-list-tile-avatar>
                                <v-list-tile-content>
                                    <v-list-tile-title>Administración</v-list-tile-title>
                                </v-list-tile-content>
                                <v-list-tile-action>
                                    <v-icon>keyboard_arrow_down</v-icon>
                                </v-list-tile-action>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/bacteriologos/">
                              <v-list-tile-title>Bacteriologos</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/laboratorios/">
                              <v-list-tile-title>Laboratorios</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/equipos/">
                                <v-list-tile-title>Equipos</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/tecnicas/">
                                <v-list-tile-title>Tecnicas</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/secciones_trabajo/">
                                <v-list-tile-title>Secciones de Trabajo</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/reactivos/">
                                <v-list-tile-title>Reactivos</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/caracteristicas/">
                                <v-list-tile-title>Caracteristicas</v-list-tile-title>
                            </v-list-tile>
        
                    
                            <v-list-tile ripple href="#/especificacion_caracteristicas/">
                                <v-list-tile-title>Especificacion de Caracteristicas</v-list-tile-title>
                            </v-list-tile>
        
                    </v-list-group>
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
        },
    }
</script>

<style>
  .main {
    width: 100% !important;
  }
</style>
