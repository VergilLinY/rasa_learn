## Deny this time
* greet
    - utter_answer_greet
* deny OR goodbye
    - utter_arrange_next_time

## Normal path
* greet{"name": "mike"}
	- slot{"name": "mike"}
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm OR confirm_in_city
    - action_record_in_city
    - utter_ask_location
* inform_location{"location": "\u5929\u5fc3\u533a"}
	- slot{"location": "\u5929\u5fc3\u533a"}
    - utter_ask_job_exchange
* deny OR no_job_exchange
	- action_record_no_job_exchange
    - utter_ask_job_situation
* confirm_job_situation{"job_situation": "\u5929\u5fc3\u533a"}
	- slot{"job_situation": "\u5929\u5fc3\u533a"}
    - utter_ask_health_status
* confirm OR confirm_health
	- action_record_health
    - action_dialogue_completion_detect

## Expand path 01
* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny OR confirm_not_in_city
    - action_record_out_city
    - utter_ask_leave_approval_status
* deny OR deny_leave_approval_status
	- action_record_no_leave_approval
    - action_detective_approval
    - utter_ask_location
* inform_location{"location": "\u5929\u5fc3\u533a"}
	- slot{"location": "\u5929\u5fc3\u533a"}
    - utter_ask_job_exchange
* confirm OR confirm_job_exchange
	- action_record_job_exchange
	- utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location": "new york", "job_exchange_reason": "because kids"}
	- slot{"new_job_location": "new york"}
	- slot{"job_exchange_reason": "because kids"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation": "\u5929\u5fc3\u533a"}
	- slot{"job_situation": "\u5929\u5fc3\u533a"}
    - utter_ask_health_status
* deny OR deny_health
	- action_record_unhealth
    - utter_ask_medical_treatment_status
* without_medical_treatment{"unhealth_status": "feel bad"}
	- slot{"unhealth_status": "feel bad"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"without_medical_reason": "no money"}
	- slot{"without_medical_reason": "no money"}
    - action_dialogue_completion_detect

## Expand path 02
* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny OR confirm_not_in_city
    - action_record_out_city
    - utter_ask_leave_approval_status
* deny OR deny_leave_approval_status
	- action_record_no_leave_approval
    - action_detective_approval
    - utter_ask_location
* inform_location{"location": "\u5929\u5fc3\u533a"}
	- slot{"location": "\u5929\u5fc3\u533a"}
    - utter_ask_job_exchange
* confirm OR confirm_job_exchange
	- action_record_job_exchange
	- utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location": "new york", "job_exchange_reason": "because kids"}
	- slot{"new_job_location": "new york"}
	- slot{"job_exchange_reason": "because kids"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation": "\u5929\u5fc3\u533a"}
	- slot{"job_situation": "\u5929\u5fc3\u533a"}
    - utter_ask_health_status
* deny OR deny_health
	- action_record_unhealth
    - utter_ask_medical_treatment_status
* with_medical_treatment{"unhealth_status": "feel bad"}
	- slot{"unhealth_status": "feel bad"}
    - action_dialogue_completion_detect

## Expand path 03
* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny OR confirm_not_in_city
    - action_record_out_city
    - utter_ask_leave_approval_status
* confirm OR confirm_leave_approval_status
	- action_record_leave_approval
    - action_detective_approval
    - utter_ask_location
* inform_location{"location": "\u5929\u5fc3\u533a"}
	- slot{"location": "\u5929\u5fc3\u533a"}
    - utter_ask_job_exchange
* confirm OR confirm_job_exchange
	- action_record_job_exchange
	- utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location": "new york", "job_exchange_reason": "because kids"}
	- slot{"new_job_location": "new york"}
	- slot{"job_exchange_reason": "because kids"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation": "\u5929\u5fc3\u533a"}
	- slot{"job_situation": "\u5929\u5fc3\u533a"}
    - utter_ask_health_status
* deny OR deny_health
	- action_record_unhealth
    - utter_ask_medical_treatment_status
* without_medical_treatment{"unhealth_status": "feel bad"}
	- slot{"unhealth_status": "feel bad"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"without_medical_reason": "no money"}
	- slot{"without_medical_reason": "no money"}
    - action_dialogue_completion_detect

## Normal Path Generate 001

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"湖北省广东市"}
    - slot{"location":"湖北省广东市"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"一切正常"}
    - slot{"job_situation":"一切正常"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 002

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_in_city
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"开福区福元路"}
    - slot{"location":"开福区福元路"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"job_exchange_reason":"那边离家比较近"}
    - slot{"job_exchange_reason":"那边离家比较近"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"工作一切顺利"}
    - slot{"job_situation":"工作一切顺利"}
    - utter_ask_health_status
* confirm_health
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 003

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - utter_ask_leave_approval_status
* deny_leave_approval_status
    - action_record_no_leave_approval
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"建安大道旁边的铁道学院"}
    - slot{"location":"建安大道旁边的铁道学院"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还算顺利"}
    - slot{"job_situation":"还算顺利"}
    - utter_ask_health_status
* deny_health
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* with_medical_treatment{"unhealth_status": "feel bad"}
	- slot{"unhealth_status": "feel bad"}
    - action_dialogue_completion_detect

## Normal Path Generate 004

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_not_in_city
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny_leave_approval_status
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"厦门金台银光大厦876号"}
    - slot{"location":"厦门金台银光大厦876号"}
    - utter_ask_job_exchange
* no_job_exchange{"job_situation":"未变动"}
    - slot{"job_situation":"未变动"}
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"都正常"}
    - slot{"job_situation":"都正常"}
    - utter_ask_health_status
