<template>
	<view>
	<!-- 头部 -->
			<!-- 头 -->
			<view style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
			   position:fixed;color:#c32136;z-index: 10;top: 50rpx;font-weight: bolder;">
				<text style="font-size: 30rpx;">新增地址</text>
			</view>
			
			
			
	<!-- 下面是内容展示 -->
	<view class="" style="margin-top: 150rpx;">
		
		<view class="addressItem">
			<view class="itemTitle">
				收货人：
			</view>
			<input type="text" v-model="username" />
		</view>
		

		<view class="addressItem">
			<view class="itemTitle">
				电话号码：
			</view>
			<input type="text" v-model="telphone"  />
		</view>
		
		
		<view class="addressItem">
			<view class="itemTitle">
				收货地址：
			</view>
			<pickerAddress class="city" @change="change">{{city}}</pickerAddress>
		</view>
		
		<view class="addressBox">
			<view class="itemTitle">
				详细地址：
			</view>
			<textarea v-model="address"  />
		</view>
		
		
		<view class="defaultItem">
			<view class="itemTitle2">
				是否设为默认地址：
			</view>
			<switch @change="defaultChange" checked="true" color="#0bbbef" style="transform:scale(0.8)"/>
		</view>
		
		
		<view class="saveAddress" @click="addAddress">
			保存收货地址
		</view>
		
		 </view>
	</view>
</template>

<script>
	//import pickerAddress from '../../../components/pickerAddress/pickerAddress.vue'
	import pickerAddress from '../../../components/wangding-pickerAddress/wangding-pickerAddress.vue'
	export default{
		data(){
			return{
				city: '请选择地址',
				username:"",
				telphone:'',
				address:'',
				default:1,
				sex:0,
				back:'',
				myuseridndalladdress:{}
			}
		},
		onLoad(option) {
					//this.back=option.back
					let k=uni.getStorageSync("Myuseridndalladdress")
					this.myuseridndalladdress=k
				},
		components:{
		  pickerAddress
		},
		// onLoad(option) {
		// 	this.back=option.back
		// },
methods:{
		// 	sexChange(index){
		// 		this.sex=index
		// 	},
			defaultChange(e){
				if(e.target.value==true){
					this.default=1
					console.log("this.default",this.default)
				}else{
					this.default=2
					console.log("this.default",this.default)
				}
			},
		isEmpty(source){//判断用户名是否为空,不为空是true
						var str = source.replace(/(^\s*)|(\s*$)/g,"");
						if(str=="" || str.toLowerCase()=="null" || str.length<=0){
							return false;
						}else{
							return true;
						}
					},
		verifyTel (tel){//校手机号
						var reg = /^1([38][0-9]|4[579]|5[0-3,5-9]|6[6]|7[0135678]|9[89])\d{8}$/;
						if(reg.test(tel)){
								return true;
							}else{
								return false;
							}
					},
		
	get_length(str) {
	  //获得字符串实际长度，中文2，英文1
	  //要获得长度的字符串
	  var realLength = 0, len = str.length, charCode = -1;
	  for (var i = 0; i < len; i++) {
		charCode = str.charCodeAt(i);
		if (charCode >= 0 && charCode <= 128) 
		   realLength += 1;
		else
		   realLength += 2;
	  }
	  return realLength;
	},	
	//	
		
	change(data) {
		this.city = data.data.join('')
		console.log(data.data.join(''))
	},
	////////////////////////////////
addAddress(){
//保存地址
		console.log(this.username)
		console.log(this.telphone)
		console.log(this.address)
		console.log(this.default)//测试如上4个机制正常
		// username:"",//收货人
		// telphone:'',//电话
		// address:'',//地址
		// default:1,//1为设成默认地址,0为非默认地址
		//校验用户名不为空
						let k=this.isEmpty(this.username)
						console.log("k",k)
						if(k==false){
								uni.showToast({
								    title: '请填写收货人姓名',
								    duration: 2000
								});
								return
						}else{
							
						}
						// 	//不为空,什么也不做
		//校验手机号码
		//校验手机号
						if(this.verifyTel(this.telphone)==false){
							uni.showToast({
							    title: '请填写正确手机号',
							    duration: 2000
							});
							return
						}
		//
		//校验地址 
		if(this.address=="" || this.get_length(this.address)<6){
		   uni.showToast({
			   title: '地址应详细',
			   duration: 2000
		   });
		   return
		}//
		//校验city
		if(this.cyty=="" || this.get_length(this.city)<3 || this.city=="请选择地址"){
		   uni.showToast({
			   title: '请选择省市',
			   duration: 2000
		   });
		   return
		}
		//给地址对象数组增加一个地址对象
		let p={}//p要传到后端,先不做校验,最后做
		p['username']=this.username
		p['telphone']=this.telphone
		   p['city']=this.city
		p['address']=this.address
		p['username']=this.username
		p['default']=this.default
		p['userid']=this.myuseridndalladdress.myuserid
		console.log(p)//完美取到值
		//
		///下面,写入据库
		   uni.request({
					url: 'http://127.0.0.1/addaddress/', //仅为示例，并非真实接口地址。
					data: {
						"addobj": p
					},
					method: 'POST',
					header: {
						// 'custom-header': 'hello' //自定义请求头信息
					},
					success: res => {
						console.log(res);
						//这里来提示删除成功.但我觉得没必须写
						uni.navigateTo({
						url: '/pages/mypay/mypay'
						});
					},
					fail: res => {}
				});
		
		///写入数据库OK
		//
					
					
					
		
}//////
}
	}
</script>

<style>
	.itemTitle2{
		font-size: 28rpx;
	}
	.username{padding:0 30rpx;display: flex;height: 90rpx;align-items: center;}
	.itemTitle{width: 140rpx;font-size: 28rpx;}
	.username input{border-bottom: 1rpx solid #e5e5e5;flex:1;line-height: 90rpx;
	height: 90rpx ;}
	.addressItem{display: flex;
	margin: 0 30rpx;height: 90rpx;align-items: center;
	border-bottom: 1rpx solid #e5e5e5;}
	.addressItem text{width: 80rpx;height: 45rpx;display: block;
	border:1rpx solid #e5e5e5;font-size: 24rpx;margin-right: 10rpx;
	text-align: center;line-height: 45rpx;color: #999;}
	
	.addressItem text.sexActive{background:#0bbbef ;color: #fff;
	border:none}
	.addressBox{height: 180rpx;display: flex;margin:0 30rpx;
	border-bottom: 1rpx solid #e5e5e5;}
	.addressBox .itemTitle{width: 140rpx;line-height: 90rpx;}
	.addressBox textarea{flex: 1;height: 180rpx;padding-top: 25rpx;}
	.saveAddress{width: 600rpx;height: 80rpx;margin:80rpx auto;
	background: #0bbbef;color: #fff;font-size: 28rpx;
	text-align: center;line-height: 80rpx;border-radius: 80rpx;}
	.city{font-size: 28rpx;color: #c32136;}
	.defaultItem{margin: 0 30rpx;display: flex;height: 90rpx;
	align-items: center;justify-content: space-between;}
</style>