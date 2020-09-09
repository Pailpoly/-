<template>
  <view class="container" style="margin-top: 20rpx;">
	  <view><!-- 最外的左侧 -->
	  <view class="mytitle"><!-- 标题 -->
	  						 <text>品牌秒杀</text>
	  						 <image src="../static/myimg/rightjian.png"></image>
	  </view>
      <!-- 轮播 -->
      <swiper class="swiper" :autoplay="true" :interval="8000" :duration="6000" :current="swiperCurrent" @change="changeSwiper">
          <swiper-item><!-- 其中一个项 -->
                     <view><!-- 下面的大框 图片等-->
							<view class="contentview"><!-- 上层2个商品 -->
								  <view class="view1">
									  <image src="../static/myimg/z (1).jpg"></image>
									  <text>第一旅游</text>
								  </view>
								  <view class="view1">
										<image src="../static/myimg/z (1).jpg"></image>
										<text>女人最爱</text>
								  </view>
							</view>
							<view class="contentview"><!-- 下层2个商品 -->
								  <view class="view1">
									  <image src="../static/myimg/z (1).jpg"></image>
									  <text>川菜</text>
								  </view>
								  <view class="view1">
										<image src="../static/myimg/z (1).jpg"></image>
										<text>中华武术</text>
								  </view>
							</view>
					 </view>

          </swiper-item>
		  <swiper-item><!-- 其中一个项 -->
		             <view><!-- 下面的大框 图片等-->
		  							<view class="contentview"><!-- 上层2个商品 -->
		  								  <view class="view1">
		  									  <image src="../static/myimg/z (1).jpg"></image>
		  									  <text>旅游</text>
		  								  </view>
		  								  <view class="view1">
		  										<image src="../static/myimg/z (1).jpg"></image>
		  										<text>化妆</text>
		  								  </view>
		  							</view>
		  							<view class="contentview"><!-- 下层2个商品 -->
		  								  <view class="view1">
		  									  <image src="../static/myimg/z (1).jpg"></image>
		  									  <text>川菜</text>
		  								  </view>
		  								  <view class="view1">
		  										<image src="../static/myimg/z (1).jpg"></image>
		  										<text>武术</text>
		  								  </view>
		  							</view>
		  					 </view>
		  
		  </swiper-item>
			<swiper-item><!-- 其中一个项 -->
			           <view><!-- 下面的大框 图片等-->
										<view class="contentview"><!-- 上层2个商品 -->
											  <view class="view1">
												  <image src="../static/myimg/z (1).jpg"></image>
												  <text>PS设计</text>
											  </view>
											  <view class="view1">
													<image src="../static/myimg/z (1).jpg"></image>
													<text>3D动画</text>
											  </view>
										</view>
										<view class="contentview"><!-- 下层2个商品 -->
											  <view class="view1">
												  <image src="../static/myimg/z (1).jpg"></image>
												  <text>电脑维修</text>
											  </view>
											  <view class="view1">
													<image src="../static/myimg/z (1).jpg"></image>
													<text>奶茶工艺</text>
											  </view>
										</view>
								 </view>
			
			</swiper-item>
		<swiper-item><!-- 其中一个项 -->
		           <view><!-- 下面的大框 图片等-->
									<view class="contentview"><!-- 上层2个商品 -->
										  <view class="view1">
											  <image src="../static/myimg/z (1).jpg"></image>
											  <text>高级电工</text>
										  </view>
										  <view class="view1">
												<image src="../static/myimg/z (1).jpg"></image>
												<text>服装设计</text>
										  </view>
									</view>
									<view class="contentview"><!-- 下层2个商品 -->
										  <view class="view1">
											  <image src="../static/myimg/z (1).jpg"></image>
											  <text>会计</text>
										  </view>
										  <view class="view1">
												<image src="../static/myimg/z (1).jpg"></image>
												<text>征服</text>
										  </view>
									</view>
							 </view>
		
		</swiper-item>
	 <swiper-item><!-- 其中一个项 -->
	            <view><!-- 下面的大框 图片等-->
	 							<view class="contentview"><!-- 上层2个商品 -->
	 								  <view class="view1">
	 									  <image src="../static/myimg/z (1).jpg"></image>
	 									  <text>高级电工</text>
	 								  </view>
	 								  <view class="view1">
	 										<image src="../static/myimg/z (1).jpg"></image>
	 										<text>服装设计</text>
	 								  </view>
	 							</view>
	 							<view class="contentview"><!-- 下层2个商品 -->
	 								  <view class="view1">
	 									  <image src="../static/myimg/z (1).jpg"></image>
	 									  <text>会计</text>
	 								  </view>
	 								  <view class="view1">
	 										<image src="../static/myimg/z (1).jpg"></image>
	 										<text>征服</text>
	 								  </view>
	 							</view>
	 					 </view>
	 
	 </swiper-item>
