CREATE TABLE `dim_customers` (
  `customer_id` varchar(255) PRIMARY KEY,
  `customer_name` varchar(255),
  `gender` varchar(255),
  `age` int,
  `email` varchar(255),
  `customer_type` varchar(255)
);

CREATE TABLE `dim_travel_package` (
  `package_id` varchar(255) PRIMARY KEY,
  `package_name` varchar(255),
  `package_type` varchar(255),
  `duration_days` int,
  `price_per_pax` int,
  `destination` varchar(255),
  `category` varchar(255)
);

CREATE TABLE `dim_feedback` (
  `feedback_id` varchar(255) PRIMARY KEY,
  `package_id` varchar(255),
  `booking_id` varchar(255),
  `satisfaction_score` int,
  `feedback_date` date,
  `comments` text,
  `rating_hotel` int,
  `rating_guide` int,
  `would_recommend` int
);

CREATE TABLE `dim_refund` (
  `refund_id` varchar(255) PRIMARY KEY,
  `booking_id` varchar(255),
  `customer_id` varchar(255),
  `refund_date` date,
  `refund_amount` int,
  `refund_percentage` decimal,
  `reason` text,
  `refund_status` varchar(255)
);

CREATE TABLE `dim_travel_guide` (
  `staff_id` varchar(255) PRIMARY KEY,
  `staff_name` varchar(255),
  `role` varchar(255),
  `working_status` varchar(255),
  `comission_rate` decimal
);

CREATE TABLE `fact_sales` (
  `booking_id` varchar(255) PRIMARY KEY,
  `customer_id` varchar(255),
  `package_id` varchar(255),
  `guide_id` varchar(255),
  `booking_date` date,
  `travel_date` date,
  `num_of_pax` int,
  `discount_promotion` int,
  `channel` varchar(255),
  `payment_status` varchar(255),
  `payment_method` varchar(255)
);

CREATE TABLE `dim_date` (
  `date_key` date PRIMARY KEY,
  `full_date` date,
  `day` int,
  `month` int,
  `monthname` varchar(255),
  `year` int,
  `weekday` varchar(255),
  `is_weekend` int
);

ALTER TABLE `dim_feedback` ADD FOREIGN KEY (`booking_id`) REFERENCES `fact_sales` (`booking_id`);

ALTER TABLE `dim_refund` ADD FOREIGN KEY (`booking_id`) REFERENCES `fact_sales` (`booking_id`);

ALTER TABLE `fact_sales` ADD FOREIGN KEY (`customer_id`) REFERENCES `dim_customers` (`customer_id`);

ALTER TABLE `fact_sales` ADD FOREIGN KEY (`package_id`) REFERENCES `dim_travel_package` (`package_id`);

ALTER TABLE `fact_sales` ADD FOREIGN KEY (`guide_id`) REFERENCES `dim_travel_guide` (`staff_id`);

ALTER TABLE `fact_sales` ADD FOREIGN KEY (`booking_date`) REFERENCES `dim_date` (`date_key`);

ALTER TABLE `fact_sales` ADD FOREIGN KEY (`travel_date`) REFERENCES `dim_date` (`date_key`);


// Exists in BigQuery as `ppnj.dim_customers`
