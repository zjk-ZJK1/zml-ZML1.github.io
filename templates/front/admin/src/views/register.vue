<template>
	<div>
		<div class="register-container">
			<video autoplay muted loop>
				<source src="http://codegen.caihongy.cn/20241022/4bb307b2a15240a4940bc9569f731da8.mp4" type="video/mp4">
				<source src="http://codegen.caihongy.cn/20241022/4bb307b2a15240a4940bc9569f731da8.mp4" type="video/ogg">
				您的浏览器不支持 video 标签。
			</video>
			<el-form v-if="pageFlag=='register'" ref="ruleForm" class="rgs-form animate__animated animate__backInDown" :model="ruleForm" :rules="rules">
				<div class="rgs-form2">
					<div class="title">基于Hive的中国汽车销售的数据分析与预测</div>
					<div class="register-btn">
						<div class="register-btn1">
							<button type="button" class="r-btn" @click="login()">注册</button>
						</div>
						<div class="register-btn2">
							<div class="r-login" @click="close()">已有账号，直接登录</div>
						</div>
					</div>
				</div>
			</el-form>
		</div>
	</div>
</template>

<script>
	import 'animate.css'
export default {
	data() {
		return {
			ruleForm: {
			},
			forgetForm: {},
            pageFlag : '',
			tableName:"",
			rules: {},
		};
	},
	mounted(){
		this.pageFlag = this.$route.query.pageFlag
		if(this.$route.query.pageFlag=='register'){
			
			let table = this.$storage.get("loginTable");
			this.tableName = table;
		}
	},
	created() {
	},
	destroyed() {
		  	},
	methods: {
		changeRules(name){
			if(this.rules[name]){
				return true
			}
			return false
		},
		// 获取uuid
		getUUID () {
			return new Date().getTime();
		},
		close(){
			this.$router.push({ path: "/login" });
		},

        // 多级联动参数


		// 注册
		login() {
			var url=this.tableName+"/register";
			this.$http({
				url: url,
				method: "post",
				data:this.ruleForm
			}).then(({ data }) => {
				if (data && data.code === 0) {
					this.$message({
						message: "注册成功",
						type: "success",
						duration: 1500,
						onClose: () => {
							this.$router.replace({ path: "/login" });
						}
					});
				} else {
					this.$message.error(data.msg);
				}
			});
		}
	}
};
</script>

