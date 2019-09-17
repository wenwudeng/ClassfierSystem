<template>
  <div clas="outer" style="text-align: center">
    <!--图片显示-->
    <el-row :gutter="20">
      <el-col :span="6" v-for="(i,index) in srcList1" :key="index">
        <el-image
          style="width: 300px;height:250px;margin-top: 20px"
          :src="require('@/assets/img/'+i.img)"
        >
        </el-image>
        <div style="margin-top: 3px">
          <!--选择器-->
          <el-select v-model="i.isTrue" clearable placeholder="请选择" style="margin-left: 30px">
            <el-option v-for="(item,index) in items" :key="index" :value="item"></el-option>
          </el-select>
        </div>
      </el-col>
      <el-button type="primary" style="margin-top: 30px;width: 400px" @click="submit">提交</el-button>
    </el-row>


  </div>
</template>

<script>
  export default {
    data() {
      return {
        srcList1: [],
        items: ['True', 'False'],
      };
    },
    methods: {
      /*后台传送修改值*/
      submit() {
        this.$axios
          .post('/transData/', {
            result: this.srcList1
          })
          .then(response => {
            this.srcList1 = response.data.img
            this.$message.success("提交成功");
            this.getData()
          })
          .catch(error => {
          });
      },

      getData() {
        this.$axios
          .post('/getImage/')
          .then(response => {
            this.srcList1 = response.data.img
          })
          .catch(error => {
          });
      }
    },

    /*加载页面之前先获取后台数据*/
    created() {
      /*获取数据库地图片址*/
      this.getData()
    }

  }
</script>

<style>


</style>
