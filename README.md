# vue-json-template

一个基于 vue，根据 json 渲染 html 的模板系统，**无需构建工具即可使用\*.vue单文件组件**作为模板。

使用 vuep 实现在线编译，用一个简易的配置文件动态加载外部JS/CSS，便于使用第三方组件。

## 配置

模板目录结结构

```
├── index.html
└── templates
    ├── index.json 
    ├── a
    │   ├── config.json
    │   ├── data.json
    │   └── index.vue (可选)
    └── b
        ├── config.json
        ├── data.json
        └── index.vue

```

`index.json` 为模板索引文件 `default` 用于指定默认模板，`templates` 用于声明模板列表，`loaclhost/127.0.0.1` 域下右键可以快速切换模板。

```json
{
  "default": "",
  "templates": []
}
```

`data.json` 为数据文件，用于注入到模板中 `index.vue` 的 `data`。必须包含`html-title`。

`index.vue` 为模板入口组件，`data`中必须包含 `DATA_INJECT_HERE` ，用于提供注入点(用文本替换实现注入，比较粗暴2333)。

`config.json` 为模板配置文件，可以指定自定义的外部 JS/CSS，指定需要继承的模板。

```json
{
  "external-js": [
    "https://unpkg.com/element-ui/lib/index.js"
  ],
  "external-css": [
    "https://unpkg.com/element-ui/lib/theme-chalk/index.css"
  ]
//  ,"extends": "resume-diygod"
}
```

[vuep.run 在线调试](https://vuep.netlify.com/)

## 注意

由于加载组件是直接读取源码，故所有相对路径均是相对于`index.html` 而不是模板根目录，需要用到相对于模板根目录的路径的地方请用 `__DIR__/`开头。

## 协议

MIT
