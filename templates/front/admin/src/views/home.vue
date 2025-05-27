<template>
	<div class="home-content">
		<!-- title -->
		<div id="home-title" class="home-title animate__animated">
			<div class="titles" >
				{{this.$project.projectName}}
			</div>
		</div>
		<!-- statis -->
		<div class="statis-box">
			<div id="statis1" class="statis1 animate__animated" v-if="isAuth('monthlysalesofmanufacturers','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-zhangjie8"></span>
				</div>
				<div class="right">
					<div class="num">{{monthlysalesofmanufacturersCount}}</div>
					<div class="name">厂商每月销售总数</div>
				</div>
			</div>
			<div id="statis2" class="statis2 animate__animated" v-if="isAuth('monthlysalesofcarmodels','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-chujia3"></span>
				</div>
				<div class="right">
					<div class="num">{{monthlysalesofcarmodelsCount}}</div>
					<div class="name">车型每月销量总数</div>
				</div>
			</div>
			<div id="statis3" class="statis3 animate__animated" v-if="isAuth('overallsalesofcars','首页总数')">
				<div class="left">
					<span class="icon iconfont icon-qita3"></span>
				</div>
				<div class="right">
					<div class="num">{{overallsalesofcarsCount}}</div>
					<div class="name">汽车总体销量总数</div>
				</div>
			</div>
		</div>
		<!-- statis -->
	
		<!-- echarts -->
	</div>
