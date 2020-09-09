<template>
  <view class="container">
      <!-- 轮播 -->
      <swiper class="swiper" :autoplay="true" :interval="2000" :duration="1000" :current="swiperCurrent" @change="changeSwiper">
          <swiper-item v-for="item in swiperImg" :key="item.id">
              <image class="swiper-item" :src="item" mode="widthFix"></image>
          </swiper-item>
      </swiper>
      <!-- 轮播指示点样式修改 -->
      <view class="dots">
          <block v-for="(item,index) in swiperImg.length" :key="item">
              <view class="dot" :class="index==swiperCurrent ? ' active' : ''"></view>
          </block>
      </view>
	  <!-- 下面是广告图 -->
	  <view class="imgview">
		  <image style="" src="../static/myimg/ttt46.jpg"></image>
	  </view>
  </view>
</template>

<script>
	export default {
	    data() {          
	        return {              
	            swiperImg: [
	'../static/myimg/1.jpg',
	'../static/myimg/2.jpg',
	'../static/myimg/3.jpg',
	'../static/myimg/4.jpg',
	'../static/myimg/5.jpg',
	'../static/myimg/6.jpg'
				
				],
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
	
	.imgview{
		margin: 0 auto;
	}
	.imgview image{
		width: 500rpx;height: 72rpx; margin: 0 auto;margin-left: 120rpx;
	}
	
	
	
	.swiper-item {
	    width: 700rpx;
	    height: 240rpx;
	    border-radius: 16rpx;
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
	  width: 740rpx;height: 370rpx;background-color: #c93756;margin: 0 auto;
	  border-radius: 16rpx;box-sizing: border-box;padding: 5rpx;
  }
  .swiper {
      width: 700rpx;
      height: 240rpx;
      border-radius: 16rpx;
      overflow: hidden;
      margin-top: 16rpx;
      position: relative;
      margin-left: 18rpx;
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