* confirm_health
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 005

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_in_city
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"湖南省长沙市天心区芙蓉南路神龙大酒店88楼"}
    - slot{"location":"湖南省长沙市天心区芙蓉南路神龙大酒店88楼"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"到花花大酒店","job_exchange_reason":"那边比较娱乐性强一点"}
    - slot{"job_exchange_reason":"那边比较娱乐性强一点"}
    - slot{"new_job_location":"到花花大酒店"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"比较好福利"}
    - slot{"job_situation":"比较好福利"}
    - utter_ask_health_status
* deny_health
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* without_medical_treatment{"unhealth_status":"胃疼好些了"}
    - slot{"unhealth_status":"胃疼好些了"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"without_medical_reason":"工作太忙了啊哪有时间去看病"}
    - slot{"without_medical_reason":"工作太忙了啊哪有时间去看病"}
    - action_dialogue_completion_detect

## Normal Path Generate 006

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_in_city
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"湖北省襄樊市51中对面的李记牛肉馆"}
    - slot{"location":"湖北省襄樊市51中对面的李记牛肉馆"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还行"}
    - slot{"job_situation":"还行"}
    - utter_ask_health_status
* confirm_health
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 007

* greet
    - utter_answer_greet
* deny
    - utter_arrange_next_time

## Normal Path Generate 008

* greet{"name":"李强"}
    - slot{"name":"李强"}
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"泰山西边的阿里啦谷"}
    - slot{"location":"泰山西边的阿里啦谷"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"job_exchange_reason":"以前的公司负债"}
    - slot{"job_exchange_reason":"以前的公司负债"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"正常上下班"}
    - slot{"job_situation":"正常上下班"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 009

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"长沙市雨花区木加马坡的45号"}
    - slot{"location":"长沙市雨花区木加马坡的45号"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"马兰山马兰坡华茂大厦","job_situation":"不想离家太远"}
    - slot{"job_situation":"不想离家太远"}
    - slot{"new_job_location":"马兰山马兰坡华茂大厦"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还行"}
    - slot{"job_situation":"还行"}
    - utter_ask_health_status
* deny_health
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* with_medical_treatment{"unhealth_status":"脸上的皮炎还没消"}
    - slot{"unhealth_status":"脸上的皮炎还没消"}
    - action_dialogue_completion_detect

## Normal Path Generate 010

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny_leave_approval_status
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"湖南省长沙市世界之窗"}
    - slot{"location":"湖南省长沙市世界之窗"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"工作在五一广场","job_exchange_reason":"前面的工作太紧张压力太大"}
    - slot{"job_exchange_reason":"前面的工作太紧张压力太大"}
    - slot{"new_job_location":"工作在五一广场"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"正常上下班"}
    - slot{"job_situation":"正常上下班"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 011

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"湖南省长沙市开福区福元路18号"}
    - slot{"location":"湖南省长沙市开福区福元路18号"}
    - utter_ask_job_exchange
