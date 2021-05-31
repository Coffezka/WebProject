<template>
    <div class="block block_new_operation">
        <div class="nameBlock">
            <img src="/assets/img/emoji/trophy.png">
            Финансовая цель
        </div>
        <div class="bContent" v-if="balance < goal">
			<radial-progress-bar 
				:diameter="200"
				:completed-steps="balance"
				:total-steps="goal"
				innerStrokeColor="#464C7A"
				startColor="#FFAA78"
				stopColor="#FF5497"
				class="circle"
			>
            	<img src="/assets/img/icons/save-money.svg" class="piggy">
			</radial-progress-bar>
			<div class="info">
				<div class="goal">{{name}}</div>
				<div class="infos">Накоплено</div>
				<div class="sum">
					<animated-number
						:value="balance"
						:formatValue="formatToPrice"
						:duration="300"
					/>
				</div>
				<div class="infos">Цель</div>
				<div class="sum">
					<animated-number
						:value="goal"
						:formatValue="formatToPrice"
						:duration="300"
					/>
				</div>
			</div>
        </div>
		<div class="bContent" v-else>
			<div class="info">
				<div class="goal">Цель достигнута!</div>
				<div class="infos">Вы собрали ${{goal}}!</div>
			</div>
		</div>
    </div>
</template>
<script>
	import AnimatedNumber from "animated-number-vue";
    export default {
        props: {
            balance: Number
        },
		components: {
			AnimatedNumber
		},
        data(){
            return{
				name: 'Машина',
				goal: 1000
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
    	float: left;
		padding-bottom: 20px;
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
	.blocks .block_stats{
		width: calc(60% - 30px);
	}
	.block_new_operation .bContent{
		width: 80%;
		margin-left: 10%;
	}
	.block_stats .bContent{
		width: 90%;
		height: 100px !important;
		margin-left: 5%;
	}
	.bContent small{
		color: rgb(133, 125, 245);
		text-align: center;
		display: block;
		margin-bottom: 10px;
		font-size: 17px;
	}
	.piggy{
		width: 90px;
	}
	.circle{
		float: left;
	}
	.info{
		float: left;
		margin-left: 50px;
	}
	.info .infos{
		color: grey;
		font-size: 22px;
	}
	.info .sum{
		font-size: 35px;
		font-weight: 1000;
		color: #FF5497;
	}
	.info .goal{
		font-size: 35px;
		font-weight: 1000;
		color: #ffe554;
	}
</style>