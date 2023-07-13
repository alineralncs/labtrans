<script>
import axios from 'axios';

export default {
    data() {
        return {
            data: [], 
            videosUnicos: [],
            dadosFiltrados: []
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8888/videos/')
            .then(response => {
                // console.log(response.data);
                this.data = response.data;
                this.dadosFiltrados = this.data;
                this.videosUnicos = this.data.map(item => item.video).filter((value, index, self) => self.indexOf(value) === index);

            })
            .catch(error => {
                console.error(error);
            });
    },
    methods: {
        mostrarVideo(video) {
            this.dadosFiltrados = this.data.filter(item => item.video === video);
        },
    
    },
  
};

</script>

<template>
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
                        <thead class="text-xs text-gray-100 uppercase bg-violet-400  ">
                            <tr>
                                <th scope="col" class="px-6 py-3">
                                    Video
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    KM Inicial
                                </th>
                                <th scope="col" class="px-6 py-3">
                                    KM Final
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="bg-white border-b " v-for="item in dadosFiltrados" :key="item.id">
                                <th scope="row"
                                    class="px-6 py-4 font-medium   hover:underline whitespace-nowrap ">
                                    <span class="bg-violet-400 text-white p-2 rounded">
                                        {{ item.nome }}
                                    </span>
                                   
                                </th>
                                <td class="px-6 py-4">
                                    {{ item.km_ini }}
                                </td>
                                <td class="px-6 py-4">
                                    {{ item.km_final }}
                                </td>
            
                            </tr>


                        </tbody>
                    </table>

                </div>
            </div>
        </div>
    </div>
</template>