<template>
	<view>


<!-- 下面是标题  -->
<view style="width: 750rpx;height: 130rpx;background-color: #e9e7ef;display: flex;justify-content: center;align-items: center;">
	<view style="width: 80rpx;height: 4rpx;background-color: #808080;position: relative;left: -40rpx;"></view>
	<view style="font-size: 50rpx;position: relative;top: -19rpx;left: -24rpx;"><text>.</text></view>
	<view style="color: #ff2d51;font-size: 50rpx;"><text>东京书城</text></view>
	<view style="width: 80rpx;height: 4rpx;background-color: #808080;position: relative;left: 40rpx;"></view>
	<view style="font-size: 50rpx;position: relative;top: -19rpx;left: -65rpx;"><text>.</text></view>
</view>

<!-- 下面是内容 -->

<!-- 下面的大块-->
	<view class="wrapper">
		<view class="bleft"><!-- 左边 -->
			<view class="mytitle" style="margin-top: 20rpx;">
				<text style="font-weight: bolder;margin-left: 10rpx;margin-top: 40rpx;">文艺时光</text>
			</view>
			<view class="mytitle2">
				<text style="color: #808080;margin-left: 10rpx;margin-top: 20rpx;font-size: 20rpx;">5折封顶</text>
			</view>
			<view class="myimg">
				<image style="width: 150rpx;height: 170rpx;margin-left: 160rpx;margin-top: 30rpx;" src="../static/myimg/kkk/k%20(989).jpg" mode=""></image>
			</view>
		</view>
		
		
		<view class="bright"><!-- 右边 -->
			 <view class="bright1" style="display: flex;justify-content: space-between;box-sizing: border-box;
			 padding: 20rpx 25rpx;">
					<view style="display: flex;flex-direction: column;align-items: center;justify-content: center;">
						<text style="font-weight: bolder;margin-top: -20rpx;">电子书</text>
						<text style="font-size: 20rpx;color: #808080;">2件4折</text>
					</view>
				
					<view>
						<image style="width: 100rpx;height: 120rpx;" src="../static/myimg/kkk/k%20(982).jpg" mode=""></image>
					</view>
			 </view>
			 <view class="" style="height: 2rpx;width: 366rpx;background-color: #f2f2f3;
			 position: relative;top:-10rpx">
			 	
			 </view>
			 
			 <view class="bright2">
				 <view class="bright1" style="display: flex;justify-content: space-between;box-sizing: border-box;
				 padding: 20rpx 25rpx;">
				 					<view style="display: flex;flex-direction: column;align-items: center;justify-content: center;">
				 						<text style="font-weight: bolder;margin-top: -20rpx;">精选童书</text>
				 						<text style="font-size: 20rpx;color: #808080;">5折封顶</text>
				 					</view>
				 				
				 					<view>
				 						<image style="width: 90rpx;height: 100rpx;" src="../static/myimg/kkk/k%20(982).jpg" mode=""></image>
				 					</view>
				 </view>
			 </view>
		</view>

		
		
		<!-- 这个组件的最外层标记是如下这个view -->
	</view>
	<!-- 开始接着下面的版块来 -->
	<!-- 第二层 -->
	<view class="twodiv"  style="width: 732rpx;height: 250rpx;margin: 0 auto;
			position: relative;top: -295rpx;display: flex;justify-content: space-around;">
		<!-- 其中一个项,一共有4个 -->
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						畅读经典
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(980).jpg" mode=""></image>
				</view>
				
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						经济态势
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(981).jpg" mode=""></image>
				</view>
				
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						科技之颠
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(986).jpg" mode=""></image>
				</view>
				
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						吃喝玩乐
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(992).jpg" mode=""></image>
				</view>
	</view>
<!-- 第三层 -->
	<!-- 第二层 -->
	<view class="twodiv"  style="width: 732rpx;height: 250rpx;margin: 0 auto;
			position: relative;top: -315rpx;display: flex;justify-content: space-around;">
		<!-- 其中一个项,一共有4个 -->
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						畅读经典
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(980).jpg" mode=""></image>
				</view>
				
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						经济态势
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(981).jpg" mode=""></image>
				</view>
				
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						科技之颠
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(986).jpg" mode=""></image>
				</view>
				
				<view style="display: flex;flex-direction: column;justify-content: center;align-items: center;margin-top: 15rpx;">
					<text style="font-weight: bold;margin-top: 10rpx;">
						吃喝玩乐
					</text>
					<text style="color: #797979;font-size: 20rpx;margin-top: 5rpx;">
						5折封顶
					</text>
					<image style="width: 90rpx;height: 110rpx;margin-top: 10rpx;" src="../static/myimg/kkk/k%20(992).jpg" mode=""></image>
				</view>
	</view>
	<!--  -->
</view>
</template>

<script>
	export default {
		
	}
</script>

<style scoped>
	.bleft{
		border-top-left-radius: 15rpx;
		background: #ffffff;
		height: 300rpx;width: 366rpx;
	}
	.bright{
		border-top-right-radius: 15rpx;
		background: #ffffff;
		height: 300rpx;width: 366rpx;
		margin-left: 5rpx;
	}
	.wrapper{
		display: flex;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	/* 标题 的CSS */
.bimage{
	height: 84rpx;width: 400rpx;
}
.btitle{
	height: 100rpx;width: 750rpx;
	display: flex;justify-content: center;align-items: center;
}
/* 下面的大块 */
.wrapper{
	width: 734rpx;margin: 0 auto;height: 600rpx;
}

</style>
