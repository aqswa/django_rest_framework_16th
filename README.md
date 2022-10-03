# CEOS 16기 백엔드 스터디 모델링 및 drf 연습을 위한 레포


## 2주차 미션: DB 모델링 및 Django ORM

### 투두메이트 모델링 ERD
<img width="100%" src="https://user-images.githubusercontent.com/69039161/193408814-d2dc72c3-29e5-4c98-ab4a-a96cd574ce73.png"/>  
사용자 : 프로필 = 1 : 1
사용자 : 팔로잉 = N : M
사용자 : 목표 = 1 : N
사용자 : 일기 = 1 : N
사용자 : 시간 알림 = 1 : N
사용자 : 팔로잉 = N : M
목표 : 할 일 = 1 : N
목표 : 간편입력 = 1 : N
목표 : 보관함 = 1 : N
간편입력 : 요일 = N : M
간편입력 : 할 일 = 1 : N
할 일 : 할 일 응원 : 사용자 = 1 : 1 : 1
일기 : 일기 응원 : 사용자 = 1 : 1 : 1


<img width="70%" src="https://user-images.githubusercontent.com/69039161/193409903-e5bf1a4d-c8c1-4f78-9b5e-07da2b214dea.png"/>

<img width="70%" src="https://user-images.githubusercontent.com/69039161/193410055-a452a0d0-ee5d-419d-a6ba-8065aaf64ba2.png"/>
<img width="70%" src="https://user-images.githubusercontent.com/69039161/193410082-e9023040-9cf4-4491-9511-4caa5f0fb7ac.png"/>

<img width="70%" src="https://user-images.githubusercontent.com/69039161/193410103-71233aaf-786b-49fd-be7d-d8f9539c2ed8.png"/>

<img width="70%" src="https://user-images.githubusercontent.com/69039161/193410124-0a94e05a-ff60-462d-a67d-c85961bafe21.png"/>


### ORM 활용해보기
1. **데이터베이스에 해당 모델 객체 3개 넣기**
	![image](https://user-images.githubusercontent.com/69039161/193408634-cabb82c2-fe0a-4a78-9080-203e778f3e70.png)  
	
2. **삽입한 객체들을 쿼리셋으로 조회해보기 (단, 객체들이 객체의 특성을 나타내는 구분가능한 이름으로 보여야 함)**

	![스크린샷(177)](https://user-images.githubusercontent.com/69039161/193408735-5cb78a3d-60fb-4590-8496-465e559f10f1.png)  
    
3. **filter 함수 사용해보기**
	![image](https://user-images.githubusercontent.com/69039161/193408722-b9e9f262-edcc-409a-a184-8406d015dd6b.png)  


### 간단한 회고

#### 1. null=True와 blank=True
null=True와 blank=True의 차이
null=True 는 필드의 값이 NULL(정보 없음)로 저장되는 것을 허용합니다. 결국 데이터베이스 열에 관한 설정입니다.  
blank=True 는 필드가 폼(입력 양식)에서 빈 채로 저장되는 것을 허용합니다. 장고 관리자(admin) 및 직접 정의한 폼에도 반영됩니다.  
null=True 와 blank=True 를 모두 지정하면 어떤 조건으로든 값을 비워둘 수 있음을 의미합니다.  
단, CharFields()와 TextFields()에서는 예외입니다.
장고는 이 경우 NULL을 저장하지 않으며, 빈 값을 빈 문자열('')로 저장합니다.

#### 2. 어려웠던 부분

1. 간편 입력으로 입력된 할 일을 활성화하면 간편 입력과 수정, 삭제가 동기화되지 않는다.  
그런데 다시 보관함으로 이동하면 간편입력과 동기화돼서, 간편 입력을 통해 수정과 삭제가 된다.  
활성화한 일의 시간을 바꾸고 다시 보관함으로 이동해 비활성화시키면 입력했던 시간은 사라진다. 
간편 입력과 할 일의 관계가 어떻게 된건지 아직도 모르겠다. 일단은 on_delete=CASCADE라고 썼고 수정, 삭제할 때 is_active가 true인 할 일은 수정하지 않는다라고 생각하기로 했고, 삭제를 할 때는 is_active가 true인 할 일의 foreignkey를 없애고 삭제한다는 말도 안되는 기능을 가정하기로 했다~!


2. 팔로우/팔로잉 기능도 어떻게 짜야할지 고민하다가 그냥 프로필에 manytomanyfield로 넣었고, user에서는 follower라는 단어로 가져온다고 가정했는데 더 좋은 방법이 있을 것 같다. 

3. 할 일과 일기를 응원하는 기능은 manytomanyfield로 연결하려고 했지만 응원마다 이모지가 반드시 있어야 해서 각각 두 개의 외래키로 연결된 모델 클래스를 만들었다. 

4. 간편입력에서 반복되는 요일은 선택하는 부분도 고민이 됐다. 여러 요일을 선택하지만 선택지가 7개밖에 없는데 manytomanyfield를 사용하는게 이상하다는 생각이 들었다. 그런데 choicefield에서 여러 개를 선택하려면 django-multiselectfieldf를 설치해야한다는 stackoverflow를 보고 그냥 했다. 

5. erd를 짜고 나니 날짜로 필터링되는 경우가 훨씬 많을 것 같아서 좀 더 날짜 중심으로 erd를 짜는게 더 좋을 것 같다는 생각이 들었지만 시간이 없었다. 

투두메이트에 기능이 이렇게 많은지 몰랐다. 생각보다 오래걸렸다ㅜ 모델이 도대체 어떻게 짜여진건지 모르겠는 기능들이 있어서 고민을 많이 해야 했다. 특히 간편 입력 기능이 너무 어려웠다. 할 일이 활성화됐다가 간편 입력이었다가 보관함에 가는 기준을 알려고 투두메이트를 만들어보고 모르는 사람 팔로우도 했다! 
