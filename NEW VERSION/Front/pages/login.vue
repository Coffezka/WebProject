<template>
    <div>
		<div class="page">
			<div class="logIn" v-if="!isAuthenticated">
				<div class="left">
					<h1>Авторизация</h1><br>
					Авторизуйтесь для начала использования нашего сервиса.
<button @click="test()">test</button>
				</div>
				<div class="right">
					<div><fa :icon="['fas', 'sign-in-alt']"/></div><br>
					<div class="input">
						<input type="text" name="name" v-model="name" placeholder="Логин">
						<fa class="inputIcon" :icon="['fas', 'user']"/>
					</div>
					<div class="input">
						<input :type="checkPass?'text':'password'" name="password" v-model="password" placeholder="Пароль">
						<fa class="inputIcon" :icon="['fas', 'lock']"/>
						<fa v-on:click="checkPass?checkPass=false:checkPass=true" class="checkPass" :icon="['fas', 'eye']"/>
					</div>
					<nuxt-link class="lostPassword" to="/lostpassword">Забыли пароль?</nuxt-link>
					<button type="submit" value="Submit" v-on:click="login">Войти</button>
					<div class="goToRegister"><nuxt-link to="/register">Создать новый аккаунт</nuxt-link></div>
				</div>
			</div>
			<div v-else>
				Вы уже авторизованы!
				<button type="submit" value="Submit" v-on:click="logout">Выйти с аккаунта</button>
			</div>
		</div>
    </div>
</template>

<script>
import Vue from "vue";
import { API } from '~/plugins/api.js';

