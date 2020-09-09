

<template>
	<view v-if="show">
		
		<!-- 写个标题  -->
		<!-- 写个标题  -->
		<view style="width: 750rpx;height: 60rpx;line-height: 60rpx;display: flex;justify-content: center;
		           margin-top: 50rpx;color: #f00056; ">
			<text>购物车</text>
		</view>
		
		<!-- 如果没有登陆 -->
		<!-- 如果没有登陆 -->
		<view class="cartEmpty" v-if="isLogin==0">
			<image src="../../static/myimg/cartEmpty.png" mode="" class="cartEmptyImg"></image>
			<view class="cartEmptyTip">
				亲,您需要登录才能查看购物车哟~~.
			</view>
			<navigator url="../login/login?backurl=1" class="cartLogin">
				立即登录
			</navigator>
			
		</view>
		<!-- 登陆了,但是购物车为空 -->
		<!-- 登陆了,但是购物车为空 -->
		<view v-else>
					<!-- 如果购物车为空 -->
					<!-- 如果购物车为空 -->
					<view class="cartEmpty" v-if="cartlist.length==0"><!-- cartlist为购物车中的商品对象数组 -->
						<image src="../../static/myimg/cartEmpty.png" mode="" class="cartEmptyImg"></image>
						<view class="cartEmptyTip">
							亲,您的购物车空空如也~~
						</view>
					</view>
					
					<!-- 如果购物车有商品 -->
					<!-- 如果购物车有商品 -->
					<view class="cartListBox" v-else>
						<view class="cartList">
							<uni-swipe-action>
							    <uni-swipe-action-item  
								:options="options" 
								@click="delBtn($event,item.id,index)"
								v-for="(item,index) in cartlist" :key="index">
									<view class="cartItem">
										<label @click="checkboxChage(index)">
											<image src="../../static/myimg/checkbox1.png" mode="" v-if="item.flag"></image>
											<image src="../../static/myimg/checkbox.png" mode="" v-else></image>
										</label>
	<!-- 占位 -->
	<view style="width: 30rpx;height: 20rpx;background-color: #fff;">
		
	</view>
	<!-- 上面是占位 -->
										<view class="mainImg">
											<image :src="'/static'+item.small_image" mode=""></image>
										</view>
	<!-- 占位 -->
	<view style="width: 30rpx;height: 20rpx;background-color: #fff;">
		
	</view>
	<!-- 上面是占位 -->
										<view class="cartItemContent">
											<view class="content-title">
												{{item.name}}
											</view>
											<view class="content-attr">
												{{item.spec}} 
											</view>
											<view class="content-price">
												¥{{item.price}}
												<view class="numOption">
	<view class="optionBtn" @click="reduce(index)">
		-
	</view>
													<view class="numTxt">
														<input type="text" v-model="item.num" />
													</view>
<view class="optionBtn" @click="add(index)">
	+
</view>
												</view>
											</view>
										</view>
									</view>
									</uni-swipe-action-item>
							</uni-swipe-action>
						</view>
<!-- 占位 -->
<view style="width: 750rpx;height: 100rpx;background-color: #fff;">
	
</view>
<!-- 以上是占位 -->
						
						<view class="bottomEmpty">
							
						</view>
<!-- 下面是全选区 -->
						<view class="cartBottom" style="z-index: 88;">
							<label @click="allCheckChange">
								<image src="../../static/myimg/checkbox1.png" mode="" v-if="allCheck"></image>
								<image src="../../static/myimg/checkbox.png" mode="" v-else></image>
								全选
							</label>
							<view class="cartBottomRight">
								总价:<text style="color: red;">¥{{totalprice}}</text>
								<view class="payBtn" @click="cartBuy">
									去结算<text>(共<text 
									style="color: #ff2d51;font-weight: bold;font-size: 26rpx;">
									{{totalnum}}</text>件)</text>
								</view>
							</view>
						</view>
					</view>
				</view>
		

		<!--  -->
		<!--  -->
		
		
		
		
		<!--  -->
		<!--  -->
	</view>
</template>




































