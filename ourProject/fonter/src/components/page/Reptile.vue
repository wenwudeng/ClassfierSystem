<template>
  <div>
    <div>爬虫</div>
    <div>
      <select v-model="url_value">
        <option value="1" default>百度</option>
        <option value="2">搜狗</option>
      </select>
      <input v-model="word"/>
      <button @click="reptile">爬虫</button>
    </div>
    <div v-for="img in this.img_list" :key="img">
      <img :src="img">
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
    };
  },

  methods: {
    reptile(){
      console.log(this.word);
      this.$axios
      .post('/reptile/', {
        url_value: this.url_value,
        word: this.word
      })
      .then(response => {
        var temp = [];
        temp =  response.data.img_local;
        for(var i = 0; i < temp.length; i++){
          console.log(require("../../assets/img/" + temp[i]));
          this.img_list.push(require("../../assets/img/" + temp[i]));
        }
      })
      .catch(error => {});

    }
  },

  created() {
    // this.$axios
    //   .post('/reptile/', {
    //     url_value: 1,
    //     word: "羊"
    //   })
    //   .then(response => {
    //     var temp = [];
    //     temp =  response.data.img_local;
    //     for(var i = 0; i < temp.length; i++){
    //       console.log(require("../../assets/img/" + temp[i]));
    //       this.img_list.push(require("../../assets/img/" + temp[i]));
    //     }
    //   })
    //   .catch(error => {});
  }
}
</script>

<style>

</style>