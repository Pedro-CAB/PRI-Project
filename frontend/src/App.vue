<template>
  <section class="search-page">
        <img src="@/assets/steamhunter-logo.png" alt="SteamHunter Logo" class="steamhunter-logo">
        <h1 class="logo-text">SteamHunter</h1>
        <h2 class="logo-text">Standard Search</h2>
          <div class="search-container">
            <div class="search-form" id="name-form">
              <input v-model="standard" @input="search" class="search-bar" placeholder="Search for a Videogame!">
            </div>
          </div>
        <h2 class="logo-text">Advanced Search</h2>
        <div class="search-container">
          <div class="search-form" id="name">
            <input v-model="name" @input="search" class="search-bar" placeholder="Name">
          </div>
          <div class="search-form" id="genres-categories">
            <input v-model="genres" @input="search" class="search-bar" placeholder="Genre">
            <input v-model="categories" @input="search" class="search-bar" placeholder="Category">
          </div>
          <div class="search-form" id="language">
            <input v-model="languages" @input="search" class="search-bar" placeholder="Language">
          </div>
          <div class="search-form" id="developers-publishers">
            <input v-model="developers" @input="search" class="search-bar" placeholder="Developer">
            <input v-model="publishers" @input="search" class="search-bar" placeholder="Publisher">
          </div>
          <div class="rows-form" id="rows-button">
            <input v-model="rows" @input="search" class="search-bar" placeholder="Nº Results">
            <button @click="searchSolr()" class="search-button">
              <img src="@/assets/searchIcon.png" alt="Search Icon" class="search-icon">
            </button>
            <button @click="redirectToResults">Go to Results</button>
          </div>
        </div>
      </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      genres: '',
      categories: '',
      languages: '',
      developers: '',
      publishers: '',
      tags: '',
      rows: 10,
      standard: '',
    };
  },
  methods: {
    async searchSolr() {
      let query = '';
      let first = true;
      if(this.$data['standard']){
        query = 'name:' + this.$data['standard'] + ',\nabout_info:' + this.$data['standard'] + ',\ntags:' + this.$data['standard'];
      }
      else{
        for (const key in this.$data) {
        if (first && this.$data.hasOwnProperty(key) && this.$data[key] !== '' && key != 'rows' && key != 'standard'){
          query = `${key}:${this.$data[key]}`;
          first = false;
        }
        else if (this.$data.hasOwnProperty(key) && this.$data[key] !== '' && key != 'rows' && key != 'standard') {
          query += `,\n${key}:${this.$data[key]}`;
        }
      }
      }
      console.log("Query: " + query)
      console.log("Rows: " + this.$data['rows'])
      try {
        const solrEndpoint = 'http://localhost:8983/solr/games/select?';
        const response = await axios.get(solrEndpoint, {
          params: {
            q: query,
            rows: this.$data['rows'],
          },
        }
        );
        // Handle the Solr response
        console.log('Solr Response:', response.data);
        // Redirect to the result page with the response data
        this.$router.push({
          name: 'result',
          params: { responseData: response.data },
        });
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
    redirectToResults() {
      // Assuming you have some data to send, let's say an ID
      const id = 123; // Replace with your actual data

      // Use router.push to navigate to the destination page with data
      this.$router.push({ name: 'result', params: { id } });
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
</style>