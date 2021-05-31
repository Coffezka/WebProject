<template>
	<div>
		<WishlistNew v-if="new_wish_modal" />

		<div class="block block_new_operation">
			<div class="nameBlock">
				<img src="/assets/img/emoji/light.png">
				Мои хотелки
			</div>
			<div class="bContent">
				<div class="wish" v-for="(i, id) in wishes" v-bind:key="i.date" 
				@click="done(id)">
                    <fa :icon="['fas', 'check']"/>
					<div class="describe">
						{{i.name}}<br>
					</div>
					<div class="date">
						До {{millsToDate(i.date)}}
					</div>
				</div>
				<div class="wish empty" v-if="Object.keys(wishes).length < 4" 
				@click="new_wish_modal = true">
					<div class="plus">
						+
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
<script>
	import WishlistNew from '~/components/modals/Wishlist_new.vue'
    export default {
        props: {
            
        },
        data(){
            return{
				new_wish_modal: false,
                wishes: {
					1: {
						name: 'Самолетик',
						date: 1621195800000
					},
					2: {
						name: 'Мащинка',
						date: 1621095800000
					}
				}
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
				return (this.$moment(milliseconds).format('lll'));
			},
			done(id){
				delete this.wishes[id]
				this.$forceUpdate()
			}
		},
		components: {
			WishlistNew
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
	.bContent{
		width: 90%;
		margin-left: 5%;
	}
	.wish{
		width: calc(50% - 44px);
		padding: 10px;
		margin: 20px;
		height: 100px;
		border: 2px solid #444B87;
		border-radius: 10px;
		float: left;
		cursor: pointer;
		transition: 0.2s;
	}
	.wish .describe{
		font-weight: 800;
		color: white;
		font-size: 19px;
	}
	.wish .date{
		margin-top: 30px;
		color: grey;
		font-weight: 400;
	}
	.wish svg{
		display: none;
		transition: 0.2s;
	}
	.wish:hover svg{
		transition: 0.2s;
		display: block;
		position: absolute;
		color: #2aff2abd;
		font-size: 48px;
		margin-left: 67px;
		margin-top: 16px;
	}
	.empty{
		background: #262b50;
		cursor: pointer;
		transition: 0.2s;
	}
	.empty:hover{
		background: #313766;
		transition: 0.2s;
	}
	.empty .plus{
		font-size: 70px;
		font-weight: 400;
		text-align: center;
		line-height: 60px;
		color: #444B87;
		transition: 0.2s;
	}
	.empty:hover .plus{
		color: #161a41;
		transition: 0.2s;
	}

</style>