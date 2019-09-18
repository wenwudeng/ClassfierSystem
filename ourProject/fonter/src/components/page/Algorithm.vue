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
        <el-button type="warning" @click="cleanTest()">清空测试结果</el-button>

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
       algorithmName:"",
       acc1:0.8,
       acc2:0,
       acc3:0,
       acc4:0,
       time1:57,
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
             // {'算法': '算法一', '准确度': 0.9, '时间':54},
             // {'算法': '算法二', '准确度': 0.7, '时间':42},
             // {'算法': '算法三', '准确度': 0.85, '时间':49},
             // {'算法': '算法四', '准确度': 0.88, '时间':67},
            ]
         }
       }
  },
  methods:{
    show(){
      if(this.radio == 1){
        this.algorithmName = '算法一'
        this.$axios
          .get('/cnnTest/',{})
          .then(data =>{
            if (data.data !==null){
              let algorithmPerf={}
              this.$set(algorithmPerf,'算法',this.algorithmName)
              this.$set(algorithmPerf,'准确度',data.data.acc)
              this.$set(algorithmPerf,'时间',data.data.runtime)
              this.chartData.rows.push(algorithmPerf)
              this.$message({
                message: '测试结果已展示',
                type: 'success'
              });
            }
            else {
              this.$message({
                showClose: true,
                message: '算法测试出错，请重试',
                type: 'error'
              });
            }
          })
      }
      else if(this.radio == 2){
        this.algorithmName = '算法二'
        this.$axios
          .get('/knnTest/',{})
          .then(data =>{
            if (data.data !==null){
              let algorithmPerf={}
              this.$set(algorithmPerf,'算法',this.algorithmName)
              this.$set(algorithmPerf,'准确度',data.data.acc)
              this.$set(algorithmPerf,'时间',data.data.runtime)
              this.chartData.rows.push(algorithmPerf)
              this.$message({
                message: '测试结果已展示',
                type: 'success'
              });
            }
            else {
              this.$message({
                showClose: true,
                message: '算法测试出错，请重试',
                type: 'error'
              });
            }
          })
      }
      else if(this.radio == 3){
        this.algorithmName = '算法三'
        this.$axios
          .get('/bpTest/',{})
          .then(data =>{
            if (data.data !==null){
              let algorithmPerf={}
              this.$set(algorithmPerf,'算法',this.algorithmName)
              this.$set(algorithmPerf,'准确度',data.data.acc)
              this.$set(algorithmPerf,'时间',data.data.runtime)
              this.chartData.rows.push(algorithmPerf)
              this.$message({
                message: '测试结果已展示',
                type: 'success'
              });
            }
            else {
              this.$message({
                showClose: true,
                message: '算法测试出错，请重试',
                type: 'error'
              });
            }
          })
      }
      else if(this.radio == 4){
        this.algorithmName = '算法四'
      }

    },
    cleanTest(){
      this.$message({
          message: '测试结果已清空',
          type: 'success'
        });
      this.chartData.rows=[]
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
