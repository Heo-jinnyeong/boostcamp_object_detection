![header](https://capsule-render.vercel.app/api?type=rect&color=gradient&text=재활용%20품목%20분류를%20위한%20Object%20Detection&fontSize=30)

# Members
- **김도윤**  : 2 stage model(detector, feature extractor 위주의 실험 진행_faster, cascade, htc, etc.), ensemble(wbf), hyperparameter tuning
- **김윤호**  : augmentation(Auto-augmentation, Mosaic, Multi-Scale) 실험, 2 stage model(ATSS-Dyhead, cascade rcnn), stratifiedGroupKfold 구현
- **김종해**  : 1 stage model (RetinaNet, yolov7) 실험, stratifiedGroupKfold 구현, WeightedBoxesFusion 실험
- **조재효**  : augmentation(TTA, albumentation), 1stage model (yolov7), 2 stage model(cascade_swin_b), hyperparameter tuning, k-fold, ensemble (wbf)
- **허진녕**  : EDA, 1 stage model (yolov3, yolof, yolox) 실험, hyperparameter tuning(atss_dyhead), k-fold, ensemble (wbf)


# 프로젝트 개요
> 제작한 모델을 사용함으로써 1 차적 목표인 쓰레기 장에서의 정확한 분리수거를 돕고 어린 아이들 대상 양질의 교육 자료를 제공한다. 
위와 같은 목표를 달성함으로 궁극적으로 지구 환경 보호에  이바지한다. <sup>[[1]](#footnote_1)</sup>

# 프로젝트 수행 절차
<h3> 1. 데이터 EDA
<h3> 2. Baseline 모델 선정
<h3> 3. Augmentation
<h3> 4. K-fold
<h3> 5. Hyperparameter Tuning & Ensemble


# 문제정의
<h3> 1. 데이터 불균형  </h3>
  
- EDA 결과 Battery에 대한 Annotation 수가 전체 23,144개 중 159개로 상당히 적었다.
- 하지만 Confusion Matrix로 확인 결과, Battery에 대한 예측은 올바르게 이루지고 있어 추가적인 작업은 진행하지 않았다.

<h3> 2. Validation Set 구성  </h3>

- 이미지 한 장에 존재하는 annotation의 개수는 1개에서 71개이다.
- 즉 이미지 안에서 여러 개의 Annotation이 존재하기 때문에 Stratified Group K-fold를 적용하여 Validation Set을 구성하였다.


# Advanced Techniques
<h3> 1. WBF (Weighted Boxes Fusion)   </h3>  




# Reference
<a name="footnote_1">[1]</a> 출처 : Aistage
