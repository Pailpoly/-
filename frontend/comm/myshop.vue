<template>
	<view>
<!-- 标题 -->
<view style="width: 750rpx;height: 150rpx;background-color: #e9e7ef;display: flex;justify-content: center;align-items: center;">
	<view style="width: 80rpx;height: 4rpx;background-color: #808080;position: relative;left: -40rpx;"></view>
	<view style="font-size: 50rpx;position: relative;top: -19rpx;left: -24rpx;"><text>.</text></view>
	<view style="color: #ff2d51;font-size: 50rpx;"><text>东京shop</text></view>
	<view style="width: 80rpx;height: 4rpx;background-color: #808080;position: relative;left: 40rpx;"></view>
	<view style="font-size: 50rpx;position: relative;top: -19rpx;left: -65rpx;"><text>.</text></view>
</view>
	
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/1e1r1.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>linux</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥21
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/zzzxf.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>满汉全席</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥88
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	

<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/ds122.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>思维力</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥28
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/sdfdee.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>川菜</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥80
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/e5e445221d.png"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>家常菜</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥38
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/d22.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>数学</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥50
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->		
	
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/1e1r1.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>linux shell</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥21
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/2sdf21.png"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>python</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥56
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/2z2z2.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>深度实践</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥99
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/4e4.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>命令大全</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥66
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/32sd1f23.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>python入门</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥32
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/45664.png"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>专注力</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥88
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/ds32f.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>四川小吃</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥22
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/e2e2e2.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>家常小炒</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥36
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/ttsd22.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>火锅</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥103
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/saawee.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>python爬虫</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥66
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/z22z2z.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>趣味python</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥55
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/x02x02.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>江湖菜</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥35
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/zxcfds5rfds.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>舌尖上的中国</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥21
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/t32231.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>教师数学材料</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥64
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
		
		
		
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/231.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>军事知识</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥210
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/df5645.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>心理学</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥888
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/主图4.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>基因</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥55
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/safdas.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>大众心理</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥66
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		
		
		
<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/dfee.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>社交力</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥33
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/eeee.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>云南</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥97
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->			
		


<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/asdfsd2323.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>云南</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥29
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/asdfsd2323.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>自助游</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥77
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	





<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/555.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>上海</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥68
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/safdd21rf.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>清海</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥94
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	










<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/dsf322.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>东北</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥21
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/sdeee55e.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>java</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥88
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	







<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/eee212xf.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>java高阶</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥74
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/s[ring.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>spring</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥48
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	




<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/sdfdsf.png"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>程序员与刑法</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥55
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/dd24241.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>公司法</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥37
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	




<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/dsfds0d.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>民法典</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥128
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/r456t456.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>法律咨询大全</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥56
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	




<!-- 空白行 -->
<view style="width: 750rpx;height: 8rpx;background-color: #f0f0f4;"></view>
<!-- 第一对商品 -->		<!-- 把第一对商品无限复制,每复制一行就是一行的出现,把图片和标题,价格,改一下,就行了,其它的不用动 -->
<view style="width: 750rpx;background-color:#f2f2f3 ;height: 500rpx;display: flex;">
	<!-- 左侧 -->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;margin-left: 8rpx;">
							<!-- 左侧的内容 4层 -->
							<!-- 图 -->
							<view style="width: 100%;display: flex;justify-content: center;">
									<image style="width: 280rpx;height: 330rpx;" src="../static/book/e33e322rf.jpg"></image>
							</view>
							<!-- 标题 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								<text>美国商法</text>
							</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							自营</view>	
						<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
						border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
						line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
						margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
						包邮</view>
							<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
							border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
							line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
							margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
							领券</view>
					
							<!-- 价格 -->
							<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
								￥152
							</view>
							<!-- 找相似 -->
							<view>
								<view style="font-size: 20rpx;color: #808080;position: relative;
								left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
								border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
								text-align: center;height:30rpx;line-height: 30rpx;">
									找相似
								</view>
							</view>
	
	</view>
	
	<!-- 中间空白 -->
	<view style="width: 8rpx;height: 500rpx;background-color: #f2f2f3;">
		
	</view>
	
	<!-- 右侧 .-->
	<view style="width: 363rpx;height: 500rpx;border-radius: 10rpx;background-color: #ffffff;">
			<!-- 左侧的内容 4层 -->
				<!-- 图 -->
				<view style="width: 100%;display: flex;justify-content: center;">
						<image style="width: 280rpx;height: 330rpx;" src="../static/book/sadfasd.jpg"></image>
				</view>
				<!-- 标题 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					<text>本草纲目</text>
				</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 35rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				自营</view>	
			<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
			border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
			line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
			margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
			包邮</view>
				<view style="border-width: 1rpx;border-color: #ff2d51;border-style: solid;
				border-radius: 5rpx;font-size: 20rpx;color:#ff2d51 ;display: inline;height: 20rpx;
				line-height: 15rpx;display:inline-flex;justify-content: center;align-items: center;
				margin-left: 10rpx;padding-top: 3rpx;padding-bottom: 3rpx">
				领券</view>
								
				<!-- 价格 -->
				<view style="margin-left: 35rpx;font-weight: bold;margin-top: 15rpx;">
					￥41
				</view>
				<!-- 找相似 -->
				<view>
					<view style="font-size: 20rpx;color: #808080;position: relative;
					left: 250rpx;top: -38rpx;border-style: solid;border-color: #808080;
					border-radius: 5rpx;border-width: 1rpx;display:inline-block;width: 70rpx;
					text-align: center;height:30rpx;line-height: 30rpx;">
						找相似
					</view>
				</view>
				
	<!-- 右侧完成 -->		
	</view>
	
</view>
<!-- 第一对商品结束 -->	


























		
		
		
		
		
	</view>
</template>

<script>
	//import uniTag from "@/components/uni-tag/uni-tag.vue"
	export default {
		data(){
			return{
				
			}
		},
		//components: {uniTag}
	}
</script>

<style scoped>
.bimage{
	height: 84rpx;width: 400rpx;
}
.btitle{
	height: 100rpx;width: 750rpx;background-color: #f3f3f3;
	display: flex;justify-content: center;align-items: center;
}
</style>