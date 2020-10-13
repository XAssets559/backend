# User模块

## Model

### User

- id：采用uuid1生成全球唯一码
- nick_name：班级序列号+姓名；String
- student_id：学号；String
- passwords：hash加密；String
- email：邮箱；EmailField
- grades：分数；Float；满分60
- status：defult = Student；String

### Scripts

- submit_time：提交时间；DataField；auto_now=True
- context：代码；Textarea
- to_user：foriegnKey-->student；
- title：题目;String

### Task

- submit_time：提交时间；DataField；auto_now=True
- demo_scripts：代码；Textarea
- to_user：foriegnKey-->teacher；
- title：题目;String
- descriptions：描述;String

## serializers

与model相对应

### UserSerializers

采用ModelSerializers，拥有以下五个参数：

- nick_name：用户的昵称（班级序列号+姓名）
- passwords：密码
- student_id：学号,StudentOnly
- email：邮箱
- status：用户的状态（教师/学生）

### TaskSerializers

同上，拥有以下三个参数：

- title：任务的题目
- descriptions：任务的描述
- demo_scripts：该任务的示例代码，需要学生写的部分用“||”隔开

### ScriptSerializers

同上，拥有以下两个参数

- context：学生提交的正确代码
- submit_time：提交时间



## 接口

- Server：http://127.0.0.1:8000
- 模块Url：{server}/user/
- Login：localhost/user/login/
  - GET:HELLO

  - POST

    - | 参数名               | 必选 | 说明      |
      | -------------------- | ---- | --------- |
      | nick_name/student_id | 是   | 昵称/学号 |
      | passwords            | 是   | 密码      |

    - 响应

      ```json
      {
          data:""
          status:200(成功)
      		   206(用户名/学号 密码不匹配)
      		   400(其他错误)
      }
      ```

      
- Register：{模块URL}/register/：已完成
  - GET：HELLO
  
  - POST
    
    - | 参数名     | 必选       | 说明          |
      | ---------- | ---------- | ------------- |
      | nick_name  | 是         | 昵称          |
      | student_id | status = 1 | 学号          |
      | passwords  | 是         | 密码          |
      | email      | 是         | 邮箱          |
      | status     | 是(选择)   | 0-老师/1-学生 |
      
    - 响应
    
      ```json
      {
          data:""
          status:200(成功)
      		   206(昵称或者学号已经被注册)
      		   400(其他错误)
      }
      ```
    
      
- index：{模块URL}/index/：未完成