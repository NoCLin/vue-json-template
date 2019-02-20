<template>
    <div class="container">
        <div v-if="name">
            <div class="sidebar">
                <div class="title">
                    <img src="__DIR__/img/resume-head.jpg">
                    <h1>{{name}}</h1>
                    <h2>{{slogan}}</h2>
                </div>
                <ul class="side-info">
                    <li class="someRight">
                        <dt><i class="icon-bookmark"></i>Contact. 联系方式</dt>
                        <dd><i class="icon-phone-1"></i>
                            {{contact.cellphone}}
                        </dd>
                        <dd v-if="contact.email">
                            <i class="icon-mail-alt"></i>
                            {{contact.email}}
                        </dd>
                        <dd v-if="contact.wechat">
                            <i class="icon-wechat"></i>
                            {{contact.wechat}}
                        </dd>
                        <dd v-if="contact.qq">
                            <i class="icon-qq"></i>
                            {{contact.qq}}
                        </dd>
                    </li>
                    <li class="someRight">
                        <dt><i class="icon-bookmark"></i>Application. 应聘岗位</dt>
                        <dd>{{this["apply-position"]}}</dd>
                    </li>
                </ul>
                <div class="note" v-html="markdown_render(note)">
                </div>
            </div>
            <div class="main">
                <ul class="main-info">
                    <li class="someRight">
                        <dt><i class="icon-bookmark"></i>Basic info. 基本信息</dt>
                        <dd><strong>{{name}} / {{gender}} / {{birth}}</strong></dd>
                        <dd><strong>毕业院校:</strong> <span>{{school}}</span></dd>
                        <dd v-if="contact.blog">
                            <strong>博客:</strong>
                            <a :href="contact.blog" target="_blank">{{contact.blog}}</a>
                        </dd>
                        <dd v-if="contact.github">
                            <strong>GitHub:</strong>
                            <a :href="'https://github.com/'+contact.github" target="_blank">@{{contact.github}}</a>
                        </dd>
                    </li>
                    <li>
                        <dt><i class="icon-bookmark"></i>Education. 教育背景</dt>
                        <div>
                            <ul class="exp">
                                <li v-for="education in educations">
                                    <div class="circle"></div>
                                    <h4>{{education.school}}</h4>
                                    <p v-html="markdown_render(education.info)"></p>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li>
                        <dt><i class="icon-bookmark"></i>Experience. 项目与工作经验</dt>
                        <div v-for="exp in exps">
                            <h3>
                                <img v-if="exp.img" :src="exp.img">
                                <span v-html="markdown_render(exp.company)"></span>
                            </h3>
                            <h3><span>{{exp.info}}</span></h3>
                            <ul class="exp">
                                <li v-for="project in exp.projects">
                                    <div class="circle"></div>
                                    <h4>
                                        <span>{{project.name}}</span>
                                        <a v-if="project.code" :href="project.code" target="_blank"><i
                                                class="icon-link"></i>源代码</a>
                                        <a v-if="project.demo" :href="project.demo" target="_blank"><i
                                                class="icon-link"></i>Demo</a>
                                    </h4>
                                    <p v-html="markdown_render(project.info)"></p>
                                </li>
                            </ul>
                        </div>
                    </li>
                    <li>
                        <dt><i class="icon-bookmark"></i>Skill. 技能清单</dt>
                        <ul class="exp">
                            <li v-for="skill in skills">
                                <div class="circle"></div>
                                <p v-html="markdown_render(skill.info)"></p>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        <div v-else>
            加载错误
        </div>
    </div>
</template>

<script>
    export default {
      methods: {
        markdown_render (arg) {
          // eslint-disable-next-line no-undef
          return marked((arg instanceof Array) ? arg.reduce((total, str) => total + str) : arg)
        }
      },
      filters: {
        markdown: function (arg) {
          return this.markdown_render(arg)
        }
      },
      // eslint-disable-next-line no-undef
      data: () => (Object.assign(DATA_INJECT_HERE,
        {}
      ))
    }
