<template>
	<div class="header">
		<div class="logo">
			<img src="/assets/img/logo.png" alt="MyWallets">
		</div>
		<div class="pagename">
			Личный кабинет
		</div>
		<div class="avatar">
			<img src="/assets/img/empty_avatar.png" alt="EnJay - аватар">
		</div>
		<div class="userinfo">
			{{name}}<br>
			<div class="settings" @click="openSettings()">
				<fa :icon="['fas', 'cog']"/>
			</div>
		</div>
	</div>
</template>
<script>
    export default {
        props: {
            
        },
        data(){
            return{
				name: 'EnJay'
            }
        },
        created(){
            if (!process.browser) {
                return
            }
        },
        methods: {
            openSettings(){
				this.$parent.settings_modal = true
			}
        }
    }
</script>
<style scoped>
	.logo{
		padding: 7px 20px;
		float: left;
		border-right: 1px solid #353c70;
	}
	.pagename{
		float: left;
		color: white;
		margin-left: 40px;
		font-size: 30px;
		margin-top: 45px;
		font-weight: 1000;
		line-height: 25px;
	}
	.header{
		width: 100%;
		background: #2C325C;
		height: 120px;
		margin-top: 0px;
    	margin-top: -141px;
		box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
	}
	.header .avatar{
		width: 100px;
		height: 100px;
		border-radius: 50%;
		overflow: hidden;
		background: #1D2141;
		margin-right: 20px;
		margin-top: 10px;
		float: right;
	}
	.header .avatar img{
		width: 90%;
		margin: 5%;
		border: 5px solid #2C325C;
		border-radius: 50%;
	}
	.header .userinfo{
		float: right;
		color: white;
		margin-right: 25px;
		font-size: 30px;
		margin-top: 20px;
		font-weight: 200;
		line-height: 25px;
	}
	.header .userinfo span{
		font-size: 22px;
		font-weight: 400;
	}
	.header .userinfo .settings{
		margin-top: 15px;
		background: rgba(255, 255, 255, 0.1);
		border-radius: 50%;
		width: 40px;
		height: 40px;
		font-size: 22px;
		text-align: center;
		line-height: 40px;
		float: right;
		transition: 0.2s;
		cursor: pointer;
	}
	.header .userinfo .settings:hover{
		background: rgba(255, 255, 255, 0.3);
		transition: 0.2s;
	}
</style>