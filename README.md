# NSGA-II 기반 수리부속 재고 최적화 분석모델

> **방산 IPS 수리부속 소요예측 및 재고수준 의사결정을 위한 NSGA-II 기반 다목적 최적화 모델**

---

## 1. 프로젝트 개요

본 프로젝트는 방산 **IPS(Integrated Product Support, 종합군수지원)** 분야에서 수리부속의 적정 재고수준을 산정하기 위한 분석모델입니다.

본 모델은 단순히 고장률이 높은 품목을 많이 구매하는 방식이 아니라, 다음 요소를 동시에 고려하여 **비용-효과 최적 재고정책**을 탐색합니다.

| 고려 요소 | 설명 |
|---|---|
| 구매비용 | 수리부속을 구매하는 데 필요한 비용 |
| 보유비용 | 재고를 보유함에 따라 발생하는 비용 |
| 정비비용 | 고장 발생 후 정비에 필요한 비용 |
| 고장률 | 품목의 고장 발생 가능성 |
| QPA | 장비 1대에 들어가는 해당 품목 수량 |
| FLEET_SIZE | 전체 운용 장비 수 |
| 정비계층 | O/I/D 정비 단계 |
| 리드타임 | 부품 확보 또는 수리/보급까지 걸리는 시간 |
| 운용가용도 Ao | 장비가 필요한 시간 중 실제 운용 가능한 비율 |

최종 결과는 **비용(Cost)** 과 **운용가용도(Ao)** 사이의 상충관계를 보여주는 **Pareto front** 및 **통합 trade-off map**으로 제시됩니다.

---

## 2. 모델의 성격

본 모델은 `scikit-learn` 계열의 지도학습 예측모델이 아닙니다.

즉, 과거 데이터를 학습해서 새로운 `y` 값을 예측하는 모델이 아니라, 입력된 품목정보와 정비/보급 조건을 기반으로 여러 목적함수를 동시에 만족하는 재고정책을 탐색하는 **다목적 최적화 모델**입니다.

```text
AI
└── Computational Intelligence
    └── Evolutionary Computation
        └── Genetic Algorithm
            └── NSGA-II
                └── Multi-Objective Optimization
```

| 구분 | 설명 |
|---|---|
| 모델 유형 | 다목적 최적화 모델 |
| 알고리즘 | NSGA-II |
| 최적화 방식 | 진화연산 기반 메타휴리스틱 |
| 결과 형태 | Pareto 최적해 집합 |
| 목적 | 수리부속 재고정책 의사결정 지원 |

---

## 3. 핵심 기능

### 3.1 수리부속 재고수준 최적화

- 품목별 재고수량 탐색
- O/I/D 정비계층별 재고 배분
- 불필요한 과재고 억제
- 장기 리드타임 품목 보호재고 고려

### 3.2 운용가용도 개선

- 수리부속 부족으로 인한 대기시간 감소
- 목표 운용가용도 미달량 최소화
- DT_diag, DT_wait, DT_restore 분해 진단

### 3.3 비용-효과 Trade-off 분석

- 비용과 Ao 간 Pareto front 생성
- 여러 목표 Ao를 순회하는 target sweep 지원
- 통합 trade-off map 생성

### 3.4 OPUS10 입력자료 연계

- 백만시간당 고장률을 연간 고장강도로 변환
- QPA 반영
- FLEET_SIZE 반영
- 장비 기준 고장강도와 전체 수리부속 수요강도 분리

---

## 4. 입력파일

기본 입력파일명은 다음과 같습니다.

```text
radar_1000_parts_bom.xlsx
```

코드 상단에서 입력파일 경로를 변경할 수 있습니다.

```python
XLSX_PATH = "radar_1000_parts_bom.xlsx"
```

Colab에서 파일을 직접 업로드하려면 다음 값을 `True`로 변경합니다.

```python
USE_COLAB_UPLOAD = True
```

---

## 5. 입력 컬럼 설명

### 5.1 필수 컬럼

아래 컬럼은 반드시 필요합니다.

