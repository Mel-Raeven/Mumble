<template>
  <div class="container">
    <div class="menubar">
      <button v-on:click="$router.push('/FriendRequest')" class="menubutton">Friend invite</button>
      <button v-on:click="logout()" class="menubutton">Logout</button>
    </div>
    <div class="friendbar">
      <h1 class="friendsheader">{{decodedtoken['username']}}'s friends</h1>
      <div class="friendscontainer">
      </div>
    </div>
  </div>
</template>
  
<script>


export default {
  setup() {
    const jose = require('jose')
    const decodedtoken = jose.decodeJwt(localStorage.getItem('token'))
    function logout() {
      localStorage.removeItem('token');
      window.location.reload();
    }
    return {
      logout,
      decodedtoken
    }
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

.friendbar{
  display: flex;
  height: 94%;
  width: 20rem;
  background-color: #1e1f1e;
  justify-content: center;
}

.friendsheader{
  color: #00ff8e;
}
</style>
    