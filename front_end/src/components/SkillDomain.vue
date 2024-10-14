<script setup>
import { onMounted, ref, watch } from 'vue';
import axios from 'axios';
import addTechnique from '../components/AddTechnique.vue';

const techniques = ref([])

const props = defineProps({
  id: Number,
  name: String,
  color: String,
  techniquesId: Array
})

const hover = ref(null);
const color = ref(props.color)

const emit = defineEmits(['domain-deleted', 'color-updated'])

function getTechniques() {
  for (let i = 0; i < props.techniquesId.length; i++) {
    let id = props.techniquesId[i]
    axios
      .get('/api/v1/techniques/?id=' + id)
      .then(response => {
        techniques.value.push({ 'id': id, 'name': response.data.name })
      })
      .catch(error =>
        console.log(error)
      )
  }
}

function addTechniqueToList(newTechnique) {
  techniques.value.push(newTechnique)
}

function deleteSkillDomain() {
  axios.delete(`/api/v1/skilldomains/${props.id}/`)
    .then(response => {
      console.log('Domain deleted')
      emit('domain-deleted', props.id)
    })
    .catch(error => {
      console.error('Error deleting domain', error)
    })
}

function deleteTechnique(techniqueId) {
  axios.delete(`/api/v1/techniques/${techniqueId}/`)
    .then(response => {
      console.log('Technique deleted')
      for (let i = 0; i < techniques.value.length; i++) {
        if (techniques.value[i].id === techniqueId) {
          techniques.value.splice(i, 1);
          break;
        }
      }
    })
    .catch(error => {
      console.error('Error deleting technique', error)
    })
}

function updateColor(event) {
  color.value = event.target.value;
  saveColorChange(color.value)
  emit('color-updated');
}

function saveColorChange(newColor) {
  let data = {name: props.name, color: newColor}
  axios.put(`/api/v1/skilldomains/${props.id}/`, data)
  .then(response => {
    console.log('response', response)
  })
  .catch(error => {
    console.log(error)
  });
}

onMounted(() => {
  getTechniques();
})

watch(() => props.color, (newColor) => {
  color.value = newColor;
});
</script>

<template>
  <div class="skill-domain-card">
    <div class="color-display-wrapper">
      <input type="color" class="color-display" :value="props.color" @input="updateColor" :style="{ 'border': '1.1vw solid ' + props.color }"/>
    </div>
    <img src="/trash-icon.png" class="delete-domain-icon" @click="deleteSkillDomain">
    <h1 class="domain-name"> {{ name }} </h1>
    <ul class="technique-wrapper">
      <li v-for="technique in techniques" :key="technique.id" @mouseover="hover = technique.id"
        @mouseleave="hover = null" :class="{ 'technique-hovered': hover === technique.id }">
        {{ technique.name }}
        <img src="/trash-icon.png" class="delete-technique-icon" @click="deleteTechnique(technique.id)"
        v-if="hover === technique.id">
      </li>
      <div v-if="techniques.length < 6" class="add-technique-wrapper">
        <addTechnique :domainId="id" @technique-added="addTechniqueToList" class="add-technique"> </addTechnique>
      </div>
    </ul>
  </div>
</template>

<style>
.skill-domain-card {
  position: relative;
  background-color: #f8f6ec;
  width: 25vw;
  border-radius: 20px;
  margin: 1vw;
  text-align: center;
  border: 0.5vw solid #3F494B;
  color: #3F494B;
}

.color-display-wrapper {
  position: absolute;
  left: 1%;
  top: 1%;
}

.color-display-wrapper:hover {
  border-bottom: solid #925040;
  padding-bottom: 0.1vw;
}

.color-display {
  transition: 0.5s linear;
  width: 3vw;
  height: 2vw;
  border-radius: 20px;
  padding: 0;
}

.color-display:hover {
  cursor: pointer;
}

.delete-domain-icon {
  position: absolute;
  right: 1%;
  top: 1%;
  height: 2vw;
}

.delete-domain-icon:hover {
  cursor: pointer;
}

.domain-name {
  padding: 0;
  margin: 0.5vw;
}

.technique-wrapper {
  margin: 0;
  padding: 0;
  list-style: none;
}

.technique-wrapper li {
  font-size: x-large;
  margin: 0.2vw;
}

.technique-hovered {
  font-weight: bold;
}

.delete-technique-icon {
  height: 1vw;
}

.delete-technique-icon:hover {
  cursor: pointer;
}

.add-technique-wrapper {
  margin: 1vw;
}
</style>
