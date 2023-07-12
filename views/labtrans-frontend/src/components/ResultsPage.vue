<script>
import axios from 'axios';

export default {
    data() {
        return {
            data: []
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8888/results/')
            .then(response => {
                console.log(response.data); // Check the response data
                this.data = response.data;
            })
            .catch(error => {
                console.error(error);
            });
    }
};

</script>


<template>

    <div class="w-full max-w-screen-xl mx-auto px-6">
        <div class="flex justify-center p-4 px-3 py-10">
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
                            <tr class="bg-white border-b " v-for="item in data" :key="item.id">
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