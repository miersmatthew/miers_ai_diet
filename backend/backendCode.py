import json
from itertools import product
import random

food = [("Donuts (1)","250","T","F","F","15g","15g","31g","4g","A donut is a type of fried dough pastry typically shaped like a torus and sweetened with sugar or other sweeteners. It often contains a filling or topping, such as jam, chocolate, or frosting.","https://img.sndimg.com/food/image/upload/f_auto,c_thumb,q_55,w_860,ar_3:2/v1/img/recipes/38/38/68/wmk3BwJSK2g1NYdTaczo_DSC_0163.jpg"),
("Donuts (2)","500","T","F","F","30g","30g","62g","8g","A donut is a type of fried dough pastry typically shaped like a torus and sweetened with sugar or other sweeteners. It often contains a filling or topping, such as jam, chocolate, or frosting.","https://img.sndimg.com/food/image/upload/f_auto,c_thumb,q_55,w_860,ar_3:2/v1/img/recipes/38/38/68/wmk3BwJSK2g1NYdTaczo_DSC_0163.jpg"),
("Donuts (3)","750","T","F","F","45g","45g","93g","12g","A donut is a type of fried dough pastry typically shaped like a torus and sweetened with sugar or other sweeteners. It often contains a filling or topping, such as jam, chocolate, or frosting.","https://img.sndimg.com/food/image/upload/f_auto,c_thumb,q_55,w_860,ar_3:2/v1/img/recipes/38/38/68/wmk3BwJSK2g1NYdTaczo_DSC_0163.jpg"),
("Donuts (4)","1000","T","F","F","60g","60g","124g","16g","A donut is a type of fried dough pastry typically shaped like a torus and sweetened with sugar or other sweeteners. It often contains a filling or topping, such as jam, chocolate, or frosting.","https://img.sndimg.com/food/image/upload/f_auto,c_thumb,q_55,w_860,ar_3:2/v1/img/recipes/38/38/68/wmk3BwJSK2g1NYdTaczo_DSC_0163.jpg"),
("Donuts (5)","1250","T","F","F","75g","75g","155g","20g","A donut is a type of fried dough pastry typically shaped like a torus and sweetened with sugar or other sweeteners. It often contains a filling or topping, such as jam, chocolate, or frosting.","https://img.sndimg.com/food/image/upload/f_auto,c_thumb,q_55,w_860,ar_3:2/v1/img/recipes/38/38/68/wmk3BwJSK2g1NYdTaczo_DSC_0163.jpg"),
("Fried Egg Sandwich (1)","280","T","F","F","9g","3g","26g","11g","A fried egg sandwich is a breakfast or lunch dish consisting of a fried egg served between two slices of bread. It may also include additional ingredients such as cheese, bacon, ham, or vegetables.","https://food.fnr.sndimg.com/content/dam/images/food/fullset/2016/11/3/2/NLV-Crave-Worthy_breakfast-sandwich_s4x3.jpg.rend.hgtvcom.406.406.suffix/1478289713133.jpeg"),
("Fried Egg Sandwich (2)","560","T","F","F","18g","7g","53g","22g","A fried egg sandwich is a breakfast or lunch dish consisting of a fried egg served between two slices of bread. It may also include additional ingredients such as cheese, bacon, ham, or vegetables.","https://food.fnr.sndimg.com/content/dam/images/food/fullset/2016/11/3/2/NLV-Crave-Worthy_breakfast-sandwich_s4x3.jpg.rend.hgtvcom.406.406.suffix/1478289713133.jpeg"),
("Fried Egg Sandwich (3)","840","T","F","F","27g","10g","80g","33g","A fried egg sandwich is a breakfast or lunch dish consisting of a fried egg served between two slices of bread. It may also include additional ingredients such as cheese, bacon, ham, or vegetables.","https://food.fnr.sndimg.com/content/dam/images/food/fullset/2016/11/3/2/NLV-Crave-Worthy_breakfast-sandwich_s4x3.jpg.rend.hgtvcom.406.406.suffix/1478289713133.jpeg"),
("Avacado Toast (1 slice)","250","T","T","F","11g","1g","20g","5g","Avocado toast is a popular breakfast or brunch dish that consists of mashed avocado spread over a slice of toasted bread. It is often seasoned with salt, pepper, and other toppings such as eggs, tomatoes, or bacon.","https://www.eatingwell.com/thmb/YwNw19g19tS31P21KvIBFo1mVFk=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1807w-avocado-toast-recipe-8029771-2000-aefaa92c11e74e80b0bfc15788a61465.jpg"),
("Avacado Toast (2 slice)","500","T","T","F","22g","2g","40g","10g","Avocado toast is a popular breakfast or brunch dish that consists of mashed avocado spread over a slice of toasted bread. It is often seasoned with salt, pepper, and other toppings such as eggs, tomatoes, or bacon.","https://www.eatingwell.com/thmb/YwNw19g19tS31P21KvIBFo1mVFk=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1807w-avocado-toast-recipe-8029771-2000-aefaa92c11e74e80b0bfc15788a61465.jpg"),
("Avacado Toast (3 slice)","750","T","T","F","33g","3g","60g","15g","Avocado toast is a popular breakfast or brunch dish that consists of mashed avocado spread over a slice of toasted bread. It is often seasoned with salt, pepper, and other toppings such as eggs, tomatoes, or bacon.","https://www.eatingwell.com/thmb/YwNw19g19tS31P21KvIBFo1mVFk=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/1807w-avocado-toast-recipe-8029771-2000-aefaa92c11e74e80b0bfc15788a61465.jpg"),
("Pancakes (2 large)","360","T","F","F","8g","7g","37g","8g","Pancakes are a type of flat, round cake made from a batter consisting of flour, milk, eggs, and baking powder. They are typically cooked on a griddle or frying pan and served with toppings such as syrup, butter, or fruit.","https://hips.hearstapps.com/hmg-prod/images/best-homemade-pancakes-index-640775a2dbad8.jpg?crop=0.6667877686951256xw:1xh;center,top&resize=1200:*"),
("Pancakes (4 large)","720","T","F","F","16g","14g","74g","16g","Pancakes are a type of flat, round cake made from a batter consisting of flour, milk, eggs, and baking powder. They are typically cooked on a griddle or frying pan and served with toppings such as syrup, butter, or fruit.","https://hips.hearstapps.com/hmg-prod/images/best-homemade-pancakes-index-640775a2dbad8.jpg?crop=0.6667877686951256xw:1xh;center,top&resize=1200:*"),
("Pancakes (6 large)","1080","T","F","F","24g","21g","111g","24g","Pancakes are a type of flat, round cake made from a batter consisting of flour, milk, eggs, and baking powder. They are typically cooked on a griddle or frying pan and served with toppings such as syrup, butter, or fruit.","https://hips.hearstapps.com/hmg-prod/images/best-homemade-pancakes-index-640775a2dbad8.jpg?crop=0.6667877686951256xw:1xh;center,top&resize=1200:*"),
("Oatmeal (1 cup)","160","T","F","F","3g","1g","27g","5g","Oatmeal is a popular breakfast dish made by boiling oats in water or milk until they become soft and creamy. It is often served hot and can be flavored with various ingredients such as cinnamon, fruit, or nuts.","https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimg1.cookinglight.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fmedium_2x%2Fpublic%2F1647876338%2FGF2A9480.jpg%3Fitok%3Dl0sI-w6h&w=1000&c=sc&poi=face&q=60"),
("Oatmeal (2 cup)","320","T","F","F","6g","2g","54g","10g","Oatmeal is a popular breakfast dish made by boiling oats in water or milk until they become soft and creamy. It is often served hot and can be flavored with various ingredients such as cinnamon, fruit, or nuts.","https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimg1.cookinglight.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fmedium_2x%2Fpublic%2F1647876338%2FGF2A9480.jpg%3Fitok%3Dl0sI-w6h&w=1000&c=sc&poi=face&q=60"),
("Oatmeal (3 cup)","480","T","F","F","9g","3g","81g","15g","Oatmeal is a popular breakfast dish made by boiling oats in water or milk until they become soft and creamy. It is often served hot and can be flavored with various ingredients such as cinnamon, fruit, or nuts.","https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimg1.cookinglight.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2Fmedium_2x%2Fpublic%2F1647876338%2FGF2A9480.jpg%3Fitok%3Dl0sI-w6h&w=1000&c=sc&poi=face&q=60"),
("French Toast (1 slice)","300","T","F","F","11g","4g","23g","7.3g","French toast is a breakfast dish made by soaking slices of bread in a mixture of eggs, milk, and sugar, and then frying them until they are golden brown. It is often served with toppings such as syrup, butter, or fruit.","https://www.southernliving.com/thmb/YGmf_fkObjRybUqk-2HuNGf5Tvw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-french-toast-j-furniss-4x3-1-55df7e8729c444d1a250580d8cc5d864.jpg"),
("French Toast (2 slice)","600","T","F","F","22g","8g","46g","14g","French toast is a breakfast dish made by soaking slices of bread in a mixture of eggs, milk, and sugar, and then frying them until they are golden brown. It is often served with toppings such as syrup, butter, or fruit.","https://www.southernliving.com/thmb/YGmf_fkObjRybUqk-2HuNGf5Tvw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-french-toast-j-furniss-4x3-1-55df7e8729c444d1a250580d8cc5d864.jpg"),
("French Toast (3 slice)","900","T","F","F","33g","12g","69g","21g","French toast is a breakfast dish made by soaking slices of bread in a mixture of eggs, milk, and sugar, and then frying them until they are golden brown. It is often served with toppings such as syrup, butter, or fruit.","https://www.southernliving.com/thmb/YGmf_fkObjRybUqk-2HuNGf5Tvw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/classic-french-toast-j-furniss-4x3-1-55df7e8729c444d1a250580d8cc5d864.jpg"),
("Rice, chicken (1 cup)","260","F","T","T","9g","4g","22g","28g","Rice and chicken is a popular dish made by cooking chicken and rice together in a flavorful broth or sauce. It is a staple dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://www.recipetineats.com/wp-content/uploads/2018/06/Oven-Baked-Chicken-and-Rice_0.jpg?resize=650,910"),
("Rice, chicken (2 cup)","520","F","T","T","19g","8g","44g","56g","Rice and chicken is a popular dish made by cooking chicken and rice together in a flavorful broth or sauce. It is a staple dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://www.recipetineats.com/wp-content/uploads/2018/06/Oven-Baked-Chicken-and-Rice_0.jpg?resize=650,910"),
("Rice, chicken (3 cup)","780","F","T","T","28g","12g","67g","84g","Rice and chicken is a popular dish made by cooking chicken and rice together in a flavorful broth or sauce. It is a staple dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://www.recipetineats.com/wp-content/uploads/2018/06/Oven-Baked-Chicken-and-Rice_0.jpg?resize=650,910"),
("Rice, chicken (4 cup)","1040","F","T","T","38g","16g","89g","112g","Rice and chicken is a popular dish made by cooking chicken and rice together in a flavorful broth or sauce. It is a staple dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://www.recipetineats.com/wp-content/uploads/2018/06/Oven-Baked-Chicken-and-Rice_0.jpg?resize=650,910"),
("Rice, Salmon (1 cup)","210","F","T","T","8g","3g","44g","24g","Rice and salmon is a dish that typically consists of cooked rice topped with cooked or smoked salmon. It is often seasoned with herbs and spices, and can be served with additional toppings such as avocado, cucumber, or sesame seeds.","https://assets.bonappetit.com/photos/5f1b04ecda927390827b1c79/5:7/w_1405,h_1967,c_limit/Basically-SaffronSalmon-RecipeB.jpg"),
("Rice, Salmon (2 cup)","420","F","T","T","17g","6g","89g","49g","Rice and salmon is a dish that typically consists of cooked rice topped with cooked or smoked salmon. It is often seasoned with herbs and spices, and can be served with additional toppings such as avocado, cucumber, or sesame seeds.","https://assets.bonappetit.com/photos/5f1b04ecda927390827b1c79/5:7/w_1405,h_1967,c_limit/Basically-SaffronSalmon-RecipeB.jpg"),
("Rice, Salmon (3 cup)","630","F","T","T","25g","9g","134g","73g","Rice and salmon is a dish that typically consists of cooked rice topped with cooked or smoked salmon. It is often seasoned with herbs and spices, and can be served with additional toppings such as avocado, cucumber, or sesame seeds.","https://assets.bonappetit.com/photos/5f1b04ecda927390827b1c79/5:7/w_1405,h_1967,c_limit/Basically-SaffronSalmon-RecipeB.jpg"),
("Rice, Salmon (4 cup)","840","F","T","T","34g","12g","179g","98g","Rice and salmon is a dish that typically consists of cooked rice topped with cooked or smoked salmon. It is often seasoned with herbs and spices, and can be served with additional toppings such as avocado, cucumber, or sesame seeds.","https://assets.bonappetit.com/photos/5f1b04ecda927390827b1c79/5:7/w_1405,h_1967,c_limit/Basically-SaffronSalmon-RecipeB.jpg"),
("Rice, Pork (1 cup)","270","F","T","T","17g","1g","25g","17g","Rice and pork is a dish that typically consists of cooked rice and sliced or diced pork, often cooked in a sauce or marinade. It is a popular dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://takestwoeggs.com/wp-content/uploads/2021/10/Char-Siu-Pork-Homemade-Chinese-BBQ-Pork-Takestwoeggs-Final-SQ.jpg"),
("Rice, Pork (2 cup)","540","F","T","T","34g","2g","50g","34g","Rice and pork is a dish that typically consists of cooked rice and sliced or diced pork, often cooked in a sauce or marinade. It is a popular dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://takestwoeggs.com/wp-content/uploads/2021/10/Char-Siu-Pork-Homemade-Chinese-BBQ-Pork-Takestwoeggs-Final-SQ.jpg"),
("Rice, Pork (3 cup)","810","F","T","T","51g","3g","75g","51g","Rice and pork is a dish that typically consists of cooked rice and sliced or diced pork, often cooked in a sauce or marinade. It is a popular dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://takestwoeggs.com/wp-content/uploads/2021/10/Char-Siu-Pork-Homemade-Chinese-BBQ-Pork-Takestwoeggs-Final-SQ.jpg"),
("Rice, Pork (4 cup)","1080","F","T","T","68g","4g","100g","68g","Rice and pork is a dish that typically consists of cooked rice and sliced or diced pork, often cooked in a sauce or marinade. It is a popular dish in many cultures and can be seasoned with various spices and herbs to create a range of different flavors.","https://takestwoeggs.com/wp-content/uploads/2021/10/Char-Siu-Pork-Homemade-Chinese-BBQ-Pork-Takestwoeggs-Final-SQ.jpg"),
("Rice, Beef (1 cup)","330","F","T","T","14g","5g","35g","20g","Rice and beef is a dish that typically consists of cooked rice and seasoned beef, often served with vegetables and a sauce. It is a staple dish in many cultures and can be prepared in various ways, such as stir-frying or slow cooking, to create different textures and flavors.","https://assets.epicurious.com/photos/57978ae83a12dd9d56024009/1:1/w_1920,c_limit/fragrant-beef-curry-with-rice.jpg"),
("Rice, Beef (2 cup)","660","F","T","T","29g","10g","71g","40g","Rice and beef is a dish that typically consists of cooked rice and seasoned beef, often served with vegetables and a sauce. It is a staple dish in many cultures and can be prepared in various ways, such as stir-frying or slow cooking, to create different textures and flavors.","https://assets.epicurious.com/photos/57978ae83a12dd9d56024009/1:1/w_1920,c_limit/fragrant-beef-curry-with-rice.jpg"),
("Rice, Beef (3 cup)","990","F","T","T","43g","15g","106g","60g","Rice and beef is a dish that typically consists of cooked rice and seasoned beef, often served with vegetables and a sauce. It is a staple dish in many cultures and can be prepared in various ways, such as stir-frying or slow cooking, to create different textures and flavors.","https://assets.epicurious.com/photos/57978ae83a12dd9d56024009/1:1/w_1920,c_limit/fragrant-beef-curry-with-rice.jpg"),
("Rice, Beef (4 cup)","1320","F","T","T","58g","20g","142g","80g","Rice and beef is a dish that typically consists of cooked rice and seasoned beef, often served with vegetables and a sauce. It is a staple dish in many cultures and can be prepared in various ways, such as stir-frying or slow cooking, to create different textures and flavors.","https://assets.epicurious.com/photos/57978ae83a12dd9d56024009/1:1/w_1920,c_limit/fragrant-beef-curry-with-rice.jpg"),
("Pizza (1 slice)","250","F","T","T","9g","3g","16g","8g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Pizza (2 slice)","500","F","T","T","19g","7g","33g","17g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Pizza (3 slice)","750","F","T","T","29g","11g","50g","26g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Pizza (4 slice)","1000","F","T","T","39g","15g","66g","35g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Pizza (5 slice)","1250","F","T","T","49g","19g","83g","44g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Pizza (6 slice)","1500","F","T","T","59g","22g","100g","53g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Pizza (7 slice)","1750","F","T","T","69g","26g","116g","62g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Pizza (8 slice)","2000","F","T","T","79g","30g","133g","71g","Pizza is a savory dish that typically consists of a dough base topped with tomato sauce, cheese, and various ingredients such as meat, vegetables, and herbs. It is typically baked in an oven and can be served in slices or as a whole pie.","https://www.kingarthurbaking.com/sites/default/files/2022-03/Easiest-Pizza_22-2_11.jpg"),
("Burger and Fries","900","F","T","T","46g","7g","88g","34g","A burger and fries is a classic fast food meal consisting of a beef patty sandwiched between two buns, often topped with cheese, lettuce, tomato, and condiments. It is typically served with a side of french fries, which are thinly sliced and deep-fried potatoes seasoned with salt.","https://www.allrecipes.com/thmb/GvGzAzmqmTiCFP9AIisrHZav_Gw=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Copycat-Burger-and-Fries-2000-b09140d301434155bda5a8c8a40f5e95.jpeg"),
("Steak and Potatoes (8oz)","700","F","F","T","13g","2g","31g","9g","Steak and potatoes is a classic meat-and-potatoes meal that typically consists of a grilled or pan-seared steak and a side of roasted or mashed potatoes. It is often seasoned with herbs and spices, and can be served with additional vegetables or sauces.","https://www.lecremedelacrumb.com/wp-content/uploads/2019/03/feat-500x500.jpg"),
("Steak and Potatoes (12oz)","1050","F","F","T","20g","3g","47g","13g","Steak and potatoes is a classic meat-and-potatoes meal that typically consists of a grilled or pan-seared steak and a side of roasted or mashed potatoes. It is often seasoned with herbs and spices, and can be served with additional vegetables or sauces.","https://www.lecremedelacrumb.com/wp-content/uploads/2019/03/feat-500x500.jpg"),
("Cesar Salad (3 cup)","480","F","T","F","40g","4g","23g","10g","A Caesar salad is a popular salad dish made with romaine lettuce, croutons, and shaved parmesan cheese, dressed with a creamy Caesar dressing made from anchovies, garlic, lemon juice, and olive oil. It is often served as a side dish or topped with grilled chicken or shrimp for a more filling meal.","https://lindseyeatsla.com/wp-content/uploads/2021/10/Lindseyeats_Classic_Caesar_Salad.jpg"),
("Spagetti and Meatballs (1 cup)","390","F","F","T","15g","5g","49g","16g","Spaghetti and meatballs is a classic Italian-American dish that typically consists of spaghetti pasta served with tomato sauce and meatballs made from ground beef or a combination of meats, such as pork and veal. It is often topped with grated Parmesan cheese and served with garlic bread on the side.","https://hips.hearstapps.com/delish/assets/17/39/1506456062-delish-spaghetti-meatballs.jpg"),
("Spagetti and Meatballs (2 cup)","780","F","F","T","30g","11g","98g","32g","Spaghetti and meatballs is a classic Italian-American dish that typically consists of spaghetti pasta served with tomato sauce and meatballs made from ground beef or a combination of meats, such as pork and veal. It is often topped with grated Parmesan cheese and served with garlic bread on the side.","https://hips.hearstapps.com/delish/assets/17/39/1506456062-delish-spaghetti-meatballs.jpg"),
("Spagetti and Meatballs (3 cup)","1170","F","F","T","45g","17g","147g","48g","Spaghetti and meatballs is a classic Italian-American dish that typically consists of spaghetti pasta served with tomato sauce and meatballs made from ground beef or a combination of meats, such as pork and veal. It is often topped with grated Parmesan cheese and served with garlic bread on the side.","https://hips.hearstapps.com/delish/assets/17/39/1506456062-delish-spaghetti-meatballs.jpg"),
("Spagetti and Meatballs (4 cup)","1560","F","F","T","60g","23g","196g","64g","Spaghetti and meatballs is a classic Italian-American dish that typically consists of spaghetti pasta served with tomato sauce and meatballs made from ground beef or a combination of meats, such as pork and veal. It is often topped with grated Parmesan cheese and served with garlic bread on the side.","https://hips.hearstapps.com/delish/assets/17/39/1506456062-delish-spaghetti-meatballs.jpg")]

