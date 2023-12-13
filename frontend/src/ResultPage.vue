<template>
    <div class="result-page">
      <h1 class="logo-text">Search Results</h1>
      <div class="result-container">
        <pre>{{ responseData }}</pre>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      responseData: {
        type: Object,
        required: true,
      },
    },
  };
  </script>
  
  <style scoped>
    /* Your styling for the result page */
  </style>