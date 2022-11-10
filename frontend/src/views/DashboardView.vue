<template>
    <div class="container">
        <button v-on:click="logout()" class="logoutbutton"></button>
    </div>
  </template>
  
  <script>
  
  
  export default {
    setup() {
        function logout(){
            localStorage.removeItem('token');
            window.location.reload();
        }
        return{
            logout
        }
    }
  }
  
  
  
  
  
  
  
  </script>
    
  <style scoped>
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    align-content: center;
  }
 
  .logoutbutton{
    width: 20rem;
    height: 20rem;
  }
  </style>
    