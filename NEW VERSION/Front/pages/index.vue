<template>
    <div class="mainPage">
        <div class="waveWrapper waveAnimation">
            <div class="waveWrapperInner bgTop">
                <div class="wave waveTop" style="background-image: url('/assets/img/main/wawes/wave-top.png')"></div>
            </div>
            <div class="waveWrapperInner bgMiddle">
                <div class="wave waveMiddle" style="background-image: url('/assets/img/main/wawes/wave-mid.png')"></div>
            </div>
            <div class="waveWrapperInner bgBottom">
                <div class="wave waveBottom" style="background-image: url('/assets/img/main/wawes/wave-bot.png')"></div>
            </div>
        </div>
        <div class="header">
            <div class="menu">
                <div class="logo">
                    <img src="/assets/img/logo.png">
                </div>
                <ul class="buttons">
                    <a @click="openSlide(1)" class="button">Возможности</a>
                    <a @click="openSlide(2)" class="button">Безопасность</a>
                    <router-link to="/login" class="button">Войти</router-link>
                </ul>
            </div>

            <div class="describe">
                <div class="text" v-wow="{ 'animation-name': 'bounceInLeft','animation-duration': '1s'}">
                    <span class="globalDesc">Бесплатный финансовый менеджер</span><br><br>
                    <span class="afterGlobalDesc">
                        Позволяет контролировать и правильно распределять личный бюджет. Автоматическое построение удобной статистики доходов и расходов. Поможет экономить и добиваться финансовой цели.
                        <!--<br><br>
                        Не нужно ничего скачивать. Наш сервис доступен с любого браузера онлайн 24/7 в мобильном или компьютерном режиме.
                        --></span>
                    <div @click="$router.push('/register')" class="btn register">Регистрация</div>
                </div>
                <div class="image" v-wow="{ 'animation-name': 'bounceInRight','animation-duration': '1s'}">
                    <img src="/assets/img/main/macbook.png">
                </div>
            </div>
        </div>

        <div ref="slaid-1" class="text_about">В чем полезность нашего сервиса?</div>
            
        <div class="blocks">
            <div v-on:click="blockSelect=2" class="block" v-wow="{ 'animation-name': 'bounceInLeft','animation-duration': '3s'}">
                <div class="image"><img src="/assets/img/main/briefcase.svg"></div>
                <h2>Все финансы в одном месте</h2>
                <span>Объедините все ваши финансы в одной системе. Ведите общий учет наличных, карт, кредитов вкладов, криптовалюты. В кабинете нашего сервиса можете наблюдатсь общее финансовое состояние.</span>
            </div>
            <div v-on:click="blockSelect=1" class="block" v-wow="{ 'animation-name': 'bounceInLeft','animation-duration': '2s'}">
                <div class="image"><img src="/assets/img/main/revenue.svg"></div>
                <h2>Контроль доходов и расходов</h2>
                <span>Все ваши доходы и расходы по всем вашим счетам записаны в одном месте. Вы можете анализировать общую картину доходов и расходов, которые вы производили наличкой/картой/криптовалютой и т.д.</span>
            </div>
            <div v-on:click="blockSelect=3" class="block" v-wow="{ 'animation-name': 'bounceInLeft','animation-duration': '1s'}">
                <div class="image"><img src="/assets/img/main/goal.svg"></div>
                <h2>Финансовая цель</h2>
                <span>Хотите накопить большую сумму? Указав краткую информацию в кабинете, вы сможете всегда наблюдать сколько вам нужно откладывать в день/неделю или месяц.<!-- Кроме этого, у вас будут напоминания, о том, что пора отложить копеечку-->.</span> 
            </div>
        </div>

        <div ref="slaid-1" class="text_about" style="padding-top: 100px">Основной функционал</div>
        <div class="functions">
            <div class="left" v-wow="{ 'animation-name': 'bounceInLeft','animation-duration': '1s'}">
                <div class="desc color1">
                    <div class="leftDesc">
                        <div class="name">
                            Добавлене транзакции
                        </div>
                        Интуитивно понятное ручное добавление ваших операций доходов или расходов на счетах
                    </div>
                    <div class="rightImage">
                        <img src="/assets/img/main/functions/smartphone.svg">
                    </div>
                </div>
                <div class="desc color2">
                    <div class="leftDesc">
                        <div class="name">
                            Список счетов
                        </div>
                        Вы можете добавить столько счетов, сколько у вас имеется на самом деле. На каждом счету может быть 4 разных валютных пары.
                    </div>
                    <div class="rightImage">
                        <img src="/assets/img/main/functions/credit-card.svg">
                    </div>
                </div>
                <div class="desc color3">
                    <div class="leftDesc">
                        <div class="name">
                            Курсы валют
                        </div>
                        Обновление курсов происходит каждые 10 минут. Валюты: Доллар, Евро, Рубль, Гривна
                    </div>
                    <div class="rightImage">
                        <img src="/assets/img/main/functions/money-growth.svg">
                    </div>
                </div>
            </div>
            <div class="mobile" v-wow="{ 'animation-name': 'slideInUp','animation-duration': '1s'}">
                <div class="image"><img src="/assets/img/main/mobile.png"></div>
            </div>
            <div class="right" v-wow="{ 'animation-name': 'bounceInRight','animation-duration': '1s'}">
                <div class="desc color4">
                    <div class="leftImage">
                        <img src="/assets/img/main/functions/stats.svg">
                    </div>
                    <div class="leftDesc">
                        <div class="name">
                            Статистика операций
                        </div>
                        Имеется график доходов и расходов. Диаграмма растрат и полнастая история доходов и трат
                    </div>
                </div>
                <div class="desc color5">
                    <div class="leftImage">
                        <img src="/assets/img/main/functions/targeting.svg">
                    </div>
                    <div class="leftDesc">
                        <div class="name">
                            Финансовая цель
                        </div>
                        Данный модуль поможет вам накопить сумму. Включает в себя статистику и покажет, сколько вам нужно копить каждый день/неделю/месяц
                    </div>
                </div>
                <div class="desc color6">
                    <div class="leftImage">
                        <img src="/assets/img/main/functions/music-player.svg">
                    </div>
                    <div class="leftDesc">
                        <div class="name">
                            Гибкие настройки
                        </div>
                        Вы сможете настроить дизайн и управление кабинетом полностью под себя
                    </div>
                </div>	
            </div>
        </div>

        <div ref="slaid-2" class="security" v-wow="{ 'animation-name': 'fadeInUp','animation-duration': '1s'}">
            <div class="image">
                <img src="/assets/img/main/security.png">
            </div>
            <div class="text">
                <h1>Подробнее о безопасности</h1>
                
                <div class="desc">
                    <div class="dot" style="color:#FAB143"><i class="fas fa-circle"></i></div>
                    <div class="descText">Регистрация в сервисе анонимна. При желании, вы можете не указывать email, когда регистрируетесь.</div>
                </div>
                <div class="desc">
                    <div class="dot" style="color:#41A79B"><i class="fas fa-circle"></i></div>
                    <div class="descText">Все данные передаются по безопасному HTTPS протоколу с использованием шифрования.</div>
                </div>
                <div class="desc">
                    <div class="dot" style="color:#F8735E"><i class="fas fa-circle"></i></div>
                    <div class="descText">Мы не храним и не запрашиваем никаких паролей от банков/кошельков и т.п. Все изменения ваших доходов/растрат вы вносите вручную.</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {}