<swiper-item><!-- 其中一个项 -->
		           <view><!-- 下面的大框 图片等-->
									<view class="contentview"><!-- 上层2个商品 -->
										  <view class="view1">
											  <image src="../static/myimg/z (1).jpg"></image>
											  <text>高级电工</text>
										  </view>
										  <view class="view1">
												<image src="../static/myimg/z (1).jpg"></image>
												<text>服装设计</text>
										  </view>
									</view>
									<view class="contentview"><!-- 下层2个商品 -->
										  <view class="view1">
											  <image src="../static/myimg/z (1).jpg"></image>
											  <text>会计</text>
										  </view>
										  <view class="view1">
												<image src="../static/myimg/z (1).jpg"></image>
												<text>征服</text>
										  </view>
									</view>
							 </view>
		
		</swiper-item>
	  </swiper>
      <!-- 轮播指示点样式修改 -->

  </view>
  
  
  <view><!-- 最外的右侧 -->
  	  <view class="mytitle"><!-- 标题 -->
  	  						 <text>品牌秒杀</text>
  	  						 <image src="../static/myimg/rightjian.png"></image>
  	  </view>
      <!-- 轮播 -->
      <swiper class="swiper" :autoplay="true" :interval="3500" :duration="3000" :current="swiperCurrent" @change="changeSwiper">
          <swiper-item><!-- 其中一个项 -->
                     <view><!-- 下面的大框 图片等-->
  							<view class="contentview"><!-- 上层2个商品 -->
  								  <view class="view1">
  									  <image src="../static/myimg/z (1).jpg"></image>
  									  <text>印度美食</text>
  								  </view>
  								  <view class="view1">
  										<image src="../static/myimg/z (1).jpg"></image>
  										<text>海鲜之都</text>
  								  </view>
  							</view>
  							<view class="contentview"><!-- 下层2个商品 -->
  								  <view class="view1">
  									  <image src="../static/myimg/z (1).jpg"></image>
  									  <text>川菜</text>
  								  </view>
  								  <view class="view1">
  										<image src="../static/myimg/z (1).jpg"></image>
  										<text>中华武术</text>
  								  </view>
  							</view>
  					 </view>
  
          </swiper-item>
  		  <swiper-item><!-- 其中一个项 -->
  		             <view><!-- 下面的大框 图片等-->
  		  							<view class="contentview"><!-- 上层2个商品 -->
  		  								  <view class="view1">
  		  									  <image src="../static/myimg/z (1).jpg"></image>
  		  									  <text>旅游</text>
  		  								  </view>
  		  								  <view class="view1">
  		  										<image src="../static/myimg/z (1).jpg"></image>
  		  										<text>化妆</text>
  		  								  </view>
  		  							</view>
  		  							<view class="contentview"><!-- 下层2个商品 -->
  		  								  <view class="view1">
  		  									  <image src="../static/myimg/z (1).jpg"></image>
  		  									  <text>川菜</text>
  		  								  </view>
  		  								  <view class="view1">
  		  										<image src="../static/myimg/z (1).jpg"></image>
  		  										<text>武术</text>
  		  								  </view>
  		  							</view>
  		  					 </view>
  		  
  		  </swiper-item>
  			<swiper-item><!-- 其中一个项 -->
  			           <view><!-- 下面的大框 图片等-->
  										<view class="contentview"><!-- 上层2个商品 -->
  											  <view class="view1">
  												<image src="../static/myimg/z (1).jpg"></image> 
  												  <text>三国志</text>
  											  </view>
  											  <view class="view1">
  													<image src="../static/myimg/z (1).jpg"></image>
  													<text>西游记</text>
  											  </view>
  										</view>
  										<view class="contentview"><!-- 下层2个商品 -->
  											  <view class="view1">
  												  <image src="../static/myimg/z (1).jpg"></image>
  												  <text>水浒传</text>
  											  </view>
  											  <view class="view1">
  													<image src="../static/myimg/z (1).jpg"></image>
  													<text>红楼梦</text>
  											  </view>
  										</view>
  								 </view>
  			
  			</swiper-item>
  		<swiper-item><!-- 其中一个项 -->
  		           <view><!-- 下面的大框 图片等-->
  									<view class="contentview"><!-- 上层2个商品 -->
  										  <view class="view1">
  											  <image src="../static/myimg/z (1).jpg"></image>
  											  <text>化学</text>
  										  </view>
  										  <view class="view1">
  												<image src="../static/myimg/z (1).jpg"></image>
  												<text>生物之迷</text>
  										  </view>
  									</view>
  									<view class="contentview"><!-- 下层2个商品 -->
  										  <view class="view1">
  											 <image src="../static/myimg/z (1).jpg"></image>
  											  <text>粤菜</text>
  										  </view>
  										  <view class="view1">
  												<image src="../static/myimg/z (1).jpg"></image>
  												<text>化妆品</text>
  										  </view>
  									</view>
  							 </view>
  		
  		</swiper-item>
  	  <swiper-item><!-- 其中一个项 -->
  	             <view><!-- 下面的大框 图片等-->
  	  							<view class="contentview"><!-- 上层2个商品 -->
  	  								  <view class="view1">
  	  									  <image src="../static/myimg/z (1).jpg"></image>
  	  									  <text>美国之旅</text>
  	  								  </view>
  	  								  <view class="view1">
  	  										<image src="../static/myimg/z (1).jpg"></image>
  	  										<text>四川</text>
  	  								  </view>
  	  							</view>
  	  							<view class="contentview"><!-- 下层2个商品 -->
  	  								  <view class="view1">
  	  									 <image src="../static/myimg/z (1).jpg"></image>
  	  									  <text>鸿法持</text>
  	  								  </view>
  	  								  <view class="view1">
  	  										<image src="../static/myimg/z (1).jpg"></image>
  	  										<text>面食</text>
  	  								  </view>
  	  							</view>
  	  					 </view>
  	  
  	  </swiper-item>
  	  <swiper-item><!-- 其中一个项 -->
  	             <view><!-- 下面的大框 图片等-->
  	  							<view class="contentview"><!-- 上层2个商品 -->
  	  								  <view class="view1">
  	  									  <image src="../static/myimg/z (1).jpg"></image>
  	  									  <text>武当山</text>
  	  								  </view>
  	  								  <view class="view1">
  	  										<image src="../static/myimg/z (1).jpg"></image>
  	  										<text>乐山</text>
  	  								  </view>
  	  							</view>
  	  							<view class="contentview"><!-- 下层2个商品 -->
  	  								  <view class="view1">
  	  									 <image src="../static/myimg/z (1).jpg"></image>
  	  									  <text>九华山</text>
  	  								  </view>
  	  								  <view class="view1">
  	  										<image src="../static/myimg/z (1).jpg"></image>
  	  										<text>香港</text>
  	  								  </view>
  	  							</view>
  	  					 </view>
  	  
  	  </swiper-item>
  	  </swiper>
      <!-- 轮播指示点样式修改 -->
  
  </view>
  </view>
