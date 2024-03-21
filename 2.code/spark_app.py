from pyspark.sql import SparkSession
from pyspark.sql.functions import col, broadcast

# Инициализация SparkSession
spark = SparkSession.builder.appName("Продукты и категории").getOrCreate()

# Создаю пример датафрейма для продуктов
products_data = [(1, "Продукт1"), (2, "Продукт2"), (3, "Продукт3")]
products_df = spark.createDataFrame(products_data, ["product_id", "product_name"])

# Создаю пример датафрейма для категорий
categories_data = [(1, 10, "Категория1"), (2, 20, "Категория2")]
categories_df = spark.createDataFrame(categories_data, ["product_id", "category_id", "category_name"])

# Соединяю продукты и категории
product_category_pairs = products_df.join(broadcast(categories_df), "product_id", "left_outer")\
    .select("product_name", "category_name")

# Ищу продукты без категорий
products_without_categories = product_category_pairs.filter(col("category_name").isNull())\
    .select("product_name")

# Вывожу результаты
product_category_pairs.show()
products_without_categories.show()