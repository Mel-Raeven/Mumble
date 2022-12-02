<template>
  <div class="container">
    <div class="menubar">
      <button v-on:click="$router.push('/FriendRequest')" class="menubutton">Friend invite</button>
      <button v-on:click="logout()" class="menubutton">Logout</button>
    </div>
    <div class="modulesContainer">
      <div class="friendbar">
        <h1 class="friendsheader">{{decodedtoken.username}}'s friends</h1>
        <div class="friendscontainer">
          <h1 v-on:click="openChat('piet')">piet</h1>
          <h1 v-on:click="openChat('sjef')">sjef</h1>
          <h1 v-on:click="openChat('admin')">admin</h1>
        </div>
      </div>
      <div class="messageContainer">
        <button v-on:click="getMessages()"> Refresh </button>
        <div class="messages">
          <div v-for="message in messageList[0]" :key="message" style="width:100%;">
            <div class="messageUserContainer">
              <h2 class="messagesContent" v-if="(message[0][2] == decodedtoken.username)">{{message[0][1]}}</h2>
            </div>
            <div class="messageFriendContainer">
              <h2 class="messagesContentFriend" v-if="(message[0][2] != decodedtoken.username)">{{message[0][1]}}</h2>
            </div>
          </div>
        </div>
        <form class="inputForm">
          <input v-model="message" type="text" class="messageInput" required="required">
          <button v-on:click="postMessage()" class="submitMessage"> Send </button>
        </form>
      </div>
    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
import router from "@/router";
const jose = require('jose')

export default {
  data(){
    return{
      messageList:[],
      currentChat: "",
      message: "",
      decodedtoken: ""
    }
  },
  mounted(){
    this.decodedtoken = jose.decodeJwt(localStorage.getItem('token'))
  },
  methods: {
    logout() {
      localStorage.removeItem('token');
      router.push('/Authenticate')
    },

     async postMessage(){
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

    async getMessages(){
      try {
        const response = await axios.post("http://localhost:3000/message/get", {
          friend: this.currentChat,
          user: this.decodedtoken.username
        });
        const status = JSON.parse(response.status);
        if (status == "200") {
          this.messageList.length = 0
          this.messageList.push(response.data)
          console.log(this.messageList[0]);
        }
      } catch (error) {
        this.showError = true;
        setTimeout(() => {
          this.showError = false;
        }, 3000);
      }
    },

    openChat(friend){
      this.currentChat = friend;
      this.getMessages();
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
  background-color: #363030;
}

.menubar {
  display: flex;
  width: 100%;
  height: 6%;
  flex-direction: row;
  background-color: #1e1f1e;
  flex-wrap: wrap;
  justify-content: flex-end;
  align-items: center;
}

.menubutton {
  width: 8rem;
  height: 100%;
  border: none;
  background-color: #1e1f1e;
  color: whitesmoke;
  border-radius: 5px;
  font-size: 20px;
  font-family: Arial, Helvetica, sans-serif;
  margin-left: 20px;
}

.menubutton:hover {
  color: black;
  background-color: #00ff8e;
}

.modulesContainer{
  display: flex;
  height: 94%;
  width: 100%;
}

.friendbar{
  display: flex;
  height: 100%;
  width: 20rem;
  background-color: #1e1f1e;
  justify-content: flex-start;
  flex-direction: column;
  align-items: center;
}

.friendsheader{
  color: #00ff8e;
  margin-bottom: 10px;
}

.friendscontainer{
  display: flex;
  flex-direction: column;
}

.friendscontainer h1{
  margin-top: 20px;
}

.messageContainer{
  display: flex;
  height: 100%;
  width: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  justify-content: flex-end;
  flex-direction: column;
  align-items: center;
  overflow-x: hidden;
  overflow-y: auto;
}

.messageInput{
  width: 100%;
  background-color: black;
  height: 3rem;
  border-radius: 20px;
  color: white;
  font-size: 1rem;
  margin-bottom: 10px;
  margin-top: 10px; 
  border: none;
}

.messageInput:focus {
  outline-color: #00ff8e;
  outline-offset: 0.4rem;
}

.messages{
  display: flex;
  width: 98%;
  height: 90%;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
}

.messageUserContainer{
  width: 100%;
  display: flex;
  justify-content: flex-end;
}

.messageFriendContainer{
  width: 100%;
  display: flex;
  justify-content: flex-start;
}

.messagesContent{
  color: white;
  background-color: #1e1f1e;
  padding: 20px;
  padding-top: 8px;
  padding-bottom: 8px;
  border-radius: 5px;
  margin: 10px
}

.messagesContentFriend{
  color: black;
  background-color: #00ff8e;
  padding: 20px;
  padding-top: 8px;
  padding-bottom: 8px;
  border-radius: 5px;
  margin: 10px
}

.inputForm{
  width: 70%;
  display: flex;
  flex-direction: row;
  align-items: center;
  position:fixed;
  
}

.submitMessage{
  height: 3rem;
  width: 3rem;
  margin: 5px;
  border-radius: 100%;
  background-color: black;
  color: #00ff8e;
  border: none;
}
</style>
    