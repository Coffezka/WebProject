<template>
    <div class="block block_new_operation">
        <div class="nameBlock">
            <img src="/assets/img/emoji/wallet.png">
            Мои счета
        </div>
        <div class="bContent">
			<div class="wallet"
			v-for="(i, id) in wallets" v-bind:key="i.name" 
			@click="select(id)">
			<!-- <div class="hover">
				Выберите валюту
				<div class="selecter">
					<div class="valute" v-for="v in i.valutes" v-bind:key="v.name">
						{{v.name}}
					</div>
				</div>
			</div> -->
				<div v-bind:class="{checker: true, selected_wallet: selected_wallet==id}">
					<fa :icon="['fas', 'check']" />
				</div>
				<div class="icon">
					<img src="/assets/img/icons/wallet.svg">
				</div>
				<div class="name">
					{{i.name}}
				</div>
				<div class="balances">
					<div class="balance" v-for="v in i.valutes" v-bind:key="v.name">
						<!-- {{v.sum}} -->
						
						<animated-number
							:value="v.sum"
							:formatValue="formatToPrice"
							:duration="300"
						/>
						{{v.name}}
					</div>
				</div>
			</div>

			<hr>
			
            <small>Введите название нового кошелька</small>
            <div class="input">
                <input v-model="new_name">
            </div>
			<div class="checks">
  				<input type="checkbox" v-model="new_valutes" name="UAH" value="UAH">
  				<label for="UAH"> UAH</label>
  				<input type="checkbox" v-model="new_valutes" name="EUR" value="EUR">
  				<label for="EUR"> EUR</label>
  				<input type="checkbox" v-model="new_valutes" name="USD" value="USD">
  				<label for="USD"> USD</label>
  				<input type="checkbox" v-model="new_valutes" name="RUB" value="RUB">
  				<label for="RUB"> RUB</label>
			</div>

			<button @click="new_wallet()">Добавить новый</button>
        </div>
    </div>
</template>
<script>
	import AnimatedNumber from "animated-number-vue";
    export default {
        props: {
			wallets: Object,
			selected_wallet: Number
        },
		components: {
			AnimatedNumber
		},
        data(){
            return{
                new_operation: {
                    type: 0,
                    sum: 100,
				},
				new_name: '',
				new_valutes: [],
            }
        },
        created(){
            if (!process.browser) {
                return
            }
        },
        methods: {
            new_wallet(){
				var id = Object.keys(this.$parent.wallets).length

				var valutes = {}
				for(var v in this.new_valutes){
					valutes[parseInt(v)+1] = {
						name: this.new_valutes[v],
						sum: 0
					}
				}

				this.$parent.wallets[id+1] = {
					name: this.new_name,
					valutes: valutes
				}
				this.new_name = ''
				this.new_valutes = []

				this.$forceUpdate()
			},
			select(id){
				this.$parent.selected_wallet = parseInt(id)
			},
			formatToPrice(value) {
				return `${value.toFixed(2)}`;
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
	.wallet{
		width: 100%;
		margin-top: 10px;
		height: 80px;
		border: 2px solid #444B87;
		border-radius: 10px;
		transition: 0.2s;
		cursor: pointer;
	}
	/* .wallet .hover{
		position: absolute;
		width: 200px;
		background: #000000b0;
		margin-left: 20px;
		margin-top: -10px;
		border-radius: 10px;
		box-shadow: 1px 1px 5px black;
		text-align: center;
		font-weight: 1000;
		font-size: 19px;
		color: white;
	} */
	.wallet:hover{
		background: #444B87;
		transition: 0.2s;
	}
	.wallet .icon{
		width: 50px;
		margin-top: 12px;
		margin-left: 20px;
		float: left;
	}
	.wallet .icon img{
		width: 100%;
	}
	.wallet .name{
		float: left;
		margin-top: 20px;
		margin-left: 20px;
		font-size: 22px;
		color: white;
		font-weight: 600;
	}
	.wallet .balances{
		float: right;
		margin-right: 20px;
		margin-top: 4px;
	}
	.wallet .balances .balance{
		background: royalblue;
		border-radius: 30px;
		padding: 3px 10px;
		margin-top: 5px;
		text-align: center;
		color: white;
		font-weight: 600;
		font-size: 15px;
	}
	.checker{
		display: none
	}
	.selected_wallet{
		display: block;
		position: absolute;
		font-size: 20px;
		color: rgb(17, 219, 219);
		margin-left: -20px;
		margin-top: 20px;
		width: 40px;
		height: 40px;
		line-height: 40px;
		border-radius: 50%;
		background: rgba(248, 248, 248, 0.2);
		text-align: center;
	}
	.checks{
		display: flex;
		justify-content: space-between;
		color: white;
		font-size: 20px;
		line-height: 10px;
		margin: 20px 0;
	}
	
	small{
		color: rgb(133, 125, 245);
		text-align: center;
		display: block;
		margin-bottom: 10px;
		font-size: 17px;
	}
	.input{
		width: 100%;
	}
	.input input{
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
	hr{
		border-top: none;
		border-bottom: 1px solid rgb(85, 102, 177);
		margin: 40px 0
	}

	button{
		width: 100%;
		margin-top: 10px;
		height: 50px;
		border: 2px solid #444B87;
		border-radius: 10px;
		background: none;
		font-size: 18px;
		font-weight: 1000;
		color: white;
		transition: 0.2s;
		cursor: pointer;
	}
	button:hover{
		background: #444B87;
		transition: 0.2s;
		transform: scale(1.05);
	}
</style>