<template>
  <div>
    <div>爬虫</div>
    <div>
      <select v-model="url_value">
        <option value="1">百度</option>
        <option value="2">搜狗</option>
      </select>
      <input v-model="word"/>
      <button @click="reptile">爬虫</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "Reptile",
  data(){
    return{
      img_list: [],
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

      })
      .catch(error => {});

    }
  }
}
</script>

<style>

</style>