</script>

<style scoped>
@keyframes move_wave {
    0% {
        transform: translateX(0) translateZ(0) scaleY(1)
    }
    50% {
        transform: translateX(-25%) translateZ(0) scaleY(0.55)
    }
    100% {
        transform: translateX(-50%) translateZ(0) scaleY(1)
    }
}
.waveWrapper {
    overflow: hidden;
    left: 0;
    right: 0;
    bottom: 0;
    top: 0;
    margin: auto;
}
.waveWrapperInner {
    position: absolute;
    width: 100%;
    overflow: hidden;
    height: 700px;

    background-image: linear-gradient(to top, rgba(82,200,255,1) 17%, rgb(25, 96, 238) 83%);
}
.bgTop {
    z-index: 15;
    opacity: 0.5;
}
.bgMiddle {
    z-index: 10;
    opacity: 0.75;
}
.bgBottom {
    z-index: 5;
}
.wave {
    position: absolute;
    left: 0;
    width: 200%;
    height: 700px;
    background-repeat: repeat no-repeat;
    background-position: 0 bottom;
    transform-origin: center bottom;
}
.waveTop {
    background-size: 50% 100px;
}
.waveAnimation .waveTop {
  animation: move-wave 3s;
   -webkit-animation: move-wave 3s;
   -webkit-animation-delay: 1s;
   animation-delay: 1s;
}
.waveMiddle {
    background-size: 50% 120px;
}
.waveAnimation .waveMiddle {
    animation: move_wave 10s linear infinite;
}
.waveBottom {
    background-size: 50% 100px;
}
.waveAnimation .waveBottom {
    animation: move_wave 15s linear infinite;
}

