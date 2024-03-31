<script setup>
import * as echarts from 'echarts'
import {onMounted, reactive} from "vue";
import request from "@/utils/request";

const state = reactive({
  })

onMounted(() => {
  //获取数量



  let provinceCountStatisOption = {
    title: {
      text: '各个省份商品数量统计',
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
  let chart_provinceCountStatis = echarts.init(document.getElementById("chart_provinceCountStatis"))
  request.get('/core/statistics/provinceCountStatis').then(res => {
    provinceCountStatisOption.series[0].data = res.data
    // 绘制图表
    chart_provinceCountStatis.setOption(provinceCountStatisOption)
  })







  let provinceSalesStatisOption = {
    title: {
      text: '各个省份商品总销售量统计',
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
  let chart_provinceSalesStatis = echarts.init(document.getElementById("chart_provinceSalesStatis"))
  request.get('/core/statistics/provinceSalesStatis').then(res => {
    provinceSalesStatisOption.series[0].data = res.data.map(v => v.value)
    provinceSalesStatisOption.xAxis.data = res.data.map(v => v.name)
    // 绘制图表
    chart_provinceSalesStatis.setOption(provinceSalesStatisOption)
  })






  let provincePriceStatisOption = {
    title: {
      text: '各个省份商品平均价格统计',
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
  let chart_provincePriceStatis = echarts.init(document.getElementById("chart_provincePriceStatis"))
  request.get('/core/statistics/provincePriceStatis').then(res => {
    provincePriceStatisOption.series[0].data = res.data.map(v => v.value)
    provincePriceStatisOption.xAxis.data = res.data.map(v => v.name)
    // 绘制图表
    chart_provincePriceStatis.setOption(provincePriceStatisOption)
  })






  let provinceTopSalesStatisOption = {
    title: {
      text: '商品销量前10名省份统计',
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
  let chart_provinceTopSalesStatis = echarts.init(document.getElementById("chart_provinceTopSalesStatis"))
  request.get('/core/statistics/provinceTopSalesStatis').then(res => {
    provinceTopSalesStatisOption.series[0].data = res.data.map(v => v.value)
    provinceTopSalesStatisOption.xAxis.data = res.data.map(v => v.name)
    // 绘制图表
    chart_provinceTopSalesStatis.setOption(provinceTopSalesStatisOption)
  })






  let cityTopSalesStatisOption = {
    title: {
      text: '商品销量前10名城市统计',
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
  let chart_cityTopSalesStatis = echarts.init(document.getElementById("chart_cityTopSalesStatis"))
  request.get('/core/statistics/cityTopSalesStatis').then(res => {
    cityTopSalesStatisOption.series[0].data = res.data.map(v => v.value)
    cityTopSalesStatisOption.xAxis.data = res.data.map(v => v.name)
    // 绘制图表
    chart_cityTopSalesStatis.setOption(cityTopSalesStatisOption)
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
          <div style="width:100%; height: 500px" id="chart_provinceCountStatis"></div>
        </el-col>
        <el-col :span="24">
          <div style="width:100%; height: 500px" id="chart_provinceSalesStatis"></div>
        </el-col>
        <el-col :span="24">
          <div style="width:100%; height: 500px" id="chart_provincePriceStatis"></div>
        </el-col>
        <el-col :span="24">
          <div style="width:100%; height: 500px" id="chart_provinceTopSalesStatis"></div>
        </el-col>
        <el-col :span="24">
          <div style="width:100%; height: 500px" id="chart_cityTopSalesStatis"></div>
        </el-col>
      </el-row>
    </div>


  </div>
</template>