<style lang="scss" scoped>
.register-container {
	position: relative;
	background-repeat: no-repeat;
	background-size: cover;
	background: linear-gradient( 135deg, #21A5F4 0%, #21A5F4 0%, #2615BC 0%, #2615BC 0%, #228CEB 100%);
	display: flex;
	width: 100%;
	min-height: 100vh;
	justify-content: center;
	align-items: center;
	background-position: center center;
	video {
		transform: translate3d(-50%, -50%, 0);
		margin: auto;
		z-index: auto;
		top: 50%;
		left: 50%;
		object-fit: cover;
		width: 100%;
		position: absolute;
		height: 100%;
	}
	.rgs-form {
		.rgs-form2 {
		padding: 0px 0 0 0;
		margin: 0;
		background: none;
		width: 100%;
		}
		padding: 200px 150px 200px 160px ;
		margin: 40px auto;
		z-index: 1000;
		display: flex;
		background-position: 100% 100%;
		flex-wrap: wrap;
		border-radius: 0;
		background-repeat: no-repeat;
		flex-direction: column;
		background: url(http://codegen.caihongy.cn/20241017/c1556ac5c80c47598f18f1693608ea51.png)  no-repeat  left top /  100% 100%;
		width: 815px;
		align-items: flex-start;
		position: relative;
		height: auto;
		.title {
			padding: 0 150px;
			margin: 0 0 20px 0;
			color: #FFFFFF;
			background: none;
			font-weight: 500;
			width: 100%;
			font-size: 22px;
			line-height: 40px;
			text-align: center;
		}
		.list-item {
			border: 1px solid #1D90C5;
			border-radius: 0;
			padding: 0;
			margin: 0 0 20px;
			background: #0C66A9;
			display: flex;
			width: calc(100% - 0px);
			align-items: center;
			position: relative;
			flex-wrap: wrap;
			/deep/ .el-form-item__content {
				display: block;
				width: 100%;
			}
			.lable {
				padding: 0 5px 0 20px;
				z-index: 99;
				color: #fff;
				left: 10px;
				width: 130px;
				font-size: 16px;
				line-height: 50px;
				position: absolute !important;
				text-align: left;
			}
			.el-input {
				width: 100%;
			}
			.el-input /deep/ .el-input__inner {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px;
			}
			.el-input /deep/ .el-input__inner:focus {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px;
			}
			.el-input-number {
				width: 100%;
			}
			.el-input-number /deep/ .el-input__inner {
				text-align: center;
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px;
			}
			.el-input-number /deep/ .el-input__inner:focus {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px;
			}
			.el-input-number /deep/ .el-input-number__decrease {
				display: none;
			}
			.el-input-number /deep/ .el-input-number__increase {
				display: none;
			}
			.el-select {
				width: 100%;
			}
			.el-select /deep/ .el-input__inner {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px;
			}
			.el-select /deep/ .el-input__inner:focus {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px;
			}
			.el-date-editor {
				width: 100%;
			}
			.el-date-editor /deep/ .el-input__inner {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-date-editor /deep/ .el-input__inner:focus {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			.el-date-editor.el-input {
				width: 100%;
			}
			/deep/ .el-upload--picture-card {
				background: transparent;
				border: 0;
				border-radius: 0;
				width: auto;
				height: auto;
				line-height: initial;
				vertical-align: middle;
			}
			/deep/ .upload .upload-img {
				border: 1px solid #efeff7;
				padding: 0 52px;
				margin: 0 0 0 100px;
				color: #fff;
				flex: 1;
				background: none;
				font-size: 16px;
				line-height: 44px;
				height: 44px;
			}
			/deep/ .el-upload-list .el-upload-list__item {
				border: 1px solid #efeff7;
				padding: 0 52px;
				margin: 0 0 0 100px;
				color: #fff;
				flex: 1;
				background: none;
				font-size: 16px;
				line-height: 44px;
				height: 44px;
			}
			/deep/ .el-upload .el-icon-plus {
				border: 1px solid #efeff7;
				padding: 0 52px;
				margin: 0 0 0 100px;
				color: #fff;
				flex: 1;
				background: none;
				font-size: 16px;
				line-height: 44px;
				height: 44px;
			}
			/deep/ .el-upload__tip {
				color: #666;
				display: none;
				font-size: 15px;
			}
			/deep/ .el-input__inner::placeholder {
				color: #999;
				font-size: 16px;
			}
			.required {
				position: relative;
			}
			.required::after{
				color: red;
				left: 0;
				position: inherit;
				content: "*";
				order: -1;
			}
			.editor {
				border: 1px solid #1D90C5;
				color: #333;
				background: #fff;
				height: auto;
			}
			.editor>.avatar-uploader {
				line-height: 0;
				height: 0;
			}
		}
		.list-item.email {
			input {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			input:focus {
				border: 1px solid #1D90C5;
				border-radius: 0px;
				padding: 0 120px;
				color: #fff;
				background: #0C66A9;
				width: 100%;
				font-size: 16px;
				height: 50px ;
			}
			input::placeholder {
				color: #999;
				font-size: 16px;
			}
			button {
				cursor: pointer;
				border: 1px solid #1D90C5;
				border-radius: 0;
				color: #fff;
				background: #0c66a9;
				display: flex;
				width: 100px;
				justify-content: center;
				align-items: center;
				position: absolute;
				right: 0px;
				height: 50px;
			}
			button:hover {
				opacity: 0.8;
			}
		}
		.register-btn {
			width: 100%;
		}
		.register-btn1 {
			width: 100%;
		}
		.register-btn2 {
			width: 100%;
		}
		.r-btn {
			border: 0px solid rgba(0, 0, 0, 1);
			cursor: pointer;
			border-radius: 0px;
			padding: 0 10px;
			margin: 0px 0;
			color: #fff;
			background: #3FB5E3;
			font-weight: 700;
			width: 100%;
			font-size: 22px;
			min-width: 68px;
			height: 50px;
		}
		.r-btn:hover {
			border: 0px solid rgba(0, 0, 0, 1);
			opacity: 0.8;
		}
		.r-login {
			cursor: pointer;
			padding: 0;
			color: #fff;
			display: inline-block;
			text-decoration: none;
			width: 100%;
			font-size: 15px;
			line-height: 40px;
			text-align: right;
		}
		.r-login:hover {
			opacity: 1;
		}
	}
}
	
	::-webkit-scrollbar {
	  display: none;
	}
</style>