export default {
	head() {
		return {
			title: "Авторизация - MoneyITStep",
		}
	},
	data () {
		return {
			name: "",
			password: "",
			checkPass: false,
			isAuthenticated: false
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
		setTimeout(() => {
			if(this.isAuthenticated){
				this.$router.replace({ path: '/cabinet' })
			}
		}, 1000)
	},
    methods: {
		register() {
			this.$axios.post(API+"account/register", {
				username: 'saasas',
				email: 'asaasds@sa.sa',
				password: '123',
				password2: '123'
			}).then(res => {
				console.log(res.data)
				if(res.data.type=='success'){
					// this.$notify.success({
					// 	title: 'Привет!', 
					// 	message: 'Авторизация пройдена.'
					// })
					console.log('aa')
					// this.$store.commit('auth', {
					// 	login: this.name,
					// 	accessToken: res.data.token
					// });
					// this.$router.push('/cabinet')
				}else{
					console.log('err')
					
				}
			})

		},
		test(){
			var token = '53f8748bd05f653f61fb1c2d860fe150aed64a46'

			const options = {
				headers: {'Authorization': 'Token '+ token
				},
				
			};
			this.$axios.get(API+'usersBill-rest/?format=json', options)
			.then(res => {
				console.log(res.data)
			})
		},
		login() {
			this.$axios.post(API+"account/login", {
				username: 'asaasds@sa.sa',
				// email: 'asaasds@sa.sa',
				password: '123',
			}).then(res => {
				console.log(res.data)
				if(res.data.type=='success'){
					// this.$notify.success({
					// 	title: 'Привет!', 
					// 	message: 'Авторизация пройдена.'
					// })
					console.log('aa')
					// this.$store.commit('auth', {
					// 	login: this.name,
					// 	accessToken: res.data.token
					// });
					// this.$router.push('/cabinet')
				}else{
					console.log('err')
					
				}
			})

		},
		logout(){
			this.$store.commit('logout');
		}
	},
  	components: {
	}
}
</script>

<style scoped>
	.page {
		background: url(/assets/img/login_bg.png) white;
		background-position: top center;
		background-repeat: no-repeat;
		background-size: cover;
		min-height: 100vh;
		position: relative;
		padding-top: 15vh;
	}

	.logIn{
		width: 854px;
		height: 523px;
		background: url(/assets/img/login.png); 
		margin: 0 auto;
		border-radius: 15px;
		box-shadow: 0px 0px 21px -10px rgba(0,0,0,0.75);
		transition: all 0.3s ease;
		overflow: hidden;
	}

	.logIn .left{
		width: 35%;
		height: 50%;
		float: left;
		padding-top: 17%;
		margin-left: 3%;
		color: white;
		text-align: left;
		font-family: 'Raleway-Light', Arial;
	}

	.logIn .right{
		width: 40%;
		height: 100%;
		float: left;
		margin-left: 22%;
	}

	.logIn .left b{
		font-size: 20px;
	}

	.logIn .right .fa-sign-in-alt{
		font-size: 130px;
		padding: 30px;
		text-align: center;
		color: white;
		border-radius: 100px;
		margin-left: 80px;
		margin-top: 40px;

		background: rgba(98,234,255,1);
		background: -moz-linear-gradient(45deg, rgba(98,234,255,1) 0%, rgba(95,183,255,1) 100%);
		background: -webkit-linear-gradient(45deg, rgba(98,234,255,1) 0%, rgba(95,183,255,1) 100%);
		background: -o-linear-gradient(45deg, rgba(98,234,255,1) 0%, rgba(95,183,255,1) 100%);
		background: -ms-linear-gradient(45deg, rgba(98,234,255,1) 0%, rgba(95,183,255,1) 100%);
		background: linear-gradient(45deg, rgba(98,234,255,1) 0%, rgba(95,183,255,1) 100%);
		filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#62eaff', endColorstr='#5fb7ff', GradientType=1 );
	}

	.logIn .right .input{
		width: 100%
	}
	.logIn .right input{
		width: 280px;
		height: 50px;
		font-size: 20px;
		padding: 0 45px 0 50px;
		border: none;
		background: rgb(236, 236, 236);
		color: rgb(158, 158, 158);
		margin-top: 20px;
		border-radius: 10px;
		transition: all 0.3s ease;
	}
	.logIn .right input:hover{
		background: rgb(236, 236, 236);
		color: rgb(158, 158, 158);
		box-shadow: 1px 1px 6px 1px rgba(0,0,0,0.05);
		transition: all 0.3s ease;
	}
	.logIn .right input:focus{
		color: rgb(80, 80, 80);
		outline: none;
	}

	.logIn .right .inputIcon{
		margin-left: -260px;
		font-size: 20px;
		color: rgb(143, 143, 143);
		position: absolute;
		margin-top: 34px;
	}

	.logIn .right .checkPass{
		margin-left: -35px;
		margin-top: 40px;
		font-size: 20px;
		color: rgb(143, 143, 143);
		cursor: pointer;
		position: absolute;
	}
	.logIn .right .checkPass:hover{
		color: rgb(76, 134, 145);
	}

	.logIn .right a{
		font-size: 17px;
		margin-left: 52px;
		font-family: 'Raleway-Light', Arial;
		color: rgb(134, 134, 134);
	}
	.logIn .right a:hover{
		color: rgb(64, 120, 184);
	}
	.logIn .right .lostPassword{
		float:right;
		font-size: 15px;
		margin: 5px 65px 10px 0;
		color: rgb(134, 134, 134);
	}
	.logIn .right .lostPassword:hover{
		color: rgb(173, 39, 39);
	}

	.logIn .right button{
		width: 280px;
		height: 50px;
		color: white;
		font-weight: 100;
		text-align: center;
		line-height: 50px;
		font-size: 30px;
		cursor: pointer;
		background: rgb(98, 218, 255);
		transition: all 0.3s ease;
		text-decoration: none;
		border: none;
		border-radius: 10px;
		font-family: 'Raleway-Light', Arial;
	}
	.logIn .right button:hover{
		box-shadow: 1px 1px 6px 1px rgba(0,0,0,0.15);
		transition: all 0.3s ease;
		background: rgb(98, 192, 255);
	}

	.logIn .right button:focus{
		outline: none;
	}
	.logIn .right .authBy{
		font-size: 20px;
		background-color: #21D4FD;
		background-image: linear-gradient(238deg, #21D4FD 0%, #21b7ff 100%);
		margin-bottom: 7px;
	}
	.logIn .or{
		width: 90%;
		margin: 8px 5%;
	}
	.logIn .or .text{
		margin-left: calc(100%/2 - 50px);
		width: 50px;
		text-align: center;
		height: 20px;
		color: grey;
		font-weight: 100;
	}
	@media all and (max-width : 900px) {
		.logIn{
			width: 500px;
			height: 523px;
			background: white;
			transition: all 0.3s ease;
		}
		.logIn .left{
			display: none;
		}

		.logIn .right{
			width: 100%;
			height: 100%;
			float: left;
			margin-left: 22%;
		}

		.logIn .right .logo{
			font-size: 90px;
			padding: 20px;
			margin-left: 77px;
			margin-top: 40px;
		}

		.logIn .right .lostPassword{
			float: right;
			width: 50%;
			height: 20px;
			font-size: 17px;
			margin: 0px;
			margin-right: 100px;
			padding-bottom: 10px;
		}
		.logIn .or .text{
			margin: 0;
			width: 100%;
			margin-left: -25%;
		}
	}

	@media all and (max-width : 550px) {
		.logIn{
			width: 90%
		}
		.logIn .right{
			width: 80%;
			margin: 0 10% 0 10%;
			display: block;
		}
		.logIn .right input{
			width: 76%;
			height: 50px;
			font-size: 20px;
			padding: 0 12% 0 12%;
		}
		.logIn .right .inputIcon{
			margin-left: -69.5%;
		}
		.logIn .right button{
			width: 100%;
		}
		
		.logIn .right .fa-sign-in-alt{
			font-size: 80px;
			display: block;
			margin: 30px auto 0 auto
		}
		.logIn .right .lostPassword{
			float: right;
			width: auto;
			font-size: 18px;
			margin: 0px;
		}
		.logIn .right .goToRegister{
			width: 100%;
			text-align: center;
		}
		.logIn .right .goToRegister a{
			margin-left: 0px;
		}
		.logIn .or .text{
			margin: 0;
			width: 100%;
		}
	}
	@media all and (max-width : 350px) {
		.logIn .right .inputIcon{
			margin-left: -69.5%;
			font-size: 17px !important;
			margin-top: 40px;
		}
		.logIn .right .fa-sign-in-alt{
			font-size: 70px;
			margin: 30px auto 0 auto
		}
		.logIn .right input{
			font-size: 17px;
		}
	}
</style>