| 컬럼명 | 한글 의미 | 설명 |
|---|---|---|
| `Part_ID` | 품목 ID | 각 품목을 구분하는 고유 코드 |
| `Parent_ID` | 상위 품목 ID | BOM 계층에서 상위 조립체를 나타냄 |
| `Level` | BOM 계층 레벨 | L1, L2, L3 등 구조적 깊이 |
| `Maint_Echelon` | 정비계층 | 부대정비, 야전정비, 창정비 등 |
| `Failure_Rate` | 고장률 | 단위 설정에 따라 다르게 해석됨 |

필수 컬럼 중 하나라도 없으면 모델은 실행을 중단합니다.

---

### 5.2 권장 컬럼

| 컬럼명 | 한글 의미 | 설명 |
|---|---|---|
| `Unit_Price_KRW` | 단가 | 품목 1개 구매가격 |
| `Transport_Cost_KRW` | 수송비 | 품목 이동 또는 보급 수송비 |
| `Total_Lead_Time_H` | 총 리드타임 | 부품 확보까지 걸리는 총 시간 |
| `Transport_Time_H` | 수송시간 | 물류 이동에 필요한 시간 |
| `CM_Cost_KRW` | 고장정비 비용 | 고장 후 수리 비용 |
| `CM_Time_Hours` | 고장정비 시간 | 고장 후 수리에 필요한 시간 |
| `Condemnation_Rate_Pct` | 폐기율 | 수리 불가 후 폐기될 비율 |
| `PM_Cycle` | 예방정비 주기 | 예방정비 수행 주기 |
| `QPA` | 장비대당 품목수량 | 장비 1대에 들어가는 해당 품목 수량 |

---

## 6. 주요 설정값

### 6.1 고장률 단위 설정

OPUS10 입력자료는 일반적으로 **백만시간당 고장률** 형태를 사용합니다.

```python
FAILURE_RATE_UNIT = "per_million_hours"
ANNUAL_OPERATING_HOURS = HOURS_PER_YEAR
```

| 설정값 | 의미 | 설명 |
|---|---|---|
| `per_million_hours` | 백만시간당 고장률 | OPUS10 방식 |
| `annual_rate` | 연간 고장강도 | 이미 lambda/year인 경우 |
| `annual_probability` | 연간 고장확률 | 1년 내 고장확률 p |

변환식은 다음과 같습니다.

```text
연간 고장강도 = Failure_Rate × ANNUAL_OPERATING_HOURS / 1,000,000
```

예시:

```text
Failure_Rate = 0.005333
ANNUAL_OPERATING_HOURS = 8760

annual_lambda = 0.005333 × 8760 / 1,000,000
              ≈ 0.0000467 / year
```

---

### 6.2 QPA 설정

`QPA`는 **Quantity Per Assembly/Equipment**, 즉 장비 1대에 해당 품목이 몇 개 들어가는지를 의미합니다.

```python
APPLY_QPA_TO_FAILURE_RATE = True
DEFAULT_QPA = 1.0
```

QPA 컬럼이 없으면 모든 품목의 QPA는 `1.0`으로 처리됩니다.

```text
장비 1대 기준 고장강도 = 품목 1개 기준 고장강도 × QPA
```

예시:

```text
품목 1개 기준 연간 고장강도 = 0.00005
QPA = 10

장비 1대 기준 연간 고장강도 = 0.00005 × 10
                         = 0.0005
```

---

### 6.3 FLEET_SIZE 설정

`FLEET_SIZE`는 전체 운용대수를 의미합니다.

```python
FLEET_SIZE = 1.0
```

운용대수가 30대라면 다음처럼 변경합니다.

```python
FLEET_SIZE = 30.0
```

```text
수리부속 수요강도 = 장비 1대 기준 고장강도 × FLEET_SIZE
```

---

## 7. 모델 개선 단계

본 모델은 아래 단계들을 거쳐 개선되었습니다.

| 단계 | 수정 내용 | 목적 |
|---:|---|---|
| Step 1 | 진단표 추가 | 결과 원인 추적 |
| Step 2 | 고장률 단위 변환 | OPUS10 입력자료 반영 |
| Step 3 | QPA 반영 | 장비 기준 고장강도 산정 |
| Step 4 | PMIN 완화 | 후보품목 과도 탈락 방지 |
| Step 5 | lambda 분리 | Ao 계산과 수요 계산 분리 |
| Step 6 | 리드타임 수요 기반 부족확률 | 재고부족 위험 현실화 |

