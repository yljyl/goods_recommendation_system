<script setup>
import * as echarts from 'echarts/core'
import 'echarts-wordcloud'
import { onMounted } from 'vue'
import request from "@/utils/request";

onMounted(() => {
  init()
})


const init = () => {
  request.get('/core/front/wordcloud').then(res => {
    const data = res.data

    var myChart = echarts.init(document.getElementById('wordCloud'))

  const option = {
    series: [
      {
        type: 'wordCloud',
        // 要绘制云的形状,默认是 circle，可选的参数有 cardioid 、 diamond 、 triangle-forward 、 triangle 、 star
        shape: 'circle',
        keepAspect: false,
        left: 'center',
        top: 'center',
        width: '100%',
        height: '80%',
        right: null,
        bottom: null,
        sizeRange: [24, 100],
        rotationRange: [-90, 90],
        rotationStep: 45,
        gridSize: 8,
        drawOutOfBound: false,
        shrinkToFit: false,
        layoutAnimation: true,

        // 全局文本样式
        textStyle: {
          fontFamily: 'sans-serif',
          fontWeight: 'bold',
          // Color可以是回调函数或颜色字符串
          color: function () {
            // 任意颜色
            return (
              'rgb(' +
              [
                Math.round(Math.random() * 160),
                Math.round(Math.random() * 160),
                Math.round(Math.random() * 160),
              ].join(',') +
              ')'
            )
          },
        },
        emphasis: {
          focus: 'self',
          textStyle: {
            textShadowBlur: 10,
            textShadowColor: '#333',
          },
        },
        data: data,
      },
    ],
  }
  myChart.setOption(option)
  })
  
}

</script>

<template>
  <div style="background-color: white;width: 80%;height: 600px;margin: 0 auto;opacity: 0.7;">
    <h3 style="font-size: 26px;text-align: center;font-weight: bold;">词云分析</h3>
    <div id="wordCloud" style="width: 500px; height: 500px;margin: 0 auto;"></div>
  </div>
</template>