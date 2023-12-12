<template>
<v-app>
  <div class="search-page">
    <div class="outer-container">
      <div class="inner-container">
        <img src="@/assets/steamhunter-logo.png" alt="SteamHunter Logo" class="steamhunter-logo">
        <h1 class="logo-text">SteamHunter</h1>
        <div class="search-container">
          <input v-model="searchQuery" @input="search" class="search-bar" placeholder="Search in SteamHunter">
          <button @click="search" class="search-button">
            <img src="@/assets/searchIcon.png" alt="Search Icon" class="search-icon">
          </button>
        </div>
      </div>
    </div>
  </div>
</v-app>
</template>

<style scoped>

v-app{
  align:center;
  display:flex;
}

.search-page {
  position: relative;
  background-color: #171a21;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  width: 100vw;
}

.background-image {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  opacity: 0.5; /* Adjust the opacity as desired */
}

.outer-container .search-page {
  display: flex;
  justify-content: center;
}

.inner-container {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.steamhunter-logo {
  width: 150px;
  height: auto;
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
  height: auto;
}
</style>