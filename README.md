# Business Intelligence Query Assistant
Multi-agent AI system for business intelligence queries using CrewAI

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.28.8-green.svg)](https://docs.crewai.com/)

## 🎯 Overview
Multi-agent AI system that orchestrates five specialized agents to answer business questions in natural language, achieving 100% calculation accuracy and generating professional reports in under 30 seconds.

**Key Results:**
- Success Rate: 100% across all query types
- Response Time: 21 seconds average
- Accuracy: 100% validated calculations
- Output: Senior analyst-quality insights

## 📊 System Architecture

User Query → Controller → Query Interpreter → Data Analyst → Visualizer → Reporter → Final Report
                                ->
                     Business Metrics Engine (Custom Tool)


**5 Specialized Agents:**
- **Controller**: Orchestrates workflow
- **Query Interpreter**: Parses natural language
- **Data Analyst**: Calculates metrics (uses custom tool)
- **Visualization Specialist**: Designs charts
- **Insight Reporter**: Generates summaries

## 🛠️ Custom Tool: Business Metrics Engine

9 pre-configured business metrics:

| Metric | Output Example |
|--------|----------------|
| total_revenue | $2,273,662.55 |
| top_products | 1. Laptop: $1.5M |
| growth_rate | +10.24% |
| customer_count | 888 customers |
| monthly_revenue | January: $210K |

**Features:** Time filtering (Q1-Q4, months), dimensional grouping (product, region, channel), automatic validation

## 🚀 Quick Start
```bash
# Clone and setup
git clone https://github.com/g-barla/agentic-ai-bi-query-assistant.git
cd agentic-ai-bi-query-assistant
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure
echo "OPENAI_API_KEY=your_key" > .env

# Run
python run.py
```

## 📖 Usage
```python
from src.main import BIQueryAssistant

assistant = BIQueryAssistant()
result = assistant.process_query("What is our total revenue?")
print(result)
```

**Example Queries:**
- "What is our total revenue?"
- "Show me top 5 products by revenue"
- "What is our month-over-month growth rate?"
- "What was our Q1 revenue?"



## 🔮 Future Enhancements

- Database connectivity (SQL/NoSQL)
- Actual chart generation
- Multi-dataset joins
- Natural language to SQL
- ML-based anomaly detection


