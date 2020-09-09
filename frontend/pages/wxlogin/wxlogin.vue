<template>
	<view>
		
		<view style="margin-top: 120rpx;"><!-- 手机号登陆 -->
			<view>
				<text style="margin-left: 20rpx;color: #00bc12;font-weight: bold;">取消</text>
				<text style="margin-left: 235rpx;color: #000000;font-weight: bold;">登陆/注册</text>
			</view>
			
			<view style="width: 750rpx;height: 100rpx;background-color: #rrrrrr;">
				
			</view>
			
			<view style="width: 720rpx;margin: 0 auto;">
				<input style="border-bottom-style: solid;border-bottom-width: 2rpx;border-bottom-color: #f0f0f4;
				height: 80rpx;" 
				type="text" placeholder="输入手机号(新号码自动注册)"  />  
			</view>
			<view style="width: 720rpx;margin: 0 auto;">
				<input style="border-bottom-style: solid;border-bottom-width: 2rpx;border-bottom-color: #f0f0f4;
				height: 80rpx;"   type="text" placeholder="输入验证码"  /> 
				<view style="position: relative;top:-60rpx;left: 500rpx;">
					<view class="mytext" style="color: #ffffff;background-color: #00bc12;height: 40rpx;width: 160rpx;border-radius: 20rpx;
					text-align: center;line-height: 40rpx;font-size: 25rpx;">
						获取验证码</view>
				</view>
			</view>
			<view>
				<button style="margin-top: 100rpx;width: 730rpx;border-radius: 40rpx;" type="primary">登陆</button>
			</view>
		</view>
		
		
		
		
		
		
		
		
		
		
		
		<view style="margin-top: 200rpx;"><!-- 微信授权登陆 -->
		<view style="width: 750rpx;height: 40rpx;display: flex;justify-content: center;align-items: center;
		            color: #ff2121;position: relative;top: -30rpx;">
			<text>推荐使用微信直接登陆</text>
		</view>
			<view style="display: flex;justify-content: center;align-items: center;">
				<view style="width: 200rpx;height: 1rpx;background-color: #f0f0f4;"></view>
				<view style="color: #787878;margin-top: 0rpx;">第三方登陆</view>
				<view style="width: 200rpx;height: 1rpx;background-color: #f0f0f4;"></view>
			</view>
			<view class="btn" style="margin-top: 30rpx;display: flex;justify-content: center;align-items: center;">
			<navigator url="/pages/login/login" >
			<image class="btn" style="width: 80rpx;height: 80rpx;" src="../../static/myimg/weixing.png">
			</image>
			</navigator>
			</view>
			<view style="color: #787878;display: flex;justify-content: center;align-items: center;
			margin-top: 35rpx;">
				微信直接登陆
			</view>
			<view>
				<view style="color: #787878;margin-top: 35rpx;display: flex;justify-content: center;align-items: center;">
					登陆即代表您同意本站之服务协议和隐私政策
				</view>
			</view>
		</view>
	</view>
</template>


<script>
 
  export default {
    data() {
      return {
         
      };
    },
    methods: {

    }
  }
</script>
 
<style scoped>
.mytext{
	
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
outline: none;
border-color: transparent;
box-shadow:none;filter:chroma(color=#000000);
}
</style>







