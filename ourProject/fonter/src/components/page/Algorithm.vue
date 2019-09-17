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
    <div class="result-compare">
      <ve-histogram :data="chartData" :settings="chartSettings"></ve-histogram>
    </div>
  </div>
</template>

<script>
export default {
  data () {
     this.chartSettings = {

     }
     return {
       radio: 1,
       acc1:0,
       acc2:0,
       acc3:0,
       acc4:0,
       time1:0,
       time2:0,
       time3:0,
       time4:0,
         chartData: {
           columns: ['算法', '准确度','时间'],
           rows: [
             // {'算法': '算法一', '准确度': this.acc1, '时间':this.time1},
             // {'算法': '算法二', '准确度': this.acc2, '时间':time.time2},
             // {'算法': '算法三', '准确度': this.acc3, '时间':this.time3},
             // {'算法': '算法四', '准确度': this.acc4, '时间':this.time4},
             {'算法': '算法一', '准确度': 0.9, '时间':54},
             {'算法': '算法二', '准确度': 0.7, '时间':42},
             {'算法': '算法三', '准确度': 0.85, '时间':49},
             {'算法': '算法四', '准确度': 0.88, '时间':67},
           ]
         }
       }
  },
  methods:{
    show(){
      alert(this.radio)
    }
  },


}
</script>
<style>
.select-algorithm{
  padding-top: 40px;
  height: 150px;
  text-align: center;
  border-bottom: 1px dashed #8c939d;
}
 .test-btn{
   margin-top: 30px;
 }
  .result-compare{
    margin: 50px auto;
    width: 700px;
    height: 400px;
  }
</style>
