<template>
  <section class="search-page">
        <img src="@/assets/steamhunter-logo.png" alt="SteamHunter Logo" class="steamhunter-logo">
        <h1 class="logo-text">SteamHunter</h1>

          <div class="search-container">
            <div class="search-form" id="name-form">
              <input v-model="query" @input="search" class="search-bar" placeholder="Search for a Videogame!">
            </div>
          </div>
        <div class="search-container">
          <div class="rows-form" id="rows-button">
            <input v-model="rows" @input="search" class="search-bar" placeholder="Nº Results">
            <button @click="searchSolr()" class="search-button">
              <img src="@/assets/searchIcon.png" alt="Search Icon" class="search-icon">
            </button>
          </div>
        </div>
      </section>
      <div v-if="this.$data['response'].length === 0" class="results"></div>
      <section v-else>
        <table class="results">
          <tr><th>Name</th><th>About the Game</th><th>Positive Reviews</th><th>Negative Reviews</th><th>Recommendations</th></tr>
          <tr v-for="doc in this.$data['documents']">
            <td>{{doc['name']}}</td><td>{{abbreviateText(doc['about_info'][0],400)}}</td><td>{{doc['positive'][0]}}</td><td>{{doc['negative'][0]}}</td><td>{{doc['recommendations'][0]}}</td>
          </tr>
        </table>
      </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      rows: 10,
      query: '',
      response: [],
      documents: [],
    };
  },
  methods: {
    async searchSolr() {
      //console.log("Query: " + this.$data['query'])
      //console.log("Rows: " + this.$data['rows'])
      try {
        const solrEndpoint = 'http://localhost:8983/solr/games/select?';
        const response = await axios.get(solrEndpoint, {
          params: {
            q: 'name:' + this.$data['query'] + ',\nabout_info:' + this.$data['query'],
            rows: this.$data['rows'],
          },
        });
        this.$data['response'] = response;
        this.$data['documents'] = response.data['response']['docs'];
        // Handle the Solr response
        console.log('Solr Response:', response.data);
        console.log('Solr Documents:', response.data['response']['docs'])
      } catch (error) {
        console.error('Error making Solr request:', error);
        if (error.response) {
          console.log('Error response from Solr:', error.response.data);
          console.log('Status code:', error.response.status);
          console.log('Headers:', error.response.headers);
        } else if (error.request) {
          console.log('No response received from Solr. Request made but no response received.');
          console.log('Request details:', error.request);
        } else {
          console.log('Error setting up the Solr request:', error.message);
        }
      }
    },
    abbreviateText(text,length) {
      let newText = text.substr(0,length) + '...'
      return newText;
    },
  },
};
</script>

<style scoped>

.search-page {
  background-color: #171a21;
  color: #fff;
  justify-content: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 80%; /* Set height to full viewport height */
  width: 100%;
}

.steamhunter-logo {
  width: 150px;
  height: 150px;
}

.logo-text {
  font-size: 24px;
  margin-top: 10px;
}

.search-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 20px;
}

.search-bar {
  width: 400px;
  height: 40px;
  padding: 10px;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  margin-bottom: 10px;
}

.search-button {
  background-color: #4a90e2;
  height: 40px;
  color: #fff;
  border: none;
  border-radius: 5px;
  padding: 10px;
  cursor: pointer;
  width: 100px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.search-icon {
  width: 20px;
  height: 20px;
}

input {
  margin-left: 10px;
  margin-right: 10px;
  margin-top: auto;
  margin-bottom:auto;
}

#genres-categories input, #developers-publishers input {
  width: 190px;
  align-items: center;
  justify-content: center;
}

#rows-button input, #rows-button button {
  width: 100px;
  align-items: center;
  justify-content: center;
  flex-direction: line;
}

.results {
  margin-top: 20px;
  text-align: center;
  color: #fff;
  font-size: 18px;
}

.results table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

.results th, .results td {
  border: 1px solid #4a90e2;
  padding: 10px;
}

.results th {
  background-color: #4a90e2;
  color: #fff;
  font-weight: bold;
}

.results td {
  background-color: #1e2a38;
  color: #fff;
}

.results tr:nth-child(even) td {
  background-color: #233040;
}

.results tr:hover td {
  background-color: #33455e;
}
</style>