* deny
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"一切顺利"}
    - slot{"job_situation":"一切顺利"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 012

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_in_city
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"椰林东路与326国道交叉口西150米"}
    - slot{"location":"椰林东路与326国道交叉口西150米"}
    - utter_ask_job_exchange
* confirm
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"江北路那边","job_exchange_reason":"最近要回家带孩子了"}
    - slot{"job_exchange_reason":"最近要回家带孩子了"}
    - slot{"new_job_location":"江北路那边"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还算顺利"}
    - slot{"job_situation":"还算顺利"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 013

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_in_city
	- action_record_in_city
    - utter_ask_location
* inform_location{"location":"兰州市西固区福利东路"}
    - slot{"location":"兰州市西固区福利东路"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还算顺利"}
    - slot{"job_situation":"还算顺利"}
    - utter_ask_health_status
* deny_health
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* without_medical_treatment{"unhealth_status":"每天都头疼发热"}
    - slot{"unhealth_status":"每天都头疼发热"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"without_medical_reason": "too much things need to do"}
	- slot{"without_medical_reason": "too much things need to do"}
    - action_dialogue_completion_detect

## Normal Path Generate 014

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"海南藏族自治州共和县"}
    - slot{"location":"海南藏族自治州共和县"}
    - utter_ask_job_exchange
* deny
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还行"}
    - slot{"job_situation":"还行"}
    - utter_ask_health_status
* deny_health
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* with_medical_treatment{"unhealth_status":"上个星期腿骨折了"}
    - slot{"unhealth_status":"上个星期腿骨折了"}
    - action_dialogue_completion_detect

## Normal Path Generate 015

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"七界山名胜风景旅游区"}
    - slot{"location":"七界山名胜风景旅游区"}
    - utter_ask_job_exchange
* confirm
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"芥子铺旅游局","job_exchange_reason":"那边调"}
    - slot{"job_exchange_reason":"那边调"}
    - slot{"new_job_location":"芥子铺旅游局"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"顺利"}
    - slot{"job_situation":"顺利"}
    - utter_ask_health_status
* deny_health{"unhealth_status":"老是想呕吐"}
    - slot{"unhealth_status":"老是想呕吐"}
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* without_medical_treatment{"unhealth_status":"早晨起床还是感觉想吐"}
    - slot{"unhealth_status":"早晨起床还是感觉想吐"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"unhealth_status":"工作太忙了"}
    - slot{"unhealth_status":"工作太忙了"}
    - action_dialogue_completion_detect

