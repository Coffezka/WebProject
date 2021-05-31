<template>
    <div class="block block_new_operation">
        <div class="nameBlock">
            <img src="/assets/img/emoji/money-mouth-face.png">
            Новая операция
        </div>
        <div class="bContent">
            <small>Введите сумму</small>
            <div class="input">
                <input type="number" v-model="new_operation.sum">
            </div>
            <div class="switch">
                <div v-bind:class="{sw:true, sw_selected:new_operation.type==0}"
                @click="new_operation.type=0">Доход</div>
                <div v-bind:class="{sw:true, sw_selected:new_operation.type==1}"
                @click="new_operation.type=1">Уход</div>
            </div>
            <button @click="add()">Добавить</button>
        </div>
    </div>
</template>
<script>
    export default {
        props: {
            
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
            add(){
				var id = parseInt(Object.keys(this.$parent.history).length) + 1
				var d = new Date();
				var obj = {
					date: (new Date).valueOf(),
					name: this.$parent.wallets[this.$parent.selected_wallet].name,
					sum: this.new_operation.sum,
					valute: 'UAH',
					type: this.new_operation.type
				}

				this.$parent.history[id] = obj

				if(this.new_operation.type==0){
					this.$parent.wallets[this.$parent.selected_wallet].valutes[1].sum += this.new_operation.sum
				}else{
					this.$parent.wallets[this.$parent.selected_wallet].valutes[1].sum -= this.new_operation.sum

				}
				this.$parent.upd()
				this.$parent.calculateBalance()
				this.$parent.$refs.stats.add((new Date).valueOf(), this.new_operation.sum)
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
		width: 70%;
		margin-left: 15%;
	}
	.block_stats .bContent{
		width: 90%;
		height: 100px !important;
		margin-left: 5%;
	}
	.block_new_operation .bContent small{
		color: rgb(133, 125, 245);
		text-align: center;
		display: block;
		margin-bottom: 10px;
		font-size: 17px;
	}
	.block_new_operation .bContent .input{
		width: 100%;
	}
	.block_new_operation .bContent .input input{
		width: 100%;
		height: 60px;
		border-radius: 15px;
		background: #1d2453;
		color: white;
		border: none;
		outline: none;
		font-size: 30px;
		font-weight: 1000;
		text-align: center;
	}
	.block_new_operation .bContent .switch{
		width: 100%;
		padding: 10px;
		height: 70px;
		background: #1d2453;
		border-radius: 15px;
		margin-top: 20px;
		display: flex;
		justify-content: space-between;
	}
	.block_new_operation .bContent .switch .sw{
		width: calc(50% - 10px);
		height: 50px;
		border-radius: 15px;
		text-align: center;
		line-height: 50px;
		font-size: 20px;
		color: #3EF3D3;
		font-weight: 700;
		cursor: pointer;
	}
	.block_new_operation .bContent .switch .sw_selected{
		transition: 0.2s;
		background: #2b357a;
	}
	.block_new_operation .bContent .switch .sw:last-child{
		color: #FF5497;
	}
	.block_new_operation button{
		background-color: #21D4FD;
		background-image: linear-gradient(270deg, #21D4FD 0%, #B721FF 100%);
		border: none;
		border-radius: 15px;
		margin-top: 40px;
		width: 100%;
		height: 60px;
		color: white;
		font-size: 25px;
		font-weight: 600;
		transition: 0.2s;
		cursor: pointer;
	}
	.block_new_operation button:hover{
		transform: scale(1.05);
		transition: 0.2s;
	}
</style>