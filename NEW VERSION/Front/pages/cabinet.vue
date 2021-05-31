<template>
	<div>
		<Settings v-if="settings_modal" />

		<div class="page">
			<Header />
			<div class="blocks" v-if="month!=null">
				<NewOperation />
				<Wishlist />
			</div>
			<div class="blocks" v-if="month!=null">
				<Wallets :wallets="wallets" :selected_wallet="selected_wallet" />
				<History ref="history" :history="history" />
			</div>
			<div class="blocks" v-if="month!=null">
				<Stats ref="stats" :graph="month" :balance="balance" />
				<Accumulation ref="goal" :balance="balance" />
			</div>
		</div>
	</div>
</template>

<script>
import { API } from '~/plugins/api.js';
import Header from '~/components/Header.vue'
import NewOperation from '~/components/NewOperation.vue'
import Stats from '~/components/Stats.vue'
import Accumulation from '~/components/Accumulation.vue'
import Wallets from '~/components/Wallets.vue'
import History from '~/components/History.vue'
import Wishlist from '~/components/Wishlist.vue'
import Settings from '~/components/modals/Settings.vue'

export default {
	async asyncData(args) {
		const servers_all = await args.$axios.$get(API+`monitoring.all`)
		
            var month = servers_all.online_month
		return {
			month: month
		}
	},
	head() {
		return {
			title: "Личный кабинет - MoneyITStep",
		}
	},
	components: {
		NewOperation, Stats, Accumulation, Wallets, History, Wishlist, Header, Settings
	},
	data () {
		return {
			name: "EnJay",
			password: "",
			checkPass: false,
			isAuthenticated: false,
			settings_modal: false,

			wallets: {
				1: {
					name: 'ПриватБанк',
					valutes: {
						1: {
							name: 'UAH',
							sum: 0,
						},
						2: {
							name: 'EUR',
							sum: 120,
						}
					}
				},
				2: {
					name: 'monobank',
					valutes: {
						1: {
							name: 'UAH',
							sum: 0,
						},
						2: {
							name: 'USD',
							sum: 120,
						}
					}
				},
			},
			selected_wallet: 1,

			history: {
				1: {
					date: 1621454100000,
					name: 'ПриватБанк',
					sum: 500,
					valute: 'UAH',
					type: 0
				},
			},
			balance: 0,
		}
  	},
	computed: {
		// isAuthenticated () {
		// 	return this.$store.getters.authenticated
		// },
    },
	created() {
		if (!process.browser) {
			return
		}
		this.calculateBalance()
		// setTimeout(() => {
		// 	if(this.isAuthenticated){
		// 		this.$router.replace({ path: '/cabinet' })
		// 	}
		// }, 1000)
	},
    methods: {
      	login() {
			this.$axios.get(API+"account.login?name=" + this.name + "&password=" + this.password)
			.then(res => {
				if(res.data.type=='success'){
					this.$snotify.success('Привет, '+this.name+'! Рады тебя видеть!', '',{
						timeout: 5000,
						showProgressBar: true,
						closeOnClick: true,
						pauseOnHover: false
					});
					this.$store.commit('auth', {
						login: this.name,
						accessToken: res.data.token
					});
					this.$router.push('/cabinet')
				}else{
					if(res.data.error=='0'){
						this.$snotify.error('Такой пользователь не найден :(', '',{
							timeout: 2500,
							showProgressBar: true,
							closeOnClick: true,
							pauseOnHover: false
						});
					} else{
						this.$snotify.error('Пароль неверный', '',{
							timeout: 2500,
							showProgressBar: true,
							closeOnClick: true,
							pauseOnHover: false
						});
					}
				}
			})
		},
		upd(){
			this.$forceUpdate()
			this.$refs.history.upd()
		},
		logout(){
			this.$store.commit('logout');
		},
		calculateBalance(){
			this.balance = 0
			for(var b in this.wallets){
				for(var v in this.wallets[b].valutes){
					this.balance += this.wallets[b].valutes[v].sum
				}
			}

		}
	},
}
</script>

<style scoped>
	.page {
		background: #1D2141;
		background-position: top center;
		background-repeat: no-repeat;
		background-size: cover;
		height: 100%;
		position: relative;
		padding-top: 15vh;
		width: 100%;
		display: inline-block;
		padding-bottom: 4px;
	}
	.blocks{
		width: 33.33%;
		float: left;
		margin-top: 20px;
		padding-bottom: 30px;
	}
	
</style>