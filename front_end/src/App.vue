<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div>
      <nav>
        <RouterLink to="/" v-slot="{ isActive }">
          <div :class="['menu-item', { 'active-link': isActive }]">Home</div>
        </RouterLink>
        <RouterLink to="/skillsdomains" v-slot="{ isActive }">
          <div :class="['menu-item', { 'active-link': isActive }]">SkillsDomains & Techniques</div>
        </RouterLink>
        <RouterLink to="/fighters" v-slot="{ isActive }">
          <div :class="['menu-item', { 'active-link': isActive }]">Fighters</div>
        </RouterLink>
        <RouterLink to="/tournaments" v-slot="{ isActive }">
          <div :class="['menu-item', { 'active-link': isActive }]">Tournaments</div>
        </RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style>
nav {
  width: 100vw;
  background-color: #3F494B;
  display: flex;
  align-items: center;
  justify-content: center;
}

nav .menu-item {
  color: #f8f6ec;
  padding-left: 3vw;
  padding-right: 3vw;
  padding-top: 0.5vw;
  padding-bottom: 0.5vw;
  position: relative;
  text-align: center;
  border-bottom: 5px solid transparent;
  display: flex;
  transition: 0.4s;
}

nav .menu-item:hover {
  background-color: #47595d;
}

nav .menu-item.active-link {
  border-bottom-color: #925040;
}

nav .menu-item a {
  color: inherit;
  text-decoration: none;
}
</style>