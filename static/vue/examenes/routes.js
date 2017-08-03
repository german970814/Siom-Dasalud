import VueRouter from 'vue-router';

import OrdenesSinVisiomeria from './pages/ordenes.vue';
import Visiometria from './pages/visiometria.vue';

const routes = [
    {path: '/ordenes/visiometria/', component: OrdenesSinVisiomeria},
    {path: '/formulario/:id/', component: Visiometria},
]

const router = new VueRouter({routes});
export default router;
