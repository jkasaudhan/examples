-- This model retrieves order details, customer details, calculates summary statistics, and combines them.

WITH raw_orders AS (
    SELECT * FROM raw.orders
),
raw_customers AS (
    SELECT * FROM raw.customers
),
order_data AS (
    SELECT 
        order_id, 
        customer_id, 
        product_id, 
        order_value
    FROM raw_orders
),
summary_data AS (
    SELECT
        customer_id,
        COUNT(DISTINCT order_id) as total_orders,
        AVG(order_value) as avg_order_value,
        SUM(order_value) as total_order_value
    FROM order_data
    GROUP BY customer_id
),
combined_data AS (
    SELECT
        order_data.order_id,
        order_data.customer_id,
        order_data.product_id,
        order_data.order_value,
        summary_data.total_orders,
        summary_data.avg_order_value,
        summary_data.total_order_value
    FROM order_data
    LEFT JOIN summary_data ON order_data.customer_id = summary_data.customer_id
),
final_data AS (
    SELECT
        combined_data.*,
        raw_customers.first_name,
        raw_customers.last_name,
        raw_customers.email
    FROM combined_data
    INNER JOIN raw_customers ON combined_data.customer_id = raw_customers.customer_id
)

SELECT * FROM final_data
