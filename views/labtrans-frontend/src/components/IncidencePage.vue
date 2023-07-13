  <template>
  <div class=" h-screen w-screen" v-if="results">
    <div class="flex flex-col items-center flex-1 h-full justify-center px-4 sm:px-0">
      <div class="flex rounded-2xl shadow-lg w-full sm:w-3/4 lg:w-1/2 bg-white sm:mx-0" style="height: 500px">
        <div class="flex flex-col w-full md:w-1/2 p-4">
          <div class="flex flex-col flex-1 justify-center mb-8">
            <h1 class="text-3xl text-center">Consultar ocorrência de itens</h1>

            <h1 class="text-center font-thin">Aqui você consegue consultar qual km aparece a maior quantidade de Itens (Buraco, Remendo, Trinca, Drenagem)</h1>
            <div class="w-full mt-4">
              <form class="form-horizontal w-3/4 mx-auto" @submit="submitForm">
                <div class="flex flex-col mt-4">
                  <input type="text" v-model="inputValue"
                    class="flex-grow rounded-full h-8 p-6 px-6  border border-grey-700 focus:border-blue-100"
                    placeholder="Qual item deseja consultar?" />
                </div>

                <div class="flex flex-col mt-8">
                  <button type="submit"
                    class="bg-violet-500 hover:bg-violet-700 text-white text-sm font-semibold py-2 px-4 rounded-full">Consultar</button>

                </div>
              </form>

            </div>
          </div>
        </div>
        <div class="block md:inline md:w-1/2 rounded-r-lg"
          style="background: url('https://images.unsplash.com/photo-1566054299976-3eb6f6a44ead?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=687&q=80'); background-size: cover; background-position: center center;">

          <div
            class="flex justify-start cursor-pointer bg-slate-50 text-gray-700 hover:text-blue-400 hover:bg-blue-100 rounded-md px-2 py-2 my-2 m-10">
            <span class="bg-green-400 h-2 w-2 m-2 rounded-full"></span>
            <div class="flex-grow font-medium px-2">{{ results.km_maior_incidencia }} </div>
            <div class="text-sm font-normal text-gray-500 tracking-wide">KM</div>
          </div>
          <div
            class="flex justify-start cursor-pointer bg-slate-50 text-gray-700 hover:text-blue-400 hover:bg-blue-100 rounded-md px-2 py-2 my-2 m-10">
            <span class="bg-red-400 h-2 w-2 m-2 rounded-full"></span>
            <div class="flex-grow font-medium px-2">{{ results.incidencia }}</div>
            <div class="text-sm font-normal text-gray-500 tracking-wide">Ocorrências</div>
          </div>
          <div
            class="flex justify-start cursor-pointer bg-slate-50 text-gray-700 hover:text-blue-400 hover:bg-blue-100 rounded-md px-2 py-2 my-2  m-10">
            <span class="bg-blue-400 h-2 w-2 m-2 rounded-full"></span>
            <div class="flex-grow font-medium px-2">{{ results.rodovia }}</div>
            <div class="text-sm font-normal text-gray-500 tracking-wide">Rodovia</div>
          </div>
        </div>
      </div>
  </div>
</div>

</template>
  
<script>
import axios from 'axios';

export default {
  data() {
    return {
      inputValue: '',
      results: []
    };
  },
  methods: {
    submitForm(event) {
      event.preventDefault();

      axios.get(`http://127.0.0.1:8888/results/incidence/${encodeURIComponent(this.inputValue)}`)
        .then(response => {
          this.results = response.data;
          console.log(this.results = response.data)
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>