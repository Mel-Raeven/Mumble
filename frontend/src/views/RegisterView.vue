<template>
    <div class="container">
      <particles-bg color="#19E602" num="50" type="cobweb" :canvas="{ backgroundColor: '#363030' }" :bg="true" />
      <form class="loginform">
        <h1 class="title">Mumble</h1>
        <p class="logintitle"> Username</p>
        <input v-model="username" type="text" class="inputfield" required="required"/>
        <p class="logintitle">email</p>
        <input v-model="email" type="email" class="inputfield" required="required"/>
        <p class="logintitle">Password</p>
        <p>insert password</p>
        <input v-model="password" type="password" class="inputfield" required="required"/>
        <p>confirm password</p>
        <input v-model="confPassword" type="password" class="inputfield" required="required"/>
        <button v-on:click="register()" class="loginbutton"> Register </button>
      </form>
    </div>
  </template>
  
  <script>
  import { ParticlesBg } from "particles-bg-vue";
  import axios from 'axios';
  import { ref } from 'vue';
  import router from "@/router";
  
  
  
  export default {
    components: {
      ParticlesBg
    },
    setup() {
      const password = ref('');
      const username = ref('');
      const confPassword = ref('');
      const email = ref('');
  
      async function register() {
        try {
          const response = await axios.post("http://localhost:3000/register", {
            email: email.value,
            password: password.value,
            username: username.value
          });
          if (confPassword.value == password.value){
            const status = JSON.parse(response.status);
          
          if (status == "200") {
            router.push('/Authenticate')
          }
        }
        } catch (error) {
          this.showError = true;
          setTimeout(() => {
            this.showError = false;
          }, 3000);
        }
      }
      return {
        password,
        username,
        confPassword,
        email,
        register,
      }
    }
  }
  
  
  
  
  
  
  
  </script>
    
  <style scoped>
  *{
    background: none;
  }
  .container {
    display: flex;
    justify-content: center;
    align-items: center;
    align-content: center;
    }
  
  .title {
    color: #00ff8e;
    font-size: 60px;
  }
  
  .loginform {
    display: flex;
    flex-direction: column;
    flex-wrap: nowrap;
    align-content: center;
    justify-content: center;
    align-items: center;
    width: 500px;
    background-color: rgb(26, 25, 25);
    border-radius: 3px;
    transform: translate(0, 15%);
  }
  
  .logintitle {
    font-size: 30px;
    font-weight: lighter;
    font-family: Arial, Helvetica, sans-serif;
    margin: 5px;
    color: white;
  }
  
  .loginbutton {
    width: 20em;
    height: 3em;
    border: none;
    background-color: black;
    color: rgb(133, 133, 133);
    border-radius: 5px;
    margin: 20px;
    font-size: 20px;
    font-family: Arial, Helvetica, sans-serif;
    margin-top: 5rem;
  }
  
  .loginbutton:hover {
    color: black;
    background-color: #00ff8e;
  }
  
  .inputfield {
    background-color: rgb(20, 20, 20);
    border: none;
    height: 50px;
    width: 20rem;
    color: grey;
    font-size: 15px;
    border-radius: 5px;
    color: white;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 18px;
    margin-bottom: 2rem;
  
  }
  </style>
    