<template>
    <div class="block block_new_operation">
        <div class="nameBlock">
            <img src="/assets/img/emoji/history.png">
            История
        </div>
        <div class="bContent">
			<small>
				Мои траты за последние 30 дней: <span>$4000.20</span>
			</small>
			<div class="hist" v-for="(h, index) in history" v-bind:key="index">
				<div class="date">{{millsToDate(h.date)}}</div>
				<div class="wallet">{{h.name}}</div>
				<div class="type" v-if="h.type==0">Доход</div>
				<div class="type type1" v-if="h.type==1">Уход</div>
				<div class="sum">{{h.sum}} {{h.valute}}</div>
			</div>
        </div>
    </div>
</template>
<script>
    export default {
        props: {
            history: Object
        },
        data(){
            return{
                new_operation: {
                    type: 0,
                    sum: 100,
                },
            }
        },
        created(){
            if (!process.browser) {
                return
            }
        },
        methods: {
			millsToDate(milliseconds){
				this.$moment.locale('ru');
				return (this.$moment(milliseconds).format('LL'));
			},
			upd(){
				this.$forceUpdate()
			}
        }
    }
</script>
<style scoped>
	.blocks .block{
		margin: 10px;
		padding: 10px;
		background: #2C325C;
		width: calc(100% - 20px);
		border-radius: 20px;
    	float: left;
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
		width: 70%;
		margin-left: 15%;
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
	.bContent small span{
		color: white;
		font-weight: 600;
	}
	.hist{
		width: 100%;
		display: inline-block;
		padding: 15px 0;
		border-bottom: 1px solid #3d467e;
	}
	.hist .date{
		background: #21264B;
		color: #7580BD;
		padding: 3px 10px;
		font-weight: 600;
		border-radius: 50px;
		float: left;
	}
	.hist .wallet{
		color: #7B87C5;
		float: left;
		margin-left: 10px;
		margin-top: 3px;
		font-weight: 600;
	}
	.hist .sum{
		float: right;
		color: white;
		font-weight: 600;
		margin-right: 10px;
		margin-top: 3px;
	}
	.hist .type{
		float: right;
		background: #3EF3D3;
		color: white;
		padding: 3px 10px;
		font-weight: 600;
		border-radius: 50px;
	}
	.hist .type1{
		background: #FF2D7F;
	}
	
</style>