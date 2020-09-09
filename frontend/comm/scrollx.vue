<template>
    <view class="content">
		<!-- 这里是优惠券 -->
		<view>
			<image style="width: 750rpx;height: 202rpx;" src="../static/myimg/quan.png"></image>
		</view>
		
		<!-- 下方是水平滚动 -->
        <scroll-view scroll-x="true" class="scroll">
            <view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (1).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (11).gif"></image></view>
					</view>
            </view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (2).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (12).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (3).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (13).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (4).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (14).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (6).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (17).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (8).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (18).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (9).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (19).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (10).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (20).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (1).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (11).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (1).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (11).gif"></image></view>
					</view>
			</view>
			<view class="box"><!-- 其中一个项 .-->
					<view class="boxitem"><!-- 每个项包含上下2张图 -->
						<view><image style="width:120rpx ;height:130rpx ;" 
						src="../static/myimg/K (1).gif"></image></view>
						<view><image style="width:120rpx ;height:130rpx ;" src="../static/myimg/K (11).gif"></image></view>
					</view>
			</view>
        </scroll-view>
    </view>
</template>
 
 
<script>
    export default {
        data() {
            return {
 
            }
        },
        methods: {
 
        }
    }
</script>
 
<style scoped>
    .content {
      
    }
 
    .scroll {
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
		display: flex;align-items: center;justify-content: center;
		margin-top: 20rpx;
    }
 
    .box {
       display: inline-block;margin-left: 10rpx;
    }
 
    .box:last-child {
        
    }
 
    .images {
       
    }
</style>