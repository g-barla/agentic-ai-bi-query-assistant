"""
Business Metrics Engine - Custom Tool
Encapsulates business domain knowledge for common KPI calculations.
"""

import pandas as pd
import os
from typing import Optional


class BusinessMetricsEngine:
    """
    Custom tool that knows how to calculate standard business metrics.
    This encapsulates business domain knowledge - no need for agents 
    to figure out formulas each time.
    """
    
    def __init__(self):
        self.name = "Business Metrics Calculator"
        self.description = (
            "Calculates common business metrics like revenue, growth rate, "
            "customer metrics, and product performance. Knows formulas for "
            "standard business KPIs."
        )
        
        # Business knowledge: metric definitions
        self.METRIC_DEFINITIONS = {
            'total_revenue': {
                'formula': 'sum',
                'column': 'revenue',
                'description': 'Sum of all revenue'
            },
            'average_order_value': {
                'formula': 'mean',
                'column': 'revenue',
                'description': 'Average revenue per transaction'
            },
            'total_transactions': {
                'formula': 'count',
                'column': 'transaction_id',
                'description': 'Total number of transactions'
            },
            'customer_count': {
                'formula': 'unique_count',
                'column': 'customer_id',
                'description': 'Number of unique customers'
            },
            'top_products': {
                'formula': 'group_sum_ranked',
                'column': 'revenue',
                'group_by': 'product',
                'description': 'Products ranked by revenue'
            },
            'top_regions': {
                'formula': 'group_sum_ranked',
                'column': 'revenue',
                'group_by': 'region',
                'description': 'Regions ranked by revenue'
            },
            'revenue_by_channel': {
                'formula': 'group_sum',
                'column': 'revenue',
                'group_by': 'channel',
                'description': 'Revenue by sales channel'
            },
            'monthly_revenue': {
                'formula': 'time_series',
                'column': 'revenue',
                'group_by': 'month_name',
                'description': 'Revenue by month'
            },
            'growth_rate': {
                'formula': 'percentage_change',
                'column': 'revenue',
                'description': 'Month-over-month growth rate'
            }
        }
    
    def calculate(
        self, 
        metric_name: str, 
        dataframe_path: str = "data/sample_sales_data.csv",
        time_period: str = "all", 
        group_by: Optional[str] = None,
        limit: int = 5
    ) -> str:
        """
        Execute metric calculation.
        
        Args:
            metric_name: Name of the metric to calculate
            dataframe_path: Path to data file
            time_period: Time filter (e.g., 'Q1', 'January', 'all')
            group_by: Dimension to group by
            limit: Number of results for rankings
            
        Returns:
            Formatted string with calculation results
        """
        
        try:
            # Check if metric exists
            if metric_name not in self.METRIC_DEFINITIONS:
                available = ', '.join(self.METRIC_DEFINITIONS.keys())
                return f"❌ Metric '{metric_name}' not found.\n\nAvailable: {available}"
            
            # Load data
            if not os.path.exists(dataframe_path):
                return f"❌ Data file not found: {dataframe_path}"
            
            df = pd.read_csv(dataframe_path)
            df['date'] = pd.to_datetime(df['date'])
            
            # Apply time filter
            if time_period != "all":
                df = self._filter_by_time(df, time_period)
                if len(df) == 0:
                    return f"❌ No data for time period: {time_period}"
            
            # Get metric configuration
            metric_def = self.METRIC_DEFINITIONS[metric_name]
            formula = metric_def['formula']
            column = metric_def['column']
            
            # Calculate based on formula
            if formula == 'sum':
                result = df[column].sum()
                return f"✅ {metric_name}: ${result:,.2f}"
            
            elif formula == 'mean':
                result = df[column].mean()
                return f"✅ {metric_name}: ${result:,.2f}"
            
            elif formula == 'count':
                result = len(df)
                return f"✅ {metric_name}: {result:,} transactions"
            
            elif formula == 'unique_count':
                result = df[column].nunique()
                return f"✅ {metric_name}: {result:,} unique {column.replace('_', ' ')}"
            
            elif formula == 'group_sum_ranked':
                group_col = group_by or metric_def.get('group_by')
                if not group_col:
                    return "❌ This metric requires a group_by parameter"
                
                result = df.groupby(group_col)[column].sum().sort_values(ascending=False).head(limit)
                
                output = f"✅ {metric_name} (Top {limit}):\n\n"
                for rank, (name, value) in enumerate(result.items(), 1):
                    output += f"{rank}. {name}: ${value:,.2f}\n"
                return output
            
            elif formula == 'group_sum':
                group_col = group_by or metric_def.get('group_by')
                result = df.groupby(group_col)[column].sum().sort_values(ascending=False)
                
                output = f"✅ {metric_name}:\n\n"
                for name, value in result.items():
                    output += f"- {name}: ${value:,.2f}\n"
                return output
            
            elif formula == 'time_series':
                monthly = df.groupby('month_name')[column].sum()
                month_order = ['January', 'February', 'March', 'April', 'May', 'June',
                             'July', 'August', 'September', 'October', 'November', 'December']
                monthly = monthly.reindex([m for m in month_order if m in monthly.index])
                
                output = f"✅ {metric_name}:\n\n"
                for month, value in monthly.items():
                    output += f"- {month}: ${value:,.2f}\n"
                return output
            
            elif formula == 'percentage_change':
                monthly = df.groupby(df['date'].dt.to_period('M'))[column].sum()
                monthly = monthly.sort_index()
                
                if len(monthly) < 2:
                    return "❌ Need at least 2 months for growth rate"
                
                latest = monthly.iloc[-1]
                previous = monthly.iloc[-2]
                growth = ((latest - previous) / previous) * 100
                
                output = f"✅ {metric_name}:\n\n"
                output += f"Latest month: ${latest:,.2f}\n"
                output += f"Previous month: ${previous:,.2f}\n"
                output += f"Growth rate: {growth:+.2f}%\n"
                
                if growth > 0:
                    output += f"\n📈 Positive growth"
                else:
                    output += f"\n📉 Negative growth"
                
                return output
            
            else:
                return f"❌ Unknown formula: {formula}"
        
        except Exception as e:
            return f"❌ Error calculating metric: {str(e)}"
    
    def _filter_by_time(self, df, time_period):
        """Filter data by time period."""
        
        # Quarter filters
        if time_period in ['Q1', 'Q2', 'Q3', 'Q4']:
            quarter_num = int(time_period[1])
            return df[df['quarter'] == quarter_num]
        
        # Month filters
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']
        if time_period in months:
            return df[df['month_name'] == time_period]
        
        # Year filter
        if time_period.isdigit():
            return df[df['year'] == int(time_period)]
        
        return df
    
    def list_metrics(self) -> str:
        """Return list of available metrics."""
        output = "Available Metrics:\n\n"
        for name, definition in self.METRIC_DEFINITIONS.items():
            output += f"- {name}: {definition['description']}\n"
        return output