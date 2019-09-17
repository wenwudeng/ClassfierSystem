<template>
  <div style="text-align: center;margin-top: 30px">
    <br>
    <div>
      <el-select v-model="url_value" placeholder="请选择">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value">
         </el-option>
      </el-select>
      <el-input v-model="word" placeholder="请输入爬取的内容" style="width: 200px"></el-input>
      <el-date-picker
        v-model="time_value"
        value-format="yyyy-MM-dd"
        type="daterange"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期">
      </el-date-picker>
      <el-button type="primary" @click="reptile">爬虫</el-button>
    </div>

    <div clas="outer" style="text-align: center">
       <!--图片显示-->
      <el-row :gutter="20">
        <el-col :span="6" v-for="img in this.img_list" :key="img">
          <el-image
            style="width: 300px;height:250px;margin-top: 20px"
            :src='img'
          >
          </el-image>
        </el-col>
      </el-row>
      <!-- <div v-for="img in this.img_list" :key="img">
        <img :src="img">
      </div> -->
    </div>
  </div>
</template>

<script>
export default {
  name: "Reptile",
  data(){
    return{
      img_list: [],
      word: '',
      url_value: '',
      options: [{
          value: '1',
          label: '百度'
        }, {
          value: '2',
          label: '搜狗'
        }, {
          value: '3',
          label: 'bing'
        }],
        value: '',
        time_value: ''
    };
  },

  methods: {
    reptile(){
      console.log(this.word);
      this.$axios
      .post('/reptile/', {
        url_value: this.url_value,
        word: this.word,
        time_value: this.time_value,
      })
      .then(response => {

      })
      .catch(error => {});

    },
    test() {
      this.$axios
      .post('/test/', {
        time_value: this.time_value,
      });
      console.log(this.time_value);
    }
  },

  created() {
    this.$axios
      .post('/get_img/', {
      })
      .then(response => {
        var temp = [];
        temp =  response.data.img_local;
        console.log(temp);
        for(var i = 0; i < temp.length; i++){
          console.log(require("../../assets/img/" + temp[i]));
          this.img_list.push(require("../../assets/img/" + temp[i]));
        }
      })
      .catch(error => {});
  },


}
</script>

<style>

</style>
