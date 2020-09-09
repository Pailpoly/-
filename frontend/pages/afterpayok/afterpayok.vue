<template>
	<view style="background-color: #ff4e20;">
		<!-- 头 -->
		<view
			style="width: 750rpx;height: 50rpx;text-align: center;line-height: 50rpx;
   position:fixed;color:#c32136;z-index: 10;top: 50rpx;font-weight: bolder;"
		>
			<text style="font-size: 30rpx;color: #fff;">支付成功</text>
		</view>
		<!-- 支付成功提示 -->
		<view style="width: 750rpx;height: 600rpx;background-color: #ff4e20;">
			<!-- 中间的块 -->
			<view
				style="width: 650rpx;margin-left: 50rpx;height: 100rpx;position: relative;top: 250rpx;
	          border-bottom-style:dashed;border-bottom-width: 2rpx;border-bottom-color: #fff;
			  color: #fff;font-weight: 100;"
			>
				<view><text style="font-size: 35rpx;position: relative;top: -100rpx;">已支付完成</text></view>
				<view>
					<text style="position: relative;top: -80rpx;font-size: 28rpx;">实付:</text>
					<text style="position: relative;top: -80rpx;font-size: 35rpx;font-weight: bold;">1</text>
					<text style="position: relative;top: -80rpx;font-size: 28rpx;">元人民币</text>
				</view>
				<view><text style="position: relative;top: -60rpx;font-size: 26rpx;">微信支付</text></view>
			</view>
		</view>

		<!-- 支付成功的提示图片. -->
		<image
			style="width: 100rpx;height: 100rpx;z-index: 88;position: fixed;top: 180rpx;
			  left: 500rpx;"
			src="../../static/myimg/payok.png"
		></image>

		<!-- 两个按钮 -->
		<!-- 实现2个按钮 -->
		<!-- 实现2个按钮 -->
		<view @click="tt"
			style="width: 750rpx;height: 100rpx;margin-top: -230rpx;
			display: flex;align-items: center;"
		>
			<!-- 查看订单 -->
			<view
				style="width: 200rpx;height: 50rpx;border-color: #fff;border-radius: 25rpx;
				display: flex;justify-content: center;align-items: center;
			 border-width: 2rpx;border-style: solid;margin-left: 125rpx;"
			>
				<text style="color: #fff;font-size: 26rpx;">查看订单</text>
			</view>
			<!-- 继续购物 -->
			<view  @click="gotomallvue"
				style="width: 200rpx;height: 50rpx;border-color: #fff;border-radius: 25rpx;
				display: flex;justify-content: center;align-items: center;
			 border-width: 2rpx;border-style: solid;margin-left: 100rpx;"
			>
				<text style="color: #fff;font-size: 26rpx;">继续购物</text>
			</view>
		</view>
		<!-- 开奖 -->
		<!-- 抽奖. -->
		<view><image @click="pop()" style="width: 750rpx;margin-top: 50rpx;height: 487rpx;border-radius: 30rpx;" src="../../static/myimg/jiang7.png"></image></view>
		<!-- 弹窗 -->
		<mpopup ref="mpopup" :isdistance="true"></mpopup>

		<!-- 间隔条 -->
		<view style="height: 20rpx;width: 750rpx;background-color: #f0f0f4;"></view>

		<!-- 优惠券提示 -->
		<view style="width: 750rpx;height:122rpx ;background-color: #fff;">
			<image @click="pop2()" style="width: 720rpx;height: 122rpx;margin-left: 15rpx;" src="../../static/myimg/ggggg57-41.jpg" mode=""></image>
		</view>
		
	<!-- 间隔条 -->
		<view style="height: 20rpx;width: 750rpx;background-color: #f0f0f4;">	
		</view>
		
		
		
<!-- 警示信息 -->
		<view style="width: 750rpx;background-color: #fff;color: #808080;font-size: 26rpx;
		           box-sizing: border-box;padding: 25rpx 25rpx 0 25rpx">
			<text>注意:本公司不会以订单异常,系统升级为由要求您点击任何网址链接进行退款操作</text>
			
		</view>
		<view style="width: 750rpx;background-color: #fff;color: #808080;font-size: 26rpx;
		           box-sizing: border-box;padding: 15rpx 25rpx 0 25rpx"> 
			<text>本公司唯一的官方热线:15323441764</text>
		</view>		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	</view>
</template>

<script>
import mpopup from '../../components/xuan-popup/xuan-popup.vue';
export default {
	data() {
		return {};
	},
	methods: {
		pop() {
			this.$refs.mpopup.open({
				type: 'success',
				content: '抽奖已暂停',
				timeout: 2000
			});
		},
		pop2() {
			this.$refs.mpopup.open({
				type: 'success',
				content: '会员才可以领取',
				timeout: 2000
			});
		},
		gotomallvue(){
					uni.switchTab({
						url: '/pages/mall/mall'
					});
				},
				tt(){
										console.log("查看订单被点击")
										uni.navigateTo({
											url: '/pages/seeorder/seeorder'
										});
									}
	},
	components: {
		mpopup
	}
};
</script>

<style scoped></style>
