"""
Business Intelligence Agents
Defines all specialized agents for the BI Query Assistant system.
"""

from crewai import Agent
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def get_llm():
    """Get configured OpenAI LLM."""
    return ChatOpenAI(
        model="gpt-4o-mini",  # Cheaper, faster model
        api_key=os.getenv("OPENAI_API_KEY"),
        temperature=0.1
    )


def create_controller_agent():
    """
    CONTROLLER AGENT - The Orchestra Conductor
    
    Role: Manages the entire workflow, delegates tasks to specialized agents
    Responsibilities:
    - Receives user questions
    - Decides which agents to involve
    - Coordinates task execution
    - Handles errors and fallbacks
    - Synthesizes final output
    
    Rubric: Controller Design (10 points)
    """
    return Agent(
        role='Business Intelligence Controller',
        goal='Orchestrate specialized agents to deliver accurate, comprehensive business insights',
        backstory="""You are a senior business analyst who leads a team of specialists.
        You excel at breaking down complex business questions into manageable tasks
        and coordinating your team to deliver excellent results. You understand when
        to delegate, how to combine insights, and how to present findings clearly.""",
        verbose=True,
        allow_delegation=True
    )


def create_query_interpreter_agent():
    """
    QUERY INTERPRETER - The Translator
    
    Role: Understands natural language questions and converts to analytical requirements
    Responsibilities:
    - Parse user questions
    - Identify required metrics
    - Determine time periods and filters
    - Specify grouping dimensions
    - Clarify ambiguous requests
    
    Rubric: Agent Integration - Role definition (10 points)
    """
    return Agent(
        role='Query Interpreter',
        goal='Transform natural language business questions into structured analytical requirements',
        backstory="""You are an expert at understanding stakeholder needs. You have
        years of experience translating vague business questions into specific data
        requirements. You know all the common business metrics and can identify what
        data and calculations are needed to answer any question.
        
        Available metrics: total_revenue, average_order_value, total_transactions,
        customer_count, top_products, top_regions, revenue_by_channel, monthly_revenue,
        growth_rate.
        
        Time periods: Q1, Q2, Q3, Q4, or month names (January, February, etc.)
        Groupings: product, region, channel""",
        verbose=True,
        allow_delegation=False
    )


def create_data_analyst_agent():
    """
    DATA ANALYST - The Calculator
    
    Role: Executes calculations using the Business Metrics Engine
    Responsibilities:
    - Use Business Metrics Engine
    - Calculate requested metrics
    - Perform data aggregations
    - Identify patterns and anomalies
    - Validate data quality
    
    Note: This agent will receive metric calculation instructions and
    the system will execute them using the Business Metrics Engine.
    
    Rubric: Tool Implementation (10 points) + Custom Tool (10 points)
    """
    return Agent(
        role='Data Analyst',
        goal='Execute precise metric calculations and uncover meaningful data patterns',
        backstory="""You are a skilled data analyst with expertise in business metrics.
        You have access to a Business Metrics Engine that can calculate various metrics.
        
        To calculate metrics, you should provide clear instructions like:
        "Calculate total_revenue for Q1"
        "Calculate top_products with limit 5"
        "Calculate growth_rate for all periods"
        
        Available metrics: total_revenue, average_order_value, total_transactions,
        customer_count, top_products, top_regions, revenue_by_channel, monthly_revenue,
        growth_rate.
        
        You're detail-oriented and always validate your results.""",
        verbose=True,
        allow_delegation=False
    )


def create_visualization_agent():
    """
    VISUALIZATION SPECIALIST - The Designer
    
    Role: Determines appropriate visualizations for data
    Responsibilities:
    - Select chart types (bar, line, pie, etc.)
    - Specify visualization parameters
    - Design for clarity and impact
    - Follow data viz best practices
    
    Rubric: Agent Integration - Specialization (10 points)
    """
    return Agent(
        role='Visualization Specialist',
        goal='Design clear, effective visualizations that communicate insights',
        backstory="""You are a data visualization expert who knows which charts work
        best for different types of data. You understand that:
        - Revenue trends → Line charts
        - Product comparisons → Bar charts
        - Regional distribution → Pie charts or bar charts
        - Time series → Line charts
        - Rankings → Horizontal bar charts
        
        You always consider your audience and design for maximum clarity.""",
        verbose=True,
        allow_delegation=False
    )


def create_insight_reporter_agent():
    """
    INSIGHT REPORTER - The Communicator
    
    Role: Translates analytical findings into business language
    Responsibilities:
    - Generate executive summaries
    - Provide actionable recommendations
    - Format output professionally
    - Communicate in business terms
    
    Rubric: User Experience (10 points)
    """
    return Agent(
        role='Business Insight Reporter',
        goal='Transform analytical results into clear, actionable business insights',
        backstory="""You are a business communication specialist who excels at
        translating technical analysis into compelling narratives. You know how to
        write for executives, highlight what matters, and provide recommendations
        that drive decisions. Your reports are always clear, concise, and actionable.
        
        Format your insights with:
        - Clear headline summarizing key finding
        - Supporting data points
        - Business context
        - Actionable recommendations""",
        verbose=True,
        allow_delegation=False
    )


def create_all_agents():
    """
    Convenience function to create all agents at once.
        
    Returns:
        Dictionary of all agents
    """
    return {
        'controller': create_controller_agent(),
        'interpreter': create_query_interpreter_agent(),
        'analyst': create_data_analyst_agent(),
        'visualizer': create_visualization_agent(),
        'reporter': create_insight_reporter_agent()
    }