</script>

<style>
    .sidebar, .sidebar a, aside a {
        color: #fff
    }

    .main-info dd a, .main-info dd span, .main-info dd strong, h3 img, h3 span, h4 a, h4 span, iframe {
        vertical-align: middle
    }

    .title, footer p {
        text-align: center
    }

    * {
        margin: 0;
        padding: 0
    }

    body {
        background: #eee;
        font-family: PingFang TC, Avenir Next, Helvetica, Arial, Hiragino Sans GB, Microsoft YaHei, sans-serif;
        min-width: 1080px
    }

    li, ul {
        list-style: none
    }

    a {
        text-decoration: none
    }

    dd, dt, h1, h2, h3, h4, h5, p {
        cursor: default
    }

    aside {
        position: fixed;
        right: 0;
        top: 30%;
        z-index: 2
    }

    aside li {
        margin-bottom: 10px;
        -webkit-border-radius: 10px 0 0 10px;
        border-radius: 10px 0 0 10px;
        background: #00A1D6;
        -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14), 0 3px 1px -2px rgba(0, 0, 0, .2), 0 1px 5px 0 rgba(0, 0, 0, .12);
        box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14), 0 3px 1px -2px rgba(0, 0, 0, .2), 0 1px 5px 0 rgba(0, 0, 0, .12)
    }

    aside a {
        display: inline-block;
        width: 80px;
        height: 38px;
        line-height: 38px;
        padding-left: 10px
    }

    .container {
        position: relative;
        margin: 10px auto;
        -webkit-box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14), 0 3px 1px -2px rgba(0, 0, 0, .2), 0 1px 5px 0 rgba(0, 0, 0, .12);
        box-shadow: 0 2px 2px 0 rgba(0, 0, 0, .14), 0 3px 1px -2px rgba(0, 0, 0, .2), 0 1px 5px 0 rgba(0, 0, 0, .12);
        width: 1060px;
        overflow: hidden;
        -webkit-border-radius: 4px;
        border-radius: 4px
    }

    .sidebar {
        position: absolute;
        top: 0;
        bottom: 0;
        width: 300px;
        padding: 15px 15px 10000px;
        background: #29B6F6;
        line-height: 1.5;
        -webkit-box-sizing: border-box;
        box-sizing: border-box;
        margin-bottom: -10000px
    }

    .main, .skill, .skill-name, h4 {
        position: relative
    }

    .title {
        margin: 25px 0 20px
    }

    .title img {
        display: block;
        margin: 0 auto 15px;
        width: 120px
    }

    h1 {
        font-size: 28px;
        font-weight: 400
    }

    h2 {
        font-size: 14px
    }

    .side-info li {
        padding-top: 20px
    }

    .side-info dt {
        font-size: 18px;
        color: #fff;
        line-height: 40px
    }

    .side-info dd {
        font-size: 14px;
        line-height: 20px
    }

    .side-info i {
        margin-right: 3px
    }

    .someRight dd {
        margin-left: 25px
    }

    .skill-name {
        width: 100px;
        font-size: 14px;
        display: inline-block;
        left: 25px;
        top: -3px
    }

    .skill-bar-wrap {
        height: 17px;
        width: 150px;
        background: #00A1D6;
        display: inline-block;
        -webkit-border-radius: 20px;
        border-radius: 20px
    }

    .skill-bar {
        height: 17px;
        background: #fff;
        -webkit-border-radius: 20px 0 0 20px;
        border-radius: 20px 0 0 20px
    }

    .note {
        text-indent: 2em;
        margin-top: 20px;
        color: #01579B;
        font-size: 18px
    }

    .main {
        left: 300px;
        width: 720px;
        padding: 15px 20px 10000px;
        background: #fff;
        margin-bottom: -10000px
    }

    .main a {
        color: #f25d8e
    }

    .main-info > li {
        padding-top: 20px
    }

    .main-info dt {
        font-size: 24px;
        color: #00A1D6;
        line-height: 30px;
        border-bottom: 1px solid #00A1D6;
        margin: 0 0 15px -5px
    }

    .main-info dd {
        font-size: 15px;
        line-height: 27px;
        color: #616161
    }

    h4, h5 {
        color: #000
    }

    .main-info dd strong {
        color: #000;
        font-size: 16px
    }

    .github-button {
        font-size: 0
    }

    iframe {
        margin: 0 10px
    }

    h3 {
        font-size: 19px;
        color: #01579B;
        margin: 0 0 15px 5px
    }

    h3 img {
        height: 30px;
        margin-right: 10px
    }

    h4 {
        line-height: 30px;
        font-size: 18px;
        bottom: 3px
    }

    h5 {
        clear: both;
        font-size: 16px;
        line-height: 25px
    }

    .fa {
        margin-right: 2px
    }

    h4 a, h5 a {
        font-size: 12px;
        border: 1px solid #f25d8e;
        padding: 1px 3px;
        -webkit-border-radius: 5px;
        border-radius: 5px;
        margin-left: 7px
    }

    .circle {
        height: 14px;
        width: 14px;
        -webkit-border-radius: 100%;
        border-radius: 100%;
        background: #00A1D6;
        float: left;
        position: absolute;
        left: -28px;
        top: 5px
    }

    .exp {
        border-left: 2px solid #00A1D6;
        margin-left: 15px
    }

    .exp p {
        font-size: 15px;
        color: #616161;
        line-height: 23px;
        margin-bottom: 5px
    }

    .exp > li {
        position: relative;
        top: -5px;
        margin: 0 0 0 20px
    }

    .exp img {
        max-width: 100%
    }

    .exp ul > li {
        margin: 0 0 12px
    }

    .efe .task4img img {
        height: 97px;
        width: inherit
    }

    footer {
        margin: 30px 0 20px
    }

    footer p {
        color: #616161;
        font-size: 14px
    }

    footer a {
        color: #f25d8e
    }

    .throb {
        -webkit-animation: throb 1.33s ease-in-out infinite;
        animation: throb 1.33s ease-in-out infinite
    }

    @-webkit-keyframes throb {
        0%, 100% {
            -webkit-transform: scale(1)
        }
        50% {
            -webkit-transform: scale(.8)
        }
    }

    @keyframes throb {
        0%, 100% {
            -webkit-transform: scale(1);
            transform: scale(1)
        }
        50% {
            -webkit-transform: scale(.8);
            transform: scale(.8)
        }
    }

    @font-face {
        font-family: fontello;
        src: url(__DIR__/font/fontello.eot?32003456);
        src: url(__DIR__/font/fontello.eot?32003456#iefix) format("embedded-opentype"), url(__DIR__/font/fontello.woff?32003456) format("woff"), url(__DIR__/font/fontello.ttf?32003456) format("truetype"), url(__DIR__/font/fontello.svg?32003456#fontello) format("svg");
        font-weight: 400;
        font-style: normal
    }

    [class*=" icon-"]:before, [class^=icon-]:before {
        font-family: fontello;
        font-style: normal;
        font-weight: 400;
        speak: none;
        display: inline-block;
        text-decoration: inherit;
        width: 1em;
        margin-right: .2em;
        text-align: center;
        font-variant: normal;
        text-transform: none;
        line-height: 1em;
        margin-left: .2em;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale
    }

    .icon-wechat:before {
        content: '\e800'
    }

    .icon-qq:before {
        content: '\e801'
    }

    .icon-bookmark:before {
        content: '\e802'
    }

    .icon-heart:before {
        content: '\e803'
    }

    .icon-mail-alt:before {
        content: '\e804'
    }

    .icon-link:before {
        content: '\e805'
    }

    .icon-phone-1:before {
        content: '\e806'
    }
</style>
