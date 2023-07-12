<script setup>
import Rodovias from './Rodovias.vue'
</script>

<template>

      <div class="container px-6 py-16 mx-auto text-center">
        <div class="max-w-lg mx-auto">
            <!-- <h1 class="text-4xl font-semibold text-gray-800 lg:text-3xl">Segunda fase do processo seletivo LabTrans/UFSC para desenvolvedor back-end </h1>
            <p class="mt-6 text-gray-500 ">Desafio desenvolvido por Aline Rose Alencar Santos</p> -->
            <button class="px-5 py-2 mt-6 text-sm font-medium leading-5 text-center text-white capitalize bg-violet-600 rounded-lg hover:bg-violet-500 lg:mx-0 lg:w-auto focus:outline-none">
               
                <router-link to="/results"> Ver dados agrupados</router-link>
            </button>
          

           
        </div>
        <button class="px-5 py-2 mt-3 text-sm font-medium leading-5 text-center text-violet-700 capitalize bg-gray-200 rounded-lg hover:bg-violet-500 lg:mx-0 lg:w-auto focus:outline-none">
            <router-link to="/exportfiles"> Exportar dados</router-link>
        </button>
        <div class="flex justify-center mt-10 rounded-xl "  style="background: url('https://images.unsplash.com/photo-1566054299976-3eb6f6a44ead?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'); background-size: cover; background-position: center center; height: 24rem;">
            <Rodovias />
        </div>

        
    </div>
</template>

