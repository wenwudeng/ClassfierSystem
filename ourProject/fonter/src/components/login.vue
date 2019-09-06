<template>
  <div class="fullscreen">
    <div class="login-box">
      <div style="text-align: center">
        <img src="../assets/logo.png" alt class="logo" />
      </div>
      <p class="text-tips">你好，欢迎登录</p>
      <form action>
        <el-input type="text" placeholder="Username" v-model="username"></el-input>
        <el-input type="password" placeholder="Password" v-model="password" style="margin-top:5px"></el-input>
        <p class="text-tips">免密码，点击登录按钮进入</p>
        <el-button
          class="m-btn sub select-none"
          @click.prevent="handleLogin"
          v-loading="isLoging"
        >登录</el-button>
      </form>
      <div style="margin-top: 50px"></div>
      <p class="text-tips">
        <span class="footer-text">©make by Team 9</span>
        <!-- <router-link to="/test">路由测试</router-link> -->
      </p>
    </div>
  </div>
</template>
<script>
export default {
  name: "login",
  data() {
    return {
      username: "admin",
      password: "123",
      isLoging: false
    };
  },
  methods: {
    handleLogin() {
      if (!this.username || !this.password) {
        return this.$message.warning("用户名和密码不能为空");
      }
      this.isLoging = true;

      this.$axios
        .post("/login/", {
          username: this.username,
          password: this.password
        })
        .then(response => {
          if (response.data.errno === 200) {
            this.$message.success(response.data.msg);
            this.$router.push({
              path: "/home"
            });
          } else {
            this.$message.error(response.data.msg);
          }
          this.isLoging = false;
        })
        .catch(error => {});
    }
  }
};
</script>

<style>
.m-list-group {
  border-radius: 3px;
  padding: 0;
  margin: 0 0 20px;
}
.m-list-group .m-list-group-item {
  position: relative;
  display: block;
  padding: 6px 10px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #e7ecee;
}
.m-list-group .m-list-group-item:first-child {
  border-top-left-radius: 3px;
  border-top-right-radius: 3px;
}
.m-list-group .m-list-group-item:last-child {
  border-bottom-left-radius: 3px;
  border-bottom-right-radius: 3px;
}
.fullscreen {
  position: absolute;
  width: 100%;
  height: 100%;
  background: #f4f5f5;
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-box {
  position: relative;
  width: 330px;
  margin: 0 auto;
  padding: 0px 15px;
}
.login-box .logo {
  max-width: 40%;
  margin-bottom: 30px;
}
.login-box .text-tips {
  text-align: center;
  color: #909db7;
}
.login-box .m-input {
  width: 100%;
  padding: 10px;
  border: none;
  outline: none;
  box-sizing: border-box;
}
.login-box .m-btn {
  font-size: 18px;
  width: 100%;
  color: #fff;
  background-color: #36c1fa;
  display: inline-block;
  padding: 10px 12px;
  margin-bottom: 5px;
  line-height: 1.42857143;
  text-align: center;
  cursor: pointer;
  outline: none;
  border-radius: 2px;
  border: 1px solid #36c1fa;
  box-sizing: border-box;
  text-decoration: none;
}
.login-box .m-btn.m-btn-text {
  background: #fff;
  color: #36c1fa;
}
.login-box .m-btn:hover {
  background-color: #2db7f5;
}
.login-box .m-btn.m-btn-text:hover {
  background-color: #f4f5f5;
}
.login-box .m-btn:active {
  opacity: 0.8;
}
@media (max-width: 768px) {
  .login-box {
    width: auto;
  }
}
</style>