.mainPage{
    background: white;
}

.header{
    /*background-image: url(/assets/img/main/head.png);
    background-position: top center;
    background-repeat: no-repeat;
    background-size: cover;*/
    width: 100%;
    height: 700px;
    z-index: 9999999;
    margin-top: 10px;
    position: absolute;
    overflow-x: hidden;
}
.header .menu{
    width: 70%;
    margin: 0 15% 0 15%;
    display: inline-block;
    font-family: 'Exo2-Medium';
}
.header .menu .logo{
    float: left;
}
.header .menu .buttons{
    float: right;
}
.header .menu .buttons .button{
    list-style-type: none;
    float: left;
    padding: 25px 15px 25px 15px;
    color: rgb(233, 233, 233);
    font-size: 20px;
    cursor: pointer;
    transition: all 0.3s ease;
}
.header .menu .buttons .button:last-child{
    color: rgb(255, 255, 255);
}
.header .menu .buttons .button:hover{
    margin-top: -3px;
    color: rgb(237, 238, 243);
    text-shadow: 1px 3px 5px rgb(27, 27, 27, 0.5);
    transition: all 0.2s ease;
}
.header .describe{
    width: 70%;
    margin: 50px 15% 0 15%;
}
.header .describe .text{
    float: left;
    width: 35%;
    color: white;
}
.header .describe .image{
    float: left;
    width: 65%;
}
.header .describe .image img{
    width: 100%;
}
.header .describe .text .globalDesc{
    font-size: 40px;
    font-family: 'Exo2-Medium';
    line-height: 40px;
}
.header .describe .text .afterGlobalDesc{
    font-size: 20px;
    font-family: 'Exo2-Light';
}

.header .describe .btn{
    height: 80px;
    line-height: 75px;
    width: 80%;
    font-size: 35px;
    text-align: center;
    margin-top: 60px;
    cursor: pointer;
    box-shadow: 0 6px 10px 0 rgba(0,0,0,0.1);
    border-radius: 50px;
    font-family: 'Exo2-Thin';
}
.header .describe .register{
    background: rgb(147, 218, 42);
    border-top: 1px solid rgb(156, 230, 45);
    border-bottom: 1px solid rgb(135, 199, 40);
}
.header .describe .register:hover{
    background: rgb(137, 202, 39);
    border-top: 1px solid rgb(156, 230, 45);
    border-bottom: 1px solid rgb(124, 184, 35);
}