<script>
	import uniSwipeAction from '@/components/uni-swipe-action/uni-swipe-action.vue'
	import uniSwipeActionItem from '@/components/uni-swipe-action-item/uni-swipe-action-item.vue'
	
	export default {
		data() {
			return{
				allCheck:false,//全选
				empty:false,//购物车为空
				totalprice:0,//计算总金额
				totalnum:0,//计算总数据
				isLogin:0,//是否登陆0为没有,1为登陆
				cartlist:[],//购物车中商品对象数组
				show:true,//
				options:[//滑动删除
						{
							text: '删除',
							style: {
								backgroundColor: '#ff0309'
							}
						}
					  ],
			}
			},
			components:{
				uniSwipeAction,uniSwipeActionItem
			},
onLoad() {
			this.isLogin=uni.getStorageSync('myopenid')
			if(this.isLogin.trim()==""){
				this.isLogin=0
			}else{
				this.isLogin=1
			}
			console.log("isLogin的值",this.isLogin)
			
		/////////////////////////////////////////////////////////////////
		var cardata=uni.getStorageSync('myproid')//用同步,取出数组that.$forceUpdate()
		///
			let LLL=0
			let NNN=0
			cardata.forEach(function(item){
				if(item.flag==true){
				LLL=LLL+89*item.num
				NNN=NNN+item.num
		}
			})
			this.totalprice=LLL
			this.totalnum=NNN
			//this.$forceUpdate()
			///
		///
		
///页面初始化时,设置全选
var ko=[]
cardata.forEach(function(item){
		if(item.flag==true){
			ko.push(item)
		}
		})
console.log("ko是否完美",ko)	

if(ko.length==0){
	this.allCheck=false
	this.$forceUpdate()
}
if(ko.length==cardata.length){
	this.allCheck=true
	this.$forceUpdate()
}
///
		console.log("取出来的myproid",cardata)
		
				uni.request({
					url: 'http://127.0.0.1/mycardata/', //........。.....
					method: 'POST',
					data: {
						'cardata': cardata
					},
					dataType: 'json',
					success: res => {
						console.log("接到后端取回的数据",res.data);
						this.cartlist=res.data
						console.log("cartlist",this.cartlist)//接口数据已在ddd
							this.cartlist.forEach((item,index,myarray)=>{
								//item为每次的项
								///index为每次的下标
								//myarray为this.ddd
								console.log(item.id)
								cardata.forEach((m,index,myarray)=>{
										//console.log(m.id)
										if(m.id==item.id){
											item['num']=m.num
											console.log("AAAAAAAAAAAAAA")
										}
									})
								item["flag"]=false//为每一个商品对象加一个flag单选的开关属性
		
							})
							///把数据整合到购物车数据后,整合到this.ddd上了
							console.log("this.cartlist",this.cartlist)//接口数据已在ddd
							console.log("this.cartlistAAAAA",this.cartlist[0].name)
																// 	let LLL=0
																// 	let NNN=0
																// 	this.cartlist.forEach(function(item){
																// 		if(item.flag==true){
																// 		LLL=LLL+89*item.num
																// 		NNN=NNN+item.num
																// }
																// 	})
																// 	this.totalprice=LLL
																// 	this.totalnum=NNN
																	///
																	///
																	///计算总数量
						}///成功的反括号

					
				});
///

///
		
		this.cartlist=uni.getStorageSync('myproid')
			},
onShow() {
	this.isLogin=uni.getStorageSync('myopenid')
		if(this.isLogin.trim()==""){
			this.isLogin=0
		}else{
			this.isLogin=1
		}
		console.log("isLogin的值",this.isLogin)
		
	/////////////////////////////////////////////////////////////////
	//var cardata=uni.getStorageSync('myproid')//用同步,取出数组
	
	
	
	
	
	///
	/////////////////////////////////////////////////////////////////
	var cardata=uni.getStorageSync('myproid')//用同步,取出数组that.$forceUpdate()
	///
	let LLL=0
		let NNN=0
		cardata.forEach(function(item){
			if(item.flag==true){
			LLL=LLL+89*item.num
			NNN=NNN+item.num
	}
		})
		this.totalprice=LLL
		this.totalnum=NNN
		this.$forceUpdate()
		///
	///
	console.log("onshow123取出来的myproid",cardata)
	
			uni.request({
				url: 'http://127.0.0.1/mycardata/', //........。.....
				method: 'POST',
				data: {
					'cardata': cardata
				},
				dataType: 'json',
				success: res => {
					console.log(res.data);
					this.cartlist=res.data
					console.log("onshow的cartlist",this.cartlist)//接口数据已在ddd
					/////
					///整合2个对象数组
						///整合2个对象数组
						this.cartlist.forEach((item,index,myarray)=>{
							//item为每次的项
							///index为每次的下标
							//myarray为this.ddd
							console.log(item.id)
							//console.log(cardata)
							cardata.forEach((m,index,myarray)=>{
									//console.log(m.id)
									if(m.id==item.id){
										item['num']=m.num
									}
								})
							item["flag"]=false//为每一个商品对象加一个flag单选的开关属性
	
						})
						///把数据整合到购物车数据后,整合到this.ddd上了
						console.log("this.cartlist",this.cartlist)//接口数据已在ddd
									// 	let LLL=0
									// 	let NNN=0
									// 	this.cartlist.forEach(function(item){
									// 		if(item.flag==true){
									// 		LLL=LLL+89*item.num
									// 		NNN=NNN+item.num
									// 		}
									
									// 	})
									// 	this.totalprice=LLL
									// 	this.totalnum=NNN
										///
										///
									//this.cartlist=cardata//解决页面切换,选中消失的问题.重点
									//this.cartlist=uni.getStorageSync('myproid')
										///计算总数量
										
					}///成功的反括号
	
				
			});
///计算总价

///
},
methods:{////////////////////////////////////////////////////////////
//去结算
	cartBuy(){
		//取出操作购物车的用户信息和购物车信息,进行整合
		let muser=uni.getStorageSync("myopenid")//取ID
		let muserinfo=uni.getStorageSync("myuser")//取微信签名等
		let myobj=uni.getStorageSync("myproid")//取购物车商品对象数组
		
		let kongarray=[]
		myobj.forEach(function(item){
			if(item.flag==true){
				kongarray.push(item)
			}
		})
		console.log("打印一下只有flag=true的商品对象整合",kongarray)

		let mypayobj=new Object({
			kkkopenid:muser,
			kkkuser:muserinfo,
			kkkobj:kongarray
		})
		//console.log("打印一下整合后的订单对象",mypayobj)
		
		
		//如下是将购物车中所需的用户信息,购物车商品对象数组写入到本地
		uni.setStorageSync('mypayobj',mypayobj)//必须同步,写入完成后才能跳转,否则订单页先出现取不到数据
				uni.navigateTo({
						url: '/pages/mypay/mypay'
				})
	
	},
	///

	// 全选
///全选
allCheckChange(){
	if(this.allCheck==true){//如果是全选中状态
		for(var i=0;i<this.cartlist.length;i++){
			this.cartlist[i].flag=false
			this.allCheck=false
		}
	}else{//如果是非选中状态
		for(var i=0;i<this.cartlist.length;i++){
			this.cartlist[i].flag=true
			this.allCheck=true
		}
	}
	//最后刷新页面,写入本地
	this.$forceUpdate()
	///写入本地
	///
			uni.setStorage({
							key:'myproid',
							data:this.cartlist,
							success() {
								console.log('')	
							},
							fail() {
								console.log('')
							}
						}); 
	///
	///
	let LLL=0
						let NNN=0
						this.cartlist.forEach(function(item){
							if(item.flag==true){
								LLL=LLL+89*item.num
								NNN=NNN+item.num
							}
							
						
						})
						this.totalprice=LLL
						this.totalnum=NNN
						///
					
	///
},
///
	
// 单选
checkboxChage(index){
			console.log("执行了checkboxChage函数,index为",index)
			console.log(this.cartlist[index])
			this.cartlist[index].flag=!this.cartlist[index].flag
			this.$forceUpdate()//让页面强制刷新,而又不执行生命周期函数
					///写入本地
							///
									uni.setStorage({
													key:'myproid',
													data:this.cartlist,
													success() {
														console.log('')	
													},
													fail() {
														console.log('')
													}
												}); 
							
///
///统计总金额和总数量
					let LLL=0
					let NNN=0
					this.cartlist.forEach(function(item){
						if(item.flag==true){
							LLL=LLL+89*item.num
							NNN=NNN+item.num
						}
						
					
					})
					this.totalprice=LLL
					this.totalnum=NNN
					///
///
			},
	
// 滑动删除
delBtn(e,myid,index){
		var that=this
		//console.log(11)正常输出
		//console.log(e)//e作为函数之参数可以获取删除-文字,如果有删除,修改时,用的着
		//console.log(index)index作为函参同上
		console.log(myid)//正确打印出,滑动所关联的商品id
		//提示一下,真的要删除吗
			uni.showModal({
				title: '警告',
				content: '将从购物车中删除该商品,确认不购买该商品吗',
				success: function (res) {
					if (res.confirm) {
							console.log('用户点击确定');//用户确认要删除时
							//this.ddd[index].num=this.ddd[index].num-1
							///this.$forceUpdate()
							let cardata=uni.getStorageSync('myproid')
							cardata.forEach(function(xvalue,xindex,xarray){
									if(xvalue.id==myid){
										console.log(xindex)
										xarray.splice(xindex, 1)//本地直接把该 商品删除
										that.cartlist.splice(xindex, 1)//页面ddd直接把该 商品删除,
										that.$forceUpdate()
										///计算总金额和总价格
										let LLL=0
										let NNN=0
										that.cartlist.forEach(function(item){
											if(item.flag==true){
											LLL=LLL+89*item.num
											NNN=NNN+item.num
											}
									
										})
										that.totalprice=LLL
										that.totalnum=NNN
										///
										///
										///计算总数量
										///删除后,重新写入本地
												uni.setStorage({
																key:'myproid',
																data:cardata,
																success() {
																	console.log('删除后重新写入本地OK')	
																},
																fail() {
																	console.log('删除后重新写入本地失败了')
																}
															}); 
										
										///
									}
							　　　　
							 
							　　});


						
					
					} else if (res.cancel) {
						console.log('用户点击取消');
						return 
					}
				}
			});
		//
		
	},
	
	
	
	
	//数量增加
	add(index){
			var that=this
			let cardata=uni.getStorageSync('myproid')
			console.log("cardata[index].num",cardata[index].num)
			this.cartlist[index].num=this.cartlist[index].num+1
			this.$forceUpdate()
			cardata[index].num=cardata[index].num+1
			///计算总价
										let LLL=0
										let NNN=0
										this.cartlist.forEach(function(item){
											if(item.flag==true){
											LLL=LLL+89*item.num
											NNN=NNN+item.num
											}
									
										})
										this.totalprice=LLL
										this.totalnum=NNN
										///
										///
										///计算总数量
					///
			uni.setStorage({
			                key:'myproid',
			                data:cardata,
			                success() {
			                    console.log('增加后数量写入本地OK')
			                },
			                fail() {
			                    console.log('增加后数量写入本地OK失败了')
			                }
			            }); 
		},
	
	
	
	
// 减少
reduce(index){
	var that=this
	//console.log(index)测试正常,点击后输出相应商品对应下标
	//console.log(this.ddd[index])//测试正常,点击后,输出相应的商品对象
	//this.ddd[index].num=this.ddd[index].num-1//数量测试正常的减少
	//this.$forceUpdate()//强制刷新页面,加上这句,数量减少的同时,页面展示的数量才会及时更新
	//同时HTML页面变更为如下,减对应的    <input type="text"  v-model="ddd[index].num"/> 否则也不会热更新
	
	//但此时,程序重新启动/编译,ddd又会恢复到减少之前的数量,这是因为每一次onload中,我们从本地重新取
	//购物商对象数组id,num,交给后端请求 ,商品对象,num ,我们在减少时,应该更改本地的购物车id,num 这个
	//就行,对象为 var cardata=uni.getStorageSync('myproid')在减少后,要改 本地的cardata对象的数量
	//上面的index的商和myproid商品,下标,都对应,所以可以直接操作,也都是对象数组
	//写入本地,我们要同步,不能异步 
	let cardata=uni.getStorageSync('myproid')
	console.log("cardata[index].num",cardata[index].num)
	///////////////////////////////////////////////////////////////
	if(cardata[index].num<=1){
		uni.showModal({
			title: '警告',
			content: '将从购物车中删除该商品,确认不购买该商品吗',
			success: function (res) {
				if (res.confirm) {
						console.log('用户点击确定');//用户确认要删除时
						//this.ddd[index].num=this.ddd[index].num-1
						///this.$forceUpdate()
						cardata.splice(index, 1)//本地直接把该 商品删除.
						that.cartlist.splice(index, 1)//页面ddd直接把该 商品删除,
						that.$forceUpdate()
						///计算总价
										let LLL=0
										let NNN=0
										this.cartlist.forEach(function(item){
											if(item.flag==true){
											LLL=LLL+89*item.num
											NNN=NNN+item.num
											}
									
										})
										this.totalprice=LLL
										this.totalnum=NNN
										///
										///
										///计算总数量
													///
						//cardata[index].num=cardata[index].num-1
						uni.setStorage({
										key:'myproid',
										data:cardata,
										success() {
											console.log('减少后数量写入本地OK')
											// uni.showToast({
											//     title: '已加入购物车',
											//     duration: 1000
											// });
											
										},
										fail() {
											console.log('减少后数量写入本地OK失败了')
										}
									}); 
					
				
				} else if (res.cancel) {
					console.log('用户点击取消');
					return 
				}
			}
		});
	}

	else{         //如果数量大于1
		this.cartlist[index].num=this.cartlist[index].num-1
		this.$forceUpdate()
		cardata[index].num=cardata[index].num-1
		//计算总金额和总价
												let LLL=0
												let NNN=0
												this.cartlist.forEach(function(item){
													if(item.flag==true){
													LLL=LLL+89*item.num
													NNN=NNN+item.num
													}
											
												})
												this.totalprice=LLL
												this.totalnum=NNN
												///
												///
												///计算总数量
		uni.setStorage({
						key:'myproid',
						data:cardata,
						success() {
							console.log('减少后数量写入本地OK')
							// uni.showToast({
							//     title: '已加入购物车',
							//     duration: 1000
							// });
							
						},
						fail() {
							console.log('减少后数量写入本地OK失败了')
						}
					}); 
	}

			/////////////////////////////////////////////////////////////

	



	
}
	///////////////////////////////////
}

	}
