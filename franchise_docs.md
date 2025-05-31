# Franchise Comparison Framework

## Introduction

This document outlines the comprehensive comparison framework for the franchise directory platform. The framework enables users to effectively compare franchise opportunities across multiple dimensions, using standardized metrics and visualization techniques. It is designed to support both casual users seeking basic comparisons and sophisticated investors requiring in-depth analysis.

## Design Principles

1. [&lt;RawText children='Standardization'&gt;]
2. [&lt;RawText children='Normalization'&gt;]
3. [&lt;RawText children='Completeness Handling'&gt;]
4. [&lt;RawText children='Visual Clarity'&gt;]
5. [&lt;RawText children='Monetization Support'&gt;]
6. [&lt;RawText children='Mass Appeal'&gt;]

## Comparable Metrics Framework

### Core Comparison Categories

1. [&lt;RawText children='Investment &amp; Costs'&gt;]
2. [&lt;RawText children='Financial Performance'&gt;]
3. [&lt;RawText children='Growth &amp; Stability'&gt;]
4. [&lt;RawText children='Support &amp; Training'&gt;]
5. [&lt;RawText children='Legal &amp; Contractual Terms'&gt;]
6. [&lt;RawText children='Operational Requirements'&gt;]
7. [&lt;RawText children='Market Positioning'&gt;]

## Detailed Metric Breakdown

### 1. Investment &amp; Costs

| Metric   | Source   | Data Type   | Normalization Method   | Comparison Logic   |
|----------|----------|-------------|------------------------|--------------------|
|          |          |             |                        |                    |

Total Initial Investment Franchise Fee Royalty Fee Marketing Fee Estimated Payback Period Initial Inventory Cost Real Estate Requirements Equipment Costs Working Capital Requirements Total Investment per Square Foot

### 2. Financial Performance

| Metric   | Source   | Data Type   | Normalization Method   | Comparison Logic   |
|----------|----------|-------------|------------------------|--------------------|
|          |          |             |                        |                    |

Average Unit Revenue Revenue Range Average Gross Profit EBITDA Margin Cost of Goods Sold Labor Costs Occupancy Costs Average Ticket Size Sales per Square Foot Return on Investment

### 3. Growth &amp; Stability

| Metric   | Source   | Data Type   | Normalization Method   | Comparison Logic   |
|----------|----------|-------------|------------------------|--------------------|
|          |          |             |                        |                    |

Total Unit Count Unit Growth Rate (3-Year) Unit Growth Rate (5-Year) Closure Rate Transfer Rate Years in Business Years Franchising International Presence Projected New Units Franchisee Satisfaction

### 4. Support &amp; Training

| Metric   | Source   | Data Type   | Normalization Method   | Comparison Logic   |
|----------|----------|-------------|------------------------|--------------------|
|          |          |             |                        |                    |

Initial Training Duration Ongoing Training Frequency Marketing Support Technology Systems Field Support Ratio Site Selection Assistance Grand Opening Support R&amp;D Investment Supply Chain Support Franchisee Advisory Council

### 5. Legal &amp; Contractual Terms

| Metric   | Source   | Data Type   | Normalization Method   | Comparison Logic   |
|----------|----------|-------------|------------------------|--------------------|
|          |          |             |                        |                    |

Franchise Agreement Term Renewal Terms Territory Protection Transfer Fee Non-Compete Terms Termination Conditions Personal Guarantee Required Litigation History Dispute Resolution Method Required Arbitration

### 6. Operational Requirements

| Metric   | Source   | Data Type   | Normalization Method   | Comparison Logic   |
|----------|----------|-------------|------------------------|--------------------|
|          |          |             |                        |                    |

Owner Involvement Required Staffing Requirements Operating Hours Real Estate Type Inventory Requirements POS/Technology Requirements Approved Supplier Restrictions Operational Audit Frequency Minimum Performance Requirements Multi-Unit Development Options

### 7. Market Positioning

| Metric   | Source   | Data Type   | Normalization Method   | Comparison Logic   |
|----------|----------|-------------|------------------------|--------------------|
|          |          |             |                        |                    |

Industry Category Target Customer Demographics Price Point Competitive Density Market Saturation Brand Recognition Online Presence Social Media Following Customer Ratings Awards &amp; Recognition

## Normalization Rules and Methods

### 1. Range Standardization

For metrics reported as ranges (e.g., investment amounts):

```
standardized_value = (minimum_value + maximum_value) / 2
```

When comparing ranges:

```
overlap_percentage = (min(range1_max, range2_max) - max(range1_min, range2_min)) / 
                     (max(range1_max, range2_max) - min(range1_min, range2_min))
```

### 2. Currency Normalization

For financial metrics reported in different currencies:

```
normalized_value = original_value * exchange_rate_to_base_currency
```

For historical data, use the exchange rate from the reporting date.

### 3. Percentage vs. Fixed Amount

For fees reported as either percentages or fixed amounts:

```
if fee_type == "fixed":
    normalized_percentage = fixed_amount / average_unit_revenue * 100
else:
    normalized_percentage = percentage_value
```

### 4. Categorical Scoring

For categorical data requiring comparison:

1. Define a standardized scoring rubric for each category
2. Assign scores based on predefined criteria
3. Use consistent scale (typically 1-5) across all categorical metrics

Example for Territory Protection:

- 5: Exclusive territory with population/geographic guarantees
- 4: Exclusive territory with limited exceptions
- 3: Protected territory with standard exceptions
- 2: Limited protection with significant exceptions
- 1: No territorial protection

### 5. Time Period Standardization

For metrics covering different time periods:

```
annualized_value = original_value * (12 / reporting_period_months)
```

For growth rates over different periods:

```
standardized_growth_rate = (1 + original_growth_rate)^(standard_period/original_period) - 1
```

### 6. Missing Data Handling

When comparing metrics with missing data:

1. Clearly indicate missing data points
2. Exclude missing data from averages and rankings
3. Use industry averages as substitutes when appropriate (clearly marked)
4. Calculate confidence scores for comparisons based on data completeness

## Comparison Logic Implementation

### Direct Numerical Comparison

For metrics with standardized numerical values:

```
difference = franchise1_value - franchise2_value
percentage_difference = (franchise1_value - franchise2_value) / franchise2_value * 100
z_score = (franchise_value - industry_average) / industry_standard_deviation
```

### Categorical Comparison

For categorical data:

1. Map categories to standardized values
2. Compare based on predefined hierarchies
3. Use similarity scoring for multi-attribute categories

### Weighted Scoring

For overall comparison scores:

```
overall_score = sum(metric_value * weight) / sum(weights)
```

Weights should be:

- Customizable by users (premium feature)
- Preset for different user personas
- Adjusted based on data confidence

## Comparison UI Patterns

### 1. Side-by-Side Comparison Table

Purpose : Detailed metric-by-metric comparison

Features :

- Sortable columns
- Color-coded differences
- Expandable sections for detailed metrics
- Data confidence indicators
- Export functionality (premium)

Visual Treatment :

- Clean tabular format
- Sticky header for scrolling
- Highlight significant differences
- Clear section divisions

Example Structure :

```
┌─────────────────┬────────────────┬────────────────┬────────────────┐
│ Metric          │ Franchise A    │ Franchise B    │ Difference     │
├─────────────────┼────────────────┼────────────────┼────────────────┤
│ Investment      │ $250K-$400K    │ $300K-$450K    │ +$50K avg      │
│ Royalty Fee     │ 6%             │ 5%             │ -1%            │
│ Unit Count      │ 500            │ 350            │ -150           │
│ Growth Rate     │ 8.5%           │ 12.3%          │ +3.8%          │
└─────────────────┴────────────────┴────────────────┴────────────────┘
```

### 2. Radar/Spider Chart

Purpose : Multi-dimensional visual comparison

Features :

- 5-8 key dimensions on radar axes
- Overlapping franchise profiles
- Adjustable dimensions (premium)
- Industry average overlay

Visual Treatment :

- Clear axis labels
- Distinct colors for each franchise
- Adequate spacing for readability
- Interactive tooltips with detailed metrics

Example Structure :

```
Investment
                    │
                    │
                    │
                    │
Support ────────────┼────────────── Growth
                    │
                    │
                    │
                    │
               Performance
```

### 3. Bar Chart Comparison

Purpose : Direct metric comparison with context

Features :

- Grouped or stacked bars
- Industry average markers
- Percentile indicators
- Range visualization

Visual Treatment :

- Consistent color scheme
- Clear value labels
- Appropriate scale selection
- Sorting options

Example Structure :

```
Revenue ($K)
│
│    ┌───┐
│    │   │
│    │   │         ┌───┐
│    │   │         │   │
│    │   │         │   │         ┌───┐
│    │   │         │   │         │   │
└────┴───┴─────────┴───┴─────────┴───┴────
    Franchise A   Franchise B   Industry Avg
```

### 4. Scorecard Comparison

Purpose : Simplified overall comparison

Features :

- Summary scores by category
- Visual indicators of strengths/weaknesses
- Quick glance comparison
- Customizable weighting (premium)

Visual Treatment :