---

## 8. Step별 상세 설명

### Step 1. 진단표 추가

모델 결과가 왜 그렇게 나왔는지 확인하기 위해 품목별 진단 컬럼을 추가했습니다.

| 진단값 | 의미 |
|---|---|
| `FR_raw_input` | 원본 입력 고장률 |
| `FR_model_used` | 모델 계산에 실제 사용된 고장강도 |
| `annual_FR` | 연간 고장강도 |
| `lambda_eff_annual` | 보정된 연간 고장강도 |
| `lambda_eff_2y` | 2년 기준 보정 고장강도 |
| `p_need_2y` | 2년 내 필요확률 |
| `ao_impact` | Ao 영향도 |
| `mu_pipe_nom` | 명목 파이프라인 수요 |
| `stock_cap` | 재고상한 |
| `DT_wait_ratio` | 총 불가동시간 중 대기시간 비율 |

---

### Step 2. Failure_Rate 단위 변환

OPUS10의 백만시간당 고장률을 연간 고장강도로 변환합니다.

```python
FR_all = Failure_Rate × ANNUAL_OPERATING_HOURS / 1_000_000
```

이 단계는 모델 논리를 바꾸는 것이 아니라, 입력 단위를 모델 내부 단위와 일치시키는 전처리 단계입니다.

---

### Step 3. QPA 반영

품목 1개 기준 고장강도를 장비 1대 기준 고장강도로 확장합니다.

```python
annual_fr_item = FR_model_used × (1 - PM_failure_gamma)
annual_fr_system = annual_fr_item × QPA
```

| 변수 | 의미 |
|---|---|
| `annual_fr_item` | 품목 1개 기준 연간 고장강도 |
| `PM_failure_gamma` | 예방정비에 따른 고장률 완화효과 |
| `annual_fr_system` | 장비 1대 기준 연간 고장강도 |

---

### Step 4. PMIN 후보선별 기준 완화

OPUS10 고장률 변환 후 `p_need_2y`가 작아져 후보품목이 과도하게 탈락하는 문제를 완화합니다.

```python
PMIN = 0.01
```

`PMIN`은 후보품목으로 포함하기 위한 최소 필요확률 기준입니다.

---

### Step 5. lambda_system / lambda_demand 분리

Ao 계산용 고장강도와 수리부속 수요 계산용 고장강도를 분리합니다.

```python
annual_fr_item = FR_model_used × (1 - PM_failure_gamma)
annual_fr_system = annual_fr_item × QPA
annual_fr_demand = annual_fr_system × FLEET_SIZE
```

| 변수 | 사용 목적 | 설명 |
|---|---|---|
| `lambda_system` | Ao/DT 계산 | 장비 1대 기준 고장강도 |
| `lambda_demand` | 재고수요 계산 | 전체 운용대수 기준 수요강도 |

이 분리를 통해 장비 1대의 운용가용도와 전체 장비군의 수리부속 수요를 구분할 수 있습니다.

---

### Step 6. 리드타임 수요 기반 부족확률

기존에는 issue time 동안 수요가 재고를 초과할 확률을 부족확률로 보았습니다.

수정 후에는 리드타임 동안 발생하는 수요가 현재 재고를 초과할 확률을 부족확률로 봅니다.

```python
mu_lead = lambda_demand × shortage_exposure_h / HOURS_PER_YEAR
```

O/I/D 누적재고 기준 부족확률은 다음과 같습니다.

```text
p_short_O = P(lead-time demand > sO)
p_short_I = P(lead-time demand > sO + sI)
p_short_D = P(lead-time demand > sO + sI + sD)
```

| 변수 | 의미 |
|---|---|
| `p_short_O` | O-level 재고만으로 부족할 확률 |
| `p_short_I` | O+I 누적재고로도 부족할 확률 |
| `p_short_D` | O+I+D 누적재고로도 부족할 확률 |