training = [
    ('Walking', 'T', 'F', 'F', '45 Mins', 'https://images.everydayhealth.com/images/can-even-moderate-walking-help-prevent-dementia-1440x810.jpg?w=1110'),
            ('Jogging', 'T', 'F', 'F', '30 Mins', 'https://img.etimg.com/thumb/msid-71938900,width-650,height-488,imgsize-480069,,resizemode-75/running-was-also-associated-with-a-30-per-cent-lower-risk-of-death-from-cardiovascular-disease-according-to-the-study-.jpg'),
            ('Running', 'T', 'F', 'F', '25 Mins', 'https://img.etimg.com/thumb/msid-71938900,width-650,height-488,imgsize-480069,,resizemode-75/running-was-also-associated-with-a-30-per-cent-lower-risk-of-death-from-cardiovascular-disease-according-to-the-study-.jpg'),
            ('Cycling', 'T', 'F', 'F', '35 Mins', 'https://www.siroko.com/blog/c/app/uploads/2021/07/efectos-positivos_f766ef96-0811-452d-bbf8-ec38d244637a.jpg'),
            ('Swimming', 'T', 'F', 'F', '30 Mins', 'https://cdn2.stylecraze.com/wp-content/uploads/2022/03/Swimming-is-a-full-body-workout-that-burns-400-900-calories-per-hour--Here-are-3-swimming-workout-plans-by-experts-to-help-you-lose-weight--Read-on-to-shed-fat.jpg.webp'),
            ('Weight Training', 'T', 'F', 'F', '60 Mins', 'https://assets.sweat.com/html_body_blocks/images/000/021/037/original/Y2018_Summer_Series_Gym_Kelsey_14_074_imagelibrary_Low_res_1200x800_5b2df79_en49c503d8e64bde140b1a113c5926d9d6.jpg?1657780099'),
            ('Interval Training', 'T', 'F', 'F', '45 Mins', 'https://i.insider.com/5ad8fcd0066a4cf6668b479f?width=1300&format=jpeg&auto=webp'),
            ('Squats', 'F', 'T', 'F', '45 Mins', 'https://www.eatthis.com/wp-content/uploads/sites/4/2022/10/fitness-woman-performing-squats.jpg?quality=82&strip=1&w=970'),
            ('Crunches', 'F', 'T', 'F', '30 Mins', 'https://bod-blog-assets.prod.cd.beachbodyondemand.com/bod-blog/wp-content/uploads/2017/10/bb_bicycle-crunch_header1-NEW.jpg'),
            ('Bench Dips', 'F', 'T', 'F', '25 Mins', 'https://www.anytimefitness.com/wp-content/uploads/2020/07/AdobeStock_83746372-1536x1024.jpeg'),
            ('Pull-Ups', 'F', 'T', 'F', '35 Mins', 'https://hips.hearstapps.com/hmg-prod/images/mh0418-fit-pul-01-1558554157.jpg?crop=0.750xw:1.00xh;0.250xw,0&resize=1200:*'),
            ('Push-Ups', 'F', 'T', 'F', '30 Mins', 'https://www.kreedon.com/wp-content/uploads/2021/08/oYDbf5hQAePHEBNZTQMXRA-1024x576.jpg.webp'),
            ('Lunges', 'F', 'T', 'F', '60 Mins', 'https://hortonbarbell.com/wp-content/uploads/2022/05/Dumbbell-Lunge.webp'),
            ('Overhead Press', 'F', 'T', 'F', '45 Mins', 'https://www.bodybuilding.com/fun/images/2015/how-to-overhead-press-a-beginners-guide-tablet-830x467.jpg'),
            ('Yoga', 'F', 'F', 'T', '45 Mins', 'https://static01.nyt.com/images/2016/12/02/well/move/yoga_body_images-slide-HNVD/yoga_body_images-slide-HNVD-blog480.jpg'),
            ('Meditation', 'F', 'F', 'T', '30 Mins', 'https://lh3.googleusercontent.com/K4yb5g8rvsYiZenwPeulKTjQwBgyalnQWbEj4k-G2Era1V94wDyOxw2pPv5Ccc4xP9t89dSbyy_qsG_YM6-Odu0oDmNIPpQCuFpYdB1GvWYooqvvuIg0llXZLBZ2D3ddC230Pd9-'),
            ('Aerobics', 'F', 'F', 'T', '50 Mins', 'https://img.livestrong.com/1260x/clsd/getty/42e43b8bdd104d5c9b99559c45510968?type=webp'),
            ('Strength Training', 'F', 'F', 'T', '45 Mins', 'https://hips.hearstapps.com/hmg-prod/images/burning-calories-and-strengthening-her-core-with-a-royalty-free-image-1579042741.jpg?crop=0.668xw:1.00xh;0.0136xw,0&resize=1200:*')
    ]


