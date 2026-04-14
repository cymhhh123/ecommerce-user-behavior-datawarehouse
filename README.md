# 电商用户行为数仓项目

## 项目背景

为解决电商平台用户行为数据分散、分析困难的问题，构建了一套完整的数据仓库系统，实现从数据采集到业务分析的全流程自动化，为运营决策提供数据支撑。

## 技术栈

**核心技术**：

- **SQL**：Hive SQL、MySQL SQL
- **数据存储**：Hive、MySQL、PostgreSQL
- **数据处理**：Spark、Python (Pandas/NumPy)
- **任务调度**：Airflow
- **数据分析**：SQL、Pandas
- **版本控制**：Git

## 数仓架构

### 分层设计

- **ODS层**（原始数据层）：存储原始用户行为日志，保留数据原貌
- **DIM层**（维度层）：构建用户、产品等维度表，支持多维度分析
- **FACT层**（事实层）：存储用户行为事实数据，按日分区
- **DM层**（数据集市）：聚合分析结果，提供业务指标

### 数据流程

1. **数据采集**：收集用户行为日志（浏览、加购、购买、收藏）
2. **ETL处理**：使用Spark和Python进行数据清洗、转换
3. **数据入库**：将处理后的数据写入Hive数据仓库
4. **任务调度**：使用Airflow编排ETL任务，实现自动化运行
5. **数据分析**：基于数仓数据进行SQL分析，生成业务指标

## 核心指标

### 用户指标

- **活跃用户数**：日/周/月活跃用户统计
- **用户留存率**：新用户7日/30日留存分析
- **购买转化率**：从浏览到购买的转化比例
- **用户行为路径**：用户在平台的行为轨迹分析

### 产品指标

- **产品浏览量**：Top10热门产品分析
- **产品转化率**：各分类产品转化效果
- **产品关联分析**：购买相关性分析

### 销售指标

- **销售额**：日/周/月销售趋势
- **客单价**：平均订单金额
- **复购率**：用户重复购买比例

## 快速开始

### 环境准备

```bash
pip install -r requirements.txt
```

### 数据准备

1. 生成模拟数据：
   ```bash
   python scripts/data_gen/generate_mock_data.py
   ```
2. 创建Hive表结构：
   ```bash
   hive -f sql/ddl/create_tables.sql
   ```

### 运行ETL

1. 启动Airflow：
   ```bash
   airflow webserver -p 8080
   airflow scheduler
   ```
2. 在Airflow界面触发ETL任务

### 数据分析

运行SQL分析脚本：

```bash
hive -f sql/analysis/user_behavior_analysis.sql
```

## 亮点

1. **数仓分层设计**：实现了标准的ODS/DIM/FACT/DM分层架构，体现对数据仓库设计的深刻理解
2. **SQL能力**：编写了复杂的Hive SQL和MySQL SQL，包括分区表、聚合查询、窗口函数等
3. **ETL开发**：使用Python和Spark实现了完整的ETL流程，包括数据清洗、转换和加载
4. **任务调度**：使用Airflow编排ETL任务，实现自动化数据处理流程
5. **数据质量**：实现了数据清洗、去重、验证等数据质量保证措施
6. **业务价值**：通过数据分析为业务决策提供支持，体现数据的实际应用价值
7. **技术广度**：掌握Hive、Spark、Airflow、Python等多种数据技术，展示技术栈的全面性
8. **代码规范**：模块化设计，代码结构清晰，包含完整的测试用例

## 项目结构

```
ecommerce-user-behavior-datawarehouse/
├── docs/                     # 项目文档
│   ├── architecture/         # 架构设计文档
│   ├── requirements/         # 需求文档
│   └── technical/            # 技术文档
├── sql/                      # SQL 脚本
│   ├── ddl/                  # 建表语句
│   ├── dml/                  # 数据操作语句
│   └── analysis/             # 分析SQL
├── data/                     # 数据文件
│   ├── raw/                  # 原始数据
│   ├── processed/            # 处理后的数据
│   └── mock/                 # 模拟数据
├── scripts/                  # 工具脚本
│   ├── etl/                  # ETL 脚本
│   ├── data_gen/             # 数据生成脚本
│   └── utils/                # 工具函数
├── config/                   # 配置文件
│   ├── env/                  # 环境配置
│   └── jobs/                 # 任务配置
├── dags/                     # 任务调度
├── etl/                      # ETL 流程
├── warehouse/                # 数据仓库
│   ├── ods/                  # 原始数据层
│   ├── dim/                  # 维度层
│   ├── fact/                 # 事实层
│   └── dm/                   # 数据集市
├── analysis/                 # 数据分析
│   ├── reports/              # 分析报告
│   └── dashboards/           # 仪表盘
├── api/                      # API 接口
├── tests/                    # 测试代码
├── examples/                 # 示例代码
├── logs/                     # 日志文件
├── deployment/               # 部署配置
├── notebooks/                # Jupyter 笔记本
├── utils/                    # 工具函数
├── monitoring/               # 监控配置
├── README.md                 # 项目说明
├── .gitignore                # Git 忽略文件
└── requirements.txt          # 依赖文件
```