.text_about{
    font-size: 25px;
    width: 100%;
    text-align: center;
    padding-top: 750px;
}
.blocks{
    width: 70%;
    margin: 30px 15% 20px 15%;
    display: flex;
    justify-content: space-between;
    height: 100%;
}
.blocks .block{
    width: 25%;
    box-shadow: 0px 0px 60px -6px rgba(0,0,0,0.05);
    padding: 2%;
    cursor: pointer;
    border-radius: 20px;
    color: rgb(126, 126, 126);
    transition: all 0.3s ease;
    text-align: center;
}
.blocks .block .image{
    width: 110px;
    height: 110px;
    border-radius: 50%;
    text-align: center;
    margin: 0 auto 0 auto;
    background: rgba(48,117,255,1);
    background: linear-gradient(45deg, rgba(48,117,255,1) 0%, rgba(82,200,255,1) 100%);
    box-shadow: 0px 10px 20px 5px rgba(82,200,255,0.2);
}
.blocks .block .image img{
    width: 70px;
    padding-top: 18px;
}
.blocks .block h2{
    font-size: 19px;
    font-family: 'Exo2-Medium';
    color: rgb(59, 59, 59);
}
.blocks .block span{
    font-size: 16px;
    font-family: 'Exo2-Light';
}
.blocks .block:hover{
    background: rgba(48,117,255,1);
    background: linear-gradient(45deg, rgba(48,117,255,1) 0%, rgba(82,200,255,1) 100%);
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#3075ff', endColorstr='#52c8ff', GradientType=1 );
    color: white;
    transition: all 0.3s ease;
    box-shadow: 0px 0px 22px -6px rgba(0,0,0,0.35);
}

