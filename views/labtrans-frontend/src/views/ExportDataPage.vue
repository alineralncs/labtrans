<script>
import axios from 'axios';

export default {
  data() {
    return {
      files: []
    };
  },
  mounted() {
    this.getCSVFiles();
  },
  methods: {
    getCSVFiles() {
      axios.get('http://localhost:8888/results/files')
        .then(response => {
          this.files = response.data.files;
        })
        .catch(error => {
          console.error(error);
        });
    },
    getFileURL(file) {
      return `http://localhost:8888/files/download/${encodeURIComponent(file)}`;
    }
  }
};
</script>

<template>
  <div>

    <div class=" h-screen w-screen">

      <div class="flex flex-col items-center flex-1 h-full justify-center px-4 sm:px-0">

        <div class="flex rounded-2xl shadow-lg w-full sm:w-3/4 lg:w-1/2 bg-white sm:mx-0" style="height: 500px">

          <div class="w-full mt-4">
            <h1 class="mb-4 text-2xl font-normal md:text-3xl lg:text-4xl text-center">
              <span class="font-semibold">Dados</span> em <span class="font-semibold">csv</span>
            </h1>
            <div v-if="files.length === 0">
              <div class="flex justify-center">
                <div
                  class="loader ease-linear rounded-full border-4 border-t-4 border-gray-200 h-10 w-10 flex justify-start ">
                </div>

              </div>
            </div>
            <div
              class="flex justify-start cursor-pointer bg-slate-50 text-gray-700 hover:text-violet-400 hover:bg-violet-50 rounded-md px-2 py-2 my-2 m-10"
              v-for="file in files" :key="file">

              <span class="bg-green-400 h-2 w-2 m-2 rounded-full ">
              </span>
              <div class="flex-grow font-medium px-2"> {{ file }}</div>
              <div
                class="text-sm font-normal text-gray-50 tracking-wide hover:text-white-100 hover:bg-violet-700 bg-violet-400 p-2 rounded-full ">

                <a :href="getFileURL(file)" download>
                  Download
                  <!-- <svg xmlns="http://www.w3.org/2000/svg" height="1em" fill="#22c55e"
                    viewBox="0 0 512 512">
                    <path
                      d="M256 0a256 256 0 1 0 0 512A256 256 0 1 0 256 0zM376.9 294.6L269.8 394.5c-3.8 3.5-8.7 5.5-13.8 5.5s-10.1-2-13.8-5.5L135.1 294.6c-4.5-4.2-7.1-10.1-7.1-16.3c0-12.3 10-22.3 22.3-22.3l57.7 0 0-96c0-17.7 14.3-32 32-32l32 0c17.7 0 32 14.3 32 32l0 96 57.7 0c12.3 0 22.3 10 22.3 22.3c0 6.2-2.6 12.1-7.1 16.3z" />
                  </svg> Download -->
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

