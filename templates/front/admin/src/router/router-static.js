import Vue from 'vue';
//配置路由
import VueRouter from 'vue-router'
Vue.use(VueRouter);
//1.创建组件
import Index from '@/views/index'
import Home from '@/views/home'
import Board from '@/views/board'
import Login from '@/views/login'
import NotFound from '@/views/404'
import UpdatePassword from '@/views/update-password'
import pay from '@/views/pay'
import register from '@/views/register'
import center from '@/views/center'
	import monthlysalesofcarmodelsforecast from '@/views/modules/monthlysalesofcarmodelsforecast/list'
	import overallsalesofcars from '@/views/modules/overallsalesofcars/list'
	import monthlysalesofmanufacturers from '@/views/modules/monthlysalesofmanufacturers/list'
	import monthlysalesofcarmodels from '@/views/modules/monthlysalesofcarmodels/list'


//2.配置路由   注意：名字
export const routes = [{
	path: '/',
	name: '系统首页',
	component: Index,
	children: [{
		// 这里不设置值，是把main作为默认页面
		path: '/',
		name: '系统首页',
		component: Home,
		meta: {icon:'', title:'center', affix: true}
	}, {
		path: '/updatePassword',
		name: '修改密码',
		component: UpdatePassword,
		meta: {icon:'', title:'updatePassword'}
	}, {
		path: '/pay',
		name: '支付',
		component: pay,
		meta: {icon:'', title:'pay'}
	}, {
		path: '/center',
		name: '个人信息',
		component: center,
		meta: {icon:'', title:'center'}
	}
	,{
		path: '/monthlysalesofcarmodelsforecast',
		name: '销量预测',
		component: monthlysalesofcarmodelsforecast
	}
	,{
		path: '/overallsalesofcars',
		name: '汽车总体销量',
		component: overallsalesofcars
	}
	,{
		path: '/monthlysalesofmanufacturers',
		name: '厂商每月销售',
		component: monthlysalesofmanufacturers
	}
	,{
		path: '/monthlysalesofcarmodels',
		name: '车型每月销量',
		component: monthlysalesofcarmodels
	}
	]
	},
	{
		path: '/login',
		name: 'login',
		component: Login,
		meta: {icon:'', title:'login'}
	},
	{
		path: '/board',
		name: 'board',
		component: Board,
		meta: {icon:'', title:'board'}
	},
	{
		path: '/register',
		name: 'register',
		component: register,
		meta: {icon:'', title:'register'}
	},
	{
		path: '*',
		component: NotFound
	}
]
//3.实例化VueRouter  注意：名字
const router = new VueRouter({
	mode: 'hash',
	/*hash模式改为history*/
	routes // （缩写）相当于 routes: routes
})
const originalPush = VueRouter.prototype.push
//修改原型对象中的push方法
VueRouter.prototype.push = function push(location) {
	return originalPush.call(this, location).catch(err => err)
}
export default router;
