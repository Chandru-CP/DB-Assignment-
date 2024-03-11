1.Explain the relationship between the "Product" and "Product_Category" entities from the above diagram. 
Ans:
Based on the provided Image we can say that, the "Product" and “Product_Category” entities have a many-to-one relationship. This indicates that a
product can have more than one category linked with it, however a product can only be associated with one category.

The “Product_Category” entity's id column is referenced by the “category_id” foreign key column in the context of the "Product" entity.
The connection between the two entities is established in this way.
For example:
  •	If “Product” entity is :
      •	id: 1
      •	name: Samsung A53
      •	desc: Samsung latest smartphone
      •	SKU: ABC123
      •	category_id: 1 
      •	inventory_id: 1
      •	price: $540
      •	discount_id: 10 
      •	created_at: 2022-04-06 06:00:00
      •	modified_at: 2023-04-06 06:00:00
      •	deleted_at: null
  •	In “Product” entity for category_id we have passed value 1 so in “Product_Category” entity we have set for ID 1 we have to set like  :
      •	id: 1
      •	name: Electronics
      •	desc: Electronics products
      •	created_at: 2023-12-08 06:00:00
      •	modified_at: 2024-12-08 06:00:00
      •	deleted_at: null


In this example, the Samsung A53 product belongs to the Electronics category, which is represented by the “Product_Category” entity with ID 1.
The “category_id” column in the "Product" entity specifies the ID of the “Product_Category” entity it belongs to.

2. How could you ensure that each product in the "Product" table has a valid category assigned to it?
Ans:
To ensure that each product in the “Product” table has a valid category assigned to it, you can set the null argument of the ForeignKey field
 to False in the Product model

For example:category_id = models.ForeignKey(Product_Category, on_delete=models.CASCADE, null=False)
