<template>
	<view>
<!-- 头 -->
<!-- 头 -->
<view style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
   position:fixed;color:#c32136;z-index: 10;top: 50rpx;font-weight: bolder;">
	<text style="font-size: 30rpx;">地址编辑</text>
</view>		
<!-- 下面是内容 -->	
<view class="addressItem" style="margin-top: 150rpx;">
			<view class="itemTitle">
				收货人：
			</view>
			<input type="text" v-model="username"  />
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
			<view class="itemTitle">
				默认地址：
			</view>
			<template v-if="defaultAddress==1">
				<switch checked="true" color="#0bbbef"
				style="transform:scale(0.8)" @change="defaultChange"/>
			</template>
			<template v-else>
				<switch color="#0bbbef"
				style="transform:scale(0.8)" @change="defaultChange"/>
			</template>
			
		</view>
		
		
		<view class="saveAddress" @click="editAddress">
			保存收货地址
		</view>		
		
<!--  -->		
	</view>
</template>

<script>
	import pickerAddress from '../../../components/wangding-pickerAddress/wangding-pickerAddress'
	export default {
		data() {
			return {
				username:'',
				telphone:'',
				address:'',
				defaultAddress:1,
				//sex:0,
				city: '请选择省市',
				aid:'',//list.vue地址列表页传过来的要编辑的地址数据库中的id
			}
		},
onLoad(option) {
	var that=this
	//对付condi的代码
	var arr = Object.keys(option);
	if(arr.length == 0){//true
		option["id"]=2
	};
	///
		console.log("接收到的option",option)
		console.log("edit页面接到的参数",option.id)
		this.aid=option.id
///
			let k=uni.getStorageSync("Myuseridndalladdress")
			let m=k.myaddress//m为对象数组
			
			m.forEach(function(item){
				if(item.id==option.id){
					that.username=item.aname
					that.telphone=item.aphone
					that.address=item.aaddress
					that.defaultAddress=item.adefaultaddress
					that.city=item.city
					
					
				}
			})












//
		},
////////////////////////////
methods: {
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
	defaultChange(e){
					if(e.target.value==true){
						this.defaultAddress=1;
					}else{
						this.defaultAddress=0;
					}
				},
				sexChange(index){
					this.sex=index
				},
				getAddress(id){
					this.$request('/member/getAddressInfo',{id:id})
					.then(res=>{
						this.username=res.data.username
						this.telphone=res.data.telphone
						this.city=res.data.city
						this.address=res.data.address
						this.defaultAddress=res.data.default
						this.sex=res.data.sex
						console.log(res.data)
					})
				},
				change(data) {
					this.city = data.data.join('')
					console.log(data.data.join(''))
				},
editAddress(){
	var tthat=this
	//验证表单
	// username:'',//绑定收货人
					// telphone:'',//绑定电话
					// address:'',//绑定地址
					// defaultAddress:1,//绑定默认开关
					// city: '请选择收货地址',
					// aid:'',//list.vue地址列表页传过来的要编辑的地址数据库中的id
					console.log(this.username)
					console.log(this.telphone)
					console.log(this.address)
					console.log(this.defaultAddress)//测试如上4个机制正常
					console.log(this.city)
					console.log(this.aid)
					//校验收货人
					let k=this.isEmpty(this.username)
					console.log("k",k)
					if(k==false){
							uni.showToast({
							    title: '请填写收货人',
							    duration: 2000
							});
							return
					}else{
						
					}
					// 	//不为空,什么也不做
					
					//校验手机号
					if(this.verifyTel(this.telphone)==false){
						uni.showToast({
						    title: '请填写正确手机号',
						    duration: 2000
						});
						return
					}
					console.log(this.address)//没有填详细地址,则打印省市(选择的),填了则只打印详细地址后面的
					//校验详细地址 
					if(this.address=="" || this.get_length(this.address)<6){
					   uni.showToast({
					       title: '地址应详细',
					       duration: 2000
					   });
					   return
					}
					//校验city
					if(this.cyty=="" || this.get_length(this.city)<6 || this.city=="请选择省市"){
					   uni.showToast({
					       title: '请选择省市',
					       duration: 2000
					   });
					   return
					}
					//校验结束
					//给地址对象数组增加一个地址对象
					let p={}//p要传到后端,先不做校验,最后做
					p['username']=this.username
					p['telphone']=this.telphone
					p['city']=this.city
					p['address']=this.address
					//p['username']=this.username
					p['default']=this.defaultAddress
					p['aid']=this.aid
					console.log(p)//完美取到值
					//
					///下面,写入据库
					   uni.request({
					   			url: 'http://127.0.0.1/Changeaddress/', //仅为示例，并非真实接口地址。
					   			data: {
					   				"addobj": p
					   			},
					   			method: 'POST',
					   			header: {
					   				// 'custom-header': 'hello' //自定义请求头信息
					   			},
					   			success: res => {
											console.log(res.data);
											let k=uni.getStorageSync("Myuseridndalladdress")
											let u=k.myaddress
											console.log("tthat.aid",tthat.aid)
											u.forEach(function(item){
												if(item.id==tthat.aid){//修改该条地址的信息
													  item.aname=tthat.username
													  item.aphone=tthat.telphone
													  item.city=tthat.city
													  item.aaddress=tthat.address
													  item.adefaultaddress=tthat.defaultAddress
												}
											})
											k.myaddress=u
											uni.setStorageSync('Myuseridndalladdress', k)
									//已新增完成
										uni.navigateTo({
											url: '/pages/address/list/list'
										                });
					   			
					   			},
					   			fail: res => {}
					   		});
					
					///写入数据库OK
					
					
				
}
},///////////////////
		components:{
				    pickerAddress
				},
	}
</script>

<style>
.addressItem text.sexActive{background:#0bbbef ;color: #fff;
	border:none}
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