</template>
<script>
import 'animate.css'
//0
import router from '@/router/router-static'
import * as echarts from 'echarts'
export default {
	data() {
		return {
			monthlysalesofmanufacturersCount: 0,
			monthlysalesofcarmodelsCount: 0,
			overallsalesofcarsCount: 0,
		};
	},
	mounted(){
		this.init();
		this.getmonthlysalesofmanufacturersCount();
		this.getmonthlysalesofcarmodelsCount();
		this.getoverallsalesofcarsCount();
		window.addEventListener('scroll', this.handleScroll)
		setTimeout(()=>{
			this.handleScroll()
		},100)
	},
	computed: {
		avatar(){
			return this.$storage.get('headportrait')?this.$storage.get('headportrait'):''
		},
	},
	methods:{
		handleScroll() {
			let arr = [
				{id:'home-title',css:'animate__fadeInUp'},
				{id:'statis1',css:'animate__fadeInUp'},
				{id:'statis2',css:'animate__fadeInUp'},
				{id:'statis3',css:'animate__fadeInUp'},
			]
			
			for (let i in arr) {
				let doc = document.getElementById(arr[i].id)
				if (doc) {
					let top = doc.offsetTop
					let win_top = window.innerHeight + window.pageYOffset
					// console.log(top,win_top)
					if (win_top > top && doc.classList.value.indexOf(arr[i].css) < 0) {
						// console.log(doc)
						doc.classList.add(arr[i].css)
					}
				}
			}
		},
		init(){
			if(this.$storage.get('Token')){
				this.$http({
					url: `${this.$storage.get('sessionTable')}/session`,
					method: "get"
				}).then(({ data }) => {
					if (data && data.code != 0) {
						router.push({ name: 'login' })
					}
				});
			}else{
				router.push({ name: 'login' })
			}
		},
		getmonthlysalesofmanufacturersCount() {
			this.$http({
				url: `monthlysalesofmanufacturers/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.monthlysalesofmanufacturersCount = data.data
				}
			})
		},
		getmonthlysalesofcarmodelsCount() {
			this.$http({
				url: `monthlysalesofcarmodels/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.monthlysalesofcarmodelsCount = data.data
				}
			})
		},
		getoverallsalesofcarsCount() {
			this.$http({
				url: `overallsalesofcars/count`,
				method: "get"
			}).then(({
				data
			}) => {
				if (data && data.code == 0) {
					this.overallsalesofcarsCount = data.data
				}
			})
		},
	}
};
</script>
<style lang="scss" scoped>
	.home-content {
		padding: 60px 0px;
		margin: 20px 0 0 80px;
		background: url(http://codegen.caihongy.cn/20241212/c085feb1bcc943f3b8cc1b44b9839c59.png) no-repeat center top / cover;
		display: flex;
		min-height: 100vh;
		justify-content: flex-start;
		position: relative;
		flex-wrap: wrap;
		.home-title {
			border-radius: 5px;
			padding: 10px 0;
			box-shadow: 0 0px 0px rgba(0,0,0,.3);
			margin: 10px 0;
			display: none;
			width: 100%;
			justify-content: center;
			align-items: center;
			transition: 0.3s;
			.titles {
				padding: 0 0 0 12px;
				color: #333;
				font-size: 24px;
				line-height: 44px;
			}
		}
		.home-title:hover {
			transform: translate3d(0, 0px, 0);
			z-index: 1;
			background: rgba(255,255,255,.12);
		}
		.statis-box {
			border-radius: 10px;
			padding: 10px ;
			margin: 0 0 0 10px;
			background: none;
			display: flex;
			width: 100%;
			justify-content: center;
			align-items: center;
			flex-wrap: wrap;
			order: 2;
			height: auto;
			.statis1 {
				border: 1px solid #0F1330;
				border-radius: 10px;
				padding: 10px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: 200px;
				transition: 0.3s;
				height: 90px;
				.left {
					border-radius: 100%;
					background: #e9f0f9;
					display: none;
					width: 66px;
					justify-content: center;
					align-items: center;
					height: 66px;
					.iconfont {
						color: #2582f3;
						font-size: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #0F1330;
						font-weight: 500;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 15px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis1:hover {
				transform: translate3d(0, 0px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis2 {
				border: 1px solid #0F1330;
				border-radius: 10px;
				padding: 10px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: 200px;
				transition: 0.3s;
				height: 90px;
				.left {
					border-radius: 100%;
					background: #fcece1;
					display: none;
					width: 60px;
					justify-content: center;
					align-items: center;
					height: 60px;
					.iconfont {
						color: #f56c17;
						font-size: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #0F1330;
						font-weight: 500;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 15px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis2:hover {
				transform: translate3d(0, 0px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis3 {
				border: 1px solid #0F1330;
				border-radius: 10px;
				padding: 0 10px 0px 10px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: 200px;
				transition: 0.3s;
				height: 90px;
				.left {
					border-radius: 100%;
					background: #e7fbfd;
					display: none;
					width: 60px;
					justify-content: center;
					align-items: center;
					height: 60px;
					.iconfont {
						color: #21c2f6;
						font-size: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #0F1330;
						font-weight: 500;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 15px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis3:hover {
				transform: translate3d(0, 0px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis4 {
				border: 1px solid #0F1330;
				border-radius: 10px;
				padding: 0 10px 0px 10px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: 200px;
				transition: 0.3s;
				height: 90px;
				.left {
					border-radius: 100%;
					background: #e0ffe9;
					display: none;
					width: 60px;
					justify-content: center;
					align-items: center;
					height: 60px;
					.iconfont {
						color: #45d45a;
						font-size: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #0F1330;
						font-weight: 500;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 15px;
						line-height: 24px;
						height: 24px;
					}
				}
			}
			.statis4:hover {
				transform: translate3d(0, 0px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
			.statis5 {
				border: 1px solid #0F1330;
				border-radius: 10px;
				padding: 0 10px 0px 10px;
				margin: 10px;
				background: #fff;
				display: flex;
				width: 200px;
				transition: 0.3s;
				height: 90px;
				.left {
					border-radius: 100%;
					background: #fbe8db;
					display: none;
					width: 60px;
					justify-content: center;
					align-items: center;
					height: 60px;
					.iconfont {
						color: #d26515;
						font-size: 40px;
					}
				}
				.right {
					flex-direction: column;
					display: flex;
					width: 160px;
					justify-content: center;
					align-items: center;
					.num {
						margin: 5px 0;
						color: #333;
						font-weight: 500;
						font-size: 30px;
						line-height: 24px;
						height: 24px;
					}
					.name {
						margin: 5px 0;
						color: #666;
						font-size: 15px;
						line-height: 24px;
						height: 24px;
						order: 2;
					}
				}
			}
			.statis5:hover {
				transform: translate3d(0, 0px, 0);
				z-index: 1;
				background: rgba(255,255,255,1);
			}
		}
	}
	
	.echarts-flag-2 {
		display: flex;
		flex-wrap: wrap;
		justify-content: space-between;
		padding: 10px 20px;
		background: rebeccapurple;
	
		&>div {
			width: 32%;
			height: 300px;
			margin: 10px 0;
			background: rgba(255,255,255,.1);
			border-radius: 8px;
			padding: 10px 20px;
		}
	}
	.animate__animated {
		animation-fill-mode: none;
	}
</style>
