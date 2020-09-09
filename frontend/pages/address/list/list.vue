<template>
	<view>
		<!-- 头部 -->
		<!-- 头 -->
				<view style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
				   position:fixed;color:#c32136;z-index: 10;top: 50rpx;font-weight: bolder;">
					<text style="font-size: 30rpx;">地址管理</text>
				</view>
	<!-- . -->
	
	<view style="position: relative;left: 25rpx;top: 60rpx;z-index:300">
	<image @click="gotolistback" style="width: 40rpx;height: 40rpx;" src="../../../static/myimg/goback.png"></image>
	</view>
	
	
	<!-- 下面是内容区 -->
	<view>	
		
			<view class="addresslist" v-if="myshow"><!-- 用户有地址时,显示地址 -->
				<uni-swipe-action>
				    <uni-swipe-action-item 
					:options="options" @click="onClick($event,index,item.id)" @change="change"
					v-for="(item,index) in addressList" :key="index"
					>
				        <view class="addressItem" @click="addressCheck(item.id)">
				        	<view class="addressMain">
								
				        		<text class="username">{{item.aname}}</text>
				        		<text class="telphone">{{item.aphone}}</text>
				        		<text class="default" v-if="item.default==1">默认</text>
				        	</view>
				        	<view class="addressInfo">
				        		{{item.city}}{{item.aaddress}}
				        	</view>
				        </view>
				    </uni-swipe-action-item>
					
					
				</uni-swipe-action>
			
			</view>
			
			
			
			
			
			
			<view class="empty" v-else><!-- 用户没有地址时,显示空图,并提示 -->
				<image src="/static/myimg/address.png" mode=""></image>
				<text>用户没有收货地址,请添加</text>
			</view>
			
			

			
			<view class="addBtn" @click="addUrl" >
				添加新地址
			</view>
			
	</view>
	<!-- 上面是内容区 -->
	
	
<view style="height: 100rpx;width: 750rpx;background-color: #fff;">
	
</view>
	
	</view>
</template>

<script>
	import uniSwipeAction from '@/components/uni-swipe-action/uni-swipe-action.vue'
	import uniSwipeActionItem from '@/components/uni-swipe-action-item/uni-swipe-action-item.vue'
	export default {
	    components: {
	        uniSwipeAction,
	        uniSwipeActionItem
	    },
		data(){
			return{
				myshow:false,//地址是否为空,为空时,显示图片和提示添加地址
				options:[
				        {
				            text: '删除',
				            style: {
				                backgroundColor: '#ff0309'
				            }
				        }, {
				            text: '编辑',
				            style: {
				                backgroundColor: '#0bbbef'
				            }
				        }
				      ],
				addressList:[],//地址对象数组
				back:''
			}
		},
		onLoad(option) {
			//先来取地址列表和用户id      
			let myaddressList=uni.getStorageSync("Myuseridndalladdress")
			this.addressList=myaddressList.myaddress//取得了地址对象数组
			if(this.addressList.length==0){
				this.myshow=false
			}else{
				this.myshow=true
			}
			
			
			if(option.back==1){
				this.back=option.back
			}else{
				this.back=0
			}
			
		},
 methods:{
	 ///////////////////////////////////////
	  addressCheck(myid){		
	 		console.log(myid)
	 		//最好的方案是,点击该条地址,去数据库修改它,改为默认地址
	 		//因为mypay确认订单页onshow就是默认搜索默认地址来展示
	 		///下面,写入据库
	 		   uni.request({
	 					url: 'http://127.0.0.1/addressgotomypay/', //仅为示例，并非真实接口地址。
	 					data: {
	 						"myid": myid
	 					},
	 					method: 'POST',
	 					header: {
	 						// 'custom-header': 'hello' //自定义请求头信息
	 					},
	 					success: res => {
	 						console.log(res);
	 						//已新增完成
	 							uni.navigateTo({
	 								url: '/pages/mypay/mypay'
	 											});
	 					
	 					},
	 					fail: res => {}
	 				});
	 		
	 		///写入数据库OK		
	  },
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 /////////////////////////////////
	 			 ///跳回list.vue
	 			 gotolistback(){
	 				 uni.navigateTo({
	 				     url: '/pages/mypay/mypay'
	 				 });
	 			 },
	 			change(data) {
	 				this.city = data.data.join('')
	 				console.log(data.data.join(''))
	 			},
	 // 增加地址
 addUrl(){
 //我们直接先跳到add.vue去操作,在add.vue的onload中取得用户的id就可以了
 
	uni.navigateTo({
		url: '/pages/address/add/add'
		});
 
 },
			 ///
//删除地址,或编辑地址
onClick(e,index,id){
	console.log(e,index,id)//e值为删除.index为地址对象数组的下标,id为地址表中的id
	if(e.content.text=="删除"){
		console.log(index,e.content.text)
		uni.showModal({
			title: '提示',
			content: '是否要删除对应数据',
			success:res=> {
				if (res.confirm) {//用户点了确认删除,执行删除动作
						this.addressList.splice(index, 1)//页面删除
						this.$forceUpdate()//页面刷新
						let k=uni.getStorageSync("Myuseridndalladdress")//同步取值
						k.myaddress.splice(index, 1)//将删除的地址对象淘汰
						console.log(k)
						uni.setStorageSync('Myuseridndalladdress', k)
///上面,本地和页面删除OK
						///下面,从数据库删除
						   uni.request({
									url: 'http://127.0.0.1/deladdress/', //仅为示例，并非真实接口地址。
									data: {
										"addressid": id
									},
									method: 'POST',
									header: {
										// 'custom-header': 'hello' //自定义请求头信息
									},
									success: res => {
										console.log(res);
										//这里来提示删除成功.但我觉得没必须写
									
									},
									fail: res => {}
								});
						
						///从数据库删除OK
						
					
				} else if (res.cancel) {
					console.log('用户点击取消');
				}
			}
		})
	}
///////////////////////////////////////////////////////////////////////////				
				if(e.content.text=="编辑"){
					console.log(index,'您点击的是编辑')
					//跳到地址编辑页,用户id在编辑页onload去取,这里把地址id传过去就成
					uni.navigateTo({
						url: '/pages/address/edit/edit?id='+id
					                });
				}
				
				

		    },//////////////////////////////////


}///		  
	}
</script>

<style>
	.addresslist{
		margin-top: 150rpx;
	}
.empty image{width: 330rpx;height: 210rpx;display: block;margin: 200rpx auto 0;}
.empty text{font-size: 24rpx;color: #999;line-height: 80rpx;text-align: center;
display: block;}
	.addressItem{padding:0 35rpx;width: 100%;
	border-bottom: 1rpx solid #e5e5e5;}
	.addressMain{line-height: 40rpx;font-size: 28rpx;padding-top: 30rpx;}
	.addressMain .telphone{padding: 0 20rpx 0 10rpx;}
	.addressMain .default{background: #1fc8f2;color: #fff;font-size: 20rpx
	;padding:0 10rpx;}
	.addressInfo{font-size: 24rpx;line-height: 36rpx;
	color: #999;padding-bottom: 36rpx;}
	
	.addBtn{height: 90rpx;position: fixed;bottom: 0;width: 100%;left:0;
	background: #0bbbef;color: #fff;text-align: center;line-height: 90rpx;
	font-size: 28rpx;}
</style>