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
     <!-- <ul>
      <li v-for="item in data" :key="item.id">
        {{ item }}
      </li>
    -->
    <!-- <div class="px-4 md:px-10 py-4 md:py-7">
                <div class="flex items-center justify-between "> -->
        <div class="w-full max-w-screen-xl mx-auto px-6">
        <div class="flex justify-center p-4 px-3 py-10">
            <div class="w-full ">
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-blue-50 dark:bg-gray-700 dark:text-gray-400">
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
            <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700" v-for="item in data" :key="item.id">
                <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    {{ item.highway }}
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
                    <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">{{ item.drenagem }}</a>
                </td>
            </tr>
     
           
        </tbody>
    </table>
</div>
</div>
</div>
</div>
</template>