## Normal Path Generate 016

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_not_in_city
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* confirm_leave_approval_status
    - action_record_leave_approval
    - slot{"leave_approval_status":"hold_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"苏州市吴中区工业园区塘浦路与西华林街交叉口(东南200米"}
    - slot{"location":"苏州市吴中区工业园区塘浦路与西华林街交叉口(东南200米"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"job_exchange_reason":"上一份工作"}
    - slot{"job_exchange_reason":"上一份工作"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还算顺利"}
    - slot{"job_situation":"还算顺利"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 017

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"无锡市锡山区春鑫路50号"}
    - slot{"location":"无锡市锡山区春鑫路50号"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"云林春雷苑","job_exchange_reason":"那边的酒店生意比较好"}
    - slot{"job_exchange_reason":"那边的酒店生意比较好"}
    - slot{"new_job_location":"云林春雷苑"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"都挺好的"}
    - slot{"job_situation":"都挺好的"}
    - utter_ask_health_status
* deny_health{"unhealth_status":"得了肩周炎"}
    - slot{"unhealth_status":"得了肩周炎"}
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* without_medical_treatment{"unhealth_status":"每天都很疼"}
    - slot{"unhealth_status":"每天都很疼"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"job_exchange_reason":"家里事情比较多"}
    - slot{"job_exchange_reason":"家里事情比较多"}
    - action_dialogue_completion_detect

## Normal Path Generate 018

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"上海市浦东新区祝桥镇南祝公路盐仓汽车站向南300米"}
    - slot{"location":"上海市浦东新区祝桥镇南祝公路盐仓汽车站向南300米"}
    - utter_ask_job_exchange
* deny
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还行"}
    - slot{"job_situation":"还行"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 019

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_not_in_city
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny_leave_approval_status
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"上海市浦东新区祝桥镇盐朝公路835号"}
    - slot{"location":"上海市浦东新区祝桥镇盐朝公路835号"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"浦东分局派出所","job_exchange_reason":"单位把"}
    - slot{"job_exchange_reason":"单位把"}
    - slot{"new_job_location":"浦东分局派出所"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"一切顺利"}
    - slot{"job_situation":"一切顺利"}
    - utter_ask_health_status
* deny_health{"unhealth_status":"得了肩周炎"}
    - slot{"unhealth_status":"得了肩周炎"}
    - action_record_unhealth
    - utter_ask_medical_treatment_status
* without_medical_treatment{"unhealth_status":"感冒了在家休息"}
    - slot{"unhealth_status":"感冒了在家休息"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"without_medical_reason":"工作忙"}
    - slot{"without_medical_reason":"工作忙"}
    - action_dialogue_completion_detect

## Normal Path Generate 020

* greet{"name":"陈明"}
    - slot{"name":"陈明"}
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* confirm
    - action_record_leave_approval
    - slot{"leave_approval_status":"hold_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"上海市浦东新区盐朝公路与红三中心路交叉口"}
    - slot{"location":"上海市浦东新区盐朝公路与红三中心路交叉口"}
    - utter_ask_job_exchange
* deny
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"顺利"}
    - slot{"job_situation":"顺利"}
    - utter_ask_health_status
* deny
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* without_medical_treatment
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"job_exchange_reason":"家里的事情太多了"}
    - slot{"job_exchange_reason":"家里的事情太多了"}
    - action_dialogue_completion_detect

## Normal Path Generate 021

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* confirm
    - action_record_leave_approval
    - slot{"leave_approval_status":"hold_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"遵义市红花岗区新舟镇迎宾大道"}
    - slot{"location":"遵义市红花岗区新舟镇迎宾大道"}
    - utter_ask_job_exchange
* deny
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"很开心"}
    - slot{"job_situation":"很开心"}
    - utter_ask_health_status
* deny_health{"unhealth_status":"牙齿疼"}
    - slot{"unhealth_status":"牙齿疼"}
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* with_medical_treatment
    - action_dialogue_completion_detect

## Normal Path Generate 022

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"湖南省长沙市长沙县黄兴大道"}
    - slot{"location":"湖南省长沙市长沙县黄兴大道"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"顺利"}
    - slot{"job_situation":"顺利"}
    - utter_ask_health_status
* confirm
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 023

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny_leave_approval_status
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"长沙市芙蓉区农大路1号"}
    - slot{"location":"长沙市芙蓉区农大路1号"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"东湖小区","job_exchange_reason":"那边交通好"}
    - slot{"job_exchange_reason":"那边交通好"}
    - slot{"new_job_location":"东湖小区"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"顺利"}
    - slot{"job_situation":"顺利"}
    - utter_ask_health_status
