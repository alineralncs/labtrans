<script setup>

</script>

<template>

      <div class="container px-6 py-16 mx-auto text-center">
        <div class="max-w-lg mx-auto">
            <h1 class="text-4xl font-semibold text-gray-800 lg:text-3xl">Segunda fase do processo seletivo LabTrans/UFSC para desenvolvedor back-end </h1>
            <p class="mt-6 text-gray-500 ">Desafio desenvolvido por Aline Rose Alencar Santos</p>
            <button class="px-5 py-2 mt-6 text-sm font-medium leading-5 text-center text-white capitalize bg-violet-600 rounded-lg hover:bg-blue-500 lg:mx-0 lg:w-auto focus:outline-none">
               
                <router-link to="/results"> Ver dados agrupados</router-link>
            </button>
          

           
        </div>
        <button class="px-5 py-2 mt-3 text-sm font-medium leading-5 text-center text-violet-700 capitalize bg-gray-200 rounded-lg hover:bg-blue-500 lg:mx-0 lg:w-auto focus:outline-none">
            <router-link to="/exportfiles"> Exportar dados</router-link>
        </button>
        <div class="flex justify-center mt-10">
            <img class="object-cover w-full h-96 rounded-xl lg:w-4/5" src="http://rodovias.org/wp-content/uploads/2018/03/rodovia-br-116-rs-2.jpg" />
        </div>
    </div>
</template>

