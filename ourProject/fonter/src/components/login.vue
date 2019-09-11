<template>
  <div>
    <vue-particles style="background:#f4f5f5;position:fixed;width:100%;height:100%;"></vue-particles>
    <div class="fullscreen">
      <div class="login-box" style="margin-top:-10px">
        <div style="text-align: center">
          <img src="../assets/logo.png" alt class="logo" />
        </div>
        <transition name="el-zoom-in-center" :duration="350">
          <div v-if="boxType">
            <p class="text-tips">你好，欢迎登录</p>
            <el-form :model="loginForm">
              <el-form-item prop="username">
                <el-input
                  type="text"
                  placeholder="请输入用户名或手机号"
                  v-model="loginForm.username"
                  clearable
                ></el-input>
              </el-form-item>
              <el-form-item prop="password" style="margin-top:-15px">
                <el-input
                  type="password"
                  placeholder="请输入密码"
                  v-model="loginForm.password"
                  clearable
                ></el-input>
              </el-form-item>
              <el-button class="m-btn sub select-none" @click="login" v-loading="isLoging">登录</el-button>
              <p class="text-tips">
                <a href @click.prevent="boxType = !boxType">没有账号？点击注册</a>
              </p>
            </el-form>
          </div>
        </transition>
        <transition name="el-zoom-in-center" :duration="350">
          <div v-if="!boxType">
            <p class="text-tips">你好，欢迎注册</p>
            <el-form :model="loginForm">
              <el-form-item prop="username">
                <el-input
                  type="text"
                  placeholder="请输入用户名或手机号"
                  v-model="loginForm.username"
                  clearable
                ></el-input>
              </el-form-item>
              <el-form-item prop="password" style="margin-top:-15px">
                <el-input
                  type="password"
                  placeholder="请输入密码"
                  v-model="loginForm.password"
                  clearable
                ></el-input>
              </el-form-item>
              <el-button class="m-btn sub select-none" @click="register" v-loading="isLoging">注册</el-button>
              <p class="text-tips">
                <a href @click.prevent="boxType = !boxType">已有账号？点击登录</a>
              </p>
            </el-form>
          </div>
        </transition>
        <div style="margin-top: 50px"></div>
        <p class="text-tips">
          <span class="footer-text">©make by Team 9</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "login",
  data() {
    return {
      loginForm: {
        username: "admin",
        password: "123"
      },
      isLoging: false,
      // boxType为true显示登录，false显示注册界面
      boxType: true
    };
  },

  methods: {
    login() {
      if (!this.loginForm.username || !this.loginForm.password) {
        return this.$message.warning("用户名和密码不能为空");
      }
      this.isLoging = true;

      this.$axios
        .post("/login/", {
          username: this.loginForm.username,
          password: this.loginForm.password
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
    },
    register() {
      if (!this.loginForm.username || !this.loginForm.password) {
        return this.$message.warning("用户名和密码不能为空");
      }
      this.isLoging = true;

      this.$axios
        .post("/register/", {
          username: this.loginForm.username,
          password: this.loginForm.password
        })
        .then(response => {
          if (response.data.errno === 200) {
            this.$message.success(response.data.msg);
            this.$router.push({
              path: "/login"
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
  /* background: #f4f5f5; */
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
  font-size: 15px;
  width: 100%;
  color: #fff;
  background-color: rgb(64, 158, 255);
  display: inline-block;
  padding: 10px 12px;
  margin-bottom: 5px;
  line-height: 1.42857143;
  text-align: center;
  cursor: pointer;
  outline: none;
  border-radius: 2px;
  border: 1px solid rgb(64, 158, 255);
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