</script>

<style>
.cartEmptyImg{width: 296rpx;height: 296rpx;display: block;margin:154rpx auto 0;}
.cartEmptyTip{text-align: center;font-size: 28rpx;color: #999;line-height: 160rpx;}
.cartLogin{width: 315rpx;height: 80rpx;color: #fff;background: #23baef;
font-size: 28rpx;line-height: 80rpx;text-align: center;margin:0 auto;}

.cartItem{display: flex;padding:35rpx 20rpx 30rpx;border-top:1rpx solid #e5e5e5}
.cartItem label image{width: 30rpx;height: 30rpx;}
.mainImg image{width: 200rpx;height: 200rpx;}
.cartItem checkbox{transform: scale(0.7);}
.cartItem label{display: flex;align-items: center;}
.cartItemContent{flex: 1;}
.content-title{font-size: 28rpx;line-height: 40rpx;height: 80rpx;
overflow: hidden; 
text-overflow: ellipsis;
display: -webkit-box;
-webkit-line-clamp: 2; 
-webkit-box-orient: vertical;}
.content-attr{font-size: 24rpx;color: #999;line-height: 40rpx;}
.content-price{height: 80rpx;display: flex;color: red;
align-items: center;font-size: 28rpx;justify-content: space-between;}
.numOption{display: flex;width: 154rpx;border:1rpx solid #e5e5e5;margin-left: 200rpx;}
.numOption .optionBtn{width: 44rpx;text-align: center;font-size:28rpx;color: #666;}
.numOption .numTxt{flex:1;border-left: 1rpx solid #e5e5e5
;border-right:1rpx solid #e5e5e5;}
.numOption .numTxt input{width: 100%;font-size:28rpx;text-align: center;color: #666;}
.cartBottom{position: fixed;bottom: var(--window-bottom);
width: 100%;background: #fff;font-size: 28rpx;border-top:1rpx solid #e5e5e5;
height: 106rpx;display: flex;justify-content: space-between;align-items: center;}
.cartBottom label image{width: 30rpx;height: 30rpx;margin:0 10rpx 0 20rpx}
.cartBottomRight{display: flex;align-items: center;}
.cartBottomRight .payBtn{width: 230rpx;height: 80rpx;
background: #0bbaef;color: #fff;margin:0 20rpx;border-radius: 80rpx;line-height: 80rpx;text-align: center;}
.cartBottomRight .payBtn text{font-size: 24rpx;}
.bottomEmpty{height: var(--window-bottom);;}
</style>