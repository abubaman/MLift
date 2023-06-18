<a href="https://github.com/abubaman/MLift/blob/main/readme_eng.md">for English</a>
# MLift
Machine Learning을 이용한 Weight Lifting Challenge 앱입니다.

## 개요
<p>아래 그림과 같이 카메라를 통해 사용자의 동작(현재는 스쿼트만 인식 가능)하고 이를 통해 Challenge(몇 일 동안, 하루에 몇 개의 스쿼트를 할 것인지)를 진행하는 앱입니다.</p>
<img src="/for_readme/images/main_concept.png"  width="700">

<p>현재 아래와 같은 동작의 구현이 되어 있습니다.</p>
<img src="/for_readme/images/mlift_overall.png"  width="700">


## 구성
<p>MLift는 총 3가지의 Application으로 구성되어 있습니다.</p>
- <strong>MLift :</strong> 사용자별 ID 및 Challenge 정보를 등록하고 관리하기 위한 PWA(Progressive Web App)앱입니다. 아이폰, 안드로이드, PC 모두 사용 가능하며, 아이폰, 안드로이드에는 별도 앱처럼 설치도 가능합니다.<br>
- <strong>qr_code :</strong> MLift 앱에서 설정된 사용자 정보를 가지고, 카메라에서 QR Code를 통해 로그인하기 위한 별도 PC용 앱입니다.<br>
- <strong>pushups :</strong> qr_code 앱에서 사용자 로그인 정보를 넘겨받아 실제 Weight Lift Challenge를 진행하는 앱입니다. 현재 스쿼트 동작만 인식 가능하며, 학습에 따라 여러 동작 인식이 가능합니다.
<p>아래에서 각각의 앱에 대해 상세 설명을 진행하였습니다. 다만 실제 구동 시 필요한 static 폴더의 파일들은 저작권 문제로 업로드하지 않았으며, 이는 앱의 기능 재현에는 문제가 없으나 앱의 모양에 영향을 줄 수 있습니다.</p>

### MLift
파이썬(python)과 장고(django) 그리고 장고 Rest API로 작성되었습니다. 현재 Repository의 pushups_main 폴더와 for_readme 폴더를 제외한 모든 폴더와 파일이 이 어플리케이션을 위한 파일들입니다.<br>
run_files 폴더 안에는 db에서 사용자 정보를 읽고 텔레그램 알림하는 별도 소규모 코드가 작성되어 있습니다.

### qr_code
자바스크립트로 작성되었습니다. MLift에서 자동으로 작성되는 사용자별 QR Code를 읽어 로그인 처리하는 별도 앱입니다. 라즈베리 파이, PC 그리고 맥까지 웹 브라우저와 카메라만 있다면 구동이 가능합니다. 현재 pushups_main 폴더의 qr_code 폴더 안의 파일이 해당 앱을 위한 파일입니다.

### pushups
자바스크립트로 작성되었습니다. qr_code에서 로그인 정보를 이어받아(정확히는 qr_code앱에서 변경한 DB의 정보를 인식하여) 사용자 정보를 인식하고, 이에 따라 '스쿼트 동작'을 카메라로 인식하여 챌린지를 진행하는 앱입니다. 스쿼트 동작에 대한 인식은 OpenCV와 Tensorflow를 사용한 Classification 알고리즘으로 학습하였으며, Idle/Squat 두 상태를 인식하고 이를 갯수로 처리하는 코드는 pushups_main 폴더의 pushups 폴더 내 파일에 작성하였습니다. 현재 pushups_main 폴더의 pushups 폴더 안의 파일이 해당 앱을 위한 파일입니다.