이 단계에서 장기 리드타임 품목의 재고 필요성이 더 현실적으로 반영됩니다.

---

## 9. 목적함수

본 모델은 3개의 목적함수를 사용합니다.

### F1. 총비용 최소화

```text
F1 = total_cost + AO_COST_PENALTY × ao_shortfall²
```

| 항목 | 의미 |
|---|---|
| `total_cost` | 총비용 |
| `AO_COST_PENALTY` | Ao 미달 패널티 계수 |
| `ao_shortfall` | 목표 Ao 대비 미달량 |

---

### F2. 목표 Ao 미달량 최소화

```text
F2 = max(0, AO_TARGET - Ao)
```

목표 운용가용도에 미달하는 정도를 최소화합니다.

---

### F3. 관리품목 수 및 재고수량 부담 최소화

```text
F3 = ITEM_COUNT_WEIGHT × managed_items
   + STOCK_UNIT_WEIGHT × total_stock_units
```

| 항목 | 의미 |
|---|---|
| `managed_items` | 재고 관리 대상으로 선택된 품목 수 |
| `total_stock_units` | 전체 선택 품목의 총 재고수량 |
| `ITEM_COUNT_WEIGHT` | 관리품목 수 가중치 |
| `STOCK_UNIT_WEIGHT` | 재고수량 가중치 |

---

## 10. Ao 계산 구조

`Ao`는 **Operational Availability**, 즉 운용가용도입니다.

```text
DT_total = DT_diag + DT_wait + DT_restore

Ao = T_OBS_HOURS / (T_OBS_HOURS + DT_total)
```

| 항목 | 한글 의미 | 설명 |
|---|---|---|
| `DT_total` | 총 불가동시간 | 전체 다운타임 |
| `DT_diag` | 진단시간 | 고장 진단 및 계층 추적 시간 |
| `DT_wait` | 대기시간 | 수리부속 부족 또는 보급대기 시간 |
| `DT_restore` | 복원시간 | 실제 정비 및 수리 시간 |
| `T_OBS_HOURS` | 관측시간 | 분석기간 동안의 총 시간 |

진단 비율은 다음과 같습니다.

| 진단 비율 | 의미 |
|---|---|
| `DT_diag_ratio` | 총 불가동시간 중 진단시간 비율 |
| `DT_wait_ratio` | 총 불가동시간 중 대기시간 비율 |
| `DT_restore_ratio` | 총 불가동시간 중 복원시간 비율 |

---

## 11. NSGA-II 주요 설정

```python
POP = 80
GEN = 200
SEED = 42
```

| 설정값 | 의미 | 설명 |
|---|---|---|
| `POP` | Population size | 세대별 해집단 크기 |
| `GEN` | Generation | 진화 반복 횟수 |
| `SEED` | Random seed | 난수 고정값 |

빠른 preview 실행을 원하면 다음처럼 줄일 수 있습니다.

```python
AO_TARGET_GRID = [0.90, 0.94]
POP = 24
GEN = 12
```

---

## 12. Target Sweep

본 모델은 하나의 목표 Ao만 보지 않고 여러 목표 Ao를 순회합니다.

```python
AO_TARGET_GRID = [
    0.10, 0.20, 0.30, 0.40, 0.50,
    0.60, 0.70, 0.80, 0.85, 0.90,
    0.92, 0.94
]

REPRESENTATIVE_TARGET = 0.94
```

| 설정값 | 의미 |
|---|---|
| `AO_TARGET_GRID` | 분석할 목표 Ao 목록 |
| `REPRESENTATIVE_TARGET` | 상세 결과를 출력할 대표 목표 Ao |

---

## 13. 주요 출력 결과

| 출력 | 설명 |
|---|---|
| Target-wise summary | 목표 Ao별 결과 요약 |
| Representative target summary | 대표 목표 Ao에 대한 상세 결과 |
| Pareto graph | 비용-효과 Pareto 그래프 |
| Integrated trade-off map | 목표 Ao 전체 통합 비용-효과 지도 |
| Diagnostics table | 품목별 상세 진단표 |

---

## 14. 실행 방법