</template>

<script>
	export default {
	    data() {          
	        return {              
	            
	            current: 0,
	            swiperCurrent: 0,
	        };
	    },
	    methods: {
	        changeSwiper(e) {
	            this.swiperCurrent = e.detail.current;
	        }
	    }
	
	}
	
</script>
  

<style scoped>
	/* 如下为标题和箭头样式 */
	.mytitle text{
		font-size: 30rpx;font-weight: bolder;margin-right: 10rpx;
	}
	.mytitle image{
		width: 35rpx;height: 35rpx;margin-left: 50rpx;margin-top: 5rpx;
	}
	.mytitle{
		display: flex;justify-content: flex-start;align-items: center;
		margin-top: 20rpx;margin-left: 15rpx;
	}
	
/* 一个项中上面2个图的view样式 */
	.view1 image{
		height: 120rpx;width: 120rpx;
	}
	.view1 text{
		font-size: 23rpx;margin-top: 10rpx;
	}
	.view1{
		display: flex;flex-direction: column;align-items: center;justify-content: center;
		flex: 1;
	}
	.contentview{
		display: flex;align-items: center;justify-content:space-around;
		margin-bottom: 10rpx;
	}
	

/*  */	
	.swiper {
	    width: 375rpx;
	    height: 350rpx;
	    overflow: hidden;
	    margin-top: 16rpx;
	    position: relative;
		border-style: solid;border-width: 2rpx;border-color: #CCCCCC;
		border-left-style: none;
		box-sizing: border-box;padding-top: 10rpx;padding-left: 5rpx;
	}
	.swiper-item {
	    width: 370rpx;
	    height: 350rpx;
	    background-color: #BD2C00;
	}
	.dot {
	    width: 24rpx;
	    height: 8rpx;
	    transition: all .6s;
	    background: rgba(0, 0, 0, .3);
	    margin-right: 10rpx;
	}
  .container {
      position: relative;
	  display: flex;
  }

  .active {
      width: 24rpx;
      height: 8rpx;
      background: rgba(255, 255, 255, .8);
  }
  .dots {
      position: absolute;
      bottom: 20rpx;
      left: 50%;
      // 这里一定要注意兼容不然很可能踩坑          
      transform: translate(-50%, 0);
      -webkit-transform: translate(-50%, 0);        
      z-index: 99;
      display: flex;
      flex-direction: row;
      justify-content: center;
  }
</style>