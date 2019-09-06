<template>
  <div id="classify">
    <div class="upload">
      <el-upload
        class="avatar-uploader"
        action="https://jsonplaceholder.typicode.com/posts/"
        :show-file-list="false"
        :on-success="handleAvatarSuccess"
        :before-upload="beforeAvatarUpload">
        <img v-if="imageUrl" :src="require('@/assets/'+imageUrl)" class="avatar">
        <i v-else class="el-icon-plus avatar-uploader-icon"></i>
      </el-upload>
      <el-button class="img_upload" type="primary" @click="goSort()" :disabled="this.imageUrl==''?true:false">开始分类</el-button>
    </div>
    <div class="result-display" :style="this.imageUrl==''?hidden_result:show_result">
        <el-row style="width: 430px">
        <el-col :span="24" >
          <el-card :body-style="{ padding: '0px' }" style="height: 433px;width: 430px">
            <img  :src="this.imageUrl==''?require('@/assets/logo.png'):require('@/assets/'+imageUrl)" class="image">
            <div style="padding: 14px;">
              <span style="color: #ED5A25;">分类结果：{{this.sort_result}}</span>
              <div class="bottom clearfix">
                <time class="time">{{ currentDate }}</time>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script>
export default {
  name:"classify",
  data(){
    return{
      sort_result:'羊',
      imageUrl: '',
      currentDate: new Date(),
      show_result:{'display':'block'},
      hidden_result:{'display':'none'}
    };
  },
  methods:{
    handleAvatarSuccess(res, file) {
        this.imageUrl = file.name;
      },
      beforeAvatarUpload(file) {
        // const isJPG = file.type === 'image/jpeg';
        const isLt2M = file.size / 1024 / 1024 < 2;

        // if (!isJPG) {
        //   this.$message.error('上传头像图片只能是 JPG 格式!');
        // }
        if (!isLt2M) {
          this.$message.error('上传头像图片大小不能超过 2MB!');
        }
        return isLt2M;
      },
    goSort(){
      alert("分类");
    }
    }
}
</script>

<style>
 .upload{
   height: 250px;
   text-align: center;
   border-bottom: 1px dashed #8c939d;
  }
 .img_upload{
   margin-top: 10px;
 }
.avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
  .result-display{
    width: 430px;
    margin: 5px auto;
    text-align: center;
  }
  .time {
    font-size: 13px;
    color: #999;
  }

  .bottom {
    margin-top: 13px;
    line-height: 12px;
  }

  .button {
    padding: 0;
    float: right;
  }

  .image {
    width: 425px;
    height: 360px;
    display: block;
    margin:  0 auto;
  }

  .clearfix:before, .clearfix:after {
      display: table;
      content: "";
  }

  .clearfix:after {
      clear: both
  }
</style>