- Card-based layout
- Clear scoring system
- Visual indicators (stars, bars, etc.)
- Expandable for details

Example Structure :

```
┌─────────────────────────────────────────────────────┐
│ INVESTMENT SCORE                                    │
│                                                     │
│ Franchise A: ★★★★☆  Franchise B: ★★★☆☆              │
│                                                     │
│ A has 15% lower initial investment but 1% higher    │
│ ongoing fees                                        │
└─────────────────────────────────────────────────────┘
```

### 5. Timeline Comparison

Purpose : Compare historical performance and projections

Features :

- Growth trajectories
- Unit count evolution
- Financial performance trends
- Milestone markers

Visual Treatment :

- Clear timeline axis
- Consistent data points
- Trend line visualization
- Future projection indicators

Example Structure :

```
Units
│                                      ┌─── Franchise A
│                              ┌───────┘
│                      ┌───────┘
│              ┌───────┘
│      ┌───────┘                       ┌─── Franchise B
│      │                       ┌───────┘
│      │               ┌───────┘
│      │       ┌───────┘
└──────┴───────┴───────┴───────┴───────┴─────
    2020      2021      2022      2023      2024
```

## Comparison Features by User Tier

### Free Tier

Available Comparisons :

- Basic side-by-side comparison (up to 3 franchises)
- Limited metrics (investment, royalty, unit count)
- Basic bar chart visualization
- Industry category comparison

Limitations :

- No historical data comparison
- No export functionality
- Limited customization
- No detailed financial metrics

### Premium Tier

Additional Comparisons :

- Extended side-by-side comparison (up to 10 franchises)
- Full metric set including financial performance
- All visualization types
- Historical data (3 years)
- Custom weighting of factors
- Export to PDF/Excel
- Saved comparison sets

### Premium+ Tier

Advanced Comparisons :

- Unlimited franchise comparison
- Custom metric creation
- Full historical data
- Predictive modeling
- ROI calculator integration
- API access for data export
- White-label reporting

## Implementation Considerations

### Data Quality Management

1. [&lt;RawText children='Confidence Scoring'&gt;]
    - Assign confidence scores to each metric based on data source reliability
    - Adjust visualization to reflect confidence levels
    - Provide clear indicators for estimated or derived data
2. [&lt;RawText children='Missing Data Handling'&gt;]
    - Implement consistent placeholders for missing data
    - Provide explanatory tooltips for gaps
    - Use industry averages as fallbacks with clear marking
3. [&lt;RawText children='Data Freshness'&gt;]
    - Clearly indicate data collection dates
    - Prioritize most recent FDD data
    - Implement automated data validation checks

### Performance Optimization

1. [&lt;RawText children='Precomputed Comparisons'&gt;]
    - Calculate common comparison sets in advance
    - Cache frequently compared franchises
    - Implement progressive loading for large comparison sets
2. [&lt;RawText children='Visualization Rendering'&gt;]
    - Use efficient charting libraries
    - Implement canvas-based rendering for complex visualizations
    - Optimize for mobile devices
3. [&lt;RawText children='Data Transfer Efficiency'&gt;]
    - Implement data compression for large datasets
    - Use incremental loading for extended comparisons
    - Structure API responses for minimal payload size

### User Experience Considerations

1. [&lt;RawText children='Guided Comparison Flow'&gt;]
    - Step-by-step comparison setup wizard
    - Recommended metrics based on user persona
    - Saved comparison templates
2. [&lt;RawText children='Contextual Education'&gt;]
    - Tooltips explaining metric significance
    - Comparison interpretation guides
    - Industry benchmark context
3. [&lt;RawText children='Accessibility'&gt;]
    - Alternative text for all visualizations
    - Keyboard navigation support
    - High-contrast mode option
    - Screen reader compatibility

## Sample Comparison Queries

### Basic Investment Comparison

```
SELECT 
    f.name AS franchise_name,
    (SELECT MIN(amount_low) FROM initial_investments 
     WHERE fdd_id = fdd.id AND category = 'Total Investment') AS min_investment,
    (SELECT MAX(amount_high) FROM initial_investments 
     WHERE fdd_id = fdd.id AND category = 'Total Investment') AS max_investment,
    (SELECT amount_percentage FROM ongoing_fees 
     WHERE fdd_id = fdd.id AND fee_type = 'Royalty') AS royalty_percentage
FROM 
    franchises f
JOIN 
    franchise_disclosure_documents fdd ON f.id = fdd.franchise_id
WHERE 
    f.id IN ('franchise_id_1', 'franchise_id_2', 'franchise_id_3')
    AND fdd.is_current = TRUE;
```

### Financial Performance Comparison

```
SELECT 
    f.name AS franchise_name,
    fp.metric_name,
    fp.value_average,
    fp.value_median,
    fp.sample_size,
    i.name AS industry
FROM 
    financial_performance fp
JOIN 
    franchise_disclosure_documents fdd ON fp.fdd_id = fdd.id
JOIN 
    franchises f ON fdd.franchise_id = f.id
JOIN 
    franchise_industries fi ON f.id = fi.franchise_id AND fi.is_primary = TRUE
JOIN 
    industries i ON fi.industry_id = i.id
WHERE 
    f.id IN ('franchise_id_1', 'franchise_id_2', 'franchise_id_3')
    AND fdd.is_current = TRUE
    AND fp.metric_name IN ('Average Unit Revenue', 'EBITDA Margin')
ORDER BY 
    fp.metric_name, f.name;
```

### Growth Trend Comparison

```
WITH yearly_counts AS (
    SELECT 
        f.id AS franchise_id,
        f.name AS franchise_name,
        oi.year,
        SUM(oi.opened_count) AS opened,
        SUM(oi.closed_count) AS closed,
        SUM(opened_count - closed_count) AS net_growth
    FROM 
        franchises f
    JOIN 
        franchise_disclosure_documents fdd ON f.id = fdd.franchise_id
    JOIN 
        outlet_information oi ON fdd.id = oi.fdd_id
    WHERE 
        f.id IN ('franchise_id_1', 'franchise_id_2', 'franchise_id_3')
    GROUP BY 
        f.id, f.name, oi.year
)
SELECT 
    franchise_name,
    year,
    opened,
    closed,
    net_growth,
    SUM(net_growth) OVER (PARTITION BY franchise_id ORDER BY year) AS cumulative_units
FROM 
    yearly_counts
ORDER BY 
    franchise_name, year;
```

## Conclusion

The franchise comparison framework provides a comprehensive system for standardizing, normalizing, and visualizing franchise data to enable effective comparison. By implementing tiered access to comparison features, the platform can support both basic users and sophisticated investors while creating clear monetization pathways through premium functionality.

The framework's flexibility in handling varying levels of data completeness ensures that all franchise listings can be compared effectively, while the standardized metrics and visualization patterns enable users to make informed decisions based on their specific priorities and requirements.

---

# Franchise Directory Database Schema Design

## Introduction

This document outlines the comprehensive database schema design for a franchise directory platform using Supabase (PostgreSQL). The schema is designed to capture, store, and present structured data from Franchise Disclosure Documents (FDDs), enabling easy comparison and analysis of franchise opportunities.

## Design Principles

1. [&lt;RawText children='Comprehensive Coverage'&gt;]
2. [&lt;RawText children='Scalability'&gt;]
3. [&lt;RawText children='Normalization'&gt;]
4. [&lt;RawText children='Temporal Tracking'&gt;]
5. [&lt;RawText children='Performance Optimization'&gt;]
6. [&lt;RawText children='Monetization Support'&gt;]
7. [&lt;RawText children='Mass Appeal'&gt;]

## Database Schema Overview

The database schema is organized into several interconnected components:

1. [&lt;RawText children='Core Entities'&gt;]
2. [&lt;RawText children='Financial Data'&gt;]
3. [&lt;RawText children='Operational Data'&gt;]
4. [&lt;RawText children='Legal Information'&gt;]
5. [&lt;RawText children='Analytical Components'&gt;]

## Entity Relationship Diagram (ERD)

```
[Diagram will be created separately and referenced here]
```

## Core Tables

### franchisors

Primary table for franchisor companies.

```
CREATE TABLE franchisors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    legal_name TEXT NOT NULL,
    parent_company_id UUID REFERENCES franchisors(id),
    founded_date DATE,
    headquarters_address JSONB,
    website_url TEXT,
    logo_url TEXT,
    description TEXT,
    industry_primary_id UUID REFERENCES industries(id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchisor\_predecessors

Tracks predecessor companies for franchisors (Item 1).

```
CREATE TABLE franchisor_predecessors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchisor_id UUID NOT NULL REFERENCES franchisors(id),
    predecessor_name TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    date_range TSTZRANGE,
    details TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchisor\_affiliates

Tracks affiliate companies for franchisors (Item 1).

