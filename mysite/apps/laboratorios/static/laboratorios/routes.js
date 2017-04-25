import VueRouter from 'vue-router';
import algo from './algo.vue';
import lista from './table.vue';

const routes = [
    {path: '/', component: algo},
    {path: '/bar', component: lista}
]


const router = new VueRouter({routes});
export default router;
