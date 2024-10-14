<script setup>
import axios from 'axios';
import { ref, onMounted, watch, computed } from 'vue';

const first_name = ref('')
const last_name = ref('')
const nickname = ref('')
const member_since = ref()
const first_tournament = ref()
const tournament_participation = ref()
const role = ref([])
const licePositions = ref([])
const picture = ref()

const alreadyTournament = ref(false)
const setRole = ref(false)

const addFighterDeployed = ref(false)

const emit = defineEmits(['fighter-created', 'deploy-section', 'fold-back-section'])

watch([alreadyTournament, setRole], ([newAlreadyTournament, newSetRole]) => {
    if ((newAlreadyTournament && !newSetRole) || (!newAlreadyTournament && newSetRole)) {
        addFighterDeployed.value = true;
        emit('fold-back-section');
    } else if (!newAlreadyTournament && !newSetRole) {
        addFighterDeployed.value = false;
        emit('deploy-section');
    }
});

const addFighterData = computed(() => ({
    first_name: first_name.value,
    last_name: last_name.value,
    nickname: nickname.value,
    member_since: member_since.value,
    picture: picture.value,
    first_tournament: first_tournament.value,
    tournament_participation: tournament_participation.value,
    role: role.value,
}));

function handleFileChange(event) {
    const file = event.target.files[0]
    picture.value = file
}

function getLicePositions() {
    axios
        .get('/api/v1/licepositions/')
        .then(response => {
            licePositions.value = response.data
        })
        .catch(error =>
            console.log(error)
        )
}

onMounted(() => {
    getLicePositions()
})

function saveNewFighters() {
    const data = addFighterData.value

    axios
        .post('/api/v1/fighters/', data)
        .then(response => {
            console.log('response', response)
            emit('fighter-created', response.data)
        })
        .catch(error =>
            console.log(error)
        )
}
</script>

<template>
    <div
        :class="{ 'deployed-add-fighter-wrapper': addFighterDeployed, 'folded-add-fighter-wrapper': !addFighterDeployed }">
        <h1>Add a new fighter</h1>
        <div>
            <input v-model="first_name" placeholder="New Fighter First Name*">
            <input v-model="last_name" placeholder="New Fighter Last Name">
            <input v-model="nickname" placeholder="New Fighter Nickname*">
        </div>
        <div class="picture-section">
            <div>
                <p>Member since*</p>
                <input v-model="member_since" type="date" placeholder="Member since" class="resized-input">
            </div>
            <div>
                <p>Picture</p>
                <input type="file" @change="handleFileChange" accept="image/png, image/jpeg" class="resized-input">
            </div>
        </div>
        <div class="footer-wrapper">
            <div class="optional-div">
                <div class="test">
                    <p>Already participated in a tournament</p>
                    <input v-model="alreadyTournament" type="checkbox" class="checkbox-input">
                </div>
                <div v-if="alreadyTournament" class="already-tournament">
                    <div class="tournament-row">
                        <p>First tournament</p>
                        <input v-model="first_tournament" type="date" placeholder="First tournament"
                            class="resized-input">
                    </div>
                    <div>
                        <input v-model="tournament_participation" type="number" placeholder="Number of tournament"
                            min="1" class="resized-input">
                    </div>
                </div>
            </div>
            <div class="optional-div">
                <div>
                    <p>Set lice position</p>
                    <input v-model="setRole" type="checkbox" class="checkbox-input">
                </div>
                <select v-if="setRole" v-model="role" multiple class="lice-position-select">
                    <option v-for="liceposition in licePositions" :key="liceposition.id" :value="liceposition.id">
                        {{ liceposition.position }}
                    </option>
                </select>
            </div>
            <button @click="saveNewFighters" id="save-new-fighter-button">Save</button>
        </div>
    </div>
</template>

<style>
.deployed-add-fighter-wrapper {
    width: 47vw;
    height: 19vw;
    border: 3px solid #925040;
    margin-top: 1vw;
    margin-bottom: 1vw;
    margin-left: 2vw;
    margin-right: 2vw;
    color: #925040;
    text-align: center;
}

.folded-add-fighter-wrapper {
    width: 47vw;
    height: 15vw;
    border: 3px solid #925040;
    margin-top: 1vw;
    margin-bottom: 1vw;
    margin-left: 2vw;
    margin-right: 2vw;
    color: #925040;
    text-align: center;
}

.deployed-add-fighter-wrapper div,
.folded-add-fighter-wrapper div {
    display: flex;
    justify-content: center;
}

.deployed-add-fighter-wrapper input,
.folded-add-fighter-wrapper input {
    border: 1px solid #925040;
    background-color: #d9d9d9;
    margin: 0.5vw;
    color: #925040;
}

#save-new-fighter-button {
    height: 3vw;
    width: 5vw;
    margin-left: 1vw;
    font-size: 1.5em;
    cursor: pointer;
}


.optional-div {
    display: block !important;
    margin-left: 1vw;
    margin-right: 1vw;
}

.picture-section div {
    display: flex;
    align-items: center;
    margin-left: 0.5vw;
    margin-right: 0.5vw;
}

.resized-input {
    height: 1.3vw;
    cursor: pointer;
}

.lice-position-select {
    width: 3vw;
    height: 4vw;
    border: 1px solid #925040;
    background-color: #d9d9d9;
    color: #925040;
}

::placeholder {
    opacity: 1;
}

.already-tournament {
    display: block !important;
}

.tournament-row {
    display: flex;
    align-items: center;
}

.tournament-row p,
.tournament-row input {
    margin: 0;
    padding: 0;
}

.footer-wrapper {
    display: flex;
    align-items: center;
}

.checkbox-input {
    cursor: pointer;
}
</style>