<template>
    <div class="modal-window">
        <div class="in">
			<div class="close" @click="close()">
				<fa :icon="['fas', 'times']"/>
			</div>
			<div class="modal_head"> 
				Новая хотелка<br>
				<small>Дайте краткое название и укажите, к какой дате вы хотите выполнить хотелку</small>
			</div>
			
            <div class="inputs">
                <input type="text" v-model="name" placeholder="Название">
            </div>
            
            <div class="btn buttons">
                <a @click="add()">
                    Добавить
                </a>
                <a @click="close()">ОТМЕНА</a>
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
				name: ''
            }
        },
        created(){
            if (!process.browser) {
                return
            }
        },
        methods: {
			close(){
				this.$parent.new_wish_modal = false
            },
            add(){
                var id = Object.keys(this.$parent.wishes).length + 1
                if(id>4){
                    console.log('more than 4')
                    return
                }
                this.$parent.wishes[id] = {
                    name: this.name,
                    date: 100000
                }
                this.$parent.new_wish_modal = false
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

    .in .inputs{
        width: 70%;
        margin: 30px 15%;
    }
    .in .inputs input{
        width: calc(70% - 40px);
        padding: 0 20px;
        height: 50px;
        border: none;
        border-radius: 10px;
        outline: none;
    }
    
    .modal-window .in .buttons{
        width: 450px;
        display: flex;
        justify-content: space-between;
        margin-top: 7px;
        margin-left: calc(50% - (450px / 2));
    }
    .modal-window .in .btn a{
        width: 60%;
        float: left;
        height: 45px;
        line-height: 45px;
        font-size: 20px;
        color: black;
        display: block;
        font-weight: 800;
        background: #FDE400;
        border-radius: 5px;
        transition: 0.2s;
        text-align: center;
        cursor: pointer;
    }
    .modal-window .in .btn a:hover{
        box-shadow: 0 0 7px #FDE400;
        transition: 0.2s;
    }
    .modal-window .in .btn a:last-child{
        width: 35%;
        background: none;
        color: white;
        border: 1px solid white;
        cursor: pointer;
    }
    .modal-window .in .btn a:last-child:hover{
        border: 1px solid #FDE400;
        transition: 0.2s;
        box-shadow: 0 0 7px #FDE400, inset 0px 0px  7px #FDE400;
    }
</style>