<template>
	<view>
		<view scroll-y="true" style="background-color: #f8f8f8;">
			<!-- 头部标题 -->
			<!-- 头 -->
			<view
				style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
   position:fixed;color:#c32136;z-index: 10;top: 50rpx;font-weight: bolder;"
			>
				<text style="font-size: 30rpx;">确认订单</text>
			</view>
			<!-- 返回购物车页 -->
			<view style="width: 750rpx;">
				<image
					@click="bback"
					src="/static/myimg/return.png"
					style="width: 40rpx;height: 40rpx;z-index: 200;
	    position: relative;top: 50rpx;left: 20rpx;"
				></image>
			</view>
			<!-- 支付提示 -->
			<view class="jiang"><text style="color: #ff461f;margin-left: 30rpx;">请在24小时内完成支付,超时自动关闭订单</text></view>

			<!-- 选择地址 -->
			<view
				style="width: 730rpx;height: 160rpx;background-color: #fff;border-radius: 30rpx;margin: 0 auto;
     margin-top: 20rpx;overflow: hidden;"
			>
				<!-- 下面这个图是地址下面的彩色线条 -->
				<image
					style="width: 750rpx;height: 8rpx;position: relative;top: 128rpx;z-index: 80;
	   "
					src="../../static/myimg/xiahua9.png"
				></image>
				<view style="margin-top: -20rpx;font-weight: bolder;margin-left: 10rpx;">
					<text id="dname" ref="dname">
						<!-- 收货人和电话 -->
						{{ koname }}
					</text>
					<text ref="dphone" style="margin-left: 60rpx;">{{ kophone }}</text>
				</view>
				<!-- 下面是地址 -->
				<!-- 下面是地址 -->
				<!-- 下面是地址 -->
				<view style="font-size: 25rpx;margin-left: 10rpx;margin-top: 20rpx;">
					<text
						style="color: #ff2d51;display: inline-block;width: 60rpx;height: 30rpx;
		    line-height: 30rpx;border-radius: 15rpx;border-style: solid;border-width: 1rpx;
			border-color: #ff2d51;text-align: center;margin-right: 10rpx;"
					>
						默认
					</text>
					<text ref="daddress">{{ kcity }}{{ koaddress }}</text>
				</view>
				<!-- 上面是地址 -->
				<!-- 上面是地址 -->
				<!-- 上面是地址 -->
				<!-- 下面是编辑箭头 -->
				<view style="position: relative;left: 650rpx;top: -90rpx;">
					<image @click="toaddresslist" style="width: 40rpx;height: 40rpx;" src="../../static/myimg/bianji.png"><!-- 这张图是地址右侧地址的图标 --></image>
				</view>
			</view>
			<!-- 支付方式 -->
			<view
				style="width: 730rpx;height: 80rpx;background-color: #fff;margin-top: 20rpx;
	        z-index: 100;border-radius: 20rpx;margin-left: 10rpx;line-height: 80rpx;"
			>
				<text style="margin-left: 15rpx;font-size: 26rpx;">支付方式:</text>
				<image style="width: 30rpx;height: 30rpx;margin-left: 360rpx; position: relative;top: 7rpx;" src="../../static/myimg/weixing%20(2).png"></image>
				<text style="margin-left: 15rpx;font-size: 26rpx;">微信支付</text>
				<image style="width: 30rpx;height: 30rpx;margin-left: 50rpx;position: relative;top: 7rpx;" src="../../static/myimg/rightjian.png"></image>
			</view>
			<!-- 下面是灰色空白占位 -->
			<view style="width: 750rpx;height: 15rpx;background-color: #f0f0f4;"></view>
			<!-- 商品展示 -->
			<!-- 商品展示 -->
			<view v-for="(item, index) in myallobj.kkkobj">
				<view
					style="width: 730rpx;height: 350rpx;border-radius: 20rpx;background-color:#fff;
              margin-left: 10rpx;box-sizing: border-box;padding: 10rpx 0 0 10rpx;display: flex;"
				>
					<!-- 左边图片 -->
					<view><image style="width: 220rpx;height: 230rpx;box-shadow: 20rpx;" :src="imageurl + item.small_image"></image></view>
					<!-- 右边标题和细节 -->
					<view style="margin-left: 20rpx;">
						<view style="font-weight: bolder;margin-top: 10rpx;">{{ item.name }}</view>
						<view style="color: #758a99;font-size: 26rpx;margin-top: 10rpx;">{{ item.spec }}</view>
						<view style="font-size: 26rpx;color: #c32136;margin-top: 10rpx;"><text>支持7天无理由退货</text></view>
						<view style="color: #c32136;margin-top: 10rpx;">
							<text>¥{{ item.price }}</text>
						</view>
						<view style="position: relative;left: 300rpx;top: -25rpx;font-size: 26rpx;">
							<text>{{ item.num }}件</text>
						</view>
					</view>
				</view>
				<!-- 留言 -->
				<view
					style="width: 720rpx;height: 60rpx;margin-left: 15rpx;background-color: #f8f8f8;position: relative;
              top: -90rpx;border-radius: 30rpx;line-height: 60rpx;"
				>
					<text style="font-size: 26rpx;opacity: 0.9 !important;margin-left: 15rpx;">留言:</text>
					<input
						style="width: 600rpx;position: relative;
	        top: -50rpx;left: 90rpx;maxlength:20"
						type="text"
					/>
				</view>
				<!-- 	下面是灰色空白占位-->
				<view style="width: 750rpx;height: 15rpx;background-color: #f0f0f4;"></view>
			</view>

			<!-- 下面是配送 -->
			<view
				style="width: 730rpx;height: 80rpx;background-color: #fff;margin-top: 20rpx;
		z-index: 100;border-radius: 20rpx;margin-left: 10rpx;line-height: 80rpx;"
			>
				<text style="margin-left: 15rpx;font-size: 26rpx;">配送:</text>

				<text style="margin-left: 200rpx;font-size: 26rpx;">包邮,顺丰速运(顺丰不能到达的用邮政)</text>
			</view>

			<!-- 发票区 -->
			<view
				style="width: 730rpx;height: 300rpx;background-color: #fff;margin-top: 20rpx;
		z-index: 100;border-radius: 20rpx;margin-left: 10rpx;line-height: 80rpx;font-size: 26rpx;"
			>
				<!-- 1块 -->
				<view>
					<text style="margin-left: 15rpx;">发票</text>
					<text style="margin-left: 460rpx;">不开发票</text>
					<image style="width: 30rpx;height: 30rpx;margin-left: 50rpx;position: relative;top: 7rpx;" src="../../static/myimg/rightjian.png"></image>
				</view>
				<!-- 2块 -->
				<view>
					<text style="margin-left: 15rpx;">优惠券</text>
					<text style="margin-left: 505rpx;">无</text>
					<image style="width: 30rpx;height: 30rpx;margin-left: 50rpx;position: relative;top: 7rpx;" src="../../static/myimg/rightjian.png"></image>
				</view>
				<!-- 3块 -->
				<view>
					<text style="margin-left: 15rpx;">礼品卡</text>
					<text style="margin-left: 505rpx;">无</text>
					<image style="width: 30rpx;height: 30rpx;margin-left: 50rpx;position: relative;top: 7rpx;" src="../../static/myimg/rightjian.png"></image>
				</view>
				<!-- 4块 -->
				<view>
					<text style="margin-left: 15rpx;">会员卡号</text>
					<text style="margin-left: 303rpx;">办理会员,享受9折</text>
					<image style="width: 30rpx;height: 30rpx;margin-left: 50rpx;position: relative;top: 7rpx;" src="../../static/myimg/rightjian.png"></image>
				</view>
			</view>

			<!-- 核对信息块 -->
			<view
				style="width: 730rpx;height: 300rpx;background-color: #fff;margin-top: 20rpx;
		z-index: 100;border-radius: 20rpx;margin-left: 10rpx;line-height: 80rpx;font-size: 26rpx;
		color: #000;font-weight: bold;"
			>
				<!-- 1块 -->
				<view>
					<text style="margin-left: 15rpx;">付款总金额</text>
					<text style="margin-left: 460rpx;color: #ff2121;">{{ mytotalprice }}元</text>
				</view>
				<!-- 2块 -->
				<view>
					<text style="margin-left: 15rpx;">运费</text>
					<text style="margin-left: 540rpx;color: #ff2121;">0元</text>
				</view>
				<!-- 3块 -->
				<view>
					<view>
						<text style="margin-left: 15rpx;">{{ koname }}(收)</text>
						<text style="margin-left: 50rpx;">{{ kophone }}</text>
					</view>
					<view>
						<text style="margin-left: 15rpx;position: relative;top: -20rpx;">{{ kcity }}{{ koaddress }}</text>
					</view>
				</view>
			</view>

			<!-- 最低部占位,实现全页面内容可以显示 -->
			<view style="width: 750rpx;height: 100rpx;"></view>

			<!-- 提交 -->
			<view
				style="width: 720rpx;height: 80rpx;background-color: #808080;overflow: hidden;
            border-radius: 40rpx;position: fixed;bottom: 10rpx;left: 15rpx;line-height: 80rpx;
			display: flex;color: #fff;"
			>
				<view @click="twt0" style="width: 470rpx;background-color: #3d3b4f;">
					<text style="margin-left: 20rpx;">实付:</text>
					<text style="font-size: 40rpx;margin-left: 8rpx;">{{ mytotalprice }}</text>
					<text style="margin-left: 8rpx;">元</text>
				</view>
				<view @click="topay" style="width: 250rpx;background-color: #ff2121;text-align: center;"><text>提交订单</text></view>
			</view>

			<!--  -->
		</view>
	</view>
