import axios from 'axios';

export async function fetchFighters() {
  const response = await axios.get('/api/v1/fighters/');
  return response.data;
}

export async function fetchSkillDomains() {
  const response = await axios.get('/api/v1/skilldomains/');
  return response.data;
}

export async function fetchFighterById(id) {
  const response = await axios.get(`/api/v1/fighters/${id}/`);
  return response.data;
}

export async function fetchTechniqueLevelById(id) {
  const response = await axios.get(`/api/v1/techniques_levels/${id}/`);
  return response.data;
}

export async function updateTechniqueLevel(data) {
  const response = await axios.post('/api/v1/techniques_levels/', data);
  return response.data;
}