필요 라이브러리는 다음과 같습니다.

```bash
pip install numpy pandas matplotlib openpyxl
```

실행 방법은 다음과 같습니다.

```bash
python nsga_step6_lead_time_shortage_integrated.py
```

만약 파일이 `.txt` 형식이라면 `.py`로 확장자를 변경한 뒤 실행합니다.

```text
nsga_step6_lead_time_shortage_integrated.txt
→ nsga_step6_lead_time_shortage_integrated.py
```

---

## 15. Colab 실행 방법

Google Colab에서 실행하려면 코드 상단을 다음처럼 변경합니다.

```python
USE_COLAB_UPLOAD = True
```

그러면 실행 시 파일 업로드 창이 나타나고, 업로드한 Excel 파일이 입력자료로 사용됩니다.

---

## 16. 결과 해석 방법

| 상황 | 해석 |
|---|---|
| `Best Ao`가 높고 `total_cost`가 낮음 | 비용 대비 효과가 좋은 해일 가능성 |
| `DT_wait_ratio`가 높음 | 재고정책이 Ao 개선에 큰 영향을 줌 |
| `DT_restore_ratio`가 높음 | 재고보다 정비시간 개선이 중요할 수 있음 |
| `p_need_2y`는 낮지만 `stock_cap`이 큼 | 고장빈도는 낮지만 리드타임 또는 영향도가 큰 품목일 수 있음 |
| `selected_manage = 1` | NSGA-II가 재고 관리 대상으로 선택한 품목 |
| `total_stock_best` | 최종 권장 재고수량 |
| `sO_best`, `sI_best`, `sD_best` | O/I/D 계층별 권장 재고수량 |

---

## 17. 주의사항

### 17.1 Failure_Rate 단위 확인

OPUS10 자료라면 다음 설정을 사용합니다.

```python
FAILURE_RATE_UNIT = "per_million_hours"
```

이미 연간 고장률이면 다음처럼 변경합니다.

```python
FAILURE_RATE_UNIT = "annual_rate"
```

연간 고장확률이면 다음처럼 변경합니다.

```python
FAILURE_RATE_UNIT = "annual_probability"
```

---

### 17.2 QPA 확인

QPA가 없으면 모든 품목이 1로 처리됩니다.

실제 장비 내 동일 품목 수량이 중요하면 반드시 QPA를 입력해야 합니다.

---

### 17.3 FLEET_SIZE 확인

기본값은 1입니다.

```python
FLEET_SIZE = 1.0
```

실제 운용대수가 있으면 반드시 수정해야 합니다.

---

### 17.4 DRM Excel 주의

DRM은 문서보안 또는 복사방지 기능입니다.

DRM으로 보호된 Excel 파일은 `pandas`가 읽지 못할 수 있습니다. 이 경우 일반 `.xlsx` 파일로 다시 저장한 후 사용해야 합니다.

---

### 17.5 실행시간

품목 수가 많고 target grid가 많으면 실행시간이 길어질 수 있습니다.

먼저 preview 설정으로 검증한 뒤 정식 실행하는 것을 권장합니다.

---

## 18. 권장 GitHub 파일 구조

```text
project/
├── README.md
├── nsga_step6_lead_time_shortage_integrated.py
├── radar_1000_parts_bom.xlsx
├── output/
│   ├── summary_by_target.csv
│   ├── integrated_solutions.csv
│   ├── diagnostics_table.csv
│   └── pareto_curve.png
```

| 파일 | 설명 |
|---|---|
| `README.md` | 모델 설명 문서 |
| `nsga_step6_lead_time_shortage_integrated.py` | Step-6 기준 최종 분석 코드 |
| `radar_1000_parts_bom.xlsx` | 입력 BOM 및 품목 데이터 |
| `summary_by_target.csv` | 목표 Ao별 요약 결과 |
| `integrated_solutions.csv` | 전체 target sweep 통합 해집합 |
| `diagnostics_table.csv` | 품목별 진단표 |
| `pareto_curve.png` | 비용-효과 Pareto 그래프 |

---

## 19. 연구모형 설명 문장

논문 또는 기술보고서에서는 다음과 같이 설명할 수 있습니다.

