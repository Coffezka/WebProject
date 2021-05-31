import { Line } from 'vue-chartjs'

export default {
  extends: Line,


  // props: ['data', 'options'],
  
  props: {
    labels: {
      type: Array,
      default: null
    },
    data: {
      type: Array,
      default: null
    },
    options: {
      type: Object,
      default: null
    }
  },
  watch: {
    chartData () {
      this.$data._chart.update()
    }
  },
  mounted () {
    this.gradient = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450)
    this.gradient.addColorStop(0, 'rgba(183, 33,255, 1)')
    this.gradient.addColorStop(1, 'rgba(33, 212, 253, 0.6)');

    this.gradient2 = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450)
    this.gradient2.addColorStop(0, 'rgba(183, 33,255, 0.3)')
    this.gradient2.addColorStop(1, 'rgba(33, 212, 253, 0.1)');

    var data = {
      labels: this.labels,
      datasets: [
        {
          label: "",
          borderColor: this.gradient,
          pointBackgroundColor: 'white',
          borderWidth: 2,
          pointBorderColor: 'violet',
          backgroundColor: this.gradient2,
          data: this.data
        },
      ]
    }
    this.renderChart(data, this.options)
    console.log(this.$refs.canvas)
    
  }
}
