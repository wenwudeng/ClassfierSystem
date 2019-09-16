<template>
  <div clas="outer" style="text-align: center">
    <!--图片显示-->
    <el-row :gutter="20">
      <el-col :span="6" v-for="(i,index) in srcList" :key="index">
        <el-image
          style="width: 300px;height:250px;margin-top: 20px"
          :src='i.url'
        >
        </el-image>
        <div style="margin-top: 3px">
          <!--选择器-->
          <el-select v-model="i.sign" clearable placeholder="请选择" style="margin-left: 30px">
            <el-option v-for="(item,index) in items" :key="index" :value="item"></el-option>
          </el-select>
        </div>
      </el-col>
        <el-button type="primary" style="margin-top: 30px;width: 400px" >提交</el-button>
    </el-row>



  </div>
</template>

<script>
  export default {
    data() {
      return {
        srcList:
          [{url: 'https://fuss10.elemecdn.com/e/5d/4a731a90594a4af544c0c25941171jpeg.jpeg', sign: null},
            {url: 'https://fuss10.elemecdn.com/1/8e/aeffeb4de74e2fde4bd74fc7b4486jpeg.jpeg', sign: null},
            {url: 'http://ask.qcloudimg.com/article-cover-image/1065788/y98nuaaxl2.png', sign: null},
            {url: 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3647170051,871438825&fm=26&gp=0.jpg'},
            {url: 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3647170051,871438825&fm=26&gp=0.jpg'},
            {url: 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3647170051,871438825&fm=26&gp=0.jpg'},
            {url: 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3647170051,871438825&fm=26&gp=0.jpg'},
            {url: 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3647170051,871438825&fm=26&gp=0.jpg'},],
        items: ['是', '不是'],
        value: ''
      };
    },
    methods: {}

  }
</script>

<style>


</style>