.functions{
    width: 90%;
    margin: 0 5% 0 5%;
    margin-top: 50px;
    display: inline-block;
}
.functions .desc{
    max-width: 70%;
    padding: 20px;
    border-radius: 10px;
    margin-top: 50px;
    background: rgb(255, 255, 255);
    box-shadow: 0px 0px 22px -6px rgba(0,0,0,0.35);
    font-size: 17px;
    font-family: 'Exo2-Light';
    background: linear-gradient(45deg, #EECFBA, #C5DDE8);
    color: white;
    transition: 0.3s;
}
.functions .desc .leftDesc{
    float: left;
    width: 75%;
}
.functions .desc .rightImage{
    float: right;
    width: 25%;
}
.functions .desc .leftImage{
    float: left;
    width: 25%;
}
.functions .desc img{
    filter: invert(1);
    width: 80%;
    text-align: right;
    opacity: 0.7;
    line-height: 50%;
    transition: 0.3s;
}
.functions .desc .name{
    width: 100%;
    font-size: 25px;
    font-family: 'Exo2-Bold';
}
.functions .left{
    float: left;
    width: 35%;
}
.functions .mobile{
    float: left;
    width: 30%;
    text-align: center;
}
.functions .right{
    float: left;
    width: 35%;
}
.functions .left .desc{
    float: right;
    text-align: right;
}
.functions .right .desc{
    float: left;
}
.functions .mobile img{
    width: 70%;
    transition: 2s;
}
.functions .mobile:hover img{
    width: 75%;
    transition: 1s;
}
.functions .desc:hover{
    box-shadow: 0px 0px 40px -6px rgba(0,0,0,0.30);
    transition: 0.3s;
}
.functions .desc:hover img{
    opacity: 1;
    transition: 0.3s;
}


.functions .color1{
    background: linear-gradient(-45deg, #52E5E7, #360940);
}
.functions .color2{
    background: linear-gradient(-45deg, #FEC194, #FF0061);
}
.functions .color3{
    background: linear-gradient(-45deg, #E2B0FF, #9F44D3);
}
.functions .color4{
    background: linear-gradient(45deg, #43CBFF, #9708CC);
}
.functions .color5{
    background: linear-gradient(45deg, #FDD819, #E80505);;
}
.functions .color6{
    background: linear-gradient(45deg, #F05F57, #360940);
}

.security{
    width: 100%;
    height: 500px;
    display: inline-block;
    margin-top: 100px;
    display: flex;
    justify-content: space-between;
}
.security .image{
    width: 40%;
    padding-right: 50px;
    float: left;
}
.security img{
    height: 100%;
    float: right;
}
.security .text{
    width: 60%;
    padding: 40px 0% 5px 3%;
    float: left;
    color: rgb(70, 75, 71);
}
.security .text h1{
    font-family: 'Exo2-Bold';
    font-size: 40px;
    color: #3D3C51;
}
.security .text .desc{
    width: 70%;
    margin-top: 30px;
    display: inline-block;
    line-height: 25px;
}
.security .text .desc .dot{
    width: 30px;
    font-size: 7px;
    float: left;
    position: absolute;
}
.security .text .desc .descText{
    color: #9292A4;
    float: left;
    font-family: 'Exo2-Light';
    font-size: 25px;
    padding-left: 30px;
}

@media all and (max-width : 1400px) {
    .header .menu{
        width: 90%;
        margin: 0 5% 0 5%;
    }
    .header .describe{
        width: 90%;
        margin: 10px 5% 0 5%;
    }
    .blocks{
        width: 90%;
        margin: 30px 5% 20px 5%;
    }
    .functions .desc{
        max-width: 95%;
    }
    .functions .mobile img{
        width: 90%;
    }
    .functions .mobile:hover img{
        width: 90%;
    }
}

@media all and (max-width : 900px) {
    .waveWrapperInner {
        height: 900px;
    }
    .wave {
        height: 900px;
    }
    .text_about{
        margin-top: 0px;
    }
    .header{
        height: 1050px;
    }
    .header .menu{
        float: left;
        width: 100%;
        margin: 0;
    }
    .header .menu .logo{
        float: left;
        width: 100%;
        text-align: center;
    }
    .header .menu .buttons{
        float: left;
        width: 100%;
        margin: 0 auto 0 auto;
    }
        
    .header .describe{
        width: 90%;
        margin: 10px 5% 0 5%;
        text-align: center;
    }
    .header .describe .text{
        float: left;
        width: 100%;
        color: white;
    }
    .header .describe .image{
        float: left;
        width: 115%;
        margin-left: -10%;
        margin-top: 30px;
    }
    .header .describe .image img{
        width: 100%;
        text-align: center;
    }
    .header .describe .btn{
        height: 60px;
        line-height: 60px;
        width: 100%;
        font-size: 25px;
        margin-top: 20px;
    }
    
    .text_about{
        padding-top: 900px;
    }
    .blocks{
        width: 90%;
        margin: 30px 5% 20px 5%;
        display: block;
        height: 100%;
    }
    .blocks .block{
        width: 95%;
        margin-bottom: 15px;
    }
    .blocks .block:first-child{
        border-radius: 20px 20px 20px 20px;
    }
    .blocks .block:last-child{
        border-radius: 20px 20px 20px 20px;
    }

    .blocks .block .dropdown{
        display: none;
    }    

    .functions{
        margin-top: 15px;
    }
    .functions .desc{
        margin-top: 20px;
    }
    .functions .left{
        float: left;
        width: 100%;
    }
    .functions .right{
        float: left;
        width: 100%;
    }
    .functions .mobile{
        display: none;
    }

    .security{
        width: 100%;
        margin-top: 100px;
        display: inline-block;
    }
    .security .image{
        width: 100%;
        padding-right: 0px;
        float: none;
        text-align: center;
    }   
    .security img{
        width: 60%;
        float: none;
    }
    .security .text{
        width: 100%;
        padding: 40px 0% 5px 0%;
        float: none;
    }
    .security .text .desc{
        width: 70%;
        margin-top: 30px;
        margin: 0 15% 0 15%;
    }
    .security .text h1{
        font-size: 30px;
        text-align: center;
    }
}


@media all and (max-width : 500px) {
    .header .menu{
        width: 100%;
        margin: 0 0% 0 0%;
    }
    .header .menu .buttons{
        margin-left: -5%;
    }
    .header .menu .buttons .button{
        padding: 25px 7px 25px 7px;
    }
}
</style>
