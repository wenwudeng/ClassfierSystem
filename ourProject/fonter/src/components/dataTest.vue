<template>
    <div class="about">
        <h1>this is a test</h1>
      {{d2}}
      拉拉
      <p v-for="d in dl">
        {{d}}
      </p>
      <button @click="init">点击获取数据</button>
    </div>
</template>

<script>
    export default {
        name: "dataTest",
        data:function () {
          return{
            dl:['ABC','CDE'],
            d2:'默认'
          }
        },
        methods:{
            init:function () {
              let _this=this
                this.$http.request({
                  url:_this.$url+'data/',
                  method:'get',
                }).then(function (response) {
                  _this.dl=response.data
                  console.log("shuju",response)
                }).catch(function (response) {
                  console.log("shuju",response)
                })
            }
      }
    }
</script>

<style scoped>

</style>