> 본 연구모형은 OPUS10 형식의 백만시간당 고장률을 연간 고장강도로 변환하고, 장비대당 품목수량(QPA) 및 운용대수(FLEET_SIZE)를 반영하여 장비 기준 고장강도와 전체 운용대수 기준 수리부속 수요강도를 분리하였다. 이후 리드타임 동안의 포아송 수요를 기반으로 재고부족확률을 산정하고, NSGA-II 알고리즘을 이용하여 비용, 목표 운용가용도 미달량, 관리품목/재고수량 부담을 동시에 최소화하는 Pareto 최적 재고대안을 도출하였다.

간단히 표현하면 다음과 같습니다.

> 본 모델은 NSGA-II 기반 다목적 진화최적화 알고리즘을 활용하여 수리부속 재고수준의 비용-효과 trade-off를 분석하고, 목표 운용가용도 달성을 위한 Pareto 최적 재고정책을 도출하는 의사결정 지원모델이다.

---

## 20. 주요 약어 및 컬럼 용어집

| 용어 | 한글 의미 | 설명 |
|---|---|---|
| `Ao` | 운용가용도 | 장비가 필요한 시간 중 실제 운용 가능한 비율 |
| `BOM` | 부품구성표 | Bill of Materials |
| `CM` | 고장정비 | Corrective Maintenance |
| `PM` | 예방정비 | Preventive Maintenance |
| `QPA` | 장비대당 품목수량 | 장비 1대에 들어가는 해당 부품 수량 |
| `FLEET_SIZE` | 운용대수 | 전체 운용 장비 수 |
| `Failure_Rate` | 고장률 | 품목 고장 발생률 |
| `MTBF_Hours` | 평균고장간격 | 고장과 고장 사이의 평균 시간 |
| `Maint_Echelon` | 정비계층 | O/I/D 정비 수준 |
| `Lead Time` | 리드타임 | 부품 확보까지 걸리는 시간 |
| `Transport Time` | 수송시간 | 물류 이동에 필요한 시간 |
| `Condemnation_Rate_Pct` | 폐기율 | 수리 불가 후 폐기될 비율 |
| `lambda` | 고장강도 | 일정 기간 동안 기대되는 고장횟수 |
| `lambda_system` | 장비 기준 고장강도 | 장비 1대 기준 고장강도 |
| `lambda_demand` | 수요 기준 고장강도 | 전체 운용대수 기준 수리부속 수요강도 |
| `p_need_2y` | 2년 내 필요확률 | 2년 동안 해당 수리부속이 필요할 확률 |
| `stock_cap` | 재고상한 | 최적화 중 허용하는 최대 재고수량 |
| `selected_manage` | 관리대상 선택 여부 | 1이면 선택, 0이면 미선택 |
| `sO_best` | O계층 재고 | 부대정비 수준 권장 재고 |
| `sI_best` | I계층 재고 | 야전정비 수준 권장 재고 |
| `sD_best` | D계층 재고 | 창정비 수준 권장 재고 |
| `Pareto front` | 파레토 전선 | 비용-효과 최적해 경계 |
| `C-E curve` | 비용-효과 곡선 | Cost-Effectiveness curve |
| `target sweep` | 목표값 순회분석 | 여러 목표 Ao를 바꿔가며 분석 |
| `diagnostics table` | 진단표 | 품목별 계산결과 상세표 |

---

## 21. 라이선스

본 저장소의 라이선스는 사용자가 GitHub 정책에 맞게 별도 지정해야 합니다.

공개 저장소로 운영할 경우 다음 라이선스를 검토할 수 있습니다.

- MIT License
- Apache License 2.0

---

## 22. 작성 기준

본 README는 **Step-6 기준 모델**을 설명합니다.

Step-6 기준 핵심 특징은 다음과 같습니다.

- OPUS10 백만시간당 고장률 변환
- QPA 반영
- PMIN 후보선별 완화
- `lambda_system` / `lambda_demand` 분리
- 리드타임 수요 기반 부족확률
- NSGA-II 기반 Pareto 최적화
- target Ao sweep 기반 통합 trade-off map
