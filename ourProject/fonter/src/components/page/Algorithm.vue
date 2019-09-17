<template>
  <div class="algorithm">
    <div class="select-algorithm">
      <el-radio-group v-model="radio"  size="medium ">
        <el-radio :label="1">算法一</el-radio>
        <el-radio :label="2">算法二</el-radio>
        <el-radio :label="3">算法三</el-radio>
        <el-radio :label="4">算法四</el-radio>
      </el-radio-group>
      <div class="test-btn">
       <el-button type="primary" @click="show()">算法测试</el-button>
      </div>
    </div>
    <div>
       <chart ref="chart1" :options="orgOptions" :auto-resize="true"></chart>
    </div>
  </div>
</template>

<script>
export default {
  data () {
      return {
        radio: 1,
      orgOptions: {}
      };
    },
  methods:{
    show(){
      alert(this.radio)
    }
  },
  mounted() {
    this.orgOptions = {
        xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        yAxis: {
            type: 'value'
        },
        series: [{
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line',
            smooth: true
        }]
    }
  }

}
</script>
<style>
.select-algorithm{
  padding-top: 40px;
  height: 200px;
  text-align: center;
  border-bottom: 1px dashed #8c939d;
}
 .test-btn{
   margin-top: 30px;
 }
</style>
