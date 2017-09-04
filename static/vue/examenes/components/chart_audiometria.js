import VueCharts from 'vue-chartjs'
import { Bar, Line } from 'vue-chartjs'

export default Line.extend({

    mixins: [VueCharts.mixins.reactiveProp],

    props: ['chartData', 'options'],

    mounted() {
        this.renderChart(this.chartData, this.options);
    }

})
