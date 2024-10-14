<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import skilldomain from '../components/SkillDomain.vue';
import addskilldomain from '../components/AddSkillDomain.vue';

const skills_domains_array = ref([])

function getSkillsDomains() {
  axios
    .get('/api/v1/skilldomains/')
    .then(response => {
      console.log('response', response)
      skills_domains_array.value = response.data
    })
    .catch(error => {
      console.error('Failed to fetch skill domains:', error);
    });
}

function addDomainToList(newDomain) {
  skills_domains_array.value.push(newDomain)
  console.log('skills_domains_array.value', skills_domains_array.value)
}

function removeDomainFromList(id) {
  const index = skills_domains_array.value.findIndex(domain => domain.id === id);
  if (index !== -1) {
    skills_domains_array.value.splice(index, 1);
  } else {
    console.warn(`Domain with id ${id} not found in the array.`);
  }
}

function updateSkillDomainData(id, index) {
  console.log('id', id)
  axios
    .get(`/api/v1/skilldomains/${id}/`)
    .then(response => {
      console.log('response', response)
      skills_domains_array.value[index] = response.data
    })
    .catch(error => {
      console.error(`Failed to update domain with id ${id}:`, error);
    });
}

onMounted(() => {
  getSkillsDomains();
})
</script>

<template>
  <div class="container">
    <div id="skill-domain-card-container">
      <skilldomain v-for="(domain, index) in skills_domains_array" :key="domain.id" :id="domain.id" :name="domain.name"
        :color="domain.color" :techniquesId="domain.techniques" @domain-deleted="removeDomainFromList(domain.id)"
        @color-updated="updateSkillDomainData(domain.id, index)"></skilldomain>
      <addskilldomain v-if="skills_domains_array.length < 6" @domain-added="addDomainToList"></addskilldomain>
    </div>
  </div>
</template>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 2.5vw;
}

.description-card {
  background-color: #3F494B;
  color: #f8f6ec;
  width: 90vw;
  height: 8vw;
  border-radius: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 2vw;
  margin-top: 2vw;
}

#skill-domain-card-container {
  display: grid;
  grid-gap: 1vw;
  grid-template-columns: repeat(3, 1fr);
}
</style>