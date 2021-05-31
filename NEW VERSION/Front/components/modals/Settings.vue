<template>
    <div class="modal-window">
        <div class="in">
			<div class="close" @click="close()">
				<fa :icon="['fas', 'times']"/>
			</div>
			<div class="modal_head"> 
				Настройки<br>
				<small>Выберите, на сколько вы хотите продлить привилегию</small>
			</div>
			asdasd
		</div>
	</div>
</template>
<script>
    export default {
        props: {
            
        },
        data(){
            return{
				
            }
        },
        created(){
            if (!process.browser) {
                return
            }
        },
        methods: {
			close(){
				this.$parent.settings_modal = false
			}
        }
    }
</script>
<style scoped>
    .modal-window {
        position: fixed;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
        z-index: 999;
        transition: all 0.3s;
        pointer-events: auto;
        color: white;
        background-color: rgba(42, 134, 177, 0.1);
        backdrop-filter: blur(5px);
    }
    .modal-window .in{
        width: 700px;
        height: 300px;
        border-radius: 20px;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: #608AE7;
    }
    .modal-window .modal_head{
        width: calc(100% - 110px);
        margin-top: 30px;
        padding: 0 30px 0 80px;
        font-size: 25px;
        font-weight: 600;
    }
    .modal-window .modal_head small{
        font-size: 14px;
        color: #BFD0F5;
        margin-top: 2px;
        font-weight: 300;
        display: block;
    }
	
	.close{
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
		margin-left: 630px;
		margin-top: 20px;
		position: absolute;
	}
	.close:hover{
		background: rgba(255, 255, 255, 0.3);
		transition: 0.2s;
	}
</style>