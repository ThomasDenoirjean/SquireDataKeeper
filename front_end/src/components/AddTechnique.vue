<script setup>
import { ref } from 'vue';
import axios from 'axios';

const newTechniqueName = ref('')

const props = defineProps({
    domainId: Number,
})

function addNewTechnique() {
    const data = {
        name: newTechniqueName.value,
        domain: props.domainId
    }

    axios.post('/api/v1/techniques/', data)
        .then(function (response) {
            console.log('Technique added', response.data)
            emit('technique-added', response.data)
            newTechniqueName.value = ''
        })
        .catch(function (error) {
            console.log(error);
        });
}

const emit = defineEmits(['technique-added'])
</script>

<template>
    <span>
        <input v-model="newTechniqueName" placeholder="New Technique Name" class="technique-name-input"> </input>
        <button type="button" @click="addNewTechnique" class="add-technique-button"> Add </button>
    </span>
</template>

<style>
.technique-name-input {
    border: solid #925040;
    background-color: #d9d9d9;
}

::placeholder {
    color: #925040;
    opacity: 1;
}

.add-technique-button {
    margin: 0.5vw;
    height: 1.5vw;
}

.add-technique-button:hover {
    cursor: pointer;
}
</style>
