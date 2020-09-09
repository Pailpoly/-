<template>
	<view>
		<!-- 页面标题 -->

		<view><IndexNav></IndexNav></view>
		<!-- 第一个组件 -->
		<view><JiFen></JiFen></view>
		<!-- 积分组件 -->
		<view><ScrollX></ScrollX></view>
		<!-- 水平滚动导航 -->
		<view><Swi></Swi></view>
		<!-- 轮播图组件 -->
		<view class="myBest"><BestProduct></BestProduct></view>
		<!-- 畅销榜 -->
		<view><KILL></KILL></view>
		<!-- 秒杀 -->
		<!-- <view><OK></OK></view><!-- 品牌秒杀和拼团组件 -->
		-->
		<view><DaPai></DaPai></view>
		<!-- 今日大牌组件 -->
		<view><BOOK></BOOK></view>
		<!-- 东京书城组件 -->
		<view><clothes></clothes></view>
		<!-- 服装显示组件 -->
		<view><jdshop></jdshop></view>
		<!-- 东京超市 -->
		<view><child></child></view>
		<!-- 儿童专区 -->
		<view><tuijian></tuijian></view>
		<!-- 推荐 -->
		<view><lingshi></lingshi></view>
		<!-- 零食惠 -->
		<view><myshop></myshop></view>
		<!-- 为您推荐 -->

		<!-- 回到顶部 -->
		<view class="top" :style="{ display: flag === true ? 'block' : 'none' }">
			<image
				style="width: 90rpx;height: 90rpx;opacity: 0.8;border-radius: 45rpx;"
				src="../../static/myimg/ding.png"
				class="topc"
				type="arrowthinup"
				size="50"
				@click="top"
			></image>
		</view>
	</view>
</template>

<script>
import DaPai from '../../comm/dapai.vue';
import OK from '../../comm/OK.vue';
import KILL from '../../comm/kill.vue';
import BestProduct from '../../comm/bestproduct.vue';
import Swi from '../../comm/swi.vue';
import IndexNav from '../../comm/indexnav.vue';
import JiFen from '../../comm/jifen.vue';
import ScrollX from '../../comm/scrollx.vue';
import BOOK from '../../comm/book.vue';
import clothes from '../../comm/clothes.vue';
import jdshop from '../../comm/jdshop.vue';
import child from '../../comm/child.vue';
import tuijian from '../../comm/tuijian.vue';
import lingshi from '../../comm/lingshi.vue';
import myshop from '../../comm/myshop.vue';

export default {
	data() {
		return {
			flag: false //回到顶部显隐的开关变量
		};
	},
	onLoad() {},
	methods: {
		top() {
			//回到顶部
			uni.pageScrollTo({
				scrollTop: 0,
				duration: 300
			});
		},
		onPageScroll(e) {
			//根据距离顶部距离是否显示回到顶部按钮
			if (e.scrollTop > 600) {
				//当距离大于600时显示回到顶部按钮
				this.flag = true;
			} else {
				//当距离小于600时隐藏回到顶部按钮
				this.flag = false;
			}
		}
	},
	components: {
		IndexNav,
		JiFen,
		ScrollX,
		Swi,
		BestProduct,
		KILL,
		OK,
		DaPai,
		BOOK,
		clothes,
		jdshop,
		child,
		tuijian,
		lingshi,
		myshop
	}
};
</script>

<style scoped>
.myBest {
	margin-left: 10rpx;
	margin-top: 20rpx;
}
/* 回到顶部 */


.top {
		position: relative;
		display: none; /* 先将元素隐藏 */
	}
 
	.topc {
		position: fixed;
		right: 0;
		background: #F0F0F0;
		top: 70%;
		height: 50px;
		line-height: 50px;
	}




</style>
