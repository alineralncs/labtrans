
import HomePage from '../views/HomePage.vue'

import ResultsPage from '../views/ResultsPage.vue'

import IncidencePage from '../components/IncidencePage.vue'

import ExportDataPage from '../views/ExportDataPage.vue'

import Videos from '../components/Videos.vue'

import Rodovias from "../components/Rodovias.vue"

const routes = [
    { path: '/', component: HomePage },
    { path: '/results', component: ResultsPage },
    { path: '/incidence', component: IncidencePage },
    { path: '/exportfiles', component: ExportDataPage },
    { path: '/videos', component: Videos },
    {path:  '/rodovias', component: Rodovias}
  ]
  
  export default routes