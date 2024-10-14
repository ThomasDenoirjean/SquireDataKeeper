<script setup>

</script>

<template>
  <div class="hello-wrapper">
    <div class="introduction">
      <div>
        <img src="/tournoi_anjou.jpg" class="introduction-img">
      </div>
      <div class="introduction-description">
        <h1> Welcome to Squire Data Keeper!</h1>
        <p>
          Welcome, noble lords and ladies! SquireDataKeeper is your trusted companion in the realm of buhurt team
          management.
          Whether you're starting your journey or commanding the flower of your nation's chivalry, our system will keep
          your
          fighters organized and battle-ready.
          This system is designed for buhurt, also known as medieval combat or full-contact medieval fighting, which is
          a
          modern sport that recreates historical tournaments and melees from the Middle Ages. Participants wear
          authentic
          armor
          and use blunt replicas of medieval weapons to compete in individual or team battles.
        </p>
      </div>
      <div>
        <img src="/buhurt_fight.jpg" class="introduction-img">
      </div>
    </div>
    <div class="features">
      <h1 class="feature-title">Features</h1>
      <ul class="feature-list">
        <li class="feature-lign">
          <img src="/crossed_sword.png" class="sword-emoji">
          <h3 class="bold">Skills and Techniques:</h3> Strategize your fighters' growth by defining skill sets and
          techniques.
        </li>
        <li class="feature-lign">
          <img src="/crossed_sword.png" class="sword-emoji">
          <h3 class="bold">Fighter Profiles:</h3> Maintain detailed records of your warriors' combat expertise.
        </li>
        <li class="feature-lign">
          <img src="/crossed_sword.png" class="sword-emoji">
          <h3 class="bold">Tournament Records:</h3> Keep track of your tournament achievements and individual fighter
          performances.
        </li>
      </ul>
    </div>
  </div>
</template>

<style>
.hello-wrapper {
  margin-top: 3vw;
  color: #3F494B;
  margin-left: auto;
  margin-right: auto;
  width: 80vw;
}

.introduction-description {
  width: 50vw;
  margin-left: 1vw;
  margin-right: 1vw;
}

.introduction-description p {
  font-size: 1.2em;
}

.introduction-img {
  height: 15vw;
}

.introduction {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.sword-emoji {
  height: 2vw;
}

.feature-title {
  margin-bottom: 1vw;
}

.feature-list {
  margin: 0;
}

.feature-lign {
  display: flex;
  flex-direction: row;
  align-items: center;
  font-size: 1.5em;
  margin-bottom: 1vw;
}

.bold {
  margin-left: 0.5vw;
  margin-right: 0.5vw;
  margin-top: 0;
  margin-bottom: 0;
}
</style>