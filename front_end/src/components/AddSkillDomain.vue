<script setup>
import { ref } from 'vue';
import axios from 'axios';

const newDomainName = ref('')

function addNewSkillDomain() {
  const data = {
    name: newDomainName.value,
    techniques: []
  }
  axios.post('/api/v1/skilldomains/', data)
    .then(response => {
      console.log('Skill domain added', response.data)
      emit('domain-added', response.data)
      newDomainName.value = ''
    })
    .catch(error => {
      console.error('Error adding skill domain', error)
    })
}

const emit = defineEmits(['domain-added'])
</script>

<template>
  <div class="add-skill-domain-card">
    <h1> Add a new Skill Domain</h1>
    <span>
      <input v-model="newDomainName" placeholder="New Skill Domain Name" class="domain-name-input"> </input>
      <button type="button" @click="addNewSkillDomain" id="add-domain-button"> Add </button>
    </span>
  </div>
</template>

<style>
.add-skill-domain-card {
  position: relative;
  background-color: #f8f6ec;
  width: 25vw;
  border-radius: 20px;
  margin: 1vw;
  text-align: center;
  border: 0.5vw solid #925040;
  color: #925040;
}

#add-domain-button {
  margin: 0.5vw;
  height: 1.5vw;
}

.domain-name-input {
  border: solid #925040;
  background-color: #d9d9d9;
}
</style>
