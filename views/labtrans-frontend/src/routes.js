import HomePage from "./components/HomePage.vue"

import ResultsPage from './components/ResultsPage.vue'

import IncidencePage from './components/IncidencePage.vue'

const routes = [
    { path: '/', component: HomePage },
    { path: '/results', component: ResultsPage },
    { path: '/incidence', component: IncidencePage },

  ]
  
  export default routes