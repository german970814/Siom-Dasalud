import VueRouter from 'vue-router';

import Laboratorios from './pages/laboratorios.vue';
import Equipos from './pages/equipos.vue';
import Tecnicas from './pages/tecnicas.vue';
import SeccionesTrabajo from './pages/secciones_trabajo.vue';
import Reactivos from './pages/reactivos.vue';
import Caracteristicas from './pages/caracteristicas.vue';
import EspecificacionCaracteristica from './pages/especificacion_caracteristica.vue';
import OrdenesLaboratorios from './pages/ordenes_laboratorios.vue';

const routes = [
    {path: '/laboratorios/', component: Laboratorios},
    {path: '/equipos/', component: Equipos},
    {path: '/tecnicas/', component: Tecnicas},
    {path: '/secciones_trabajo/', component: SeccionesTrabajo},
    {path: '/reactivos/', component: Reactivos},
    {path: '/caracteristicas/', component: Caracteristicas},
    {path: '/especificacion_caracteristicas/', component: EspecificacionCaracteristica},
    {path: '/ordenes_laboratorios/', component: OrdenesLaboratorios},
]


const router = new VueRouter({routes});
export default router;