bList = list(filter(lambda x: x[2] == "T", food))
lList = list(filter(lambda x: x[3] == "T", food))
dList = list(filter(lambda x: x[4] == "T", food))


def getBmi(weight, height):
    return weight / height ** 2
    
def getBmr(gender, weight, height, age):
    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    elif gender == "female":
        bmr = 447.593 + (9.247 * weight) + (3.098 * height * 100) - (4.330 * age)
    else:
        #unknown gender, something went wrong, just assume male 
        bmr = 88.362 + (13.397 * weight) + (4.799 * height * 100) - (5.677 * age)
    return bmr

def getCalNeeds(activityLev, bmr):
    # Activity level assignments
    # 1.2 - "sedentary"
    # 1.375 - "lightly active"
    # 1.55 - "moderately active"
    # 1.725 - "very active"
    calNeeds = bmr * activityLev
    return calNeeds

def getCalGoal(calNeeds, goal):
    if goal == 'Gain Weight':
        return calNeeds * 1.1
    elif goal == 'Lose Weight':
        return calNeeds * 0.9
    elif goal == 'Maintain Weight':
        return calNeeds
    else:
        #unknown goal, something went wrong, just assume Maintain Weight
        return calNeeds
    
def user_fitness(goal):
    if goal == 'Lose Weight':
        matching_record_wg = [record for record in training if record[1] == "T"]
        record = random.sample(matching_record_wg,2)
        return record;
    elif goal == 'Gain Weight':
        matching_record_wl = [record for record in training if record[2] == "T"]
        record = random.sample(matching_record_wl,2)
        return record;
    else: 
        matching_record_mw = [record for record in training if record[3] == "T"]
        record = random.sample(matching_record_mw,2)
        return record;

