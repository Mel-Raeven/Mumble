<template>
  <div class="container">
    <form>
      <h1>Whats your friends name?</h1>
      <input v-model="username" type="text" class="inputfield" />
      <button>Send request</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  methods: {
    async sendInvite(){
      try {
        const response = await axios.post("http://localhost:3000/message/post", {
          content: this.message,
          destination: this.currentChat,
          from: this.decodedtoken.username
        });
        const status = JSON.parse(response.status);
        if (status == "200") {
         this.getMessages()
        }
      } catch (error) {
        this.showError = true;
        setTimeout(() => {
          this.showError = false;
        }, 3000);
      }
    },
  }
}
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
}

.container {
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  align-content: center;
  background-color: #363030;
}

h1 {
  color: #00ff8e;
  font-size: 40px;
  margin: 20px;
  margin-bottom: 5rem;
}

form {
  display: flex;
  flex-direction: column;
  flex-wrap: nowrap;
  align-content: center;
  justify-content: center;
  align-items: center;
  width: 500px;
  background-color: rgb(26, 25, 25);
  border-radius: 3px;
}

button {
  border: none;
  background-color: black;
  padding: 10px;
  color: whitesmoke;
  border-radius: 5px;
  font-size: 20px;
  font-family: Arial, Helvetica, sans-serif;
  margin-bottom: 1rem;
}

button:hover {
  color: black;
  background-color: #00ff8e;
}

.inputfield {
  background-color: black;
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