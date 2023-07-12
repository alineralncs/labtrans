<script>
import axios from 'axios';

export default {
    data() {
        return {
            data: [], 

        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8888/rodovias/')
            .then(response => {
                // console.log(response.data);
                this.data = response.data;

            })
            .catch(error => {
                console.error(error);
            });
    },

    
   
  
};
</script>
<template>
        <div v-if="data.length === 0">
            <div class="flex justify-center">
              <div class="loader ease-linear rounded-full border-4 border-t-4 border-gray-200 h-10 w-10 flex justify-start "></div>

            </div>
        </div>
   <div class="flex justify-center h-64 p-3">

  <div class="py-10 pb-3 mt-10 m-1 rounded-xl relative opacity-80 bg-white group hover:bg-purple-200 cursor-pointer transition ease-out duration-300 " v-for="rodovia in data" :key="rodovia.id">
    <h1 class="text-3xl font-bold group-hover:text-purple-300 transition ease-out duration-300">Rodovia - {{rodovia.nome}}</h1>
    <div class="px-7 mt-10">
      <h2 class="text-1xl mt-4 font-bold">Km inicial: {{rodovia.km_ini}} km</h2>
      <p class="mt-2  group-hover:opacity-70">Km final: {{rodovia.km_final}} km</p>
    </div>
  </div>
</div>
</template>