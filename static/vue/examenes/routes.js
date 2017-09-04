import VueRouter from 'vue-router';

import OrdenesSinVisiomeria from './pages/ordenes.vue';
import Visiometria from './pages/visiometria.vue';
import Visiometra from './pages/visiometra.vue';
import OrdenesSinAudiometria from  './pages/ordenes_audiometria.vue';
import Audiometria from './pages/audiometria.vue';

const routes = [
    {path: '/ordenes/visiometria/', component: OrdenesSinVisiomeria},
    {path: '/formulario/:id/', component: Visiometria},
    {path: '/visiometra/', component: Visiometra},
    {path: '/ordenes/audiometria/', component: OrdenesSinAudiometria},
    {path: '/formulario/audiometria/:id/', component: Audiometria},
]

const router = new VueRouter({routes});
export default router;