</template>

<script>
export default {
	data() {
		return {
			//下面是地址的
			koname: '例:张三',
			kophone: '12345678912',
			kcity: '中国广东省深圳市',
			koaddress: '请填写地址',
			myaddressdata: [], //存关联用户所有地址,对象数组
			myallobj: {}, //存所有对象
			imageurl: '/static/' //给动态图片路径加前缀
		};
	},
	onLoad() {
		var tthat = this;
		let p = uni.getStorageSync('mypayobj'); //用同步,取出数组
		this.myallobj = p;
		console.log('mypay订单页面初始化取数据', p);
		//此时图片路径为small_image: "drug_img/2020/07/05/%E4%B8%BB%E5%9B%BE5.jpg"
		//应该为"/static/myimg/s1.png"才能取到

		/////下面是地址相关
		//第一步,获取登陆用户的id,
		let myuserid = uni.getStorageSync('userid'); //用同步,取出数组
		console.log('用户表中的id', myuserid); //测试正常
		//取到后,我们要发给后端到查该用户关联的所有地址,在地址表中的
		uni.request({
			url: 'http://127.0.0.1/getalladdress/', //仅为示例，并非真实接口地址。
			data: {
				myid: myuserid
			},
			method: 'POST',
			header: {
				// 'custom-header': 'hello' //自定义请求头信息
			},
			success: res => {
				//console.log(res);
				console.log('收到后端发来的登陆用户的所有地址', res.data);
				//console.log("收到后端发来的登陆用户的第一条地址相关",res.data[0].aname);
				this.myaddressdata = res.data;
				//console.log("myaddressdata",this.myaddressdata)
				//res.data就是登陆用户在myusertwo表中的id,我们现在写入本地
				let myuseridandalladdress = {};
				myuseridandalladdress['myuserid'] = myuserid;
				myuseridandalladdress['myaddress'] = res.data;
				uni.setStorage({
					key: 'Myuseridndalladdress',
					data: myuseridandalladdress
				});
				////////////////////在这,我来了,我要判断地址数据了,,无地址
				if (res.data.length == 0) {
					//你莫走,弹个小窗吧..
					uni.showToast({
						title: '请填写收货地址信息',
						duration: 3000
					});
					return;
				} ////
				///
				var q = [];
				if (res.data.length > 0) {
					res.data.forEach(function(item) {
						if (item.adefaultaddress == '1') {
							q.push(item);
						}
					});
				}
				console.log('q', q); //测试正常
				if (q.length == 0) {
					//有地址,不管多少条,没有设置默认地址
					//这里将res.data[0]拿到HTML页面展示
					tthat.koname = res.data[0].aname;
					tthat.kophone = res.data[0].aphone;
					tthat.koaddress = res.data[0].aaddress;
					tthat.kcity = res.data[0].city;
				} else {
					///有地址,有设置默认地址,在这里处理,就是q里面的对象
					tthat.koname = q[0].aname;
					tthat.kophone = q[0].aphone;
					tthat.koaddress = q[0].aaddress;
					tthat.kcity = q[0].city;
				}

				///
			},
			fail: res => {
				console.log('openid数据写入失败');
			}
		});
		//
		//////.
	},
	methods: {
		//测试支付
		twt0() {
			//pay(){
			uni.request({
				url: 'http://127.0.0.1:80/payOrder/',
				method: 'POST',
				header: {
					'content-type': 'application/json'
				},
				data: {
					user_id: 30, //用户id,用户表里面的
					price: 128
				},
				success: res => {
					console.log('success');
					console.log(res);
					console.log(res.data);

					uni.requestPayment({
						provider: 'wxpay',

						timeStamp: res.data.timeStamp,
						nonceStr: res.data.nonceStr,
						package: 'prepay_id=' + String(res.data.prepay_id),
						signType: 'MD5',
						paySign: res.data.paySign,

						success: function(res) {
							console.log('success:' + JSON.stringify(res));
							// 支付成功，给后台发送数据，保存订单
							console.log('支付成功');
						},
						fail: function(err) {
							console.log('fail:' + JSON.stringify(err));
							// 支付失败，给后台发送数据，保存订单
							console.log('支付失败');
						}
					});
				},
				fail: res => {
					console.log('fail');
					console.log(res);
				},
				complete: () => {}
			});

			//}
		},
		////////////////////////////////////支付
topay() {
			var bthat = this;
			console.log('终于来到支付的时间了,好兴奋');
			let wxuserid = uni.getStorageSync('userid'); //取登陆用户的id----------字符串
			//console.log(wxuserid)//OK
			let wxopenid = uni.getStorageSync('myopenid'); //取登陆用户的openid-----字符串
			//console.log(wxopenid)//OK

			//取数据库默认地址id到后端去取
			//下面 wxcartobj  -----对象
			let wxcartobj = uni.getStorageSync('mypayobj'); //openid,微信详细信息,购物车对象数组,三个一并获取
			//console.log(wxcartobj)//OK
			//所以,我们干脆把前两个,也加入第三个,这个对象里面集合,只用加一下用户id就成了
			wxcartobj['wxuserid'] = wxuserid;
			//console.log("wxcartobj------------------",wxcartobj)//完美

			//提示,支付金额为3元
			uni.showToast({
				title: '改为1元,测试',
				duration: 5000
			});
			/////这里开始支付鸟
			//pay(){
			uni.request({
				url: 'http://127.0.0.1:80/payOrder/',
				method: 'POST',
				header: {
					'content-type': 'application/json'
				},
				data: {
					wxcartobj: wxcartobj //所有东东都传到后端
				},
				success: res => {
					//在这里,已经支付成功了
					console.log('success支付成功888');
					console.log(res);
					console.log(res.data); //这里含有订单编号了
					let mydingdan = res.data['mydindanbianhao2'];
					console.log("订单编号",mydingdan)
					//如上取到订单编号了
					uni.requestPayment({
						provider: 'wxpay',

						timeStamp: res.data.timeStamp,
						nonceStr: res.data.nonceStr,
						package: 'prepay_id=' + String(res.data.prepay_id),
						signType: 'MD5',
						paySign: res.data.paySign,

						success: function(res) {
							////////////////////////////////////////////////支付成功后,订单所有数据写入数据库的代码///////////////
							console.log('狗狗狗success:' + JSON.stringify(res));
							//狗狗狗success:{"errMsg":"requestPayment:ok"}
							console.log('用户支付成功666');
							console.log('前端第一时间取得订单编号', mydingdan);
							//写入数据库开始
							wxcartobj['mydingdan'] = mydingdan; //所有数据全集成到该 对象内
							//现在已取到用户数据,订单商品数据,订单编号
							uni.request({
								url: 'http://127.0.0.1/gotodindan/', //仅为示例，并非真实接口地址。
								data: {
									wxcartobj: wxcartobj
								},
								method: 'POST',
								header: {
									// 'custom-header': 'hello' //自定义请求头信息
								},
								success: res => {
									console.log(res);
									uni.navigateTo({
										url: '/pages/afterpayok/afterpayok'
									});
								},
								fail: res => {}
							});

							/////////////////////////////////////////////////////////////////////////////////写入数据库完成///
						},
						fail: function(err) {
							console.log('fail:' + JSON.stringify(err));
							// 支付失败，给后台发送数据，保存订单
							console.log('支付失败333');
						}
					});
				},
				fail: res => {
					console.log('fail');
					console.log(res);
				},
				complete: () => {}
			});
			/////上面开始支付鸟..到这里已走完代码
		},
		///////////////////////////////////////////////////////////////////////////////////////
		toaddresslist() {
			console.log('准备跳到list.vue地址列表页');
			uni.navigateTo({
				url: '/pages/address/list/list'
			});
		},
		///测试地址
		cheshi() {
			uni.request({
				url: 'http://127.0.0.1/addaddress/', //仅为示例，并非真实接口地址。
				data: {
					userid: '24',
					addressinfo: '广东省深圳市福田区华强北'
				},
				method: 'POST',
				header: {
					// 'custom-header': 'hello' //自定义请求头信息.
				},
				success: res => {
					console.log(res);
					console.log(res.data);
				},
				fail: res => {}
			});
		},
		////////////////////////////////////////
		///返回
		bback() {
			uni.switchTab({
				url: '../order/order'
			});
		}
		////
	},
	computed: {
		//总金额
		mytotalprice: function() {
			let z = 0;
			let k = this.myallobj.kkkobj;
			k.forEach(function(item) {
				z = z + item.num * item.price;
			});
			return z;
		}
	}
};
</script>

<style>
.jiang {
	margin-top: 80rpx;
	width: 720rpx;
	height: 80rpx;
	margin-left: 15rpx;
	border-radius: 20rpx;
	opacity: 0.8;
	line-height: 80rpx;
	background: #f9e868;
	background: -moz-linear-gradient(top, #f9e868 0%, #fefcea 54%, #fefcea 54%, #efe081 100%);
	background: -webkit-linear-gradient(top, #f9e868 0%, #fefcea 54%, #fefcea 54%, #efe081 100%);
	background: linear-gradient(to bottom, #f9e868 0%, #fefcea 54%, #fefcea 54%, #efe081 100%);
	filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#f9e868', endColorstr='#efe081',GradientType=0 );
}
</style>



