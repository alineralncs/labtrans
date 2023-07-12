import HomePage from "./components/HomePage.vue"

import ResultsPage from './components/ResultsPage.vue'

import IncidencePage from './components/IncidencePage.vue'

import ExportData from './components/ExportData.vue'

const routes = [
    { path: '/', component: HomePage },
    { path: '/results', component: ResultsPage },
    { path: '/incidence', component: IncidencePage },
    { path: '/exportfiles', component: ExportData },

  ]
  
  export default routes