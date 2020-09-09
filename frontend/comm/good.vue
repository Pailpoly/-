<template>
	<!-- 最外层固定左右联动区 -->
	<view style="width: 750rpx;height: 1040rpx;background-color: #CCCC77;
	overflow: hidden;display: flex;position: relative;top: -60rpx;">

		
		
		
		
	

<!-- 左侧开始 -->
<view class="cateleft">
	
	<scroll-view style="overflow: auto;" class="cateNameList" scroll-y="true"  scroll-with-animation>
		<view class="cateNameItem" :class="{ cateActive: index == current }"  @click="menuTab(index)">
			
			<view class="cateLine"></view>
		</view><!-- 这个view是为了解决无法点击第一项'图书'而设置的 -->
		
		<view class="cateNameItem" :class="{ cateActive: index == current }" v-for="(item, index) in cate.data" :key="index" @click="menuTab(index)">
			{{ item.title }}
			<view class="cateLine"></view>
		</view>
	</scroll-view>
</view>
<!-- 左侧结束 -->










<!-- 右侧开始 -->
<view class="cateright">
<scroll-view class="cateRightScroll" scroll-y="true" :scroll-into-view="'cate' + mainCurrent" scroll-with-animation @scroll="rightScroll">
	<view class="cateItem" v-for="(item, index) in cate.data" :key="index" :id="'cate' + index">
		<view class="caterightTitle">
			——
			<text>{{ item.title }}</text>
			——
		</view>
		<view class="cateRightList">
			<view class="cateRightItem" v-for="(child, childindex) in item.product" :key="childindex">
				<navigator hover-class="none" :url="'../detail/detail?id=' + child.id">
					<image :src="'/static'+child.small_image" mode=""></image>
					<!-- <my-image :imgpath="imgUrl + child.mainimage"></my-image> -->
					<text>{{ child.name }}</text>
				</navigator>
			</view>
		</view>
	</view>

	<view style="height: 30rpx;width: 100%;"></view>
</scroll-view>

</view>

<!-- 右侧结束 .-->
			
			
			
			
			
		
	</view>
</template>

<script>
export default {
	data() {
		return {
			cate: [],
			current: 0,
			rectInfo: [],
			mainCurrent: 0,
			scrollTop: 0
		};
	},
	created() {
		console.log('123开始执行onload');
		this.getData();
		console.log('执行了onload');
	},
	mounted() {
		setTimeout(() => {
			this.getRectInfo();
			console.log(this.rectInfo);
		}, 200);
	},
	methods: {
		getData() {
			uni.request({
				url: 'http://127.0.0.1/vvv/',
				success: res => {
					this.cate = res.data;
					console.log('许飞');
					console.log(res);
					console.log('许飞' + this.cate);
					console.log('许飞message-----' + this.cate);
					
					console.log('许飞message-----' + typeof(this.cate));
					console.log(this.cate.data);
					console.log(this.cate.data[0].title);//女装男装
					//this.cate.data 就是对象数组,数组内有22分类表对象,
				}
			});
		},
		//滚动.
		rightScroll(e) {
			var scrollTop = e.detail.scrollTop;
			console.log('滚动' + scrollTop);
			var index;

			for (var i = 0; i < this.rectInfo.length; i++) {
				if (scrollTop > this.rectInfo[i].top && scrollTop < this.rectInfo[i].bottom) {
					this.current = i;
					this.scrollTop = i * uni.upx2px(100);
				}
			}
		},
		//菜单选择
		menuTab(index) {
			this.current = index;
			this.mainCurrent = index;
			this.scrollTop = index * uni.upx2px(100);
			console.log("许鹏飞",index)//以0开始
		},
		//获取矩形信息
		getRectInfo() {
			var top = 0;
			var bottom = 0;
			var temp = 0;
			for (var i = 0; i < this.cate.length; i++) {
				let view = uni
					.createSelectorQuery()
					.in(this)
					.select('#cate' + i);

				view.fields(
					{
						size: true,
						rect: true
					},
					data => {
						top = temp;
						bottom = top + data.height;
						temp += data.height;
						this.rectInfo[i] = { top: top, bottom: bottom };
					}
				).exec();
			}
		}
	}
};
</script>

<style>
page {
	background: #f7f7f7;
}
.search {
	height: 110rpx;
	width: 100%;
	background: #fff;
	display: flex;
	justify-content: center;
	align-items: center;
}
.searchBox {
	width: 690rpx;
	height: 70rpx;
	border-radius: 10rpx;
	font-size: 28rpx;
	color: #999;
	background: #f7f7f7;
}
.searchBox navigator {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 70rpx;
}
.searchBox image {
	width: 38rpx;
	height: 38rpx;
	margin-right: 12rpx;
}
/* .cate {原来的
	position: absolute;
	top: 120rpx;
	bottom: 0;
	width: 100%;
	display: flex;
} */
/* 下面是我改的 */
.cate{
	display: flex;
}


.cateleft {
	width: 200rpx;
	background: #f7f7f7;
	height: 100%;
}
.cateNameList {
	height: 100%;
	overflow: auto;
}
.cateRightList {
	height: auto;
	overflow: hidden;
}
.cateNameItem {
	font-size: 28rpx;
	color: #000;
	line-height: 100rpx;
	text-align: center;
	position: relative;
}
.cateActive {
	background: #fff;
}
.cateLine {
	position: absolute;
	width: 8rpx;
	height: 30rpx;
	background: #f7f7f7;
	top: 35rpx;
}
.cateActive .cateLine {
	background: #ff2121;
	height: 70rpx;margin-top: -17rpx;
} /* 这一句是左侧的激活红色左边块 */

.cateright {
	width: 550rpx;
	background: #fff;
	height: 100%;
}
.cateRightScroll {
	height: 100%;
	overflow: auto;
}
.caterightTitle {
	line-height: 86rpx;
	padding-top: 16rpx;
	color: #999;
	font-size: 28rpx;
	text-align: center;
}
.caterightTitle text {
	padding: 0 30rpx;
}
.cateRightItem {
	width: 33.33%;
	float: left;
	margin-top: 20rpx;
}
.cateRightItem image {
	width: 160rpx;
	height: 160rpx;
	display: block;
	margin: 0 auto;
}
.cateRightItem text {
	line-height: 36rpx;
	font-size: 24rpx;
	text-align: center;
	display: block;
	width: 100%;
	overflow: hidden;
	text-overflow: ellipsis;
	white-space: nowrap;
}
</style>