<template>
	<div class="block block_stats">
		<div class="nameBlock">
			<img src="/assets/img/emoji/money-bag.png">
			Мои средства
		</div>
		<div class="bContent">
			<LineChart :labels="stats.date" :data="stats.sum" :options="options" />
		</div>
		<div class="balance">
			<div class="full">
				<animated-number
					:value="balance"
					:formatValue="formatToPrice"
					:duration="300"
				/>
			</div>
			<div class="descr">Общий баланс</div>
		</div>
	</div>
</template>
<script>
	import AnimatedNumber from "animated-number-vue";
    export default {
        props: {
            graph: Object,
			balance: Number
        },
		components: {
			AnimatedNumber
		},
        data(){
            return{
				stats: {
					date: [1621457700000, 1621528200000, 1621540500000],
					sum: [100, 600, 200]
				},
                new_operation: {
                    type: 0,
                    sum: 100,
                },
				options: {
					maintainAspectRatio: false,
					responsive: true,
					legend: {display: false},
					elements: { point: { radius: 0 } },
					
					scales: {
						xAxes: [{
							type: 'time',
							// distribution: 'linear',
							time: {
								minUnit: 'minute'
							},
							ticks: {
								maxTicksLimit: 16,
							},
						}]
					}
				},
            }
        },
        created(){
            if (!process.browser) {
                return
            }
        },
        methods: {
			formatToPrice(value) {
				return `$ ${value.toFixed(2)}`;
			},
			add(date, sum){
				this.stats.date.push(date)
				this.stats.sum.push(sum)
				this.$forceUpdate()
			}
        }
    }
</script>
<style scoped>
	.blocks .block{
		margin: 10px;
		padding: 10px;
		width: calc(100% - 20px);
		background: #2C325C;
		border-radius: 20px;
	}
	.blocks .block .nameBlock{
		font-weight: 1000;
		color: white;
		text-align: center;
		font-size: 25px;
		line-height: 80px;
	}
	.blocks .block .nameBlock img{
		position: absolute;
		width: 63px;
		transform: rotate(16deg);
		margin-left: -75px;
		margin-top: 10px;
	}
	.block_new_operation .bContent{
		width: 70%;
		margin-left: 15%;
	}
	.block_stats .bContent{
		width: 90%;
		margin-left: 5%;
		display: inline-block;
	}
	.balance{
		display: inline-block;
	}
	.balance .full{
		font-weight: 1000;
		color: white;
		font-size: 35px;
		margin-top: 10px;
		margin-left: 20px;
	}
	.balance .descr{
		font-size: 20px;
		color: grey;
		font-weight: 400;
		margin-left: 20px;
	}
</style>