import VueRouter from 'vue-router';

import Laboratorios from './pages/laboratorios.vue';
import Equipos from './pages/equipos.vue';
import Tecnicas from './pages/tecnicas.vue';
import SeccionesTrabajo from './pages/secciones_trabajo.vue';
import Reactivos from './pages/reactivos.vue';
import Caracteristicas from './pages/caracteristicas.vue';
import EspecificacionCaracteristica from './pages/especificacion_caracteristica.vue';
import OrdenesLaboratorios from './pages/ordenes_laboratorios.vue';
import Formatos from './pages/formatos.vue';
import Bacteriologos from './pages/bacteriologos.vue';
import Resultados from './pages/resultados.vue';
import TomaMuestra from './pages/toma_muestra.vue';
import Empleados from './pages/empleados.vue';

const routes = [
    {path: '/laboratorios/', component: Laboratorios},
    {path: '/equipos/', component: Equipos},
    {path: '/tecnicas/', component: Tecnicas},
    {path: '/secciones_trabajo/', component: SeccionesTrabajo},
    {path: '/reactivos/', component: Reactivos},
    {path: '/caracteristicas/', component: Caracteristicas},
    {path: '/especificacion_caracteristicas/', component: EspecificacionCaracteristica},
    {path: '/ordenes_laboratorios/', component: OrdenesLaboratorios},
    {path: '/formatos/:id/', component: Formatos},
    {path: '/bacteriologos/', component: Bacteriologos},
    {path: '/resultados/:id/', component: Resultados},
    {path: '/toma_muestra/', component: TomaMuestra},
    {path: '/empleados/', component: Empleados},
]

// router.beforeEach((to, from, next) => {
//     if (to.matched.some(record => record.meta.requiresAuth)) {
//       // this route requires auth, check if logged in
//       // if not, redirect to login page.
//       if (!auth.loggedIn()) {
//         next({
//           path: '/login',
//           query: { redirect: to.fullPath }
//         })
//       } else {
//         next()
//       }
//     } else {
//       next() // make sure to always call next()!
//     }
// })

const router = new VueRouter({routes});
export default router;
