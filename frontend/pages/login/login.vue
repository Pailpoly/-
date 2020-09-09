<template>
	<view>
		<button
			style="background-color: #4CD964;color: #ffffff;
width: 700rpx;margin-top: 200rpx;border-radius: 40rpx;"
			open-type="getUserInfo"
			lang="zh_CN"
			@getuserinfo="onGotUserInfo"
		>
			确认授权微信登陆
		</button>
	</view>
</template>

<script>
export default {
	data() {
		return {
			topenid:'',
			tuser:''
			
		};
	},
	methods: {
		onGotUserInfo(e) {
			console.log("eeeeeeeeee",e)
			console.info(e.detail);
			console.info(e.detail.userInfo);
			console.info("抽疯",e.detail.errMsg);//getUserInfo:ok 表成功 getUserInfo:fail auth deny表失败
			console.info("抽疯成功",e.detail.errMsg.indexOf("ok"));//点了允许,会返回12  否则返回-1
			console.info("抽疯失败",e.detail.errMsg.indexOf("fail"));//点了拒绝会返回12  否则返回-1
			//如果用户点了允许,我们获取了用户数据,保存了
			
			if(e.detail.errMsg.indexOf("ok") != -1){
				console.log("用户点了允许")
				this.tuser=e.detail.userInfo
				uni.setStorage({
					key: 'myuser',
					data: e.detail.userInfo
				});
				/////下面是用户数据写入数据库,用户表和扩展表
				console.log('函数启动了888666');
				uni.request({
					url: 'http://127.0.0.1/usertest/', //仅为示例，并非真实接口地址。
					data: {
						"myuserinfo": this.tuser,"myopenid":this.topenid
					},
					method: 'POST',
					header: {
						// 'custom-header': 'hello' //自定义请求头信息
					},
					success: res => {
						//用户表没建,先把成功获取用户id的功能注释
						console.log(res);
						console.log("收到后端发来的登陆用户的myusertwo表中的id",res.data);
						//res.data就是登陆用户在myusertwo表中的id,我们现在写入本地
						uni.setStorage({
							key: 'userid',
							data: res.data
						});
					
					},
					fail: res => {
						console.log("openid数据写入失败");
					}
				});
				
				/////
				
				uni.showToast({
					title: '欢迎您,已登陆',
					duration: 2000
				});
				
				uni.switchTab({
					url: '/pages/index/index'
				});
				
			}else{
				console.log("用户点了拒绝")
				//这里放他拒绝了之后,我们的代码,可以跳到登陆页让它手机号登陆等等
				return
			}
			
			// if(e.detail.errMsg.indexOf("fail") != -1){
			// 	console.log("用户点了拒绝")
			// }
			
			
		}
	},
	created() {
		
	},
	onLoad() {
		///////////////////////////////////////////
		//漫路h
		uni.login({
			success: res => {
				//code值(5分钟失效)
				console.log('我的code-----' + res.code);
				//小程序appid
				let appid = 'wx8f60753d3939d7c1'; //\
				//小程序secret
				let secret = 'a51dc26912ddde5e7c254bc70448b09b'; //\
				//wx接口路径
				let url = 'https://api.weixin.qq.com/sns/jscode2session?appid=' + appid + '&secret=' + secret + '&js_code=' + res.code + '&grant_type=authorization_code';
				uni.request({
					url: url, // 请求路径
					method: 'GET', //请求方式
					success: result => {
						//响应成功
						//这里就获取到了openid了
						console.log('我的openid-----' + result.data.openid);
						this.topenid=result.data.openid
						
						uni.setStorage({
							key: 'myopenid',
							data: result.data.openid
						});
						////这里测试
							// console.log('函数启动了888666');
							// uni.request({
							// 	url: 'http://127.0.0.1/usertest/', //仅为示例，并非真实接口地址。
							// 	data: {
							// 		"myuserinfo": this.tuser,"myopenid":this.topenid
							// 	},
							// 	method: 'POST',
							// 	header: {
							// 		// 'custom-header': 'hello' //自定义请求头信息
							// 	},
							// 	success: res => {
							// 		console.log(res);
								
							// 	},
							// 	fail: res => {
							// 		console.log("openid数据写入失败");
							// 	}
							// });
						
						///这里测试
						
						
						
						
						
					},
					fail: err => {} //失败
				});
			}
		});
		///////////////////上面是获取code和opendid,下面是获取微信头像签名位置等信息

		/////////////////////////////////
	}
};
</script>

<style scoped></style>
