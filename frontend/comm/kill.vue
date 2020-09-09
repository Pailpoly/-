<template>
	<view>
		
		
	<view v-if="aaa" style="display: flex;align-items: center;margin-top: 20rpx;margin-left: 10rpx;">
		<text style="font-weight: bolder;margin-left: 10rpx;">秒杀</text>
		<text style="width: 20rpx;height: 10rpx;display: inline-block;"></text>
		<!-- 修改颜色 -->
		<uni-countdown color="#FFFFFF" background-color="#00B26A" border-color="#00B26A" :day="0" :hour="0" :minute="1" :second="0"></uni-countdown>
	</view>
	
	<!-- 商品展示 -->
	<view class="content"><!-- 下方商品展示 -->
				<view><!-- 第一个项 -->
						<view><!-- 图片 -->
							<image class="myimg1" src="../static/myimg/z%20(1).jpg"></image>
						</view>
						<view class="view3"><!-- 现价 -->
							<text class="mytext1">￥28</text>
						</view>
						<view class="view3"><!-- 原价 -->
							<text class="deleted">￥98</text>
						</view>
				</view>
				<view class="">
					    <view><!-- 图片 -->
					    	<image class="myimg1"src="../static/myimg/z%20(2).jpg"></image>
					    </view>
						<view class="view3"><!-- 现价 -->
							<text class="mytext1">￥28</text>
						</view>
						<view class="view3"><!-- 原价 -->
							<text class="deleted">￥98</text>
						</view>
				</view>
				<view>
					     <view><!-- 图片 -->
					     	<image class="myimg1" src="../static/myimg/z%20(2).png"></image>
					     </view>
						<view class="view3"><!-- 现价 -->
							<text class="mytext1">￥28</text>
						</view>
						<view class="view3"><!-- 原价 -->
							<text class="deleted">￥98</text>
						</view>
				</view>
				<view><!-- 第一个项 -->
						<view><!-- 图片 -->
							<image class="myimg1" src="../static/myimg/z%20(1).jpg"></image>
						</view>
						<view class="view3"><!-- 现价 -->
							<text class="mytext1">￥28</text>
						</view>
						<view class="view3"><!-- 原价 -->
							<text class="deleted">￥98</text>
						</view>
				</view>
	
					
		</view>
	
	
	
	</view>
</template>

<script>
	import uniCountdown from '@/components/uni-countdown/uni-countdown.vue'
	export default {
		data(){
			return{
				aaa:true
			}
		},
		methods:{
			
			timeup(){
				let that=this
				that.aaa=false
			}
		},
		components: {
			uniCountdown
			}
	}
</script>

<style scoped>
.view3{
		font-size: 25rpx;text-align: center;
		
	}
	.deleted{
		text-decoration:line-through;text-align: center;color: #808080;
	}
	.myimg1{
		width:120rpx;height: 120rpx;
	}
	.myimg12{
		height: 120rpx;width: 80rpx;
	}
	.content{
		display: flex;align-items: center;margin-top: 20rpx;
		justify-content: space-around;
	}
	.content view{
				
	}
	
	
	
	
	
	
	.myicon{
		width: 50rpx;height: 50rpx;
	}
	.myicon image{
		width: 50rpx;height: 50rpx;
	}
	
	
	
	
.mytext{
	font-size: 25rpx;font-weight: bolder;
}
.wrapper{
	display: flex;justify-content: flex-start;align-items: center;margin-right: 10rpx;
}
.mytime{
	margin-left: 30rpx;
}
.no{
	width: 20rpx;height: 1rpx;
}
</style>