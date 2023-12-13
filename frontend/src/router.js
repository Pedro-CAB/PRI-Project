// router.js
import { createApp } from 'vue';
import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';

const app = createApp(App);

const routes = [
  {
    path: '/result/:id',
    name: 'result',
    component: () => import('./ResultPage.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

app.use(router);

export default app; // Export the app instance as the default export
