<a href="https://github.com/abubaman/MLift/blob/main/readme_eng.md">for English</a>
# MLift
Machine Learning을 이용한 Weight Lifting Challenge 앱입니다.

## 개요
아래 그림과 같이 카메라를 통해 사용자의 동작(현재는 스쿼트만 인식 가능)하고 이를 통해 Challenge(몇 일 동안, 하루에 몇 개의 스쿼트를 할 것인지)를 진행하는 앱입니다.
<img src="/for_readme/images/main_concept.png"  width="700">

현재 아래와 같은 동작의 구현이 되어 있습니다.
<img src="/for_readme/images/mlift_overall.png"  width="700">


## 구성
<p>MLift는 총 3가지의 Application으로 구성되어 있습니다.</p>
 - MLift : 사용자별 ID 및 Challenge 정보를 등록하고 관리하기 위한 PWA(Progressive Web App)앱입니다. 아이폰, 안드로이드, PC 모두 사용 가능하며, 아이폰, 안드로이드에는 별도 앱처럼 설치도 가능합니다.
 - qr_code : MLift 앱에서 설정된 사용자 정보를 가지고, 카메라에서 QR Code를 통해 로그인하기 위한 별도 PC용 앱입니다.
 - pushups : qr_code 앱에서 사용자 로그인 정보를 넘겨받아 실제 Weight Lift Challenge를 진행하는 앱입니다. 현재 스쿼트 동작만 인식 가능하며, 학습에 따라 여러 동작 인식이 가능합니다.
<p>아래에서 각각의 앱에 대해 상세 설명을 진행하였습니다.</p>

### MLift


### qr_code
### pushups
 