def find_closest_combo(target, list1, list2, list3):
    closest_sum = float('inf')
    closest_combo = None
    for combo in product(list1, list2, list3):
        if int(combo[1][1]) >= int(combo[2][1]):
            combo_sum = int(combo[0][1]) + int(combo[1][1]) + int(combo[2][1])
            combo_std = (abs(int(combo[0][1]) - (combo_sum/3))
                + abs(int(combo[1][1]) - (combo_sum/3))
                + abs(int(combo[2][1]) - (combo_sum/3)))/3
            print(combo_std)
            if abs(target - combo_sum) < abs(target - closest_sum) and combo_std < 200:
                closest_sum = combo_sum
                closest_combo = combo
    return closest_combo

def lambda_handler(event, context):
    random.shuffle(bList)
    random.shuffle(lList)
    random.shuffle(dList)

    age = float(event['queryStringParameters']['age'])
    height = float(event['queryStringParameters']['height'])
    weight = float(event['queryStringParameters']['weight'])
    gender = event['queryStringParameters']['gender']
    activityLev = float(event['queryStringParameters']['activityLev'])
    goal = event['queryStringParameters']['goal']
    print("got here")
    bmi = getBmi(weight, height)
    bmr = getBmr(gender, weight, height, age)
    calNeeds = getCalNeeds(activityLev, bmr)
    calGoal = getCalGoal(calNeeds, goal)
    fitnessrecord = user_fitness(goal)
    print("got here")
    selFoods = find_closest_combo(calGoal, bList, lList, dList) 
    #TODO meal recomendation
    #goal = 'soem goal'

    jsonResp = {
        'bmi': bmi,
        'bmr': bmr,
        'calGoal': calGoal,
        'goal': goal,
        'foods': {
            'bfood': {'name': selFoods[0][0], 'cal': selFoods[0][1], 'fat': selFoods[0][5], 'sugar': selFoods[0][6], 'carb': selFoods[0][7], 'protien': selFoods[0][8], 'desc': selFoods[0][9], 'img': selFoods[0][10]},
            'lfood': {'name': selFoods[1][0], 'cal': selFoods[1][1], 'fat': selFoods[1][5], 'sugar': selFoods[1][6], 'carb': selFoods[1][7], 'protien': selFoods[1][8], 'desc': selFoods[1][9], 'img': selFoods[1][10]},
            'dfood': {'name': selFoods[2][0], 'cal': selFoods[2][1], 'fat': selFoods[2][5], 'sugar': selFoods[2][6], 'carb': selFoods[2][7], 'protien': selFoods[2][8], 'desc': selFoods[2][9], 'img': selFoods[2][10]},
        },
        'fitnessrecord_1': {'name': fitnessrecord[0][0], 'duration': fitnessrecord[0][4], 'img': fitnessrecord[0][5]},
        'fitnessrecord_2': {'name': fitnessrecord[1][0], 'duration': fitnessrecord[1][4], 'img': fitnessrecord[1][5]},
        'event': event
    }
    
    return {
        'statusCode': 200,
        'headers': {
            "Access-Control-Allow-Headers" : "Content-Type",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
        },
        'body': json.dumps(jsonResp)
    }