```
CREATE TABLE franchisor_affiliates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchisor_id UUID NOT NULL REFERENCES franchisors(id),
    affiliate_name TEXT NOT NULL,
    relationship_type TEXT NOT NULL,
    business_description TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchises

Primary table for franchise offerings.

```
CREATE TABLE franchises (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchisor_id UUID NOT NULL REFERENCES franchisors(id),
    name TEXT NOT NULL,
    concept_description TEXT NOT NULL,
    business_model TEXT NOT NULL,
    year_began_franchising INTEGER,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    total_units_count INTEGER,
    company_owned_count INTEGER,
    franchised_count INTEGER,
    international_count INTEGER,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchise\_disclosure\_documents

Stores metadata about each FDD document.

```
CREATE TABLE franchise_disclosure_documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchise_id UUID NOT NULL REFERENCES franchises(id),
    year INTEGER NOT NULL,
    effective_date DATE NOT NULL,
    document_url TEXT,
    is_current BOOLEAN NOT NULL DEFAULT FALSE,
    registration_states TEXT[],
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    UNIQUE(franchise_id, year)
);
```

### key\_personnel

Stores information about key officers and directors (Item 2).

```
CREATE TABLE key_personnel (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchisor_id UUID NOT NULL REFERENCES franchisors(id),
    name TEXT NOT NULL,
    title TEXT NOT NULL,
    start_date DATE,
    experience_summary TEXT,
    prior_experience JSONB,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### litigation\_records

Stores litigation information (Item 3).

```
CREATE TABLE litigation_records (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    case_name TEXT NOT NULL,
    case_number TEXT,
    court TEXT,
    filing_date DATE,
    status TEXT NOT NULL,
    description TEXT NOT NULL,
    resolution TEXT,
    resolution_date DATE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### bankruptcy\_records

Stores bankruptcy information (Item 4).

```
CREATE TABLE bankruptcy_records (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    entity_name TEXT NOT NULL,
    entity_type TEXT NOT NULL,
    court TEXT,
    filing_date DATE,
    case_number TEXT,
    disposition TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### initial\_fees

Stores initial franchise fee information (Item 5).

```
CREATE TABLE initial_fees (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    fee_type TEXT NOT NULL,
    amount_low DECIMAL(12,2),
    amount_high DECIMAL(12,2),
    is_fixed BOOLEAN NOT NULL DEFAULT FALSE,
    payment_terms TEXT,
    refund_conditions TEXT,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### ongoing\_fees

Stores ongoing fee information (Item 6).

```
CREATE TABLE ongoing_fees (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    fee_type TEXT NOT NULL,
    calculation_method TEXT NOT NULL,
    amount_percentage DECIMAL(5,2),
    amount_fixed DECIMAL(12,2),
    frequency TEXT NOT NULL,
    payment_terms TEXT,
    collection_method TEXT,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### initial\_investments

Stores estimated initial investment information (Item 7).

```
CREATE TABLE initial_investments (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    category TEXT NOT NULL,
    amount_low DECIMAL(12,2) NOT NULL,
    amount_high DECIMAL(12,2) NOT NULL,
    is_required BOOLEAN NOT NULL DEFAULT TRUE,
    payment_method TEXT,
    payment_timing TEXT,
    recipient TEXT,
    refundable BOOLEAN NOT NULL DEFAULT FALSE,
    refund_conditions TEXT,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### supplier\_restrictions

Stores information about supplier restrictions (Item 8).

```
CREATE TABLE supplier_restrictions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    category TEXT NOT NULL,
    restriction_type TEXT NOT NULL,
    approved_suppliers TEXT[],
    franchisor_is_supplier BOOLEAN NOT NULL DEFAULT FALSE,
    franchisor_revenue_percentage DECIMAL(5,2),
    specification_details TEXT,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchisee\_obligations

Stores franchisee obligations (Item 9).

```
CREATE TABLE franchisee_obligations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    obligation_category TEXT NOT NULL,
    description TEXT NOT NULL,
    fdd_section_reference TEXT,
    agreement_section_reference TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### financing\_options

Stores financing information (Item 10).

```
CREATE TABLE financing_options (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    financing_type TEXT NOT NULL,
    provider TEXT NOT NULL,
    is_direct BOOLEAN NOT NULL DEFAULT FALSE,
    amount_low DECIMAL(12,2),
    amount_high DECIMAL(12,2),
    term_length TEXT,
    interest_rate TEXT,
    down_payment TEXT,
    security_required TEXT,
    liability TEXT,
    loss_remedies TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchisor\_assistance

Stores information about franchisor assistance (Item 11).

```
CREATE TABLE franchisor_assistance (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    assistance_type TEXT NOT NULL,
    assistance_phase TEXT NOT NULL,
    description TEXT NOT NULL,
    provider TEXT,
    duration TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### training\_programs

Stores information about training programs (Item 11).

```
CREATE TABLE training_programs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    program_name TEXT NOT NULL,
    is_mandatory BOOLEAN NOT NULL DEFAULT TRUE,
    subject_matter TEXT NOT NULL,
    hours INTEGER,
    location TEXT,
    trainers_description TEXT,
    materials TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### territory\_information

Stores territory information (Item 12).

```
CREATE TABLE territory_information (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    has_exclusive_territory BOOLEAN NOT NULL,
    territory_description TEXT,
    minimum_population INTEGER,
    relocation_rights TEXT,
    expansion_rights TEXT,
    online_rights TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### trademarks

Stores trademark information (Item 13).

```
CREATE TABLE trademarks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    mark TEXT NOT NULL,
    registration_number TEXT,
    registration_date DATE,
    status TEXT NOT NULL,
    protection_description TEXT,
    litigation_history TEXT,
    usage_restrictions TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### intellectual\_property

Stores patent, copyright, and proprietary information (Item 14).

```
CREATE TABLE intellectual_property (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    ip_type TEXT NOT NULL,
    description TEXT NOT NULL,
    registration_info TEXT,
    expiration_date DATE,
    usage_rights TEXT,
    protection_measures TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### participation\_requirements

Stores information about participation requirements (Item 15).

```
CREATE TABLE participation_requirements (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    personal_participation_required BOOLEAN NOT NULL,
    participation_level TEXT,
    experience_requirements TEXT,
    certification_requirements TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### product\_restrictions

Stores information about product restrictions (Item 16).

```
CREATE TABLE product_restrictions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    restriction_type TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### renewal\_terms

Stores information about renewal terms (Item 17).

```
CREATE TABLE renewal_terms (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    term_length TEXT NOT NULL,
    renewal_options TEXT,
    conditions TEXT,
    fees TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### termination\_terms

Stores information about termination terms (Item 17).

```
CREATE TABLE termination_terms (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    termination_by TEXT NOT NULL,
    cause TEXT,
    notice_period TEXT,
    cure_period TEXT,
    obligations_post_termination TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### transfer\_terms

Stores information about transfer terms (Item 17).

```
CREATE TABLE transfer_terms (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    transfer_conditions TEXT NOT NULL,
    approval_process TEXT,
    fees TEXT,
    first_right_of_refusal BOOLEAN,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### dispute\_resolution

Stores information about dispute resolution (Item 17).

```
CREATE TABLE dispute_resolution (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    resolution_method TEXT NOT NULL,
    venue TEXT,
    governing_law TEXT,
    limitations_period TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### public\_figures

Stores information about public figures (Item 18).

```
CREATE TABLE public_figures (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    name TEXT NOT NULL,
    role TEXT NOT NULL,
    compensation TEXT,
    involvement_description TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### financial\_performance

Stores financial performance representations (Item 19).

```
CREATE TABLE financial_performance (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    representation_type TEXT NOT NULL,
    metric_name TEXT NOT NULL,
    time_period TEXT NOT NULL,
    unit_type TEXT NOT NULL,
    sample_size INTEGER,
    value_low DECIMAL(12,2),
    value_median DECIMAL(12,2),
    value_high DECIMAL(12,2),
    value_average DECIMAL(12,2),
    percentage_achieving INTEGER,
    assumptions TEXT,
    disclaimers TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### outlet\_information

Stores outlet and franchisee information (Item 20).

```
CREATE TABLE outlet_information (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    year INTEGER NOT NULL,
    state TEXT NOT NULL,
    opened_count INTEGER,
    closed_count INTEGER,
    transferred_count INTEGER,
    terminated_count INTEGER,
    non_renewed_count INTEGER,
    reacquired_count INTEGER,
    projected_openings INTEGER,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### financial\_statements

Stores financial statement information (Item 21).

```
CREATE TABLE financial_statements (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    statement_type TEXT NOT NULL,
    fiscal_year_end DATE NOT NULL,
    is_audited BOOLEAN NOT NULL DEFAULT TRUE,
    statement_data JSONB NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### contracts

Stores contract information (Item 22).

```
CREATE TABLE contracts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    contract_type TEXT NOT NULL,
    contract_name TEXT NOT NULL,
    contract_url TEXT,
    summary TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### receipt\_information

Stores receipt information (Item 23).

```
CREATE TABLE receipt_information (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    fdd_id UUID NOT NULL REFERENCES franchise_disclosure_documents(id),
    receipt_requirements TEXT NOT NULL,
    franchise_sellers TEXT[],
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Supporting Tables

### industries

Stores industry categories for franchises.

```
CREATE TABLE industries (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name TEXT NOT NULL,
    parent_id UUID REFERENCES industries(id),
    description TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchise\_industries

Many-to-many relationship between franchises and industries.

```
CREATE TABLE franchise_industries (
    franchise_id UUID NOT NULL REFERENCES franchises(id),
    industry_id UUID NOT NULL REFERENCES industries(id),
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (franchise_id, industry_id)
);
```

### franchise\_locations

Stores location information for franchises.

```
CREATE TABLE franchise_locations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchise_id UUID NOT NULL REFERENCES franchises(id),
    location_type TEXT NOT NULL,
    address JSONB,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    opened_date DATE,
    status TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchise\_rankings

Stores ranking information for franchises.

```
CREATE TABLE franchise_rankings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchise_id UUID NOT NULL REFERENCES franchises(id),
    ranking_source TEXT NOT NULL,
    ranking_year INTEGER NOT NULL,
    rank INTEGER NOT NULL,
    category TEXT,
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchise\_reviews

Stores user reviews of franchises.

```
CREATE TABLE franchise_reviews (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    franchise_id UUID NOT NULL REFERENCES franchises(id),
    user_id UUID NOT NULL REFERENCES auth.users(id),
    rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    is_verified_owner BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### franchise\_comparisons

Stores user-created franchise comparisons.

```
CREATE TABLE franchise_comparisons (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES auth.users(id),
    name TEXT NOT NULL,
    description TEXT,
    is_public BOOLEAN NOT NULL DEFAULT FALSE,
    franchises UUID[] NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### industry\_benchmarks

Stores industry benchmark data.

```
CREATE TABLE industry_benchmarks (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    industry_id UUID NOT NULL REFERENCES industries(id),
    metric_name TEXT NOT NULL,
    year INTEGER NOT NULL,
    value_average DECIMAL(12,2) NOT NULL,
    value_median DECIMAL(12,2),
    value_low DECIMAL(12,2),
    value_high DECIMAL(12,2),
    sample_size INTEGER NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

### user\_saved\_franchises

Stores user-saved franchises.

```
CREATE TABLE user_saved_franchises (
    user_id UUID NOT NULL REFERENCES auth.users(id),
    franchise_id UUID NOT NULL REFERENCES franchises(id),
    notes TEXT,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    PRIMARY KEY (user_id, franchise_id)
);
```

### user\_search\_history

Stores user search history.

```
CREATE TABLE user_search_history (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID NOT NULL REFERENCES auth.users(id),
    search_query JSONB NOT NULL,
    results_count INTEGER NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

## Indexes

```
-- Franchise search indexes
CREATE INDEX franchises_name_idx ON franchises USING GIN (to_tsvector('english', name));
CREATE INDEX franchises_description_idx ON franchises USING GIN (to_tsvector('english', concept_description));
CREATE INDEX franchises_industry_idx ON franchise_industries(industry_id);
CREATE INDEX franchises_units_idx ON franchises(total_units_count);
CREATE INDEX franchises_year_idx ON franchises(year_began_franchising);

-- Financial performance indexes
CREATE INDEX financial_performance_metric_idx ON financial_performance(metric_name);
CREATE INDEX financial_performance_value_avg_idx ON financial_performance(value_average);
CREATE INDEX financial_performance_value_median_idx ON financial_performance(value_median);

-- Investment indexes
CREATE INDEX initial_investments_low_idx ON initial_investments(amount_low);
CREATE INDEX initial_investments_high_idx ON initial_investments(amount_high);
CREATE INDEX initial_fees_amount_idx ON initial_fees(amount_low);
CREATE INDEX ongoing_fees_percentage_idx ON ongoing_fees(amount_percentage);

-- Location indexes
CREATE INDEX franchise_locations_geo_idx ON franchise_locations USING GIST (
    ST_SetSRID(ST_MakePoint(longitude, latitude), 4326)
);
CREATE INDEX franchise_locations_status_idx ON franchise_locations(status);

-- Temporal indexes
CREATE INDEX fdd_year_idx ON franchise_disclosure_documents(year);
CREATE INDEX fdd_current_idx ON franchise_disclosure_documents(is_current);
```

## Views

### franchise\_summary\_view

Provides a summary view of franchise information.

```
CREATE VIEW franchise_summary_view AS
SELECT 
    f.id,
    f.name,
    fr.name AS franchisor_name,
    f.year_began_franchising,
    f.total_units_count,
    f.franchised_count,
    f.company_owned_count,
    i.name AS primary_industry,
    (
        SELECT MIN(amount_low)
        FROM initial_investments ii
        JOIN franchise_disclosure_documents fdd ON ii.fdd_id = fdd.id
        WHERE fdd.franchise_id = f.id AND fdd.is_current = TRUE
        AND ii.category = 'Total Investment'
    ) AS min_investment,
    (
        SELECT MAX(amount_high)
        FROM initial_investments ii
        JOIN franchise_disclosure_documents fdd ON ii.fdd_id = fdd.id
        WHERE fdd.franchise_id = f.id AND fdd.is_current = TRUE
        AND ii.category = 'Total Investment'
    ) AS max_investment,
    (
        SELECT AVG(rating)
        FROM franchise_reviews
        WHERE franchise_id = f.id
    ) AS avg_rating,
    (
        SELECT COUNT(*)
        FROM franchise_reviews
        WHERE franchise_id = f.id
    ) AS review_count
FROM 
    franchises f
JOIN 
    franchisors fr ON f.franchisor_id = fr.id
LEFT JOIN 
    industries i ON fr.industry_primary_id = i.id
WHERE 
    f.is_active = TRUE;
```

### financial\_performance\_summary\_view

Provides a summary view of financial performance.

```
CREATE VIEW financial_performance_summary_view AS
SELECT 
    f.id AS franchise_id,
    f.name AS franchise_name,
    fp.metric_name,
    fp.time_period,
    fp.unit_type,
    fp.value_average,
    fp.value_median,
    fp.value_low,
    fp.value_high,
    fp.sample_size,
    fp.percentage_achieving,
    fdd.year AS fdd_year
FROM 
    financial_performance fp
JOIN 
    franchise_disclosure_documents fdd ON fp.fdd_id = fdd.id
JOIN 
    franchises f ON fdd.franchise_id = f.id
WHERE 
    fdd.is_current = TRUE;
```

### investment\_summary\_view

Provides a summary view of investment requirements.

```
CREATE VIEW investment_summary_view AS
SELECT 
    f.id AS franchise_id,
    f.name AS franchise_name,
    (
        SELECT SUM(amount_low)
        FROM initial_fees
        WHERE fdd_id = fdd.id
    ) AS total_initial_fees_low,
    (
        SELECT SUM(amount_high)
        FROM initial_fees
        WHERE fdd_id = fdd.id
    ) AS total_initial_fees_high,
    (
        SELECT MIN(amount_low)
        FROM initial_investments
        WHERE fdd_id = fdd.id AND category = 'Total Investment'
    ) AS total_investment_low,
    (
        SELECT MAX(amount_high)
        FROM initial_investments
        WHERE fdd_id = fdd.id AND category = 'Total Investment'
    ) AS total_investment_high,
    (
        SELECT STRING_AGG(fee_type || ': ' || 
            CASE 
                WHEN amount_percentage IS NOT NULL THEN amount_percentage || '%'
                ELSE '$' || amount_fixed::TEXT
            END, ', ')
        FROM ongoing_fees
        WHERE fdd_id = fdd.id
    ) AS ongoing_fees_summary
FROM 
    franchises f
JOIN 
    franchise_disclosure_documents fdd ON f.id = fdd.franchise_id
WHERE 
    fdd.is_current = TRUE;
```

## Functions and Triggers

### update\_timestamp\_function

```
CREATE OR REPLACE FUNCTION update_timestamp_function()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

### create\_update\_triggers

```
-- Example for one table, repeat for all tables with updated_at column
CREATE TRIGGER update_franchisors_timestamp
BEFORE UPDATE ON franchisors
FOR EACH ROW
EXECUTE FUNCTION update_timestamp_function();
```

### franchise\_search\_function

```
CREATE OR REPLACE FUNCTION franchise_search(
    search_term TEXT DEFAULT NULL,
    industry_ids UUID[] DEFAULT NULL,
    min_investment DECIMAL DEFAULT NULL,
    max_investment DECIMAL DEFAULT NULL,
    min_units INTEGER DEFAULT NULL,
    sort_by TEXT DEFAULT 'name',
    sort_order TEXT DEFAULT 'asc',
    limit_val INTEGER DEFAULT 20,
    offset_val INTEGER DEFAULT 0
)
RETURNS TABLE (
    id UUID,
    name TEXT,
    franchisor_name TEXT,
    industry TEXT,
    total_units INTEGER,
    min_investment DECIMAL,
    max_investment DECIMAL,
    avg_rating DECIMAL
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        f.id,
        f.name,
        fr.name AS franchisor_name,
        i.name AS industry,
        f.total_units_count,
        inv_summary.min_investment,
        inv_summary.max_investment,
        COALESCE(rev_summary.avg_rating, 0) AS avg_rating
    FROM 
        franchises f
    JOIN 
        franchisors fr ON f.franchisor_id = fr.id
    LEFT JOIN 
        franchise_industries fi ON f.id = fi.franchise_id AND fi.is_primary = TRUE
    LEFT JOIN 
        industries i ON fi.industry_id = i.id
    LEFT JOIN 
        LATERAL (
            SELECT 
                MIN(ii.amount_low) AS min_investment,
                MAX(ii.amount_high) AS max_investment
            FROM 
                initial_investments ii
            JOIN 
                franchise_disclosure_documents fdd ON ii.fdd_id = fdd.id
            WHERE 
                fdd.franchise_id = f.id 
                AND fdd.is_current = TRUE
                AND ii.category = 'Total Investment'
        ) inv_summary ON TRUE
    LEFT JOIN 
        LATERAL (
            SELECT 
                AVG(rating) AS avg_rating
            FROM 
                franchise_reviews
            WHERE 
                franchise_id = f.id
        ) rev_summary ON TRUE
    WHERE 
        f.is_active = TRUE
        AND (search_term IS NULL OR 
             f.name ILIKE '%' || search_term || '%' OR
             fr.name ILIKE '%' || search_term || '%' OR
             f.concept_description ILIKE '%' || search_term || '%')
        AND (industry_ids IS NULL OR
             EXISTS (
                 SELECT 1 FROM franchise_industries 
                 WHERE franchise_id = f.id AND industry_id = ANY(industry_ids)
             ))
        AND (min_investment IS NULL OR inv_summary.min_investment >= min_investment)
        AND (max_investment IS NULL OR inv_summary.max_investment <= max_investment)
        AND (min_units IS NULL OR f.total_units_count >= min_units)
    ORDER BY
        CASE 
            WHEN sort_by = 'name' AND sort_order = 'asc' THEN f.name
        END ASC,
        CASE 
            WHEN sort_by = 'name' AND sort_order = 'desc' THEN f.name
        END DESC,
        CASE 
            WHEN sort_by = 'units' AND sort_order = 'asc' THEN f.total_units_count
        END ASC,
        CASE 
            WHEN sort_by = 'units' AND sort_order = 'desc' THEN f.total_units_count
        END DESC,
        CASE 
            WHEN sort_by = 'investment' AND sort_order = 'asc' THEN inv_summary.min_investment
        END ASC,
        CASE 
            WHEN sort_by = 'investment' AND sort_order = 'desc' THEN inv_summary.min_investment
        END DESC,
        CASE 
            WHEN sort_by = 'rating' AND sort_order = 'asc' THEN rev_summary.avg_rating
        END ASC,
        CASE 
            WHEN sort_by = 'rating' AND sort_order = 'desc' THEN rev_summary.avg_rating
        END DESC
    LIMIT limit_val
    OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;
```

## Row-Level Security (RLS) Policies

```
-- Enable RLS on tables that need it
ALTER TABLE franchise_reviews ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_saved_franchises ENABLE ROW LEVEL SECURITY;
ALTER TABLE franchise_comparisons ENABLE ROW LEVEL SECURITY;
ALTER TABLE user_search_history ENABLE ROW LEVEL SECURITY;

-- Create policies
CREATE POLICY franchise_reviews_user_policy ON franchise_reviews
    USING (user_id = auth.uid() OR is_verified_owner = TRUE);

CREATE POLICY user_saved_franchises_user_policy ON user_saved_franchises
    USING (user_id = auth.uid());

CREATE POLICY franchise_comparisons_user_policy ON franchise_comparisons
    USING (user_id = auth.uid() OR is_public = TRUE);

CREATE POLICY user_search_history_user_policy ON user_search_history
    USING (user_id = auth.uid());
```

## Schema Evolution and Versioning

The schema includes timestamps on all tables to track changes over time. For annual FDD updates, the 

```
franchise_disclosure_documents
```

 table links to specific years, allowing historical data to be preserved while maintaining current information.

## Monetization Features

1. [&lt;RawText children='Premium Data Access'&gt;]
2. [&lt;RawText children='Comparison Tools'&gt;]
3. [&lt;RawText children='Industry Benchmarks'&gt;]
4. [&lt;RawText children='Historical Trends'&gt;]
5. [&lt;RawText children='Investment Opportunity Scoring'&gt;]

## Performance Considerations

1. [&lt;RawText children='Indexing Strategy'&gt;]
2. [&lt;RawText children='Materialized Views'&gt;]
3. [&lt;RawText children='Partitioning'&gt;]
4. [&lt;RawText children='Query Optimization'&gt;]
5. [&lt;RawText children='Caching Layer'&gt;]

## Next Steps

1. Implement database migrations
2. Create seed data for testing
3. Develop API endpoints for data access
4. Implement data extraction and ingestion processes
5. Set up monitoring and performance tuning

---

# Franchise Disclosure Document (FDD) Research Summary

## Overview

The Franchise Disclosure Document (FDD) is a legally required document containing 23 standardized items that all franchisors must disclose to prospective franchisees. This document serves as the foundation for our database schema design, ensuring we capture all relevant data points for comprehensive analysis and comparison.

## The 23 FDD Items

### Item 1: The Franchisor and any Parents, Predecessors, and Affiliates

- General review of the company
- Information about predecessors or affiliates
- Overview of the business opportunity
- Market information for products/services
- Known government regulations
- Competitor information

### Item 2: Business Experience

- Background data on key officers, directors, and employees
- Management responsibility information
- Work experience from past five years
- Other experience as officers/directors of other companies

### Item 3: Litigation

- Disclosures of past or current litigation
- Legal actions involving the company or key people
- Both civil and criminal cases
- Pending or settled cases

### Item 4: Bankruptcy

- Bankruptcy disclosures for the company or key people
- Personal bankruptcy information for senior management
- Corporate bankruptcy for companies where they were officers
- Covers past 10 years

### Item 5: Initial Fees

- Initial franchise fee amounts
- Payment terms and schedules
- Refund conditions if applicable

### Item 6: Other Fees

- Ongoing royalties
- Advertising fund contributions
- Local and cooperative advertising fees
- Training fees (initial and additional)
- Renewal and transfer fees
- Software usage/support fees
- Audit fees
- Consulting fees
- Other costs and reimbursements

### Item 7: Estimated Initial Investment

- Comprehensive breakdown of startup costs
- Ranges of potential costs in tabular format
- Initial advertising allowances
- Operating capital reserves
- Location-specific cost variations

### Item 8: Restrictions on Sources of Products and Services

- Product offering controls
- Equipment and supply requirements
- Approved supplier information
- Specification requirements
- Revenue earned from franchisee purchases
- Percentage of total purchases controlled by franchisor

### Item 9: Franchisee's Obligations

- Tabular format of responsibilities
- Cross-references to specific sections of FDD and franchise agreement
- Major areas of business responsibility
- Real estate and site selection obligations

### Item 10: Financing

- Terms and conditions of financing
- Direct or indirect financing options
- Payment schedules and terms

### Item 11: Franchisor's Assistance, Advertising, Computer Systems, and Training

- Pre-opening assistance details
- Ongoing support services
- Training program information
- Required franchise systems
- Computer point of sale requirements
- Advertising program details

### Item 12: Territory

- Protected or exclusive territory information
- Territory size and boundaries
- Variance in territory provisions between franchises
- Restrictions and protections

### Item 13: Trademarks

- Trademark information and status
- Registration details
- Protection provisions
- Usage guidelines

### Item 14: Patents, Copyrights, and Proprietary Information

- Patent information
- Copyright details
- Proprietary information protection
- Intellectual property usage rights

### Item 15: Obligation to Participate in the Actual Operation

- Personal obligations in business operation
- Direct involvement requirements
- Management participation expectations

### Item 16: Restrictions on What the Franchisee May Sell

- Product/service offering restrictions
- Approved product lines
- Limitations on sales

### Item 17: Renewal, Termination, Transfer, and Dispute Resolution

- Renewal terms and conditions
- Termination circumstances and procedures
- Transfer restrictions and fees
- Dispute resolution methodologies
- Negotiation/mediation requirements
- Arbitration provisions

### Item 18: Public Figures

- Information about public figures involved
- Promotional relationships
- Celebrity endorsements

### Item 19: Financial Performance Representations

- Unit financial performance data
- Revenue and/or expense presentations
- Assumptions and explanations
- Disclaimers and limitations
- Historical performance metrics

### Item 20: Outlets and Franchisee Information

- Number and location of franchise units
- Ownership transfer information
- Closure information
- Growth trajectory data
- Success rates

### Item 21: Financial Statements

- Audited financial statements (3 years)
- Financial strength indicators
- Stability metrics

### Item 22: Contracts

- All required agreements
- Franchise agreement
- Personal guarantees
- Real estate assignments
- Advertising agreements
- Territorial development schedules

### Item 23: Receipts

- Acknowledgment of FDD receipt
- Timing verification
- Signature requirements

## Key Considerations for Database Schema

1. [&lt;RawText children='Temporal Data Handling'&gt;]
2. [&lt;RawText children='Data Standardization Needs'&gt;]
    - Financial figures (currencies, percentages vs. fixed amounts)
    - Date formats and time periods
    - Ranges vs. specific values
    - Geographic/territory standardization
3. [&lt;RawText children='Relationship Complexity'&gt;]
    - Franchisor to multiple franchisees
    - Franchisee to multiple locations
    - Historical performance tracking
    - Comparative metrics across franchises
4. [&lt;RawText children='Monetization Opportunities'&gt;]
    - Premium access to financial performance data
    - Comparative analysis tools
    - Historical trend analysis
    - Investment opportunity scoring
5. [&lt;RawText children='Mass Appeal Features'&gt;]
    - Intuitive search and filtering
    - Visual data representation
    - Standardized comparison metrics
    - Industry benchmarking

---

# Franchise Profile Information Architecture

## Introduction

This document outlines the comprehensive information architecture for franchise profile pages within the franchise directory platform. The profile pages serve as the central hub for users to evaluate franchise opportunities, providing structured, accessible, and actionable information derived from Franchise Disclosure Documents (FDDs).

## Design Principles

1. [&lt;RawText children='Information Hierarchy'&gt;]
2. [&lt;RawText children='Visual Clarity'&gt;]
3. [&lt;RawText children='Completeness Handling'&gt;]
4. [&lt;RawText children='User-Centric Design'&gt;]
5. [&lt;RawText children='Monetization Support'&gt;]
6. [&lt;RawText children='Mass Appeal'&gt;]

## User Personas

### Primary Personas

1. [&lt;RawText children='Prospective Franchisee'&gt;]
    - Needs: Investment requirements, profitability metrics, operational details
    - Goals: Evaluate business viability, compare opportunities, understand commitments
    - Behaviors: In-depth research, multiple visits, document downloads
2. [&lt;RawText children='Investor'&gt;]
    - Needs: Financial performance, growth trends, market positioning
    - Goals: Assess ROI potential, identify growth opportunities, evaluate risk
    - Behaviors: Quantitative analysis, industry comparisons, historical tracking
3. [&lt;RawText children='Franchise Consultant'&gt;]
    - Needs: Comprehensive data access, comparison tools, client-sharing features
    - Goals: Match clients with opportunities, provide expert analysis, track industry trends
    - Behaviors: Advanced filtering, detailed comparisons, report generation
4. [&lt;RawText children='Researcher/Analyst'&gt;]
    - Needs: Raw data access, industry benchmarks, historical trends
    - Goals: Identify patterns, produce reports, analyze market segments
    - Behaviors: Data exports, advanced analytics, longitudinal studies

## Information Architecture Overview

The franchise profile is structured in a modular, hierarchical format with progressive disclosure of information complexity. The architecture follows a "critical information first" approach while providing clear pathways to more detailed content.

### Top-Level Structure

1. [&lt;RawText children='Hero Section'&gt;]
2. [&lt;RawText children='Summary Cards'&gt;]
3. [&lt;RawText children='Financial Section'&gt;]
4. [&lt;RawText children='Operational Details'&gt;]
5. [&lt;RawText children='Legal Information'&gt;]
6. [&lt;RawText children='Historical Data'&gt;]
7. [&lt;RawText children='Comparison Tools'&gt;]
8. [&lt;RawText children='Resources'&gt;]

## Detailed Section Breakdown

### 1. Hero Section

Purpose : Establish brand identity and provide immediate context

Components :

- Franchise logo and header image
- Franchise name and tagline
- Franchisor company name
- Industry category with icon
- Year established and franchising since
- Unit count (total, franchised, company-owned)
- Average rating (if available)
- Quick action buttons (save, compare, contact)

Visual Treatment :

- Full-width header with brand-appropriate imagery
- Prominent logo placement
- Clean typography hierarchy
- Key metrics displayed as badges/pills

Data Sources :

- franchises
- franchisors
- franchise\_industries
- franchise\_reviews

### 2. Summary Cards

Purpose : Provide at-a-glance decision factors for quick evaluation

Components :

- Investment Range Card
    - Total initial investment range
    - Franchise fee
    - Ongoing royalty percentage
    - Estimated payback period (premium)
- Business Overview Card
    - Business model summary
    - Target customer
    - Competitive advantages
    - Required experience
- Performance Snapshot Card (Premium)
    - Average unit revenue
    - Profit margin range
    - Top performer metrics
    - Success rate indicator
- Territory &amp; Growth Card
    - Available territories
    - Unit growth trend
    - International presence
    - Development schedule

Visual Treatment :

- Card-based layout with consistent height
- Visual indicators for ranges (sliders/gauges)
- Color-coding for comparative metrics
- Icons for quick recognition

Data Sources :

- initial\_investments
- initial\_fees
- ongoing\_fees
- financial\_performance
- territory\_information
- outlet\_information

### 3. Financial Section

Purpose : Provide detailed financial requirements and performance data

Components :

- Initial Investment Breakdown
    - Itemized cost table with ranges
    - Interactive chart visualization
    - Notes and explanations
    - Financing options (if available)
- Ongoing Fees Structure
    - Royalty fees
    - Marketing/advertising fees
    - Technology fees
    - Other recurring costs
- Financial Performance (Tiered Access)
    - Basic: General statements and ranges
    - Premium: Detailed unit economics
    - Premium+: Comparative performance metrics
- Financial Requirements
    - Net worth requirements
    - Liquid capital needed
    - Credit score minimums
    - Financing assistance details

Visual Treatment :

- Expandable/collapsible detailed tables
- Interactive charts with filtering options
- Clear labeling of premium content
- Comparison toggles for benchmarking

Data Sources :

- initial\_investments
- initial\_fees
- ongoing\_fees
- financial\_performance
- financing\_options

### 4. Operational Details

Purpose : Explain day-to-day business operations and requirements

Components :

- Business Model Explanation
    - Revenue streams
    - Customer acquisition model
    - Operational hours
    - Staffing requirements
- Real Estate &amp; Location
    - Space requirements
    - Location types
    - Build-out specifications
    - Site selection assistance
- Training &amp; Support
    - Initial training details
    - Ongoing support programs
    - Technology systems
    - Marketing assistance
- Supply Chain
    - Supplier restrictions
    - Proprietary products
    - Inventory requirements
    - Purchase obligations

Visual Treatment :

- Process flow diagrams
- Timeline visualizations for training
- Support system icons and explanations
- Location type imagery

Data Sources :

- franchisee\_obligations
- franchisor\_assistance
- training\_programs
- supplier\_restrictions
- participation\_requirements

### 5. Legal Information

Purpose : Provide transparency on contractual obligations and legal considerations

Components :

- Contract Terms Summary
    - Term length
    - Renewal conditions
    - Transfer rights
    - Termination clauses
- Litigation History
    - Recent legal actions
    - Bankruptcy disclosures
    - Regulatory issues
- Franchisee Obligations
    - Operational requirements
    - Reporting requirements
    - Compliance standards
- Intellectual Property
    - Trademark information
    - Patent details
    - Usage restrictions

Visual Treatment :

- Timeline visualization for contract term
- Color-coded risk indicators
- Expandable sections for detailed legal text
- Document preview thumbnails

Data Sources :

- litigation\_records
- bankruptcy\_records
- franchisee\_obligations
- renewal\_terms
- termination\_terms
- transfer\_terms
- trademarks
- intellectual\_property

### 6. Historical Data

Purpose : Show performance and growth trends over time

Components :

- Unit Growth Chart
    - Annual openings/closings
    - Projected growth
    - Turnover rates
- Performance Trends (Premium)
    - Revenue trends
    - Profitability changes
    - Investment requirement changes
- Ownership Changes
    - Transfers
    - Reacquisitions
    - Terminations
- FDD Historical Changes
    - Year-over-year changes in key terms
    - Fee adjustments over time
    - Support program evolution

Visual Treatment :

- Interactive time-series charts
- Growth visualization with projections
- Color-coded status changes
- Year-over-year comparison sliders

Data Sources :

- outlet\_information
- financial\_performance
- franchise\_disclosure\_documents

### 7. Comparison Tools

Purpose : Enable direct comparison with similar franchises

Components :

- Quick Compare Widget
    - Side-by-side metrics with selected franchises
    - Industry average benchmarks
    - Similarity score
- Investment Comparison
    - Initial investment range comparison
    - Fee structure differences
    - ROI potential comparison (Premium)
- Support Comparison
    - Training program differences
    - Marketing support comparison
    - Technology systems comparison
- Performance Comparison (Premium)
    - Unit economics side-by-side
    - Growth rate comparison
    - Success metrics comparison

Visual Treatment :

- Interactive comparison tables
- Radar/spider charts for multi-metric comparison
- Side-by-side bar charts
- Visual indicators for advantages/disadvantages

Data Sources :

- All relevant tables with comparison logic
- industry\_benchmarks
- franchise\_comparisons

### 8. Resources

Purpose : Provide additional information and next steps

Components :

- Document Library
    - FDD download (registration required)
    - Marketing brochures
    - Sample agreements
- Franchisee Resources
    - Current franchisee testimonials
    - Franchisee interview questions
    - Due diligence checklist
- Request Information
    - Contact form
    - Information packet request
    - Discovery day scheduling
- Related Content
    - News articles
    - Industry reports
    - Related franchises

Visual Treatment :

- Document thumbnails with preview
- Testimonial cards with franchisee images
- Clear call-to-action buttons
- Related content carousel

Data Sources :

- franchise\_disclosure\_documents
- contracts
- External content references

## Information Hierarchy and Priority

### Tier 1 (Immediately Visible)

- Franchise name and logo
- Industry category
- Total investment range
- Ongoing fees (royalty %)
- Unit count and growth trend
- Business model summary
- Average rating

### Tier 2 (Primary Scroll)

- Detailed investment breakdown
- Financial performance indicators
- Training and support summary
- Territory information
- Key differentiators
- Quick comparison widget

### Tier 3 (Secondary Scroll/Tab Navigation)

- Operational details
- Legal information summary
- Historical performance data
- Franchisee obligations
- Detailed fee structures

### Tier 4 (Expandable/Detailed Views)

- Complete legal disclosures
- Comprehensive financial data
- Historical FDD changes
- Advanced comparison tools
- Document library

## Handling Data Completeness Variations

### Complete Data Strategy

- Full feature enablement
- Comprehensive visualizations
- Detailed comparative analysis
- Premium feature availability

### Partial Data Strategy

- Clear indication of available vs. unavailable data
- Placeholder visualizations with explanatory text
- Focus on available strengths
- Alternative metrics when primary metrics unavailable

### Minimal Data Strategy

- Simplified profile view
- Emphasis on qualitative information
- Prominent information request options
- Clear disclosure of limitations

### Visual Indicators

- Completeness meter for each section
- Color-coding for data confidence
- Explicit labeling of estimated/derived data
- Source attribution for all metrics

## Monetization Integration

### Free Tier Features

- Basic franchise information
- Investment range summary
- General business model details
- Limited comparisons
- Basic search and filtering

### Premium Tier Features

- Detailed financial performance data
- Advanced comparison tools
- Historical trend analysis
- Comprehensive benchmarking
- Export and reporting capabilities

### Premium+ Tier Features

- Predictive success modeling
- Customized territory analysis
- Investment return calculators
- Consultant-level analytics
- API access for data integration

### Visual Treatment of Premium Content

- Subtle premium badges on gated content
- Preview snippets of premium data
- Clear upgrade paths within user flow
- Value proposition messaging for conversion

## User Interface Wireframes

### Desktop Profile Layout

```
┌─────────────────────────────────────────────────────────────┐
│                      HERO SECTION                           │
│  ┌─────┐                                                    │
│  │LOGO │  FRANCHISE NAME          ★★★★☆ (4.2)               │
│  └─────┘  Franchisor Company      Est. 1985 • 500+ Units    │
│                                                             │
│           [SAVE]  [COMPARE]  [REQUEST INFO]                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────┐ ┌─────────────────┐ ┌─────────────────────┐
│  INVESTMENT     │ │  BUSINESS       │ │  PERFORMANCE        │
│  $100K - $500K  │ │  Fast-Casual    │ │  $800K Avg Revenue  │
│  5% Royalty     │ │  Restaurant     │ │  15-20% Profit      │
│  [Details ▼]    │ │  [Details ▼]    │ │  [Premium ⭐]        │
└─────────────────┘ └─────────────────┘ └─────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  TABS:  Overview | Financial | Operations | Legal | Compare  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Content based on selected tab]                            │
│                                                             │
│  • Detailed tables                                          │
│  • Interactive charts                                       │
│  • Expandable sections                                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                   QUICK COMPARISON                          │
│                                                             │
│  This Franchise    Industry Average    Similar Franchise    │
│  [Metrics with visual comparison indicators]                │
│                                                             │
│  [Add to Comparison] [View Full Comparison]                 │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                      RESOURCES                              │
│                                                             │
│  [FDD Download]  [Brochure]  [Sample Agreement]             │
│                                                             │
│  Related Franchises:  [Carousel of similar opportunities]   │
└─────────────────────────────────────────────────────────────┘
```

### Mobile Profile Layout

```
┌───────────────────────┐
│      HERO SECTION     │
│  ┌─────┐              │
│  │LOGO │ FRANCHISE    │
│  └─────┘ NAME         │
│                       │
│  ★★★★☆ (4.2)          │
│  500+ Units           │
│                       │
│  [SAVE] [COMPARE]     │
└───────────────────────┘

┌───────────────────────┐
│     QUICK STATS       │
│                       │
│  $100K-$500K          │
│  Investment           │
│                       │
│  5% Royalty           │
│                       │
│  Fast-Casual          │
│  Restaurant           │
└───────────────────────┘

┌───────────────────────┐
│  NAVIGATION TABS      │
│  [Horizontally        │
│   scrollable tabs]    │
└───────────────────────┘

┌───────────────────────┐
│                       │
│  [Tab content         │
│   optimized for       │
│   mobile viewing]     │
│                       │
└───────────────────────┘

┌───────────────────────┐
│  [REQUEST INFO]       │
│  Prominent CTA        │
└───────────────────────┘

┌───────────────────────┐
│  SIMILAR FRANCHISES   │
│  [Vertical list with  │
│   quick metrics]      │
└───────────────────────┘
```

## Interactive Elements

### Data Visualization Components

1. [&lt;RawText children='Investment Range Slider'&gt;]
    - Interactive visualization of investment components
    - Adjustable to show different scenarios
    - Comparison with industry averages
2. [&lt;RawText children='Unit Economics Calculator'&gt;]
    - Input-driven financial modeling
    - Customizable assumptions
    - ROI and break-even projections
3. [&lt;RawText children='Territory Map'&gt;]
    - Available territories visualization
    - Existing unit locations
    - Market saturation indicators
4. [&lt;RawText children='Performance Comparison Charts'&gt;]
    - Side-by-side metric comparison
    - Radar charts for multi-dimensional comparison
    - Historical trend lines
5. [&lt;RawText children='Success Factors Gauge'&gt;]
    - Visual indicator of key success metrics
    - Comparative positioning
    - Strength/weakness visualization

### User Interaction Points

1. [&lt;RawText children='Save and Collection Features'&gt;]
    - Add to saved franchises
    - Create custom collections
    - Notes and annotations
2. [&lt;RawText children='Comparison Tools'&gt;]
    - Add to comparison list
    - Side-by-side detailed comparison
    - Export comparison results
3. [&lt;RawText children='Information Requests'&gt;]
    - Direct contact forms
    - Document request workflows
    - Appointment scheduling
4. [&lt;RawText children='Customization Options'&gt;]
    - Preferred metrics selection
    - View customization
    - Notification preferences

## SEO Considerations

### Page Structure

- Semantic HTML with proper heading hierarchy
- Structured data markup (Schema.org)
- Franchise-specific metadata

### Content Strategy

- Unique, detailed franchise descriptions
- Industry-specific terminology
- Location-based content where applicable

### Technical SEO

- Canonical URLs for franchise profiles
- Proper handling of historical/outdated FDDs
- Mobile optimization
- Page speed considerations

## Accessibility Considerations

- Color contrast compliance
- Screen reader compatibility
- Keyboard navigation support
- Alternative text for all visualizations
- Responsive design for all device types

## Implementation Recommendations

### Progressive Enhancement

- Core content available without JavaScript
- Enhanced visualizations with JS enabled
- Fallback options for all interactive elements

### Performance Optimization

- Lazy loading of below-the-fold content
- Image optimization
- Data caching strategies
- Asynchronous loading of premium features

### Content Management

- Templated sections for consistent presentation
- Dynamic content blocks based on data availability
- Automated data quality indicators

## Conclusion

The franchise profile information architecture balances comprehensive data presentation with user-friendly design, ensuring that users of all types can efficiently evaluate franchise opportunities. By implementing a tiered information hierarchy with progressive disclosure, the platform accommodates both casual browsers and serious investors while creating clear monetization pathways through premium content access.

The architecture's flexibility in handling varying levels of data completeness ensures that all franchise listings provide value, while the consistent structure enables effective comparison and analysis across opportunities.

---

# Implementation Considerations and Monetization Strategy

## Introduction

This document outlines key implementation considerations and a monetization strategy for the franchise directory platform. It builds upon the previously defined database schema, profile architecture, and comparison framework, incorporating best practices for data handling, performance, scalability, SEO, and revenue generation.

## 1. Data Extraction Strategy

Challenge : Extracting structured data from diverse PDF FDDs, which can vary in format despite standardized items.

Proposed Strategy : LLM-Powered Extraction Pipeline

1. [&lt;RawText children='PDF Preprocessing'&gt;]
2. [&lt;RawText children='LLM Prompt Engineering'&gt;]
3. [&lt;RawText children='LLM API Integration'&gt;]
4. [&lt;RawText children='Structured Data Output'&gt;]
5. [&lt;RawText children='Validation Layer'&gt;]
6. [&lt;RawText children='Database Ingestion'&gt;]

Key Considerations :

- [&lt;RawText children='LLM Choice'&gt;]
- [&lt;RawText children='Prompt Iteration'&gt;]
- [&lt;RawText children='Cost Management'&gt;]
- [&lt;RawText children='Error Handling'&gt;]
- [&lt;RawText children='Scalability'&gt;]

## 2. Update and Versioning Approach

Challenge : Handling annual FDD updates while preserving historical data for trend analysis.

Proposed Strategy : Leveraging the 

```
franchise_disclosure_documents
```

 Table

1. [&lt;RawText children='FDD Versioning'&gt;]
2. [&lt;RawText children='Data Association'&gt;]
3. [&lt;RawText children='Historical Access'&gt;]
4. [&lt;RawText children='Current Data View'&gt;]
5. [&lt;RawText children='Change Tracking'&gt;]
6. [&lt;RawText children='Update Process'&gt;]

## 3. Performance Optimization

Challenge : Ensuring fast load times and query responses for a data-intensive platform.

Recommendations :

1. [&lt;RawText children='Database Tuning'&gt;]
2. [&lt;RawText children='Caching Strategy'&gt;]
    - [&lt;RawText children='API Level'&gt;]
    - [&lt;RawText children='Frontend Level'&gt;]
    - [&lt;RawText children='CDN'&gt;]
3. [&lt;RawText children='Materialized Views'&gt;]
4. [&lt;RawText children='Asynchronous Operations'&gt;]
5. [&lt;RawText children='Efficient Query Design'&gt;]
6. [&lt;RawText children='Frontend Optimization'&gt;]

## 4. Scalability Considerations

Challenge : Handling growth in the number of franchises, users, and data volume.

Recommendations :

1. [&lt;RawText children='Supabase Scaling'&gt;]
2. [&lt;RawText children='Stateless Backend'&gt;]
3. [&lt;RawText children='Serverless Functions'&gt;]
4. [&lt;RawText children='Database Read Replicas'&gt;]
5. [&lt;RawText children='Load Balancing'&gt;]
6. [&lt;RawText children='Asynchronous Data Pipeline'&gt;]
7. [&lt;RawText children='Archiving'&gt;]

## 5. Technology Stack Recommendation

Based on user preferences and industry best practices for SEO and data-driven applications:

- [&lt;RawText children='Database'&gt;]
- [&lt;RawText children='Backend'&gt;]
- [&lt;RawText children='Frontend'&gt;]
- [&lt;RawText children='Data Extraction'&gt;]
- [&lt;RawText children='Task Queue (Optional)'&gt;]
- [&lt;RawText children='Caching (Optional)'&gt;]
- [&lt;RawText children='Deployment'&gt;]

Rationale :

- [&lt;RawText children='Supabase'&gt;]
- [&lt;RawText children='Python Backend'&gt;]
- [&lt;RawText children='Next.js/React'&gt;]
- [&lt;RawText children='Alignment'&gt;]

## 6. SEO Strategy

Goal : Maximize organic visibility, leveraging the platform's rich dataset.

Recommendations :

1. [&lt;RawText children='Programmatic SEO (pSEO)'&gt;]
    - [&lt;RawText children='Template Creation'&gt;]
    - [&lt;RawText children='Automated Page Generation'&gt;]
    - [&lt;RawText children='Internal Linking'&gt;]
2. [&lt;RawText children='Structured Data (Schema.org)'&gt;]
    - Implement relevant Schema.org types (e.g., 
    - Use JSON-LD format for structured data injection.
3. [&lt;RawText children='Keyword Optimization'&gt;]
4. [&lt;RawText children='Content Strategy'&gt;]
5. [&lt;RawText children='On-Page SEO'&gt;]
6. [&lt;RawText children='Technical SEO'&gt;]

## 7. Monetization Model

Goal : Generate revenue while providing value to different user segments.

Proposed Strategy : Tiered Subscription Model + Add-ons

### Subscription Tiers:

1. [&lt;RawText children='Free Tier'&gt;]
    - [&lt;RawText children='Target'&gt;]
    - [&lt;RawText children='Features'&gt;]
    - [&lt;RawText children='Monetization'&gt;]
2. [&lt;RawText children='Premium Tier (e.g., "Pro")'&gt;]
    - [&lt;RawText children='Target'&gt;]
    - [&lt;RawText children='Features'&gt;]
    - [&lt;RawText children='Pricing'&gt;]
3. [&lt;RawText children='Enterprise/Investor Tier (e.g., "Elite")'&gt;]
    - [&lt;RawText children='Target'&gt;]
    - [&lt;RawText children='Features'&gt;]
    - [&lt;RawText children='Pricing'&gt;]

### Additional Monetization Opportunities:

1. [&lt;RawText children='Lead Generation'&gt;]
2. [&lt;RawText children='Premium Reports'&gt;]
3. [&lt;RawText children='Consultant Directory'&gt;]
4. [&lt;RawText children='Sponsored Content'&gt;]

Implementation Notes :

- Integrate with a payment gateway (e.g., Stripe, Paddle).
- Implement robust access control based on subscription levels using Supabase RLS and backend logic.
- Track feature usage to optimize pricing and tier offerings.
- Clearly communicate the value proposition of each tier.

## Conclusion

Successful implementation requires a robust data extraction pipeline, a well-managed database, and a scalable, performant architecture. The recommended technology stack supports these requirements while enabling advanced features and strong SEO performance. A tiered monetization model allows the platform to cater to diverse user needs and generate sustainable revenue, leveraging the unique value derived from structured FDD data.

---

# Franchise Directory Database Schema and Design Project

## Overview

This project provides a comprehensive database schema and design plan for a franchise directory website that aggregates and analyzes Franchise Disclosure Documents (FDDs). The platform is designed to extract, store, and present structured data from FDDs to enable easy comparison and analysis of franchise opportunities.

## Key Deliverables

1. [&lt;RawText children='Database Schema Design'&gt;]
    - Complete Supabase (PostgreSQL) database schema
    - Table definitions, relationships, and constraints
    - Indexes and optimization strategies
    - Views and functions for common operations
2. [&lt;RawText children='FDD Research Summary'&gt;]
    - Detailed breakdown of all 23 FDD items
    - Key data points and relationships
    - Standardization requirements
3. [&lt;RawText children='Franchise Profile Information Architecture'&gt;]
    - User personas and information hierarchy
    - Detailed section breakdown
    - UI wireframes and visualization components
    - Data completeness handling strategies
4. [&lt;RawText children='Comparison Framework'&gt;]
    - Comparable metrics with sources
    - Normalization rules and methods
    - Comparison UI patterns
    - Sample comparison queries
5. [&lt;RawText children='Implementation and Monetization Strategy'&gt;]
    - Data extraction strategies from PDF FDDs
    - Update and versioning approach
    - Performance optimization recommendations
    - Scalability considerations
    - SEO strategy
    - Monetization model

## Technology Stack

- [&lt;RawText children='Database'&gt;]
- [&lt;RawText children='Backend'&gt;]
- [&lt;RawText children='Frontend'&gt;]
- [&lt;RawText children='Data Extraction'&gt;]
- [&lt;RawText children='Deployment'&gt;]

## Key Features

- Comprehensive data model capturing all 23 FDD items
- Tiered information architecture for mass appeal
- Advanced comparison capabilities
- Historical data tracking
- Monetization through subscription tiers
- SEO optimization with programmatic page generation

## Next Steps

1. Implement the database schema in Supabase
2. Develop the data extraction pipeline
3. Create the frontend UI components
4. Implement the comparison engine
5. Set up the subscription and payment system

## Project Status

All deliverables are complete and ready for implementation.

---

# Franchise Directory Database Schema and Design Project

## Tasks

### Research and Preparation

- [x] Read and understand the project requirements
- [x] Clarify requirements with user
- [x] Research FDD structure and 23 standard items
- [x] Research franchise industry standards and practices
- [x] Research competitor offerings and differentiation opportunities
- [ ] Research best practices for financial data platforms

### Database Schema Design

- [x] Design comprehensive Supabase database schema for all 23 FDD items
- [x] Create entity-relationship diagrams (ERDs)
- [x] Define data types, relationships, and constraints
- [x] Design indexes and optimization strategies
- [x] Create SQL schema definitions for Supabase implementation
- [x] Document data validation rules and constraints

### Franchise Profile Information Architecture

- [x] Design information organization for franchise profile pages
- [x] Establish priority/hierarchy of information
- [x] Create sample UI wireframes for profile pages
- [x] Design data visualization components
- [x] Document handling of data completeness variations

### Comparison Framework

- [x] Identify all comparable metrics with sources
- [x] Define comparison logic and normalization rules
- [x] Design recommended comparison UI patterns
- [x] Create sample comparison queries
- [x] Design visual comparison components

### Implementation Considerations

- [x] Outline data extraction strategies from PDF FDDs
- [x] Design update and versioning approach
- [x] Document performance optimization recommendations
- [x] Provide scalability considerations
- [x] Design monetization features and opportunities

### Final Deliverables

- [x] Compile complete database schema documentation
- [x] Finalize all visual components and diagrams
- [x] Review and validate all deliverables
- [x] Prepare final presentation of results