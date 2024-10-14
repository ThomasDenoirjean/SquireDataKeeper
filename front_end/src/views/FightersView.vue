<script setup>
import { ref, onMounted, watch } from 'vue';
import { fetchFighters, fetchSkillDomains, fetchFighterById, updateTechniqueLevel } from '../services/apiService';
import fighter from '../components/Fighter.vue';
import chart from '../components/FighterStatChart.vue';
import addfighter from '../components/AddFighter.vue';

const fighters = ref([]);
const skillDomains = ref([]);
const selectedFighter = ref(null);
const statDataByDomain = ref([]);
const techniquesLevelsIDS = ref([]);
const MAXNUMBEROFGRAPHS = ref(6);
const deployed = ref(true);


// asked chatGPT to polish my code there
const getFighters = async () => {
  try {
    fighters.value = await fetchFighters();
    selectedFighter.value = fighters.value[0];
  } catch (error) {
    console.error(error);
  }
};

const getSkillsDomains = async () => {
  try {
    skillDomains.value = await fetchSkillDomains();
  } catch (error) {
    console.error(error);
  }
};

const updateSelectedFighter = async (index) => {
  selectedFighter.value = fighters.value[index];
};

const getFighterDataForChart = () => {
  if (!selectedFighter.value) return;

  statDataByDomain.value = [];
  techniquesLevelsIDS.value = [];

  const uniqueDomainArray = [...new Set(selectedFighter.value.techniques_levels.map(level => level.technique.domain))];

  uniqueDomainArray.forEach(domainId => {
    const techniques = selectedFighter.value.techniques_levels.filter(level => level.technique.domain === domainId);
    const techniqueNames = techniques.map(level => level.technique.name);
    const techniqueLevels = techniques.map(level => level.level);
    const domain = skillDomains.value.find(skillDomain => skillDomain.id === domainId);

    if (domain) {
      statDataByDomain.value.push({
        labels: techniqueNames,
        datasets: [{
          label: domain.name,
          data: techniqueLevels,
          backgroundColor: domain.color
        }]
      });
      techniques.forEach(level => techniquesLevelsIDS.value.push(level.id));
    }
  });
};

watch(selectedFighter, getFighterDataForChart);

onMounted(() => {
  getFighters();
  getSkillsDomains();
});

const updateTechniqueLevelHandler = async (newTechniqueLevel) => {
  const [techniqueIndex, techniqueNewLevel, skillDomainIndex] = newTechniqueLevel;
  let stepAddedToGatheredTechniqueIndex = 0;

  if (skillDomainIndex > 0) {
    const uniqueDomainArray = [...new Set(selectedFighter.value.techniques_levels.map(level => level.technique.domain))];

    for (let i = 0; i < skillDomainIndex; i++) {
      stepAddedToGatheredTechniqueIndex += selectedFighter.value.techniques_levels.filter(level => level.technique.domain === uniqueDomainArray[i]).length;
    }
  }

  const actualTechniqueIndex = stepAddedToGatheredTechniqueIndex + techniqueIndex;
  const data = {
    id: techniquesLevelsIDS.value[actualTechniqueIndex],
    new_level: techniqueNewLevel
  };

  try {
    await updateTechniqueLevel(data);
    selectedFighter.value = await fetchFighterById(selectedFighter.value.id);
    fighters.value = fighters.value.map(fighter => fighter.id === selectedFighter.value.id ? selectedFighter.value : fighter);
  } catch (error) {
    console.error(error);
  }
};

const removeFighterFromList = (fighter) => {
  const fighterIndex = fighters.value.indexOf(fighter);
  selectedFighter.value = fighters.value[fighterIndex + 1] || fighters.value[fighterIndex - 1];
  fighters.value.splice(fighterIndex, 1);
};

const addFighterToList = (fighter) => {
  fighters.value.push(fighter);
};
</script>

<template>
  <div id="fighters-page">
    <div>
      <div :class="{ 'deployed-fighter-list': deployed, 'folded-fighter-list': !deployed }">
        <fighter v-for="(fighter, index) in fighters" :key="fighter.id" :fighter="fighter"
          :selectedFighter="selectedFighter" @click="updateSelectedFighter(index)"
          @fighter-deleted="removeFighterFromList"></fighter>
      </div>
      <div>
        <addfighter @fighter-created="addFighterToList" @fold-back-section="deployed = false"
          @deploy-section="deployed = true"></addfighter>
      </div>
    </div>
    <div class="charts-wrapper">
      <chart v-for="(data, index) in statDataByDomain" :key="index" :empty="false" :chartData="data" :index="index"
        @update-technique-level="updateTechniqueLevelHandler"></chart>
      <chart v-for="n in (MAXNUMBEROFGRAPHS - statDataByDomain.length)" :key="n" :empty="true" :chartData="null" :index="99"></chart>
    </div>
  </div>
</template>

<style>
#fighters-page {
  display: inline-flex;
}

.deployed-fighter-list {
  background-color: #F8F6EC;
  width: 47vw;
  height: 24vw;
  text-align: center;
  overflow: auto;
  border: 3px solid #3F494B;
  margin: 1vw 2vw;
}

.folded-fighter-list {
  background-color: #F8F6EC;
  width: 47vw;
  height: 20vw;
  text-align: center;
  overflow: auto;
  border: 3px solid #3F494B;
  margin: 1vw 2vw;
}

.charts-wrapper {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}
</style>