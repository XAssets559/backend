# Index模块

这是主页。需要以下几个部分：

- 文章推荐：5篇

- 任务列表

- 排行榜-->grades
- 广告（采用轮播图）


### 接口
server = 127.0.0.1:8000

#### 任务列表

url = 127.0.0.1:8000/task/

- 语法：get task/

- 请求参数

  - | 参数名 | 必选 | 说明                                                         |
    | ------ | ---- | ------------------------------------------------------------ |
    | change | 是   | 如果是编辑页面(教师后台中)，change = True,如果是主页，为False |

- 响应

  ```json
  [
   {"id": 2, 
    "title": "wer", "to_user": "xiahaitao", "c_time": "2020-10-29T11:25:31.674000Z"},
   {"id": 1,
    "title": "retybhfd",
    "to_user": "xiahaitao",
    "c_time": "2020-10-20T13:15:42.701000Z"}
  ]
  ```


#### 文章列表

url = 127.0.0.1:8000/article/

- 语法：get article/

- 请求参数

  - | 参数名 | 必选 | 说明                                                         |
    | ------ | ---- | ------------------------------------------------------------ |
    | change | 是   | 如果是编辑页面(教师后台中)，change = True,如果是主页，为False |

    

- 响应

  ```json
  [
      {
          "id": "6e603592-106e-11eb-b472-002381250f5b",//文章id
          "title": "wqrdfsgdf",//文章标题
          "des": "fgdsg",//文章描述
          "author": "xiahaitao",//创建人
          "c_time": "2020-10-17T11:46:44.919800Z"//创建时间
      },
      {
          "id": "6b39a134-106e-11eb-98f2-002381250f5b",
        "title": "第一题",
          "des": "eqwe",
          "author": "xiahaitao",
          "c_time": "2020-10-17T11:46:39.632800Z"
      }
  ]
  ```
  
  

#### 任务创建

url：127.0.0.1:8000/create_task/

- 语法：post create_task/

- 请求参数

  - | 参数名       | 必选 | 说明           |
    | ------------ | ---- | -------------- |
    | title        | 是   | 题目的标题     |
    | descriptions | 是   | 题目的描述     |
    | demo_scripts | 是   | 题目的示例代码 |

- 响应

  ```json
  无
  ```

  

#### 文章创建

url：127.0.0.1：8000/create_article/

- 语法：post create_article/

  - | 参数名  | 必选 | 说明           |
    | ------- | ---- | -------------- |
    | title   | 是   | 文章的标题     |
    | des     | 是   | 文章的描述     |
    | context | 是   | 文章的主题内容 |



#### 任务详情页

url：127.0.0.1：8000/task_detial/<pk>

- 语法：get task_detial/<pk>

  - | 参数名 | 必选 | 说明     |
    | ------ | ---- | -------- |
    | pk     | 是   | 题目的id |

    

- 响应

  - ```json
    {"title": "retybhfd",
     "descriptions": "retetwe",
     "demo_scripts": "rtreter",
     "to_user": "xiahaitao",
     "c_time": "2020-10-20T13:15:42.701000Z"}
    ```

    

#### 文章详情页

url：127.0.0.1：8000/article_detial/<pk>

- 语法：get article_detial/<pk>

  - | 参数名 | 必选 | 说明     |
    | ------ | ---- | -------- |
    | pk     | 是   | 题目的id |

    

- 响应

  - ```json
    {"title": "\u7b2c\u4e00\u9898",
     "des": "32re",
     "context": "tetet",
     "author": "xiahaitao",
     "c_time": "2020-10-20T13:15:30.764000Z"}}
    ```

    