* deny_health{"unhealth_status":"肺结核正在住院"}
    - slot{"unhealth_status":"肺结核正在住院"}
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* with_medical_treatment{"unhealth_status":"目前正在住院观察中"}
    - slot{"unhealth_status":"目前正在住院观察中"}
    - action_dialogue_completion_detect

## Normal Path Generate 024

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_not_in_city
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny_leave_approval_status
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"天心区书院路9号"}
    - slot{"location":"天心区书院路9号"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"挺好的一切顺利"}
    - slot{"job_situation":"挺好的一切顺利"}
    - utter_ask_health_status
* deny_health
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* with_medical_treatment{"unhealth_status":"当前健康状况良好"}
    - slot{"unhealth_status":"当前健康状况良好"}
    - action_dialogue_completion_detect

## Normal Path Generate 025

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_in_city
    - action_record_in_city
    - slot{"is_in_city":"in_city"}
    - utter_ask_location
* inform_location{"location":"长沙市岳麓区岳麓街道后湖村杜家塘15号"}
    - slot{"location":"长沙市岳麓区岳麓街道后湖村杜家塘15号"}
    - utter_ask_job_exchange
* confirm_job_exchange
    - action_record_job_exchange
    - slot{"is_job_exchange":"job_exchange"}
    - utter_ask_exchange_reason
* answer_job_exchange_reason{"new_job_location":"后湖国际艺术中心","job_exchange_reason":"那边环境更好"}
    - slot{"job_exchange_reason":"那边环境更好"}
    - slot{"new_job_location":"后湖国际艺术中心"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"很顺利"}
    - slot{"job_situation":"很顺利"}
    - utter_ask_health_status
* confirm_health
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 026

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* confirm_not_in_city
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny_leave_approval_status
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"长沙市天心区青山路鑫远湘府逸园"}
    - slot{"location":"长沙市天心区青山路鑫远湘府逸园"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还行"}
    - slot{"job_situation":"还行"}
    - utter_ask_health_status
* confirm_health
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## Normal Path Generate 027

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* confirm_leave_approval_status
    - action_record_leave_approval
    - slot{"leave_approval_status":"hold_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"2期7栋门面103(近金帆路)附近"}
    - slot{"location":"2期7栋门面103(近金帆路)附近"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"还算顺利"}
    - slot{"job_situation":"还算顺利"}
    - utter_ask_health_status
* confirm_health
    - action_record_health
    - slot{"is_health_OK":"ok"}
    - action_dialogue_completion_detect

## New Story

* greet
    - utter_answer_greet
* confirm
    - utter_identifying
    - action_voiceprint_verification
    - utter_whether_in_city
* deny
    - action_record_out_city
    - slot{"is_in_city":"out_city"}
    - utter_ask_leave_approval_status
* deny
    - action_record_no_leave_approval
    - slot{"leave_approval_status":"without_approval"}
    - action_detective_approval
    - utter_ask_location
* inform_location{"location":"湖南省长沙市芙蓉区南阳街8号华联商住楼"}
    - slot{"location":"湖南省长沙市芙蓉区南阳街8号华联商住楼"}
    - utter_ask_job_exchange
* no_job_exchange
    - action_record_no_job_exchange
    - slot{"is_job_exchange":"job_regular"}
    - utter_ask_job_situation
* confirm_job_situation{"job_situation":"很开心"}
    - slot{"job_situation":"很开心"}
    - utter_ask_health_status
* deny_health{"unhealth_status":"腿很疼"}
    - slot{"unhealth_status":"腿很疼"}
    - action_record_unhealth
    - slot{"is_health_OK":"not_good"}
    - utter_ask_medical_treatment_status
* without_medical_treatment_reason{"unhealth_status":"时常会抽搐"}
    - slot{"unhealth_status":"时常会抽搐"}
    - utter_ask_without_medical_treatment_reason
* without_medical_treatment_reason{"without_medical_reason":"感觉没有太大的问题"}
    - slot{"without_medical_reason":"感觉没有太大的问题"}
    - action_dialogue_completion_detect
