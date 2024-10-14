<script setup>
import { Chart } from 'chart.js/auto';
import { getRelativePosition } from 'chart.js/helpers';
import { onMounted, watch, ref } from 'vue';

const props = defineProps({
  empty: Boolean,
  chartData: Object,
  index: Number
});

const emit = defineEmits(['update-technique-level']);

const chartID = ref(null);
const chartInstance = ref(null);
const canvasRef = ref(null);

onMounted(() => {
  chartID.value = 'chart' + props.index.toString();

  if (canvasRef.value) {
    canvasRef.value.id = chartID.value;
  }

  const ctx = canvasRef.value.getContext('2d');

  if (ctx) {
    chartInstance.value = new Chart(ctx, {
      type: 'bar',
      data: props.chartData,
      options: {
        onClick: (e) => {
          const canvasPosition = getRelativePosition(e, chartInstance.value);
          const dataX = chartInstance.value.scales.x.getValueForPixel(canvasPosition.x);
          const dataY = chartInstance.value.scales.y.getValueForPixel(canvasPosition.y);
          const roundStep = 1;
          const techniqueIndex = dataX;
          const roundedDataY = Math.round(dataY / roundStep) * roundStep;
          emit('update-technique-level', [techniqueIndex, roundedDataY, props.index]);
        },
        scales: {
          y: {
            min: 0,
            max: 5,
          }
        }
      }
    });
  } else {
    console.error('Failed to get context for chart:', chartID.value);
  }
});

watch(
  () => props.chartData,
  (newData) => {
    if (chartInstance.value) {
      Chart.getChart(canvasRef.value.getContext('2d')).data = newData;
      Chart.getChart(canvasRef.value.getContext('2d')).update()
    }
  },
);
</script>

<template>
  <div class="chart-card">
    <RouterLink to="/skillsdomains"> <h3 v-if="empty" class="add-skill-domain-pop-up">Add a new skilldomain</h3> </RouterLink>
    <canvas ref="canvasRef"></canvas>
  </div>
</template>

<style>
.chart-card {
  margin: 1vw;
  padding: 1vw;
  border: 3px solid #3F494B;
  height: 10vw;
  position: relative;
}

.add-skill-domain-pop-up {
  position: absolute;
  top: 40%;
  left: 55%;
  transform: translate(-50%, -50%);
  color: #925040;
}
</style>