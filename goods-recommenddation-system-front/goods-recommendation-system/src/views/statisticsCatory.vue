<script setup>
import * as echarts from 'echarts'
import {onMounted, reactive} from "vue";
import request from "@/utils/request";

const state = reactive({
  })

onMounted(() => {
  //获取数量



  let categoryGoodsStatisOption = {
    title: {
      text: '不同分类的商品数量',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    series: [
      {
        type: 'pie',
        radius: '50%',
        data: [],
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
        }
      }
    ]
  };
  let chart_categoryGoodsStatis = echarts.init(document.getElementById("chart_categoryGoodsStatis"))
  request.get('/core/statistics/categoryGoodsStatis').then(res => {
    categoryGoodsStatisOption.series[0].data = res.data
    // 绘制图表
    chart_categoryGoodsStatis.setOption(categoryGoodsStatisOption)
  })







  let categorySalesStatisOption = {
    title: {
      text: '不同分类的商品的总销售量',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    xAxis: {
      type: 'category',
      data: []
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [],
        type: 'bar',
        itemStyle: {
          color: function() {
            var letters = "0123456789ABCDEF";
            var color = "#";
            for (var i = 0; i < 6; i++) {
              color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
          }
        }
      }
    ]
  };
  let chart_categorySalesStatis = echarts.init(document.getElementById("chart_categorySalesStatis"))
  request.get('/core/statistics/categorySalesStatis').then(res => {
    categorySalesStatisOption.series[0].data = res.data.map(v => v.value)
    categorySalesStatisOption.xAxis.data = res.data.map(v => v.name)
    // 绘制图表
    chart_categorySalesStatis.setOption(categorySalesStatisOption)
  })






  let categoryPriceStatisOption = {
    title: {
      text: '不同分类的商品的平均价格',
      left: 'center'
    },
    tooltip: {
      trigger: 'item'
    },
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    xAxis: {
      type: 'category',
      data: []
    },
    yAxis: {
      type: 'value'
    },
    series: [
      {
        data: [],
        type: 'bar',
        itemStyle: {
          color: function() {
            var letters = "0123456789ABCDEF";
            var color = "#";
            for (var i = 0; i < 6; i++) {
              color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
          }
        }
      }
    ]
  };
  let chart_categoryPriceStatis = echarts.init(document.getElementById("chart_categoryPriceStatis"))
  request.get('/core/statistics/categoryPriceStatis').then(res => {
    categoryPriceStatisOption.series[0].data = res.data.map(v => v.value)
    categoryPriceStatisOption.xAxis.data = res.data.map(v => v.name)
    // 绘制图表
    chart_categoryPriceStatis.setOption(categoryPriceStatisOption)
  })




})
</script>

<template>
  <div style="background-color: #ffffff;padding: 10px;border-radius: 10px;margin-top: 20px;">
    <div>
      <el-row :gutter="10">

      </el-row>
    </div>

    <div style="margin: 20px 0;">
      <el-row :gutter="10">

        <el-col :span="24">
          <div style="width:100%; height: 500px" id="chart_categoryGoodsStatis"></div>
        </el-col>
        <el-col :span="24">
          <div style="width:100%; height: 500px" id="chart_categorySalesStatis"></div>
        </el-col>
        <el-col :span="24">
          <div style="width:100%; height: 500px" id="chart_categoryPriceStatis"></div>
        </el-col>
      </el-row>
    </div>


  </div>
</template>
