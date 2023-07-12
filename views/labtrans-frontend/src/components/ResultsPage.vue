<script>
import axios from 'axios';

export default {
    data() {
        return {
            data: [], 
            rodoviasUnicas: [],
            dadosFiltrados: []
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8888/results/')
            .then(response => {
                // console.log(response.data);
                this.data = response.data;
                this.rodoviasUnicas = this.data.map(item => item.highway).filter((value, index, self) => self.indexOf(value) === index);

            })
            .catch(error => {
                console.error(error);
            });
    },
    methods: {
        mostrarRodovia(rodovia) {
            this.dadosFiltrados = this.data.filter(item => item.highway === rodovia);
            // const dados = this.data;

            // dados.forEach(item => {
            //     console.log(item.highway);
            // });
        },
    
    },
  
};

</script>


<template>
 
        <div class="flex justify-center pt-4 " >
            <div class="text-xs px-3 m-2 cursor-pointer hover:bg-purple-600 hover:text-white bg-purple-200 w-20 p-2 text-center text-purple-800 rounded-full" v-for="rodovia in rodoviasUnicas" :key="rodovia" @click="mostrarRodovia(rodovia)">
               Rodovia  {{ rodovia }}

            </div>

        </div>


    <div class="w-full max-w-screen-xl mx-auto px-6">
        <div v-if="data.length === 0">
            <div class="flex justify-center">
              <div class="loader ease-linear rounded-full border-4 border-t-4 border-gray-200 h-10 w-10 flex justify-start "></div>

            </div>
        </div>
        <div class="flex justify-center p-4 px-3 py-10" v-show="data.length > 0">
         
            <div class="w-full ">
         
                <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
        
                    <table class="w-full text-sm text-left text-gray-500 ">
                        <thead class="text-xs text-gray-100 uppercase bg-violet-600  ">
                            <tr>
                                <th scope="col" class="px-6 py-3">
                                    Rodovia
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    KM
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    Buraco
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    Remendo
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    Trinca
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    Placa
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    Drenagem
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="bg-white border-b " v-for="item in dadosFiltrados" :key="item.id">
                                <th scope="row"
                                    class="px-6 py-4 font-medium   hover:underline whitespace-nowrap ">
                                    <span class="bg-violet-400 text-white p-2 rounded">
                                        {{ item.highway }}
                                    </span>
                                   
                                </th>
                                <td class="px-6 py-4">
                                    {{ item.km }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ item.buraco }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ item.remendo }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ item.trinca }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ item.placa }}
                                </td>
                                <td class="px-6 py-4">
                                    <a href="#" class="">{{ item.drenagem }}</a>
                                </td>
                            </tr>


                        </tbody>
                    </table>

                </div>
            </div>
        </div>
    </div>
</template>